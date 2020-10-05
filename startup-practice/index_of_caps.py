def index_of_caps(word):
    count = 0
    lst = []
    for letter in list(word):
        if letter.isupper():
            lst.append(count)

        count = count + 1
    return lst


print(index_of_caps('eDaBiT'))
