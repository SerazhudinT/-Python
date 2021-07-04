n = int(input())

a = b = c = d = 0
while a ** 2 + b ** 2 + c ** 2 + d ** 2 < n:
    c = 0
    while a ** 2 + b ** 2 + c ** 2 + d ** 2 < n:
        while a ** 2 + b ** 2 + c ** 2 + d ** 2 < n:
            #print(a, b, c, d)
            while a ** 2 + b ** 2 + c ** 2 + d ** 2 < n:
                #print(a, b, c, d)

                a += 1
                #print(a, b, c, d, '\n')

            if a ** 2 + b ** 2 + c ** 2 + d ** 2 == n:
                break

            a = 0
            b += 1
            #print(a, b, c, d, '\n', '\n')

        if a ** 2 + b ** 2 + c ** 2 + d ** 2 == n:
            break

        b = 0
        c += 1

    if a ** 2 + b ** 2 + c ** 2 + d ** 2 == n:
        break

    c = 0
    d += 1

if b == 0:
    print(a)
else:
    if c == 0:
        print(a, b)
    else:
        if d == 0:
            print(a, b, c)
        else:
            print(a, b, c, d)
