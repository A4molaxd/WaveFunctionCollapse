a = 13
print(bin(3)[2:])
print(bin(3)[2:].zfill(3))
print(bin(3)[2:].zfill(3)[::-1])
print(list(bin(3)[2:].zfill(3)[::-1]))
print(int("".join(list(bin(5)[2:].zfill(3)[::-1])), 2))