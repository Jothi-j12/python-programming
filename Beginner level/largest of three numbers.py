def max(x,y):
    if x > y:
        return x
    return y
def three( x, y, z ):
    return max( x, max( y, z ) )
print(three(int(input()),int(input()),int(input())))
