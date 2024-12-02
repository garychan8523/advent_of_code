import os
import sys


day = sys.argv[1]

if not os.path.exists(f'day{day}'):
    os.makedirs(f'day{day}')

open(f'./day{day}/1.py', 'w+')
open(f'./day{day}/2.py', 'w+')
open(f'./day{day}/input', 'w+')
open(f'./day{day}/sample', 'w+')
