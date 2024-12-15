def sum(n):
    return n*(n+1)/2

space complexity: θ(1)
linear space:

def arraysum(a):
    sum=θ
    for i in a:
        sum=sum + i

        return(sum)
    
a = [12, 3, 4, 15]
arraysum(a)

With the size of the array, the space also required increases:

Space completely θ(n), Auxillary space = 0(1)

def sum(n):
    if(n<=0):
        return
    return n+ sum(n-1)