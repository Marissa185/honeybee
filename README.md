# About the Project
The project was performed by Marissa185 (Marissa) as part of the Genomics Project. The Supplementary Data is located in the `3_output` folder. The other necessary input and cli commands for reproducibility are present in `1_data` and `2_analysis`. All of these analysis were run on a linux mint system apart from DnaSP which used a windows 11 system.

## About the directory and files
The layout of the folder is as follows:  
```
honeybee
├── 1_data                                                                              # The data and its relevent information
│   ├── bioproject.csv
│   ├── complete.csv
│   ├── fasta
│   │   ├── Apis_m_mtDNA_NA_subset.fst
│   │   └── Apis_m_mtDNA_NA_total.fst
│   ├── genbank.csv
│   ├── gene_order.csv
│   ├── given.csv
│   ├── location_abv.csv
│   ├── organism_abv.csv
│   ├── scripts
│   │   ├── alignment.py
│   │   ├── bioproject_sra.sh
│   │   ├── genbank_bioproject.py
│   │   ├── given.py
│   │   └── mitoz.sh
│   ├── subset.csv
│   └── types_db_abv.csv
├── 2_analysis                                                                         # The analysis performed on the data
│   ├── 1_phylogeny
│   │   ├── cli.txt
│   │   └── genewise_BIC.csv
│   ├── 2_hyphy
│   │   ├── forground.txt
│   │   ├── hyphy_cli_commands.txt
│   │   ├── irl.txt
│   │   ├── label-tree.bf
│   │   └── remove-duplicates.bf
│   └── 3_structure
│       ├── extraparams
│       ├── fasta to structure haploid 9-7-20.R
│       ├── mainparams
│       ├── output_rm.prn
│       ├── pophelper 9-18-20.R
│       ├── struc.sh
│       └── structure
├── 3_output                                                                          # The output files generated from the analysis
│   ├── 1_phylogeny
│   │   ├── complete_380
│   │   │   ├── Apis_m_mtDNA_NA_total.fst.svg
│   │   │   ├── BIC_K3Pu+F+R3
│   │   │   │   ├── Apis_m_mtDNA_NA.fst.log
│   │   │   │   ├── Apis_m_mtDNA_NA_total.fst.bionj
│   │   │   │   ├── Apis_m_mtDNA_NA_total.fst.ckp.gz
│   │   │   │   ├── Apis_m_mtDNA_NA_total.fst.contree
│   │   │   │   ├── Apis_m_mtDNA_NA_total.fst.csv
│   │   │   │   ├── Apis_m_mtDNA_NA_total.fst.iqtree
│   │   │   │   ├── Apis_m_mtDNA_NA_total.fst.log
│   │   │   │   ├── Apis_m_mtDNA_NA_total.fst.mldist
│   │   │   │   ├── Apis_m_mtDNA_NA_total.fst.splits.nex
│   │   │   │   ├── Apis_m_mtDNA_NA_total.fst.treefile
│   │   │   │   ├── Apis_m_mtDNA_NA_total.fst.uniqueseq.phy
│   │   │   │   ├── Apis_m_mtDNA_NA_total.svg
│   │   │   │   └── supports
│   │   │   │       ├── Apis_m_mtDNA_NA_collapsed.svg
│   │   │   │       ├── Apis_m_mtDNA_NA_total.fst.treefile_
│   │   │   │       ├── Apis_m_mtDNA_NA_total.fst.treefile.collapsed
│   │   │   │       └── Apis_m_mtDNA_NA_total.fst.treefile.log
│   │   │   ├── iqtree_modelsel
│   │   │   │   ├── Apis_m_mtDNA_NA.fst.log
│   │   │   │   ├── Apis_m_mtDNA_NA_total.fst.ckp.gz
│   │   │   │   ├── Apis_m_mtDNA_NA_total.fst.iqtree
│   │   │   │   ├── Apis_m_mtDNA_NA_total.fst.log
│   │   │   │   ├── Apis_m_mtDNA_NA_total.fst.model.gz
│   │   │   │   ├── Apis_m_mtDNA_NA_total.fst.treefile
│   │   │   │   └── Apis_m_mtDNA_NA_total.fst.uniqueseq.phy
│   │   │   └── remade_w_bsupport_kidents
│   │   │       ├── Apis_m_mtDNA_NA_subset.fst.pdf
│   │   │       ├── Apis_m_mtDNA_NA_total.fst.bionj
│   │   │       ├── Apis_m_mtDNA_NA_total.fst.ckp.gz
│   │   │       ├── Apis_m_mtDNA_NA_total.fst.contree
│   │   │       ├── Apis_m_mtDNA_NA_total.fst.iqtree
│   │   │       ├── Apis_m_mtDNA_NA_total.fst.log
│   │   │       ├── Apis_m_mtDNA_NA_total.fst.mldist
│   │   │       ├── Apis_m_mtDNA_NA_total.fst.pdf
│   │   │       ├── Apis_m_mtDNA_NA_total.fst.png
│   │   │       ├── Apis_m_mtDNA_NA_total.fst.splits.nex
│   │   │       ├── Apis_m_mtDNA_NA_total.fst.svg
│   │   │       └── Apis_m_mtDNA_NA_total.fst.treefile
│   │   └── subset_132
│   │       ├── 1_model_selection
│   │       │   ├── Apis_m_mtDNA_NA_subset.fst.ckp.gz
│   │       │   ├── Apis_m_mtDNA_NA_subset.fst.iqtree
│   │       │   ├── Apis_m_mtDNA_NA_subset.fst.log
│   │       │   ├── Apis_m_mtDNA_NA_subset.fst.model.gz
│   │       │   └── Apis_m_mtDNA_NA_subset.fst.treefile
│   │       ├── 2_BIC_HKY+F+I
│   │       │   ├── Apis_m_mtDNA_NA_subset.fst.bionj
│   │       │   ├── Apis_m_mtDNA_NA_subset.fst.ckp.gz
│   │       │   ├── Apis_m_mtDNA_NA_subset.fst.contree
│   │       │   ├── Apis_m_mtDNA_NA_subset.fst.iqtree
│   │       │   ├── Apis_m_mtDNA_NA_subset.fst.log
│   │       │   ├── Apis_m_mtDNA_NA_subset.fst.mldist
│   │       │   ├── Apis_m_mtDNA_NA_subset.fst_pages-to-jpg-0001.jpg
│   │       │   ├── Apis_m_mtDNA_NA_subset.fst.pdf
│   │       │   ├── Apis_m_mtDNA_NA_subset.fst.splits.nex
│   │       │   ├── Apis_m_mtDNA_NA_subset.fst.svg
│   │       │   └── Apis_m_mtDNA_NA_subset.fst.treefile
│   │       ├── subset132_seaview.png
│   │       └── subset132_splitstree.pdf
│   ├── 2_hyphy
│   │   ├── 1_FUBAR
│   │   │   ├── 01_NAD2_unique.fst.FUBAR.cache
│   │   │   ├── 01_NAD2_unique.fst.FUBAR.json
│   │   │   ├── 02_COX1_unique.fst.FUBAR.cache
│   │   │   ├── 02_COX1_unique.fst.FUBAR.json
│   │   │   ├── 03_COX2_unique.fst.FUBAR.cache
│   │   │   ├── 03_COX2_unique.fst.FUBAR.json
│   │   │   ├── 04_ATP8_unique.fst.FUBAR.cache
│   │   │   ├── 04_ATP8_unique.fst.FUBAR.json
│   │   │   ├── 05_ATP6_unique.fst.FUBAR.cache
│   │   │   ├── 05_ATP6_unique.fst.FUBAR.json
│   │   │   ├── 06_COX3_unique.fst.FUBAR.cache
│   │   │   ├── 06_COX3_unique.fst.FUBAR.json
│   │   │   ├── 07_NAD3_unique.fst.FUBAR.cache
│   │   │   ├── 07_NAD3_unique.fst.FUBAR.json
│   │   │   ├── 08_NAD5_unique.fst.FUBAR.cache
│   │   │   ├── 08_NAD5_unique.fst.FUBAR.json
│   │   │   ├── 09_NAD4_unique.fst.FUBAR.cache
│   │   │   ├── 09_NAD4_unique.fst.FUBAR.json
│   │   │   ├── 10_NAD4L_unique.fst.FUBAR.cache
│   │   │   ├── 10_NAD4L_unique.fst.FUBAR.json
│   │   │   ├── 11_NAD6_unique.fst.FUBAR.cache
│   │   │   ├── 11_NAD6_unique.fst.FUBAR.json
│   │   │   ├── 12_CYTB_unique.fst.FUBAR.cache
│   │   │   ├── 12_CYTB_unique.fst.FUBAR.json
│   │   │   ├── 13_NAD1_unique.fst.FUBAR.cache
│   │   │   ├── 13_NAD1_unique.fst.FUBAR.json
│   │   │   ├── Apis_m_mtDNA_NA_subset_unique.fst.FUBAR.cache
│   │   │   └── Apis_m_mtDNA_NA_subset_unique.fst.FUBAR.json
│   │   ├── 2_MEME
│   │   │   ├── 01_NAD2_unique.fst.MEME.json
│   │   │   ├── 02_COX1_unique.fst.MEME.json
│   │   │   ├── 03_COX2_unique.fst.MEME.json
│   │   │   ├── 04_ATP8_unique.fst.MEME.json
│   │   │   ├── 05_ATP6_unique.fst.MEME.json
│   │   │   ├── 06_COX3_unique.fst.MEME.json
│   │   │   ├── 07_NAD3_unique.fst.MEME.json
│   │   │   ├── 08_NAD5_unique.fst.MEME.json
│   │   │   ├── 09_NAD4_unique.fst.MEME.json
│   │   │   ├── 10_NAD4L_unique.fst.MEME.json
│   │   │   ├── 11_NAD6_unique.fst.MEME.json
│   │   │   ├── 12_CYTB_unique.fst.MEME.json
│   │   │   ├── 13_NAD1_unique.fst.MEME.json
│   │   │   └── Apis_m_mtDNA_NA_subset_unique.fst.MEME.json
│   │   ├── 3_aBSREL
│   │   │   ├── 01_NAD2_unique.fst.ABSREL.json
│   │   │   ├── 02_COX1_unique.fst.ABSREL.json
│   │   │   ├── 03_COX2_unique.fst.ABSREL.json
│   │   │   ├── 04_ATP8_unique.fst.ABSREL.json
│   │   │   ├── 05_ATP6_unique.fst.ABSREL.json
│   │   │   ├── 06_COX3_unique.fst.ABSREL.json
│   │   │   ├── 07_NAD3_unique.fst.ABSREL.json
│   │   │   ├── 08_NAD5_unique.fst.ABSREL.json
│   │   │   ├── 09_NAD4_unique.fst.ABSREL.json
│   │   │   ├── 10_NAD4L_unique.fst.ABSREL.json
│   │   │   ├── 11_NAD6_unique.fst.ABSREL.json
│   │   │   ├── 12_CYTB_unique.fst.ABSREL.json
│   │   │   ├── 13_NAD1_unique.fst.ABSREL.json
│   │   │   └── Apis_m_mtDNA_NA_subset_unique.fst.ABSREL.json
│   │   ├── 4_FEL
│   │   │   ├── 01_NAD2_unique.fst.FEL.json
│   │   │   ├── 02_COX1_unique.fst.FEL.json
│   │   │   ├── 03_COX2_unique.fst.FEL.json
│   │   │   ├── 05_ATP6_unique.fst.FEL.json
│   │   │   ├── 06_COX3_unique.fst.FEL.json
│   │   │   ├── 07_NAD3_unique.fst.FEL.json
│   │   │   ├── 08_NAD5_unique.fst.FEL.json
│   │   │   ├── 09_NAD4_unique.fst.FEL.json
│   │   │   ├── 10_NAD4L_unique.fst.FEL.json
│   │   │   ├── 11_NAD6_unique.fst.FEL.json
│   │   │   ├── 12_CYTB_unique.fst.FEL.json
│   │   │   ├── 13_NAD1_unique.fst.FEL.json
│   │   │   └── Apis_m_mtDNA_NA_subset_unique.fst.FEL.json
│   │   └── Apis_m_mtDNA_NA_subset_clean.fst.cFEL.json
│   ├── 3_structure
│   │   ├── outfile_K10_rep1_f
│   │   ├── outfile_K10_rep2_f
│   │   ├── outfile_K10_rep3_f
│   │   ├── outfile_K1_rep1_f
│   │   ├── outfile_K1_rep2_f
│   │   ├── outfile_K1_rep3_f
│   │   ├── outfile_K2_rep1_f
│   │   ├── outfile_K2_rep2_f
│   │   ├── outfile_K2_rep3_f
│   │   ├── outfile_K3_rep1_f
│   │   ├── outfile_K3_rep2_f
│   │   ├── outfile_K3_rep3_f
│   │   ├── outfile_K4_rep1_f
│   │   ├── outfile_K4_rep2_f
│   │   ├── outfile_K4_rep3_f
│   │   ├── outfile_K5_rep1_f
│   │   ├── outfile_K5_rep2_f
│   │   ├── outfile_K5_rep3_f
│   │   ├── outfile_K6_rep1_f
│   │   ├── outfile_K6_rep2_f
│   │   ├── outfile_K6_rep3_f
│   │   ├── outfile_K7_rep1_f
│   │   ├── outfile_K7_rep2_f
│   │   ├── outfile_K7_rep3_f
│   │   ├── outfile_K8_rep1_f
│   │   ├── outfile_K8_rep2_f
│   │   ├── outfile_K8_rep3_f
│   │   ├── outfile_K9_rep1_f
│   │   ├── outfile_K9_rep2_f
│   │   └── outfile_K9_rep3_f
│   ├── 4_partimatrix
│   │   ├── 01_Apis_m_mtDNA_NA_NAD2.pdf
│   │   ├── 02_Apis_m_mtDNA_NA_COX1.pdf
│   │   ├── 03_Apis_m_mtDNA_NA_COX2.pdf
│   │   ├── 04_Apis_m_mtDNA_NA_ATP8.pdf
│   │   ├── 05_Apis_m_mtDNA_NA_ATP6.pdf
│   │   ├── 06_Apis_m_mtDNA_NA_COX3.pdf
│   │   ├── 07_Apis_m_mtDNA_NA_NAD3.pdf
│   │   ├── 08_Apis_m_mtDNA_NA_NAD5.pdf
│   │   ├── 09_Apis_m_mtDNA_NA_NAD4.pdf
│   │   ├── 10_Apis_m_mtDNA_NA_NAD4L.pdf
│   │   ├── 11_Apis_m_mtDNA_NA_NAD6.pdf
│   │   ├── 12_Apis_m_mtDNA_NA_CYTB.pdf
│   │   ├── 13_Apis_m_mtDNA_NA_NAD1.pdf
│   │   ├── Apis_m_mtDNA_NA_subset_12.pdf
│   │   └── Apis_m_mtDNA_NA_subset_3.pdf
│   └── DnaSP_haplotype.txt
└── README.md

25 directories, 201 files
```
## About the folders and their files
### 1_data
The folder has 2 subfolders and multiple `*.csv` files:
- `fasta`  : this folder has the complete (380) and subset (132) aligned fasta files.
- `scripts`: this folder has the scripts used to optain sequences from the given files, GenBank and BioProject repositories.
- `*.csv`  : these files contain relevant information pertaining to the sequences and their labels

