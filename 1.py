a = input("введите число ")
stp = int(input("система счисления"))
b= list(a)
n = len(a)
st= n-1
itog= 0
for i in range(n):
    itog=itog+int(b[i])*stp**st
    st=st-1
print(f"{itog}")
