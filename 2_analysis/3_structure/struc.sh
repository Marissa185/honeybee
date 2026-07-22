#!/bin/bash

# Define parameters
MAINPARAMS="mainparams"
EXTRAPARAMS="extraparams"
MIN_K=1
MAX_K=10
REPLICATES=3

# Loop through K
for K in $(seq $MIN_K $MAX_K); do
    # Loop through each replicate
    for REP in $(seq 1 $REPLICATES); do
        echo "Running K=$K, Replicate=$REP..."
        
        # Define a unique output filename
        OUT_NAME="outfile_K${K}_rep${REP}"
        
        # Run STRUCTURE using command line overrides
        ./structure -m $MAINPARAMS -e $EXTRAPARAMS -K $K -o $OUT_NAME
    done
done

echo "All STRUCTURE runs completed!"
