#自定义abs函数-*-
def my_abs(x):
    if(x>0):
        return x
    else:
        return -x

print(my_abs(-12.45))

#可定义空函数
def nop():
    pass
age =10
if age>=18:
    pass    #常用于还未想好如何实现

#返回多个值    起始返回的是一个tuple
import math   #导入math包
def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny
x,y = move(100,100,60,math.pi/6)
print(x,y)
    