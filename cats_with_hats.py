cats = {}

# Establishes cats and their hats
h = 1
for item in range(0, 100):
    catnum = "Cat %s" % h
    cats[catnum] = None
    h += 1

# Round generator
r = 1
while r <= 100:
    n = r
    while n <= 100:
        catnum = "Cat %s" % n
        old_on_off = cats[catnum]
        cats[catnum] = not old_on_off
        n += r
        print(n)
    r += 1

for item in cats:
    if cats[item] is True:
        print(item)
