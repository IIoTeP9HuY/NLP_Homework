#!/usr/bin/env python

def substituteEnd(s, src, dst):
  return s if s[len(src):] != src else s[:len(sec)] + dst


fileName = raw_input()
inputFile = open(fileName, 'r')

currentPredictions = []

ConjToSuffix = {'1C':'are', '2C':'ere', '3C':'ire'}

for line in inputFile:
  if line == '\n':
    minLen = min(len(prediction[0]) for prediction in currentPredictions)
    minPredictions = [prediction for prediction in currentPredictions if len(prediction[0]) == minLen]
    minPrediction = minPredictions[0]
    
    
    print(minPrediction[0] + '\t' + minPrediction[1])
    currentPredictions = []
  else:
    line = line.rstrip().split('\t')
    sourceWord = line[0]
    prediction = line[1].split('+')
    
    if prediction[1] != '?':
      suffix = ConjToSuffix[prediction[3]]
      if len(prediction[0]) > 0 and suffix[0] == prediction[0][-1]:
        prediction[0] = prediction[0][:-1:]
      prediction[0] += suffix

      prediction[0] = substituteEnd(prediction[0], 'glire', 'gliare')
      if prediction[0][-7] != 's':
        prediction[0] = substituteEnd(prediction[0], 'cchire', 'cchiare')



    prediction = prediction[:2]
    if prediction[1] == '?':
      prediction[0] = sourceWord
      prediction[1] = 'N'

    currentPredictions.append((sourceWord, prediction[0] + '+' + prediction[1]))

