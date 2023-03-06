# unpacking means taking each member of a collection

def fn(x, y, z):
    print(f'{x}, {y} and {z}')

if __name__ == '__main__':
    # unpack a list
    l = [4,3,2] # we have a list
    t = (8,7,6) # we have a tuple
    s = {9, 9, 4, 2} # we have a set {9, 4, 2} unique members only
    fn(*l) # the astrisk will cause Python to unpack the members of the list into separate values
    fn(*t)
    fn(*s)
    # another way to unpack a list
    a, b, c = [3,2,1] # this will automatically unpack the list
    a, b, c = (3,2,1) # this will automatically unpack the tuple
    print(a,b,c)
    # we can unpack any iterable
    gen = (x*x for x in range(3))
    fn(*gen)
