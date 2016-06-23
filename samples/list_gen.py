
# -*- coding: utf-8 -*-

L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[x.lower() for x in L1 if isinstance(x,str) ]
print(L2)