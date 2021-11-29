from typing import BinaryIO
import argparse
import sys
import os

def process_file(name: str) -> int:
    with open(name, newline='', mode='r') as input:
        with open ('output.csv', mode='w') as output:
            for line in input: 
                int_list = [int(x) for x in line.split()]            
                if sum(int_list) % 3:
                    output.write('NO\n')
                else:
                    output.write('SI\n')
    return 0

def main() -> BinaryIO:
    try:
        os.remove("output.csv") 
    except:
        raise ValueError('File no exists')
    finally:
        parser = argparse.ArgumentParser(prog='MAIN')
        parser.add_argument('--filename', type=str, default='input.csv')
        args = parser.parse_args()
        return process_file(args.filename)
    
if __name__ == '__main__':
    sys.exit(main())