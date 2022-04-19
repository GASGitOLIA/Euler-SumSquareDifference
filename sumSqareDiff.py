# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 09:17:57 2017

@author: rmaskus
"""

sumOfSquares = 0
squareOfSums = 0

for i in range (1, 101):
    sumOfSquares = sumOfSquares + i**2
    squareOfSums = squareOfSums + 1

squareOfSums = squareOfSums**2

print("The sum of the squares is:", sumOfSquares)
print("The square of the sums is:", squareOfSums)
print("The difference of squares is", sumOfSquares - squareOfSums)
