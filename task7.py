a = 0
b = 1
print(a) 
for i in range(1, 51):
    if b >= 50:
        break
    print(b)
    temp = a
    a = b
    b = temp + b
