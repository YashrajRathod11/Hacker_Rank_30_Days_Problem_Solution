#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
      
    rev_arr = arr[::-1]
    print(" ".join(map(str, rev_arr)))

    