'''
 1. 编写函数，要求输入x与y，返回x和y的平方差

2. 计算1到100的平方的和

3. 编写函数，若输入为小于100的数，返回TRUE，大于100的数，返回FALSE

4. 某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：
每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。

编写加密的函数与解密的函数。
'''

# Q1
def pingfangcha(x,y):

    return x**2-y**2

print pingfangcha(1,2)


#Q2
sum=0
for num in range(1,101):
    sum=sum+num**2

print sum

#Q3
def panduan(x):
    if(x<100): return "TRUE"
    if(x>100): return "FALSE"

num=input("Please input the number")
print panduan(num)



#Q4
def jiami(x):
    num2=0;

    num=x%10
    x=x/10
    num=(num+5)%10
    num2=num2+num*1000

    num=x%10
    x=x/10
    num=(num+5)%10
    num2=num2+num*100

    num=x%10
    x=x/10
    num=(num+5)%10
    num2=num2+num*10

    num=x%10
    x=x/10
    num=(num+5)%10
    num2=num2+num

    return num2

print jiami(1234)

def jiemi(x):
    num2=0;

    num=x%10
    x=x/10
    num=(num+5)%10
    num2=num2+num*1000

    num=x%10
    x=x/10
    num=(num+5)%10
    num2=num2+num*100

    num=x%10
    x=x/10
    num=(num+5)%10
    num2=num2+num*10

    num=x%10
    x=x/10
    num=(num+5)%10
    num2=num2+num*1

    return num2

print jiami(9876)