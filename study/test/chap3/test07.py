# 用途：练习
# 性质：初学者
# 时间：2022/7/26  14:50

#赋值运算符,运算顺序从右往左
a1=3+4
print(a1)

a=b=c=20   #链式赋值
print(a,id(a))
print(b,id(b))
print(c,id(c))

#参数赋值  += -= *= /=
a=20
a+=30
print(a)

a-=10
print(a)

a*=2
print(a)
a/=3
print(a)
print(type(a))

a//=2
print(a)
print(type(a))

a%=3
print(a)
print(type(a))

print('----------解包赋值------------')

a,b,c='hello world',30,40
print(a)
print(b)
print(c)

print('----------交换变量------------')

a,b=20,30
print('交换变量之前:',a,b)
a,b=b,a
print('交换变量之后:',a,b)

