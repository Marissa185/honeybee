#!/bin/sh 
#SBATCH --job-name="sra_parallel"                                                              
#SBATCH -o /data4/msc/home/msc25235665/thesis/scripts/sra/logs/sra_parallel_%A_%a.out                                             
#SBATCH -e /data4/msc/home/msc25235665/thesis/scripts/sra/logs/sra_parallel_%A_%a.err                                             
#SBATCH -N 1                                                                               
#SBATCH -n 6 
module load Anaconda3
conda activate 1_data

while read line
do 
  echo "Acc id : $line"
  parallel-fastq-dump  --sra-id $line --threads 4 --outdir out/ --split-files --gzip
  echo "completed : $line" 
done < complete_SRR_Acc.csv

