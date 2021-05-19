import this
import sys

print(sys.stdin.encoding)


print(sys.stdout.encoding)

print('My name is Goodboy!')

myName = "Goodboy"

if myName == "Goodboy":
    print("OK!")


class Cookie:
    pass

cookie = Cookie()

print(id(cookie))
print(dir(cookie))
print(cookie.__class__)
print(cookie.__hash__)

