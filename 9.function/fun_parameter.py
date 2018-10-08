#定义平方函数
def power(x):
    return x*x

print(power(5))

#定义n次方函数
def power_n(x,n):
    s = 1
    while n>0:
        n = n - 1
        s = s*x
    return  s

print(power_n(5,3))

#定义默认参数
def power1(x,n=2):
    s = 1
    if n>0:
       s = s * x
       n = n - 1
    return s

#定义可变参数   eg：计算a2+b2+c2+....
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

#定义关键字参数
def person(name,age,**kw):
    print("name:",name,'age:',age,'other:',kw)

person("bobo",25,city='Beijing')