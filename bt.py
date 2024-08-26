n=input("ENter the string of binary")
sum=0
inc=0
for i in n[:-1]:
    sum=sum+int(i)*(2**(inc))
    inc+=1

print(sum)
