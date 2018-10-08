#尝试编写汉诺塔的函数
#sum = 0
def move(n,a,b,c,sum=0):
    if n == 1:
        sum = sum + 1
        print('一共移动步数：',sum ,'\n')
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        sum = sum + 1
        move(1,a,b,c)
        sum = sum+1
        move(n-1,b,a,c)
move(3,'A','B','c')



