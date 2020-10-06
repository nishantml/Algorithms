def duplicates(character):
    count = 0
    Hash = dict()
    for i in list(character):
        if i in Hash:
            count += 1
            Hash[i] += 1
        else:
            Hash[i] = 1
    print(Hash)
    return count


print(duplicates("foobar"))
print(duplicates("birthday"))
print(duplicates("Hello World!"))
