#verify if everything is configured corectly.
import os
import sys
import pexpect


def pingfrom_r2():
    
    ssh_newkey= 'Are you sure you want to continue connecting'
    password= 'root'
    child = pexpect.spawn("ssh root@2001:db8:a110:babe::2 ping6 -c 1 -i 0.5 2001:db8:cafe:babe::2 | head -n -3 | sed 's/time=.*//'")
    #child.logfile = sys.stdout
    i=child.expect([ssh_newkey,'password:',pexpect.EOF])
    if i==0 :
        child.sendline('yes')
        i=child.expect([ssh_newkey,'password:',pexpect.EOF])
    if i==1 :
        child.sendline(password)
    else :
        print "connection timeout impossible to connect to r2"
        return False
   
    child.sendline("ping6 -c 3 -i 0.5 2001:db8:cafe:babe::2 | head -n -3 | sed 's/time=.*//'") 
    
    i= child.expect(['64 bytes from', 'unknown host', 'Network is unreachable'])

    if i==0: 
        print "contact r2-r1 successfull"
        return True
    else:
        print "r2 cannot contact r1"
        return False

   
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
    os.system("rm neighb.out router.out")
    
    if b == True :
        print "Your network is well configured"
    
if __name__=="__main__":
    main(sys.argv[1:])
