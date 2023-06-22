word = input("enter a word: ")
reverse = word[::-1]


def palindrom(word):
    while True:
        if word[::1] == reverse:
            print(word, "True")
            break
        if word != reverse:
            print(word, "False")
            continue


print(palindrom(word))