# encoding: utf-8
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('bar', help='one of the bars to be frobbled')
parser.add_argument('--foo', required=True)
parser.add_argument('--nargs2', nargs=2, required=True)

args = ['bar', '--foo', 'foo', '--nargs2', 'a', 'b']
option = parser.parse_args(args)
print option
