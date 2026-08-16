DAY 5 Task (20mins)
Write outputs of following without running the code:

1. strip, lstrip, rstrip methods
a = '   python is simple   '
print(a.strip())
#removes both spaces and give output
print(a.lstrip())
#removes left side spaces
print(a.rstrip())
#removes right side spaces

2. replace
a = 'python is simple, python is easy, python is allrounder'
b = a.replace('python', 'java')
#'java is simple, java is east, java is allrounder
print(a)
print(b)

3. upper, lower, swapcase, title, capitalize
a = 'PYTHON is siMPle'
print(a.lower())
#out put, python is simple
print(a.upper())
#out put, PYTHON IS SIMPLE
print(a.swapcase())
#OUT PUT,pyton IS SImplE
print(a.title())
#OUT PUT, Python Is Simple
print(a.capitalize())
#out put, Python is simple

4. count, startswith, endswith
a = 'abacad'
b = a.startswith('a')
#out put abaca
c = a.startswith('ad')
#out put ad
d = a.endswith('d')
#out put abaca
e = a.endswith('de')
#error
f = a.count('a')
#out put 3
g = a.count('ad')
#out put 1
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

5. find, rfind, index, rindex
s = 'abacada'
print(s.find('a'))
#0
print(s.find('a', 3))
#4
print(s.find('a', 4, 8)
      #-1
print(s.rfind('a'))
#6
print(s.rfind('a', 3))
#4
print(s.rfind('a', 4, 8)
      #-1
print(s.index('a'))
#0
print(s.index('a', 3))
#4
print(s.index('a', 4, 8)
      #error
print(s.index('a'))
#1
print(s.index('a', 3))
#4
print(s.index('a', 4, 8))
#error
print(s.index('z'))
#error
print(s.find('z'))
#-1

6. is methods
a = ' '
b = ' a'
print(a.isspace())
#'' ''
print(b.isspace())
#'' a
a = 'aBcD'
print(a.isalpha())
#true
b = 'aBcD1'
print(b.isalpha())
#false
c = 'aBc@D'
print(c.isapha())
#true

a = '13'
print(a.isdigit())
#true
b = '12a
print(b.isdigit())
#false

a = 'AbC123'
print(a.isalnum())
#true
b = 'Ab#C2'
print(b.isalnum())
true

a = '23$U'
print(a.isupper())
#true
b = '23%Ua'
print(b.isupper())
#false

a = '23$u'
print(a.islower())
#true
b = '23%uA'
print(b.islower())
#false



# split

a = 'badac'
print(a.split('a')
b = '   '  #3 spaces 
print(b.split(' '))
c = 'abaca'
print(c.split('a'))
d = 'iam a good person'
print(d.split())


#join
a = '@'
l = [1,2,3]
t = (1,2,3)
s = {1,2,3}
d = {3:1, 2:3, 3:1}
print(a.join(l))
print(a.join(t))
print(a.join(s))
print(a.join(d))
