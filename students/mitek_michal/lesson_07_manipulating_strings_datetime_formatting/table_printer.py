
def print_table():

    tableData=[['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

    newTable = {0:[], 1:[], 2:[], 3:[]}

    for li in tableData:
        for i in range(len(li)):
            newTable[i].append(li[i])

    longest = 0
    for key, value in newTable.items():
        length = len(''.join(value))
        if length > longest:
            longest = length

    for key, value in newTable.items():
        print(' ' * (longest - len(''.join(value))) + ' '.join(value))


if __name__ == '__main__':
    print_table()