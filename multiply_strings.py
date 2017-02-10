def multiply(num1, num2):
    product = [0] * (len(num1) + len(num2))
    pos = len(product)-1
    for n1 in reversed(num1):
        tmp = pos
        for n2 in reversed(num2):
            product[tmp] += int(n1) * int(n2)
            product[tmp - 1] += product[tmp] / 10
            product[tmp] %= 10
            tmp -= 1
        pos -= 1
            
    p = 0
    while p < len(product) - 1 and product[p] == 0:#skip leading zeros
        p += 1
            
    return ''.join(str(e) for e in product[p:])

print multiply("99", "9")
