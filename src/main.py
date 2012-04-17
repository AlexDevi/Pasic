import argparse
from pasic.transpiler import PasicTranspiler
#from .pasic.transpiler import PasicTranspiler


pasicInfo = 'PASIC 0.0 - Professional All purpose Symbolic Instruction Code to C++ Transpiler'

parser = argparse.ArgumentParser(description=pasicInfo)
parser.add_argument('infile', type=str, nargs='+', metavar='INPUT_FILE')
args = parser.parse_args()

transpiler = PasicTranspiler()
for input_file in args.infile:
    transpiler.process(input_file)