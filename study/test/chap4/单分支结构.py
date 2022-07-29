# 用途：练习
# 性质：初学者
# 时间：2022/7/28  15:37
print('--------选择结构----------')
#单分支结构    if  条件表达式
money=1000  #余额
s=int(input('请输入取款金额:'))
#判断余额是否充足
if money>=s:
    money=money-s
    print('取款成功，余额为：',money)
if money<s:
    print('余额不足')