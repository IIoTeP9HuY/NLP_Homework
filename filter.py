#!/usr/bin/env python

fileName = input()
inputFile = open(fileName, 'r')

currentPredictions = []

for line in inputFile:
	if line == '\n':
		minLen = min(len(prediction[0]) for prediction in currentPredictions)
		minPredictions = [prediction for prediction in currentPrediction if len(prediction[0]) == minLen]
		print(minPredictions)
		currentPredictions = []
	else:
		line = line.split('+')[:2]
		currentPredictions.append(line)

