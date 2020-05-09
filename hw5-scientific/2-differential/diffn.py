from math import sin, cos, pi

def dft(f, x, sign):
    si = float(sin(x))
    co = float(cos(x))
    ans = [(co, cos, 1), (-co, cos, -1), 
           (-si, sin, -1), (si, sin, 1)]

    if f == sin:
        return ans[0] if sign == 1 else ans[1]
        
    if f == cos:
        return ans[2] if sign == 1 else ans[3]

def dftn(f, x, sign, n):
    if (n == 0):
        return float(sin(x)), sin, 1

    if (n == 1):
        return dft(f, x, sign)
        
    if f == sin:
        return dftn(cos, x, sign, n-1)

    if f == cos:
        return dftn(sin, x, -sign, n-1)

x = pi/4

print("dft(sin, pi/4)= ", dft(sin, x, 1)[0])

for i in range(10):
    ans, f, sign = dftn(sin, x, 1, i)
    print('dftn(sin,', i, 'pi/4)= ', ans)
