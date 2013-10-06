#!/usr/bin/env python

fileName = raw_input()
inputFile = open(fileName, 'r')

verbPredictions = []
nounPredictions = []
adjPredictions  = []
currentPredictions = []
sourceWord = ''

conjToEnding = {'1C':'are', '2C':'ere', '3C':'ire'}

def getVerbPrediction(verbPredictions):
  if len(verbPredictions) == 0:
    return None
  
  minLen  = min([len(p[0]) for p in verbPredictions])
  shortestStems = [(p[0], p[3]) for p in verbPredictions if len(p[0]) == minLen]
  areShortestStems = [(stem, conj) for (stem, conj) in shortestStems if conj == '1C']

  stem, conj = areShortestStems[0] if len(areShortestStems) != 0 else shortestStems[0]
  return stem + conjToEnding.setdefault(conj, 'are') + '+V'


def getNounPrediction(nounPredictions):
  if len(nounPredictions) == 0:
    return None

  minLen  = min([len(p[0]) for p in nounPredictions])
  x = [p for p in nounPredictions if len(p[0]) == minLen][0]
  return x[0] + '+N'



for line in inputFile:
  if line == '\n':


    # Predictinf vp and modifying if necessary
    vp = getVerbPrediction(verbPredictions)
    if sourceWord[-5:] in ['avamo', 'asser']: vp = sourceWord[:-5] + 'are+V'
    if sourceWord[-5:] == 'ssimo': vp = sourceWord[:-5] + 're+V'
    if sourceWord[-5:] == 'ebber': vp = sourceWord[:-5] + 'e+V'
    if sourceWord[-4:] == 'rono':  vp = sourceWord[:-4] + 're+V'
    if sourceWord[-4:] == 'ebbe':  vp = sourceWord[:-4] + 'e+V'
    if sourceWord[-3:] in ['ata', 'ati']:  vp = sourceWord[:-3] + 'are+V'
    if sourceWord[-2:] in ['an', 'ar']:    vp = sourceWord[:-2] + 'are+V'
    
    # Predicting Noun
    np = getNounPrediction(nounPredictions)
    if sourceWord[-3:] in ['ate']:  np = None

    # Predicting Adjective
    ap = None
    if np == None and vp == None and ap == None: ap = sourceWord[:-1] + 'o+A'


    if sourceWord[-4:] == 'assi':
      vp = sourceWord[-4:] + 'are+V'
      np = None
      ap = None


    # Modifying knowing all predictions
    if np != None and sourceWord[-4:] == 'rono' and np[-6:] == 'rono+N':
      vp = np[:-6] + 're+V'
      np = None
    #if np != None and sourceWord[-6:] == 'assimo' and np[-8:] == 'assimo+N':
    #      vp = sourceWord[-6:] + 'are+V'
    #      np = None

    if np != None and sourceWord[-2:] == 're' and np[-4:] == 'ra+N':
      vp = np[:-4] + 're+V'
      np = None


    if ap != None and ap[-5:] == 'roo+A':
      vp = ap[:-5] + 're+V'
      ap = None
#if ap != None and sourceWord[-5:] == 'asser' and ap[-7:] == 'asseo+A':
#      vp = ap[:-5] + 'are+V'
#      ap = None

#if np != None and np[-6:] == 'rono+N':
#      vp = np[:-6] + 're+V'



    answer = sourceWord
    for w in [vp, np, ap]:
      if w != None:
        answer += '\t' + w

    print answer
  
    #nounPredictions = plausibleVerbPredictions(nounPredictions)
    #adjPredictions  = plausibleVerbPredictions(adjPredictions)
    #if sourceWord[-9:] == 'nerebbero': vp = sourceWord[:-9] + 'nare+V'
    
    #elif sourceWord[-4:] == 'ammo': vp = sourceWord[:-4] + 'are+V'
    #elif sourceWord[-4:] == 'sser': vp = sourceWord[:-4] + 're+V'

    verbPredictions = []
    adjPredictions  = []
    nounPredictions = []
  
  else:
    sourceWord, stemWithModifiers = line.split()
    stemWithModifiers = stemWithModifiers.split('+')
    type = stemWithModifiers[1]
      
    if type == 'V': verbPredictions.append(stemWithModifiers)
    if type == 'N': nounPredictions.append(stemWithModifiers)
    if type == 'A': adjPredictions.append(stemWithModifiers)
