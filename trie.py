suffixes = {}

with open('data/italian.txt.learn', 'r') as test:
  with open('data/italian.txt.learn.prediction', 'r') as predict:
    for count, line in enumerate(test):
      source = line.split()[0]
      test = line.split()[1:]
      train = predict.readline().split()[1:]
      
      for x in test:
        for y in train:
          if bool(x[-2:] == '+V') and bool(y[-2:] == '+V'): continue
          for i in xrange(min(len(x), len(y), len(source))):
            if x[i] != y[i] or x[i] != source[i]:
              suffix_from = source[i -  2:]
              suffix_my    = y[i - 2:]
              suffix_to = x[i - 2:]
          
              suffixes.setdefault(suffix_from, {}).setdefault((suffix_to, suffix_my), 0)
              suffixes[suffix_from][(suffix_to, suffix_my)] += 1
              break

    for suffix, typeCounts in suffixes.iteritems():
      for (x, y), z in typeCounts.iteritems():
        if x != y and z > 20:
          print z, suffix, typeCounts
          print
          break

