# -*- coding: utf-8 -*-
"""Exercici gràfic paràbola i línea recta - Àlex Molina

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GiptHlwWTW4Z8oXGxkTGNmHpkT8OW7rK
"""

import numpy as np   
import matplotlib.pyplot as plt

a=float(input("Posa la a: "))
b=float(input("Posa la b: "))
c=float(input("Posa la c: "))

if a != 0:
  xmin=b/a          #calcul xmin
  xmax=-2*b/a       #calcul xmax

  x=np.linspace(min(xmin,xmax), max(xmin,xmax),200)   #los puntos de la recta,
  y=x**2*a+b*x+c

  plt.axhline(y=0, color="red", linestyle="-")
  plt.axvline(x=0, color="red")
  plt.xlim(min(xmin,xmax),max(xmin,xmax))

  plt.xlabel("eje x", fontsize=15, color='black', alpha=0.8)
  plt.ylabel("eje y", fontsize=15, color='black', alpha=0.8)
  plt.title("Ejercicio gráfica")
  plt.xlim(min(xmin,xmax),max(xmin,xmax))
  x2=('$x^2$')
  tit='Gàfica de: y='+str(a)+x2+ ' + '+str(b)+'x + '+str(c)+'\n'
  plt.title(tit, fontsize=20, color='black')
  
  vx=-b/(2*a)
  vy=a*vx**2+b*vx+c

  plt.plot(vx, vy, 'o-r')

  plt.plot(x,y)
  plt.show()


else:
  a=b
  b=c
  xmin=b/a          #calcul xmin
  xmax=-2*b/a       #calcul xmax

  x=np.linspace(xmin, xmax, 30)
  y=x*a+b

  plt.axhline(y=0, color="red", linestyle="-")
  plt.axvline(x=0, color="red")
  plt.xlim(min(xmin,xmax),max(xmin,xmax))
  #plt.legend(fontsize=18)

  plt.xlabel("eje x", fontsize=15, color='black', alpha=0.8)
  plt.ylabel("eje y", fontsize=15, color='black', alpha=0.8)
  plt.title("Ejercicio gráfica")
  plt.xlim(min(xmin,xmax),max(xmin,xmax))
  tit='Gàfica de: y='+str(a)+'x +'+str(b)+'\n'
  plt.title(tit, fontsize=20, color='black')

  plt.plot(x,y)
  plt.show()