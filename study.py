print('hello world',end='\n')
print('nice to meet you')
print('a'=="a")
nums=[1,2,3]
print(nums)
hello = 3
print(hello)
total=sum(nums)+hello
print(total)
nums.insert(1,hello)#插入到指定位置，第一个数编号是0
print(nums)
price = 12
print(price)
false = "哈哈"
print(false)
num = 1
print(type(num))
nums.append(num)#在末尾插入
print(nums)
print(type(False))#看数据类型用type
print(True+False)#必须大写
m1 = 2 + 3
print(type(m1))
name = "six star"#没有引号会被识别成变量名
'''instruction'''
#占位符：%s字符串string
#%d整数
#%f浮点数
#%%
name1 = "cecilia"
age = 18
print("my name:%s,my age:%d"%(name1,age))
#%4s表示输出的整数位数，这个数大于当前位数就补齐，小于等于就不变，可以在前面添加0，默认是空格。
#浮点数默认后六位小数，遵循四舍五入原则。
name2 = 1.23456789
print('%.4f'%name2)#不能取太多位，IEEE754，前面一定要加点，不加点就是整数。
print('my name%% is 1%%' %())#如果要显示%%，必须打%%，否则会识别为占位符
print(f"my name is {name1},i am {age} years old.")#f格式化
#使用/时商一定是浮点数
#//是取整，向下取整（向0取整，相当于抹掉小数点后数字）
#%取余，**幂
#取整除若有浮点数，结果也用浮点数表示，只要运算中有浮点数，最后结果就是浮点数。
'''ctrl+z撤销，+c复制，+v粘贴，+f查找'''
#+=等效于a=a+1
n1 = 33
n2 = 66
n2+=n1
print(n2)
#纯数字不能使用赋值运算符，变量需提前赋值后才可使用。
name2=input('请输入：')#input输入函数
print(f"hello,{name2}")
input("your\tpassword:")
#转义字符
#\t一般是空四个空格   \n换行符   \r回车符，\r前面的部分会消失
# \\反转义，用来打出\,\\打印出来是\
#r加在‘’前面表示取消转义，raw
score = input("your score:")
if int(score)>=60:#一定要加冒号！！！
    print("excellent!")
else:
    print("you can do better!")
#比较运算符 ==比较两个值是否相同，相等为True；
#!=也是比较是否相同，不相等为True
a = 18
b = 12
if a==18 and b==12:
    print("right")
#else后面不需要添加任何东西
#三目运算符  格式   result = a if condition else b
print("right") if a>=b else print("wrong")

