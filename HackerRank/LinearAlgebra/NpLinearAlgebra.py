#Emilio Sebastian Conde Ludena
#July 6, 2025
#From: https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true

#install package as venv
#import Numpy Library
import numpy as np

#cast int input, is the size of matrix i.e 2 for 2x2
numberInput = int(input())

#initialize a matrix of lis
matrix = []

#for loop for range of numberInput
for i in range(numberInput):
    #take input from user as string
    rowInput = input()
    #split string into a list
    rowValues = rowInput.split()
    #create empyt list of rows
    rowFloatsList = []
    #for loop row values
    for value in rowValues:
        #cast string to float
        floatValue = float(value)
        #append to rowFloats list
        rowFloatsList.append(floatValue)

    #append to matrix the rowFloatsMatrix
    matrix.append(rowFloatsList)

#use Numpy method
determinant = np.linalg.det(matrix)

#round to 2 decimals and print
print(round(determinant, 2))
