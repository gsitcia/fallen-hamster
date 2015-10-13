import random

notes = ['a','bf','b','c','cs','d','ef','e','f','fs','g','af'];

def makeset(n):
    a = [n];
    while n > 0:
        n -= 1;
        a.append(n);
    a.reverse();
    return(a);
    
def randomset(n):
    a = makeset(n);
    m = [];
    while len(a) > 0:
        n = random.randrange(0,len(a));
        m.append(a[n]);
        del a[n];
    return(m);
    
def randomize(listo):
    a = randomset(len(listo)-1);
    m = [];
    for i in a:
        m.append(listo[i]);
    return(m);
    
def numberize(m,r=notes):
    a = [];
    for i in m:
        a.append(r.index(i));
    return(a);

def letterize(m,r=notes):
    a = [];
    for i in m:
        a.append(r[i]);
    return(a);
    
def invert(s):
    l = numberize(s)
    x = len(l);
    t = l;
    a = [l[0]];
    while len(l) > 1:
        a.append((a[-1]+l[0]-l[1])%x);
        del l[0];
    l = t;
    return(letterize(a));

def transpose(s,a):
    l = numberize(s);
    n = notes.index(a);
    x = l[0]-n;
    z = len(l);
    while z > 0:
        z -= 1;
        l[z] = (l[z]-x)%len(l);
    return(letterize(l));
    
def pad(s):
    l = s;
    x = len(l)-1;
    while x >= 0:
        if len(l[x]) == 1:
            l[x] = l[x] + '  |';
        if len(l[x]) == 2:
            l[x] = l[x] + ' |';
        x -= 1;
    return(l);

def lprint(l):
    x = '';
    for i in l:
        x = x + i;
    print(x);
    
def rowt(l):
    x = invert(l);
    for i in x:
        lprint(pad(transpose(l,i)));
    
def rowl():
    rowt(randomize(notes));

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#this one is more general
import random

notes = ['a','bf','b','c','cs','d','ef','e','f','fs','g','af'];

def makeset(n):
    a = [n];
    while n > 0:
        n -= 1;
        a.append(n);
    a.reverse();
    return(a);
    
def randomset(n):
    a = makeset(n);
    m = [];
    while len(a) > 0:
        n = random.randrange(0,len(a));
        m.append(a[n]);
        del a[n];
    return(m);
    
def randomize(listo):
    a = randomset(len(listo)-1);
    m = [];
    for i in a:
        m.append(listo[i]);
    return(m);
    
def numberize(m,r):
    a = [];
    for i in m:
        a.append(r.index(i));
    return(a);

def letterize(m,r):
    a = [];
    for i in m:
        a.append(r[i]);
    return(a);

def mod(a,b):
    return((a-1)%b+1);

def invert(l):
    x = len(l);
    t = l;
    a = [l[0]];
    while len(l) > 1:
        a.append((a[-1]+l[0]-l[1])%x);
        del l[0];
    l = t;
    return(a);

