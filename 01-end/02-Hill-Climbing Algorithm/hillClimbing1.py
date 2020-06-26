def hillClimbing(f, x, dx=0.01):
    while (True):
        print('x={0:.3f} f(x)={1:.3f}'.format(x, f(x)))
        if f(x+dx)>f(x):
            x = x + dx
        elif f(x-dx)>f(x):
            x = x - dx
        else:
            break
    return x

def f(x):
    return -1*(x*x-2*x+1)

hillClimbing(f, 0)
