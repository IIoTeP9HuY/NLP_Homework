#!/usr/bin/sh

foma -l ./italian_vova.foma

echo Building prediction...
cat ./data/italian.txt.test.clean | flookup italian.bin > ./data/italian.txt.test.predict

echo Filtering prediction...
./filter.py <<< ./data/italian.txt.test.predict > ./data/italian.txt.test.prediction

#echo Evaluating...
#python2 ./data/evaluate.py ./data/italian.txt.learn ./data/italian.txt.learn.prediction

#echo Cleaning...
#rm ./data/italian.txt.learn.clean
