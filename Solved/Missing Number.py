# cook your dish here
n = int(input())
lst = list(map(int, input().split()))
total_sum = sum(lst)
actual_sum = n*(n+1)//2
print(actual_sum - total_sum)