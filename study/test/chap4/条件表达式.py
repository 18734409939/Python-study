# 用途：练习
# 性质：初学者
# 时间：2022/7/28  16:50
'''
键盘录入两个整数，比较两个整数的大小
'''
num_a=int(input('请输入一个整数:'))
num_b=int(input('请输入另一个整数:'))
#比较大小
'''基本方法
if num_a>num_b:
    print(num_a,"大于",num_b)
elif num_a==num_b:
    print(num_a,'等于',num_b)
else:
    print(num_a,'小于',num_b)
'''
print('使用条件表达式进入比较')
print(str(num_a)+'大于'+str(num_b)   if num_a>num_b else str(num_a)+"小于"+str(num_b))