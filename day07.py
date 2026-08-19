#SET METHODS
#create a empty dict and print its type
#d = {}
#print(type(d))
#create a empty set and print its type
#s = set()
#print(type(s))
#add 5 non-sequences and 5 sequences to that set with add method
#s = {9,8,7}
#s.add(2)
#s.add(6.8)
#s.add('True')
#s.add('none')
#s.add(3+8j)
#s.add('sumi')
#s.add(range(1,3))
#s.add([1,2]) as list is mutable set does not allow in it
#s.add((3,4))
#s.add({5,6}) set also will not add in add method
#s.add({1:'a',2:'b'}) dict also not allowed in add method
#print(s)
#add 5 non-sequences and 5 sequences with update method
#s.update(2) update does not allow single elements
#s.update(6.8)
#s.update('True')
#s.update('none')
#s.update(3+8j)  non sequences are not allowed in update method
#s.update('sumi' 'sowmya')
#s.update(range(1,3))
#s.update([1,2]) 
#s.update((3,4))
#s.update({5,6})
#s.update({1:'a',2:'b'})
#print(s)
#print a set and remove first element from that set
s = {1,2,3}
s.pop()
print(s)
#remove one existing and one non-existing element from that set
s.remove(2)
#s.remove(10) error shows for non existing
print(s)

#discard one existing and one non-existing element from that set
s.discard(2)
s.discard(9) # for discard error does not show for non existing
print(s)
#remove all elements from the set
s.clear()
print(s)

#create a set {1,2,3,4}, a list [3,4,5,6]. 
a = {1,2,3,4}
b = [3,4,5,6]
#write union of set and list
print(a.union(b))

#write intersection of set and list
print(a.intersection(b))
#write difference of set and list
print(a.difference(b))
#write symmetric difference of set and list
print(a.symmetric_difference(b))
#use union, intersection, difference, symmetric difference operators on set and another set. try to change second type of list and see outputs
c = {1,2,3,4}
d = {3,4,5,6}
print(c | d)
print(c & d)
print(c - d)
print(c^d)

#DICT METHODS
#create a empty dict
d = {}
print(type(d))
#extend dict with another dict
d.update({1:2,3:6})
print(d)
#extend dict with another list
d.update( [ [1,'a'],[2,'b'],[3,'c'] ])
print(d)
#extend dict with another tuple
d.update ( ( (7,'h'),(8,'j'),(9,'l') ) )
print(d)
#extend dict with another set
d.update({(7,'k'), (8,'l'), (9,'u')})
print(d)

#create a dict with {1:'a', 2:'b', 3:'c', 4:'d'}
d = {1:'a', 2:'b', 3:'c', 4:'d'}
#remove the pair with key 4
print(d.pop(4))
#remove the pair with key 100
#print(d.pop(100)) 100 is not there in dict so error shows
#remove the pair with key 100 if not there return 'z'
print(d.pop(100,'z'))
#remove the last pair
print(d.popitem())

#remove all elements from the dict)
d.clear()
print(d)
#create a dict with {1:'a', 2:'b', 3:'c', 4:'d'}
d =  {1:'a', 2:'b', 3:'c', 4:'d'}
#get the value of key 4
print(d.get(4))
#get the value of key 
print(d.get(100))# get does not shows error it shows none ware as pop shows error
#get the value of key 100, if key is not present get 'z'
print(d.get(100,'z'))

#get the value of key 4 with setdefault
print(d.setdefault(4))
#get the value of key 100 with setdefault
print(d.setdefault(100))#set default does not shows error
#get the value of key 100 with setdefault, if key is not there add 100 with 'z'
print(d.setdefault(100,'z'))
#get all keys of dict and print its type
a =  d.keys()
print(type(a))

#get all values in dict and print its type
b = d.values()
print(type(b))
#get all items in dict and print its type
c = d.items()
print(type(c))



