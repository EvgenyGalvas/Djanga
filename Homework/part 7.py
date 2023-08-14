def checker(x):
    counter = 0
    for j in range(2, x + 1):
        if x % j == 0:
            counter += 1
    if counter == 1:
        return True
    else:
        return False


a = [6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1]
simple = []
other = []
for i in a:
    if checker(i) and i != 1:
        simple.append(i)
    elif not checker(i) and i != 1:
        other.append(i)

print("Min:", min(simple))
print("Max:", max(other))