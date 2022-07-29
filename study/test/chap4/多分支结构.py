# 用途：练习
# 性质：初学者
# 时间：2022/7/28  15:55
print('-------多分支结构----------')
'''多分支结构：if...elif....elif....else(else可省略)
从键盘录入一个成绩
90-100  A
80-90   B
70-80   C
60-70   D
0-59    E
小于0或大于100为非法数据（不在有效范围之内）
'''

score=float(input('请输入一个成绩:'))
#判断
if  score>=90 and score<=100:
    print('A级')
elif score>=80  and score<90:
    print('B级')
elif  score>=70  and  score<80:
    print('C级')
elif  score>=60  and  score<70:
    print('D级')
elif  score<60:
    print('E级')
else:
    print('成绩不合法，请重新核对')
