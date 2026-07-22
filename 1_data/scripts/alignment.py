# =======================Import Packages / Libraries===========================
import pandas as pd
# =============================================================================

# =============================================================================
# prealignment file, concatenated
# ============================================================================= 
complete_df = pd.read_csv("complete_abv_loc_typ_db_.csv")
print(complete_df.columns)

import pandas as pd

genes_order = [ 'nad2', 'cox1', 'cox2', 'atp8', 'atp6', 'cox3', 'nad3', 'nad5',  'nad4', 'nad4l', 'nad6', 'cytb', 'nad1']

df_target = complete_df
output_fasta_file = "Apis_m_mtDNA.fasta"

with open(output_fasta_file, "w") as fasta_out:
    for idx, row in df_target.iterrows():
        # Extracted directly from your precise column listing
        sample_id = row["file_id"]
        fasta_header = row["seq_name"]

        valid_sequences = []

        # Pull each gene sequence in our precise, designated order
        for gene in genes_order:
            seq_col = f"{gene}_sequence"

            # Safely extract sequence data if it exists and isn't empty/NaN
            if seq_col in df_target.columns and pd.notna(row[seq_col]):
                valid_sequences.append(str(row[seq_col]).strip())

        # Join the valid gene blocks together, separating each with 'XXXXXX'
        final_stitched_string = "NNNNNN".join(valid_sequences)

        # Only write out to the FASTA file if we successfully gathered sequences
        if final_stitched_string:
            # Format the standard FASTA header descriptor line
            fasta_out.write(f">{fasta_header}\n")

            # Write out the sequence block
            fasta_out.write(f"{final_stitched_string}\n")

print(f"'{output_fasta_file}' is generated")

