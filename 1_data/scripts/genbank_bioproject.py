# =======================Import Packages / Libraries===========================
from Bio import Entrez
from Bio import SeqIO
import pandas as pd
# =============================================================================

Entrez.email = "email"
# the ncbi search query
search_query = '("Apis mellifera"[Organism] OR apis mellifera[All Fields]) AND mitochondrion[All Fields] AND complete[All Fields]")'
print("Searching NCBI Nucleotide database...")
search_handle = Entrez.esearch(db="nucleotide", term=search_query, string= 1, retmax=500)
search_results = Entrez.read(search_handle)
search_handle.close()
id_list = search_results["IdList"]
print(f"Success! Found {len(id_list)} matching complete mitochondrial records.")

# obtaining the list
if id_list:
    id_string = ",".join(id_list)     # Convert list of IDs into a comma-separated string for fetching

    # 4. Fetch the actual sequence data
    print("Downloading records as Genbank data...")
    with Entrez.efetch(db="nucleotide", id=id_string, rettype="gb", retmode="text") as fetch_handle:
                                                              #fasta_cds_na
        records = list(SeqIO.parse(fetch_handle, "genbank"))
        
        
gene_rows = []

for record in records:
    # Find the organism name directly from the record annotations
    organism = record.annotations.get("organism", "unnamed_organism")
    
    # Find geographic location
    source_feat = next((f for f in record.features if f.type == "source"), None)
    location = source_feat.qualifiers.get("geo_loc_name", ["unnamed_loc"])[0] if source_feat else "unnamed_loc"
    # 2. Extract Collection Date
    date = record.annotations.get("date", "no_date") if record else "no_date"
    
    for feat in record.features:
        if feat.type == "CDS":
            # Extract and clean gene name
            gene_name = feat.qualifiers.get("gene") or feat.qualifiers.get("product") or ["unnamed_gene"]
            gene_str = gene_name[0].lower().strip()
            
            ## ATP 6 and 8
            if gene_str in ('atp6', 'atpase subunit 6'):
                gene_str = 'atp6'
            elif gene_str in ('atp8', 'atpase subunit 8'):
                gene_str = 'atp8'
                
            ## COX 1, 2, 3, and B                
            elif gene_str in ('co1', 'coi', 'cox1', 'cytochrome c oxidase subunit 1'):
                gene_str = 'cox1'
            elif gene_str in ('co2', 'coii', 'cox2', 'cytochrome c oxidase subunit 2'):
                gene_str = 'cox2'
            elif gene_str in ('co3', 'coiii', 'cox3', 'cytochrome c oxidase subunit 3'):
                gene_str = 'cox3'
            elif gene_str in ('cob', 'cyb', 'cytb', 'cytochrome b'):
                gene_str = 'cytb'
                
            ## NAD 1, 2, 3, 4, 4L, 5 and 6          
            elif gene_str in ('nad1', 'nd1', 'nadh dehydrogenase subunit 1'):  
                 gene_str = 'nad1'
            elif gene_str in ('nad2', 'nd2', 'nadh dehydrogenase subunit 2'): 
                 gene_str = 'nad2'
            elif gene_str in ('nad3', 'nd3', 'nadh dehydrogenase subunit 3'): 
                 gene_str = 'nad3'
            elif gene_str in ('nad4', 'nd4', 'nadh dehydrogenase subunit 4'): 
                 gene_str = 'nad4'
            elif gene_str in ('nad4l', 'nd4l', 'nadh dehydrogenase subunit 4l'): 
                 gene_str = 'nad4l'
            elif gene_str in ('nad5', 'nd5', 'nadh dehydrogenase subunit 5'): 
                 gene_str = 'nad5'
            elif gene_str in ('nad6', 'nd6', 'nadh dehydrogenase subunit 6'):
                 gene_str = 'nad6'
            else:
                 continue
                 
            extracted_feat = feat.extract(record.seq)
            gene_seq = str(extracted_feat)
            
            # Check for a partial codon at the end
            remainder = len(extracted_feat) % 3
            clean_seq_for_translation = extracted_feat[:-remainder] if remainder != 0 else extracted_feat
            
            # set to_stop=True to automatically remove trailing stop codons (*)
            gene_prod = str(clean_seq_for_translation.translate(table=5, to_stop=True))
            #gene_prod = str(clean_seq_for_translation.translate(to_stop=True))#.replace('*', '')
            
            gene_rows.append({
                "file_id": record.id,
                "gene": gene_str,
                "s": int(feat.location.start),
                "e": int(feat.location.end),
                "strand": feat.location.strand,
                "sequence": gene_seq,           
                "protein": gene_prod,           
                "location": location,
                "organism": organism,
                "date": date
            })

# DataFrame
df_long = pd.DataFrame(gene_rows)

df_pivot = df_long.pivot(
    index=["file_id", "location", "organism", "date"], 
    columns="gene", 
    values=["s", "e", "sequence", "protein"]
)

df_pivot.columns = [f"{gene}_{metric}" for metric, gene in df_pivot.columns]

df_wide = df_pivot.reset_index()

# defining the structure  
desired_order = ['file_id',  'organism'] #location
genes = ['atp6', 'atp8', 'cox1', 'cox2', 'cox3', 'cytb', 'nad1', 'nad2', 'nad3', 'nad4', 'nad4l', 'nad5', 'nad6']

for g in genes:
    desired_order.extend([f"{g}_s", f"{g}_e", f"{g}_sequence", f"{g}_protein"])

#
existing_columns = [col for col in desired_order if col in df_wide.columns]
df_reordered = df_wide[existing_columns].copy()

#write to a csv
df_reordered = df_wide[existing_columns]
df_NCBI = df_reordered
df_NCBI.to_csv("genes_NCBI.csv", index=False)