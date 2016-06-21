# -*- coding:utf-8 -*-
height=1.75
weight=80.5
bmi=weight/(height*height)
if bmi<18.5:
    print('小明体重过轻')
elif bmi<25:
    print('小明体重正常')
elif bmi<28:
    print('小明体重过重')
elif bmi<32:
    print('小明体重超重')
