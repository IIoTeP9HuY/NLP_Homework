#!/usr/bin/env python

fileName = input()
inputFile = open(fileName, 'r')

currentPredictions = []

for line in inputFile:
	if line == '\n':
		minLen = min(len(prediction[0]) for prediction in currentPredictions)
		minPredictions = [prediction for prediction in currentPredictions if len(prediction[0]) == minLen]
		minPrediction = minPredictions[0]
		print(minPrediction[0] + '\t' + minPrediction[1])
		currentPredictions = []
	else:
		line = line.split('\t')
		sourceWord = line[0]
		prediction = line[1].split('+')[:2]
		if prediction[1] == '?\n':
			prediction[0] = sourceWord
			prediction[1] = 'N'
		currentPredictions.append((sourceWord, prediction[0] + '+' + prediction[1]))

