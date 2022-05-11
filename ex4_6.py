#git 
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

def computepay(h, r):
if h < 40:
    Pay = h * r
else:
    Pay = 40 * r + (h - 40) * r * 1.5

p = computepay(45, 10,5)
print("Pay", p)
