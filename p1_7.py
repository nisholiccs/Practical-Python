no = int(input("Enter Number : "))
sum1=0
temp=int(no)

while temp!=0:
    rem = temp % 10
    sum1 = sum1 + rem * rem * rem
    temp = temp // 10

if sum1 == no:
    print(no,"is armstrong")
else:
    print(no,"is not armstrong")

