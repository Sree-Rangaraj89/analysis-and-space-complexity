This recursive function will take

T(n) = T(n/2)+ T(n/2) for 2 recurisive calls and for reset code our function will take constant time 

def prints(n):
    if(n<=0):
        return
    print("Codingal")
    prints(n/2)
    prints(n/2)