def move(n,a,b,c):
    if n==1:
        print("%s->%s"%(a,c))
    else:
        move(n-1,a,c,b)#将最上面n-1个盘子由a移动到b
        move(1,a,b,c)#将最下面1个盘子由a移动到c
        move(n-1,b,a,c)#将b上面的n-1个盘子移动到c

move(3,'A','B','C')