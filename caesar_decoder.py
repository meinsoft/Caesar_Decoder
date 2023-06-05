s = input()
key = int(input())
alpha = 'abcdefghijklmnopqrstuvwxyz'
ss = ''
for harf in s:
    if harf in alpha:
        ss += alpha[(alpha.index(harf) - key) % len(alpha)]
    else:
        ss += harf
print(ss)