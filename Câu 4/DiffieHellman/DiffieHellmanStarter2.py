p = 28151

found = False
for a in range(1, p):
    g = a
    for i in range(1, p):        
        if i == p - 1:
            found = True
            break
        if pow(a, i, p) == 1:
            break
    if found:
        break

print(g)