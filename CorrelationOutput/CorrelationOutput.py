import argparse
import pandas as pd
import numpy as np
parser = argparse.ArgumentParser(description='Take an input csv and create a correlation coefficient matrix')
parser.add_argument('input', help='Path to input file')
parser.add_argument('output', 
                   help='Output file to create, defautls to formattedOutput.csv in current directory',
                   nargs='?', 
                   default='formattedOutput.csv')
args = parser.parse_args()

df = pd.read_csv(args.input, sep=',')
matrix = np.corrcoef(df, None, False)
outFile = open(args.output, 'w')
size = len(matrix[0])
for i in range(size):
    row = matrix[i][:i + 1].tolist()
    row[i] = "-"
    outFile.write(','.join([str(x) for x in row]) + "\n")
outFile.close()
