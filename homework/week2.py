'''
 1. ��д������Ҫ������x��y������x��y��ƽ����

2. ����1��100��ƽ���ĺ�

3. ��д������������ΪС��100����������TRUE������100����������FALSE

4. ĳ����˾���ù��õ绰�������ݣ���������λ���������ڴ��ݹ������Ǽ��ܵģ����ܹ������£�
ÿλ���ֶ�����5,Ȼ���úͳ���10��������������֣��ٽ���һλ�͵���λ�������ڶ�λ�͵���λ������

��д���ܵĺ�������ܵĺ�����
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