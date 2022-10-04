
def hanoi(n,x,y,z):
    if n==1:
        print(x,"-->",z)
    else:
        #将n-1的盘子从x移动到y
        hanoi(n-1,x,z,y)
        #将最底下的盘子从x移动到z
        print(x,'-->',z)
        #再讲n-1个盘子从y移动到z
        hanoi(n-1,y,x,z)

# 递归实现汉诺塔
num = input("请输入汉诺塔层数\n")
if num.isdigit():
    hanoi(int(num),'X','Y','Z')


