a=['qq=7', 'pc=4', 'ot=9','ab=5']

target = 'pc'
for i in range(len(a)):
    label = a[i][:a[i].find('=')]
    if label == target:
        index = i
a.pop(index)
print(a)

