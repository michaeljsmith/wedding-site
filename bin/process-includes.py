#!/usr/bin/env python

from __future__ import print_function

import re
import os.path
import sys

includeRegEx = re.compile(r'\s*\<include file="(.*)"\>\s*')

def includeFile(path):
  processFile(path)

def processStream(path, stream):
  for line in stream:
    match = includeRegEx.match(line)
    if match != None:
      relativePath = match.group(1)
      includePath = os.path.join(os.path.dirname(path), relativePath)
      includeFile(includePath)
    else:
      print(line, end="")

def processFile(path):
  try:
    f = open(path)
  except IOError as e:
    print('Unable to open file "' + path + '": ', e, file=sys.stderr)
    sys.exit(1)

  processStream(path, f)

def main():
  if len(sys.argv) != 2:
    print("Invalid arguments.", file=sys.stderr)
    sys.exit(1)

  inputFile = sys.argv[1]
  processFile(inputFile)

if __name__ == '__main__':
  main()
