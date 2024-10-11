# cook your dish here
n = int(input())
print(n, end = " ")
while n > 1:
    if n % 2 == 0:
        n //= 2
        print(n, end = " ")
    elif n % 2 == 1:
        n *= 3
        n +=1 
        print(n, end = " ")