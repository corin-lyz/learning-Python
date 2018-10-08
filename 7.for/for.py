# 循环输出数组中的姓名-*-
names = ["name1","name2","name3"]
for name in names:
    print(name+'\n')

#输出从1相加到10的总和-*-
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print('%s\n' %sum)

#测试range函数-*-
list(range(5))
print(list(range(5)))

#执行从0加到100的总和-*-
sum1 = 0
for x in range(101):
    sum1 = sum1+x
print(sum1)

#测试while循环的执行-*- 计算1-100所有基数之和
sum2 = 0
n = 99
while n > 0:
      sum2 = sum2 + n
      n = n - 2
print(sum2)

#练习题 -*-break
n = 1
while n<=100:
    if n>10:
        break
    print(n)
    n = n+1
print("END")

#联系continue
n1 = 0
while n1<10:
    if n1%2==0:
        continue
    print(n1)

    