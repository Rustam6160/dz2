n = int(input())

sum = 0
for i in range(1,n+1):
    j = i * 0.1 +1
    sum = -sum - j
    print(f"{sum:.3f}, {j:.2f}")
