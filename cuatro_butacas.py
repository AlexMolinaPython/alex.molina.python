# -*- coding: utf-8 -*-
"""Cuatro butacas

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XqA-UWiarpiqEdhKxJRQT3BN2hePsegm
"""

i=1
for V in range(1,5):
  for J in range(1,5):
    if J==V :
      continue
    for P in range(1,5):
      if P==V or P==J:
        continue
      for S in range(1,5):
        if S==V or S==J or S==P:
          continue
        print(i,':','V=',V,'J=',J,'P=',P,'S=',S)
        i+=1