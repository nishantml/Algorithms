def PalindromeString(str):
    rev = str[::-1]
    if rev == str:
        return True
    else:
        return False


print(PalindromeString('abba'))
