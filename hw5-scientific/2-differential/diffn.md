# Trigonometric differentiation

## Executed result
```
> py .\diffn.py
dft(sin, pi/4)=  0.7071067811865476
dftn(sin, 0 pi/4)=  0.7071067811865476
dftn(sin, 1 pi/4)=  0.7071067811865476
dftn(sin, 2 pi/4)=  -0.7071067811865476
dftn(sin, 3 pi/4)=  -0.7071067811865476
dftn(sin, 4 pi/4)=  0.7071067811865476
dftn(sin, 5 pi/4)=  0.7071067811865476
dftn(sin, 6 pi/4)=  -0.7071067811865476
dftn(sin, 7 pi/4)=  -0.7071067811865476
dftn(sin, 8 pi/4)=  0.7071067811865476
dftn(sin, 9 pi/4)=  0.7071067811865476
```

## Use function dft(f, x, sign) instead of df(f, x, h=step)
dft(f, x, sign) is used to differentiate trigonometric function\
but only with sin(x) and cos(x)
```
```
\
for the differenciation of sin(x) snd(x):
```
sin'(x) = cos(x)
cos'(x) = -sin(x)
```
\
In dft(f, x, sign), f is the corresponding function sin(x) or cos(x)\
and sign is to determine whether the function is positive or negative\
The function retuens 3 values:\
answer in float, current trigonometric function type and the answer sign\
code written in python:
```py
def dft(f, x, sign):
    si = float(sin(x))
    co = float(cos(x))
    ans = [(co, cos, 1), (-co, cos, -1), 
           (-si, sin, -1), (si, sin, 1)]

    if f == sin:
        return ans[0] if sign == 1 else ans[1]
        
    if f == cos:
        return ans[2] if sign == 1 else ans[3]
```
\
If we want to differenciate a trigonometric function n times\
we add a function dftn(f, x, sign, n), which makes n times differenciation
```py
def dftn(f, x, sign, n):
    if (n == 0):
        return float(sin(x)), sin, 1

    if (n == 1):
        return dft(f, x, sign)
        
    if f == sin:
        return dftn(cos, x, sign, n-1)

    if f == cos:
        return dftn(sin, x, -sign, n-1)
```
