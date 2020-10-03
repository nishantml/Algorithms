def count_vowels(str_w):
    vowels = ['a', 'e', 'i', 'o', 'u']
    w_arr = list(str_w.lower())
    count = 0
    for w in w_arr:
        if w in vowels:
            count += 1
    return count


print(count_vowels('Celebration'))
