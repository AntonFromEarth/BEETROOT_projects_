'''
import sys

for d in sys.path:
    print(d)
'''

#import pkg.mod1, pkg.mod2

#from pkg import mod1

import pkg
pkg.mod1.foo()

#mod1.foo()

pkg.mod2.bar()
#print(__name__)
#print(pkg.var_init)
#print(var_init)
