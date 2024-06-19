#!/usr/bin/env python3

import sys

argc = len(sys.argv)

if argc >= 2:
    argv = sys.argv
    argv.pop(0)
    # print(argv)
    print("parameters:",len(argv))
    for i in range (len(argv)):
        print(argv[i], ': ', len(argv[i]),sep='')
        
else:
    print("none")
