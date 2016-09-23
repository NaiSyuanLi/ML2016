#!/usr/bin/env python
import sys
import numpy

i=0
row = []
col2 = []
col_num = int(sys.argv[1])
filename = sys.argv[2]
result = ""
f = numpy.loadtxt(filename)
g = (f[:,col_num])
g = numpy.transpose(f[:,col_num])
g = sorted(g)
numpy.savetxt("ans1.txt",g,fmt = "%s",newline = ",")
