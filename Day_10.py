#!/bin/python3
#Max no of consicutive '1' in an binary number!
import math
import os
import random
import re
import sys

def consicutive(n):
    s = bin(n)[2:]
    m = max(len(group) for group in s.split('0'))
    return m
 
if __name__ == '__main__':
    n = int(input().strip())
    result = consicutive(n)
    print(result)
    
