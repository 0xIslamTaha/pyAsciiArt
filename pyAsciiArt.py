import subprocess
import argparse
import time
from termcolor import colored

parser = argparse.ArgumentParser()
parser.add_argument("-d", dest = "data", help="Ascii data")
parser.add_argument("-c", dest = "color")
args = parser.parse_args()

data = args.data
color = args.color

cmd = 'figlet %s > tmp' % data
subprocess.Popen(cmd, shell=True)

time.sleep(1)
py_art = open('result.py', 'w')
py_art.write('from termcolor import colored')
py_art.write('\n')

with open('tmp', 'r') as file:
    for line in file:
        py = 'print(colored(""" %s """, "%s"))' % (line.replace('\n', ''), color)
        py_art.write(py)
        py_art.write('\n')

subprocess.Popen('rm tmp', shell=True)
