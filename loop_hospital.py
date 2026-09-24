# Patient 1 — should print 1 to 10, but stops early
# FIXED: range(1, 10) stops at 9, so range(1, 11) is needed to include 10
for i in range(1, 11):
    print(i)

# Patient 2 — should count down 3, 2, 1, but never stops
# FIXED: n was never decremented, causing an infinite loop; added n -= 1
n = 3
while n > 0:
    print(n)
    n -= 1

# Patient 3 — should add up 1+2+3+4+5 = 15, but prints the wrong total
# FIXED: total was reset to 0 inside the loop on every iteration; moved it outside
total = 0
for i in range(1, 6):
    total = total + i
print(total)