i = 1
n1, n2 = [], []

while i < 31 :
    if i % 5 == 0 :
        n1.append(i)
        i += 1
    else :
        i += 1
print('while : ' + str(n1))

for i in range(5, 31, 5) :
    n2.append(i)
print('for : ' + str(n2))