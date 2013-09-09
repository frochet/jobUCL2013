#verify if everything is configured corectly.
import os
import sys

def pingfrom_r2():
    os.system('ssh root@2001:db8:a110:babe::2 ping6 -c 3 -i 0.5 2001:db8:cafe:babe::2 >> r2neighb.out; ping6 -c 3 -i 0.5 2001:db8:dead:beef::2 >> r2router.out; ping6 -c 3 -i 0.5 2001:db8:dead:beef::1 >> r2rout.out ')
    f= open('r2neighb.out')
    a=f.read()
    if a=='':
        print "there is errors in your routing tables. pc2 unable to contact pc1."
    if ("unreachable" in a):
        print "there is errors in your routing tables. pc2 unable to contact pc1."
    f.close()
    
    f= open('r2router.out')
    a=f.read()
    f.close()
    if a=='':
        print "there is errors in your routing tables. pc2 unable to contact r1."
        return False
    if ("unreachable" in a):
        print "there is errors in your routing tables. pc2 unable to contact r1."
        return False
    return True


def ping_routers():
    os.system('ping6 -c 3 -i 0.5 2001:db8:dead:beef::1 | head -n -3 >> router.out')
    os.system('ping6 -c 3 -i 0.5 2001:db8:dead:beef::2 | head -n -3 >> router.out')
    f= open('router.out')
    a=f.read()
    f.close()
    if a=='':
        print "there is errors in your routing tables. pc1 unable to contact routers."
        return False
    if ("unreachable" in a):
        print "there is errors in your routing tables. pc1 unable to contact routers."
        return False
    return True

def ping_neighbors():
    os.system('ping6 -c 3 -i 0.5 2001:db8:a110:babe::2 | head -n -3 >> neighb.out')
    f=open('neighb.out','r')
    a=f.read()
    f.close()
    if a=='':
        print "there is errors in your routing tables. pc1 unable to contact pc2."
        return False
    if ("unreachable" in a):
        print "there is errors in your routing tables. pc1 unable to contact pc2."
        return False
    return True

def main(argv):
    b=ping_routers()
    b=(b and ping_neighbors())
    b=(b and pingfrom_r2())
    
    if b == True :
        print "Your network is well configured"
    
if __name__=="__main__":
    main(sys.argv[1:])
