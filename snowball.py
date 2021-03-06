# snowball.py

from __future__ import division, print_function
import time
import sys
import h5py
import numpy as np
import pyqtgraph as pg
import matplotlib
matplotlib.use('Agg')
from pylab import sqrt, linspace
from scipy.interpolate import RectBivariateSpline
from helperFiles.constants import *
from helperFiles.classes.Snowball import *

'''
Main function
Arguments list:
--help -prints out menu and exits
Purpose:
Return types, values:
Dependencies:
Creator: James Stauder
Date created: 1/31/18
Last edited: 2/02/18
'''
def main(argv):

    if(len(argv) > 1):
        if("--help" in argv):
            printHelpMenu()            
        for argument in argv:
            print("use --help for help")
    else:
        print("Welcome to Snowball Interface")
        
        snowball = Snowball()
        snowball.createImage('velocity')

    sys.exit()

'''
Function: printMainMenu:
Argument list: None
Purpose: Print the main menu
Return types, values: None
Dependencies: None
Creator: James Stauder
Date created: 1/31/18
Last edited: 1/31/18
'''
def printHelpMenu():
    print("Snowball Greenland Tile Generator")
    print("usage: snowball.py [--help]")
    print("optional arguments:")
    print("     --help  show help message and exit")


if __name__ == '__main__':
    main(sys.argv)
