import test

word = test.Test().getTest()

while True:
    s = input()
    if len(s) == 5:
        x = test.Test().check(word, s)
        result = ' '.join(x)
        if result == "G G G G G":
            break
        print(result)