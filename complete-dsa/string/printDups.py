def print_duplicates(str):
    hash = dict()
    for c in list(str):
        if c not in hash:
            hash[c] = 1
        else:
            hash[c] = hash[c] + 1

    for i in hash:
        if hash[i] > 1:
            print(i)


print_duplicates('test')
