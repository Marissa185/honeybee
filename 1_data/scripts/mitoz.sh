#!/bin/sh
#SBATCH --job-name="smito"
#SBATCH -o /data4/msc/home/msc25235665/thesis/scripts/sra/logs/smitoz_%A_%a.out
#SBATCH -e /data4/msc/home/msc25235665/thesis/scripts/sra/logs/smitoz_%A_%a.err
#SBATCH -N 1
#SBATCH --mem=50G
#SBATCH --mail-type=ARRAY_TASKS,FAIL
#"$SLURM_ARRAY_TASK_ID"
#SBATCH -p highmem

# Activate env
module load Anaconda3
conda activate /data4/msc/home/msc25235665/mitoz3.6

# Base directories
baseDir="/data4/msc/home/msc25235665/thesis/scripts/sra"
selectedDir="/data4/msc/home/msc25235665/thesis/scripts/sra/2_selected"
mitozDir="/data4/msc/home/msc25235665/thesis/scripts/sra/3_mito"
finalDir="/data4/msc/home/msc25235665/thesis/scripts/sra/4_final"
tmpDir="/data4/msc/home/msc25235665/thesis/scripts/sra/8_stmp"

# the i links with the slrum array batch
i="$SLURM_ARRAY_TASK_ID"

# This searches for files starting precisely with "i_" (e.g., 1_ or 2_)
forward_file=$(ls "${selectedDir}"/${i}_*_1.fastq.gz 2>/dev/null)

# Ensure the file actually exists; exit cleanly if a number is missing
if [ ! -f "${forward_file}" ]; then
    echo "Error: No forward file found matching prefix ${i}_"
    exit 1
fi

# 3. Extract variables and define paths
filename=$(basename "${forward_file}")
prefix="${filename%_1.fastq.gz}"
id="${prefix#*_}"

forward="${selectedDir}/${i}_${id}_1.fastq.gz"
reverse="${selectedDir}/${i}_${id}_2.fastq.gz"

cd "${mitozDir}"
outDir="${i}_${id}"
mkdir -p "${mitozDir}/${outDir}"
cd "${mitozDir}/${outDir}"

echo "-------------------------------------------------------"
echo "Starting MitoZ on Sample ID: $id"
echo "Forward read: ${forward}"
echo "Reverse read: ${reverse}"
echo "Out Dir: ${mitozDir}/${outDir}"
echo "Selected Dir: ${selectedDir}"
echo "mitoz Dir: ${mitozDir}"
echo "final Dir: ${finalDir}"
echo "-------------------------------------------------------"

mitoz all \
  --outprefix "${outDir}" \
  --thread_number 16 \
  --clade Arthropoda \
  --genetic_code 5 \
  --species_name "Apis mellifera" \
  --fq1 "${forward}" \
  --fq2 "${reverse}" \
  --fastq_read_length 150 \
  --data_size_for_mt_assembly 3,0 \
  --assembler megahit \
  --kmers_megahit 59 79 99 \
  --memory 50 \
  --requiring_taxa Arthropoda

cp *.result/*.megahit.mitogenome.fa.result/*.megahit.mitogenome.fa_mitoscaf.fa.gbf.cds.fasta "${finalDir}/."
cp mt_annotation/tmp_*.megahit.mitogenome.fa_mitoscaf.fa/*.megahit.mitogenome.fa_mitoscaf.fa "${tmpDir}/."

