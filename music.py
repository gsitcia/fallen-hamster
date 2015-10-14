import random

notes = ['a','bf','b','c','cs','d','ef','e','f','fs','g','af'];
hexs = [1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f'];

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

def rowtr(l):
  x = invert(l);
  s = [];
  for i in x:
    s.append(transpose(l,i));
  return(s);

def rowlr():
  return(rowtr(randomize(notes)));

def read(n,l):
  p = (n-1)%11+1
  s = ((n-p)/11)+1
  a = [];
  if s == 4:
    return(l[11-p]);
  if s == 2:
    l[p-1].reverse();
    return(l[p-1]);
  if s == 3:
    for i in l:
      a.append(i[11-p]);
    return(a);
  if s == 1:
    for i in l:
      a.append(i[p-1]);
    return(a);

def sequen(n,l):
  a = [];
  while n > 0:
    n -= 1;
    a.append(read(random.randrange(1,45),l));
  return(a);

def flatten(l):
  a = [];
  for i in l:
    for m in i:
      a.append(m);
  return(a);

def sequenf(n,l):
  return flatten(sequen(n,l));

def placenew(l,s,p):
  if random.random() <= p and len(l) > 0:
    s[notes.index(l[0])] = s[notes.index(l[0])][0:-1] + str(hexs[random.randrange(0,15)]);
    del l[0];
    if random.random() <= p:
      placenew(l,s,p/2);

def maket(l):
  s = [' A:----','BF:----',' B:----',' C:----','CS:----',' D:----','EF:----',' E:----',' F:----','FS:----',' G:----','AF:----']
  while len(l) > 0:
    for i in s:
      a = s.index(i);
      if i[-1] != '-':
        i = i + '-';
        if random.randrange(0,2) == 1 or random.randrange(0,4) == 1:
          i = i[0:-1] + '+';
          if random.randrange(0,8) == 1:
            i = i[0:-1] + str(hexs[random.randrange(0,15)]);
      if i[-1] == '-':
        i = i + '-';
      s[a] = i;
    placenew(l,s,0.5);
  for i in s:
    print(i);


def maker(n):
  maket(sequenf(n,rowlr()));

#ex = randomize(notes);
#rowt(ex);
#a = rowtr(ex);
#lprint(pad(read(13,a)));
#print(flatten(sequen(1,rowtr(['a','c','ef','b','d','g','fs','af','e','f','cs','bf']))));
#rowt(['a','c','ef','b','d','g','fs','af','e','f','cs','bf']);
maker(5);
#x = random.randrange(0,15);
#print(hexs[random.randrange(0,15)]);
