#!/usr/bin/env python

import sys

if __name__ == "__main__":
  if len(sys.argv) > 1:
    arg1 = sys.argv[1]
    print arg1
  else:
    print "Usage: python main.py [argument1]"
