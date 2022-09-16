filternum = lambda s: ''.join(
    [i for i in s if not i.isdigit()])

print(f'filternum: {filternum("rashmi101")}')

filtersum = lambda n: sum([int(i) for i in str(n)])

print(f'filtersum: {filtersum(101)}')