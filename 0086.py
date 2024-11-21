a = int(input())
b = int(input())
print(chr(60 + bool(~-a // b) + bool(a // b)))
