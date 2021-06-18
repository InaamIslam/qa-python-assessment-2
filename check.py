def three(a):
    n1 = int( "%s" % a )
    n2 = int( "%s%s" % (a,a) )
    n3 = int( "%s%s%s" % (a,a,a) ) 
    n4 = int( "%s%s%s%s" % (a,a,a,a))
    total = (n1+n2+n3+n4)
    return total


testing = three(9)
print(testing)
