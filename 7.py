scores = input().split()

a=int(scores[0])
b=int(scores[1])
c=int(scores[2])

best = a
if b > best:
    best = b
if c > best:
    best = c

print(best)
