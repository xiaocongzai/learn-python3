grade1=input("请输入小明去年的成绩")
grade2=input("请输入小明今年的成绩")
grade1_integer=int(grade1)
grade2_integer=int(grade2)
increment=(grade2_integer-grade1_integer)/grade1_integer

print('小明成绩提升了%.1f%%' % (increment*100))
