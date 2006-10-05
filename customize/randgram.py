#!/usr/local/bin/python2.4

######################################################################
# imports

import random
randint = random.randint

import deffile
tokenize_def = deffile.tokenize_def
import validate
validate_choices = validate.validate_choices


######################################################################
# globals

var = {}

def load_vars():
  f = open('matrixdef', 'r')
  line = f.readlines()
  f.close()
  
  i = 0
  while i < len(line):
    word = tokenize_def(line[i])
    if len(word) == 0:
      pass
    elif word[0] == 'Label':
      pass
    elif word[0] == 'Separator':
      pass
    elif word[0] == 'Check':
      vn = word[1]
      var[vn] = []
      var[vn].append('BOOLEAN')
    elif word[0] == 'Radio':
      vn = word[1]
      var[vn] = []
      i += 1
      while line[i] != '\n':
        word = tokenize_def(line[i])
        rval = word[1]
        var[vn].append(rval)
        i += 1
    elif word[0] == 'Text':
      vn = word[1]
      var[vn] = []
      var[vn].append(vn)
    i += 1


def random_grammar(choices_file):
  choice = {}
  for k in var.keys():
    v = var[k]
    if len(v) == 1 and v[0] == 'BOOLEAN':
      if randint(0, 1):
        choice[k] = 'on'
    else:
      choice[k] = v[randint(0, len(v) - 1)]

  f = open(choices_file, 'w')
  for k in choice.keys():
    f.write(k + '=' + choice[k] + '\n')
  f.close()


choices_file = 'rand_choices'
load_vars()
count = 0
while True:
  count += 1
  random_grammar(choices_file)
  wrong = validate_choices(choices_file)
  if len(wrong):
    f = open(choices_file, 'a')
    for k in wrong.keys():
      f.write(k + ': ' + wrong[k] + '\n')
    f.close()
  else:
    print 'Grammar #' + str(count) + ' validated'
    break