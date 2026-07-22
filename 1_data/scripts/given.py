# =======================Import Packages / Libraries===========================
from Bio.Seq import Seq
import pandas as pd
import glob
import re
import os
# =============================================================================


### Extract from given data
def parse_and_translate_mitoscaf(file_path):
    """Parses a single .cds file, cleans the filename, and translates sequences to proteins."""
    # Regex for custom headers: >Contig1;ND2;len=1002;[381:1383](+)
    header_regex = re.compile(r"^>([^;]+);([^;]+);len=(\d+);\[(\d+):(\d+)\]\(([-+])\)")
    
    base_name = os.path.basename(file_path) 
    try:
        file_id = base_name.split('_')[1] # Extracts just the colony name
    except IndexError:
        file_id = os.path.splitext(base_name)[0]
    
    file_rows = []
    current_meta = None
    current_seq = []
    
    def process_and_translate(meta, seq_list):
        """Helper function to translate and append a completed gene sequence."""
        nuc_seq_str = "".join(seq_list).strip()
        if not nuc_seq_str:
            return None
            
        meta["sequence"] = nuc_seq_str
        
        # Translation logic
        biopython_seq = Seq(nuc_seq_str)
        remainder = len(biopython_seq) % 3
        clean_seq = biopython_seq[:-remainder] if remainder != 0 else biopython_seq
        
        # Table 5 = Invertebrate Mitochondrial Code
        protein_product = str(clean_seq.translate(table=5, to_stop=True)).replace('*', '')
        meta["protein"] = protein_product
        return meta

    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
                
            if line.startswith(">"):
                # Process the previous gene block before moving to the next
                if current_meta and current_seq:
                    completed_row = process_and_translate(current_meta, current_seq)
                    if completed_row:
                        file_rows.append(completed_row)
                
                # Setup next gene block
                match = header_regex.match(line)
                if match:
                    contig, gene, length, start, end, strand = match.groups()
                    
                    # Standardize common variations to match target list
                    gene_clean = gene.upper().strip()
                    if gene_clean == 'ATP6': gene_clean = 'atp6'
                    if gene_clean == 'ATP8': gene_clean = 'atp8'
                    if gene_clean in ('CO1', 'COI', 'COX1'): gene_clean = 'cox1'
                    if gene_clean in ('CO2', 'COII', 'COX2'): gene_clean = 'cox2'
                    if gene_clean in ('CO3', 'COIII', 'COX3'): gene_clean = 'cox3'
                    if gene_clean in ('COB', 'CYB', 'CYTB'): gene_clean = 'cytb'
                    if gene_clean == 'ND1': gene_clean = 'nad1'
                    if gene_clean == 'ND2': gene_clean = 'nad2'
                    if gene_clean == 'ND3': gene_clean = 'nad3'
                    if gene_clean == 'ND4': gene_clean = 'nad4'
                    if gene_clean == 'ND4L': gene_clean = 'nad4l'
                    if gene_clean == 'ND5': gene_clean = 'nad5'
                    if gene_clean == 'ND6': gene_clean = 'nad6'

                    if 'AmC' in file_id:
                        location = "Germany"
                    elif 'RPOT' in file_id:
                        location = 'United Kingdom'
                    else:
                        location = "Ireland"
                        
                    hybrid = ('AFH1', 'F122KY', 'F143DL2022', 'F148DL2022', 'F152DL2021', 'F95DL20',
                              'F153DL2021', 'F156DL2022', 'F29GBK17', 'F29GBN17', 'F74D19', 'F89CE', 
                              'M136DL2022', 'X211W', 'TD2BND', 'TD2BLK', 'RPOT', 'NUIG22SW', 'M149DL2021' )
                    if 'AmC' in file_id:
                        organism = "Apis mellifera carnica"
                    elif file_id in hybrid:
                        organism = 'Apis mellifera hybrid'
                    else:
                        organism = "Apis mellifera mellifera"
                        
                                                      
                    current_meta = {
                        "file_id": file_id,
                        "Contig": contig,
                        "gene": gene_clean,
                        "s": int(start),
                        "location": location,
                        "organism": organism,
                        "e": int(end),
#                        "Strand": strand,
                        "Location_String": f"{start}:{end}({strand})"
                    }
                    current_seq = []
                else:
                    current_meta = None 
            else:
                if current_meta is not None:
                    current_seq.append(line)
                    
        # Process the final remaining gene at the end of the file file
        if current_meta and current_seq:
            completed_row = process_and_translate(current_meta, current_seq)
            if completed_row:
                file_rows.append(completed_row)
            
    return file_rows

# =====================================================================
# Main Execution Pipeline
# =====================================================================
folder_path = "./work_data/*.mitogenome.fa_mitoscaf.fa.gbf.cds.fasta" 
all_gene_rows = []
matched_files = glob.glob(folder_path)

if not matched_files:
    raise FileNotFoundError(f"No '.cds' files found in '{os.path.abspath(folder_path)}'.")

for file_path in matched_files:
    parsed_rows = parse_and_translate_mitoscaf(file_path)
    all_gene_rows.extend(parsed_rows)

df_long_master = pd.DataFrame(all_gene_rows)

df_pivot = df_long_master.pivot(
    index=["file_id", "organism", "location" ], 
    columns="gene", 
    values=["s", "e", "sequence", "protein"])

df_pivot.columns = [f"{gene}_{metric}" for metric, gene in df_pivot.columns]
df_wide_master = df_pivot.reset_index()

desired_order = ['file_id', "organism"] #location
target_genes = ['atp6', 'atp8', 'cox1', 'cox2', 'cox3', 'cytb', 'nad1', 'nad2', 'nad3', 'nad4', 'nad4l', 'nad5', 'nad6']

for g in target_genes:
    desired_order.extend([f"{g}_s", f"{g}_e", f"{g}_sequence"])

# Enforce explicit inclusion of existing columns
existing_columns = [col for col in desired_order if col in df_wide_master.columns]
df_given = df_wide_master[existing_columns]

# Save as a spreadsheet
df_given.to_csv("genes_given.csv", index=False)