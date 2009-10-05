#!/usr/bin/env python3
#coding:utf-8 --<>
# Purpose: Convertir texto a codigo compilable en brainfuck
# Created: 04/10/09

from sys import argv, stdout

fin = open(argv[1], "rU", buffering = 1024)

fout = open(argv[1][:-4]+".bf", "w", buffering = 1024*1024)

charCount = 0

for line in fin:
    for word in line:
        for char in word:
            charCount+=1

#inicializamos variables
print("++++++++++[", file = fout)

for i in range(0, charCount):
    print(">++++++++++", file = fout)

for i in range(0, charCount):
    print("<", file = fout, end= "")

print("-]", file = fout)

fin.seek(0)

for line in fin:
    for word in line:
        for char in word:
            n = 100
            while( chr(n) != char):
                print("-" if char < chr(n) else "+", file = fout, end = "")
                n = n - 1 if char < chr(n) else n + 1
            print(".>", file = fout)