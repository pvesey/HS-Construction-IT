# Command Line Input

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-o', '--output', action='store_true', help='output switch')

args = parser.parse_args()

if args.output:
    print("Output Switch Selected")
