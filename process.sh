#!/usr/bin/sh

cat ./data/italian.txt.learn | awk -v OFS='\t' '{ print $1 }' > ./data/italian.txt.learn.dumb
cat ./data/italian.txt.learn.dumb | flookup -x italian.bin > ./data/italian.txt.learn.predict
./filter.py ./data/italian.txt.learn.predict > ./data/italian.txt.learn.prediction
