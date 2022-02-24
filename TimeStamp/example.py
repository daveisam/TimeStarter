# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 10:41:23 2022

@author: david.inman
"""

import time_pkg
import print_pkg

def main():
    # print Hello World from Print_pkg
    print_pkg.printer.hello()
    
    # get the current pretty time and ssep
    nowPrettyTime = time_pkg.ssep.getPrettyTime()
    nowSsep = time_pkg.PrettyTime.getSsep()
    
    # Convert each type to the other type
    ssepFromDt = time_pkg.PrettyTime.prettyTimetoSsep(nowPrettyTime)
    dtFromSsep = time_pkg.ssep.ssepToPrettyTime(nowSsep)
    
    # Print them all out
    print_pkg.printer.output(nowPrettyTime)
    print_pkg.printer.output(dtFromSsep)
    print_pkg.printer.output(str(nowSsep))
    print_pkg.printer.output(str(ssepFromDt))
    
if __name__ == "__main__":
    main()
    
    