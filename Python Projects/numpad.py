numpad=((1,2,3),
        (4,5,6),
        (7,8,9),
        ('*',0,'#'))

for rows in numpad:
    for numbers in rows:
        print(numbers, end=" ")
    print()