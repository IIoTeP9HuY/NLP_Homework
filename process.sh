#!/usr/bin/sh

foma -l ./italian_vova.foma

echo Building dumb data...
cat ./data/italian.txt.learn | awk -v OFS='\t' '{ print $1 }' > ./data/italian.txt.learn.clean

echo Building prediction...
cat ./data/italian.txt.learn.clean | flookup italian.bin > ./data/italian.txt.learn.predict

echo Filtering prediction...
python filter.py <<< ./data/italian.txt.learn.predict > ./data/italian.txt.learn.prediction

echo Evaluating...
python ./data/evaluate.py ./data/italian.txt.learn ./data/italian.txt.learn.prediction

echo Cleaning...
rm ./data/italian.txt.learn.clean