### 2_analysis
The folder has 3 subfolders:
- `1_phylogeny`     : this folder contains commands used for iqtree3 in `cli.txt` and genewise selected base substitution models according to BIC in `genewise_BIC.csv`.
- `2_hyphy`         : this folder has the scripts `remove-duplicates.bf`, `label-tree.bf` used to clean the sequences and label sequences for contrast-fel respectively. The `forground.txt` and `irl.txt` are a list of sequences required for labelling in contrast-fel. The commands used for running hyphy and its respective subprograms are listed in `hyphy_cli_commands.txt`.
- `3_structure`     : this folder contains the programme files required to run STRUCTURE as `structure`, `mainparams` and `extraparams`. The `output_rm.prn` was used as an input file for running STRUCTURE. The `fasta to structure haploid 9-7-20.R` and `pophelper 9-18-20.R` was directly used and modified from the youtube videos: [haploid](https://youtu.be/EO6AtZPgz1g) and [pophelper](https://youtu.be/HJgJ4fVJq2s), respectively. The `struc.sh` was used to run STRUCTURE as a loop for 3 replicates for clusters ranging from 1 to 10.

### 3_output
The folder has 4 subfolders and a file:
- `1_phylogeny`   : this folder contains 2 main subfolders which contain the iqtree analysis done for the complete 380 sequences `complete_380` and the subset 132 sequences `subset_132`. The `subset_132` also contains the a splitstree/network view of the sequences as pdf. The `complete_380` also contains the a tree view of the sequences as pdf. There are other intemediatary also present
- `2_hyphy`       : this folder contains the genewise output files of FUBAR, MEME, aBSREL, and FEL as `1_FUBAR`, `2_MEME`, `3_aBSREL`, and`4_FEL` respectively. And contrast-FEL as `Apis_m_mtDNA_NA_subset_clean.fst.cFEL.json`.
- `3_structure` : this folder contains the output files of the STRUCTURE analysis used to generate the STURCTURE plot.
- `4_partimatrix` : this folder contains the output files of the PartiMatrix analysis. Files ranging between `[01-13]_Apis_m_mtDNA_NA_[gene].pdf` are output of the genewise matrix. The matrix of `Apis_m_mtDNA_NA_subset_12.pdf` are of complete codon 1 and 2 and `Apis_m_mtDNA_NA_subset_3.pdf` is of complete codon 3.
