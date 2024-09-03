def calculate_factorial(n):
    product=1

    for num in range(1,n+1):
        product *=num

    print(product)
calculate_factorial(5)