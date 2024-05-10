price_1kg = float(input())

j = 1
for i in range(1, 6):
    j =  j+0.2
    price = (j ) * price_1kg

    print(f"{price:.2f}")

