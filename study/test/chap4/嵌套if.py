# 用途：练习
# 性质：初学者
# 时间：2022/7/28  16:11
# 嵌套if

'''
会员   >=200     8折
      >=100     9折
      不打折
非会员 >=200     9.5折
      不打折
'''
print('-------嵌套if----------')
answer = input('请问您是会员吗？y/n')
money=float(input('请输入您的购物金额：'))
# 外层判断是否是会员
if answer=='y':
    #print("您是会员")
     if money>=200:
       print('您的购物金额为：',money*0.8)
     elif money>=100:
       print('您的购物金额为：',money*0.9)
     else:
       print('您的购物金额为：',money)
elif answer=='n':
    #print("您不是会员")
     if money>=200:
       print('您的购物金额为：',money*0.95)
     else:
       print('您的购物金额为：',money)
else:
    print('您的输入不合法，请重新输入')






