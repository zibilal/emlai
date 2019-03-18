from functools import reduce
import argparse

"""
add
sub
mul
div
"""

def addOp(arrNum):
    print(reduce((lambda x,y:x+y),arrNum))
    pass

def subOp(arrNum):
    print(reduce((lambda x,y:x-y),arrNum))
    pass

def mulOp(arrNum):
    print(reduce((lambda x,y:x*y),arrNum))
    pass

def divOp(arrNum):
    print(reduce((lambda x,y:x/y),arrNum))
    pass  

print("Calculator Script")
parser = argparse.ArgumentParser(description="PR EML week 1. Calculator script")
parser.add_argument('-add', dest='addOp', action='store_const',const=addOp, help='Add all int')
#parser.add_argument('-sum',dest='accumulate',action='store_const', const=sum, default=max, help='sum all int')

parser.add_argument('-sub', dest='subOp', action='store_const',const=subOp, help='Subtract all int')
parser.add_argument('-mul', dest='mulOp', action='store_const',const=mulOp, help='Multiply all int')
parser.add_argument('-div', dest='divOp', action='store_const',const=divOp, help='Divide all int')

parser.add_argument('integers',metavar='N', type=int, nargs='+',help='an integer to be processed')


args = parser.parse_args()

#print(args)
if(args.addOp): args.addOp(args.integers)
if(args.subOp): args.subOp(args.integers)
if(args.mulOp): args.mulOp(args.integers)
if(args.divOp): args.divOp(args.integers)

#if(len(args.integers)>0) : addOp(args.integers)