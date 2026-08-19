#create a list with 3 elements
l = [ 3,6,8 ]
#INSERT OPERATIONS
#l.append(4) # appends the give elements to existing list
#l.extend((1,2)) # extend does not allow single elements
print(l)                                                           
#appending
#add 5 types of non-sequence elements to it with append
l.append(2)
l.append(3.4)
l.append(3+4j)
l.append('true')
l.append('none')
print(l)
#add 5 types of sequences to it with append
l.append('pandu')
l.append('range(1,2)')
l.append((1,2))
l.append([4,5,6])
l.append({1,2,3})
l.append({1 : 'a', 2 : 'b'})
print(l)
#extending
#l.extend(8) extend does not allow single elements so errror exists

#add 5 types of non-sequence elements to it with extend
#l.extent(4) extend does not allow so int is not sequence so error
#l.extend(4.5)
#l.extend('false')# extend does not works wors for non sequence s it only allow sequences

#l.extend(5+7j)
#l.extend('none')

#add 5 types of sequence elements to it with extend
l.extend('chinnu')
l.extend('range(4,5)')
l.extend([1,2])
l.extend((3,4))
l.extend({6,7})
l.extend({2 :'n', 3: 'p'})
#inserting insert elements at given index area
#insert an element at index 1 and print
l.insert(1,'a')
print(l)
#insert an element at index -1 and print
l.insert (-1,'b')
print(l)
#insert an element at index 10000 and print
l.insert( 5 ,10000)
print(l)
#insert an element at index -10000 and print
l.insert( 9 , -10000)
print(l)

#DELETE OPERATIONS
#create a list with 1,2,1,3,4,1
h = [1,2,1,3,4,1]
#pop element at index 3 and print element and list
h.pop(3)
print(h)
#pop last element and print element and list
h.pop(4)
print(h)
#remove first 1 from list and print element and list
h.remove(1)
print(h)
#clear all elements in the list
h.clear()
print(h)

#UPDATE OPERATIONS
#create a list with 3,2,1,5,4 
u = [3,2,1,5,4]
#sort the list in ascending and print
u.sort()
print(u)
#create a list with 3,2,1,5,4 
v = [3,2,1,5,4]
#sort the list in descending and print
v.sort(reverse=True)
print(v)
#create a list with 3,2,1,5,4 
w = [3,2,1,5,4]
#reverse the list and print
w.reverse()
print(w)

#READ OPERATIONS
#create a list with 1,2,1,3,1, 2
x = [1,2,1,3,1,2]
#find count of 1 and 2 in list
print(x.count(1))
print(x.count(2))

#find index of 1 from start
print(x.index(1))
#find index of 1 from 2nd index
print(x.index(1,2))
#find index of 1 from 5th index
#print(x.index(1,5)) 1 is no their at index 5 so error shos

#TUPLE
#create a tuple with 1,2,1,3,1, 2
t = (1,2,1,3,1,2)
#find count of 1 and 2 in tuple
print(t.count(1))
print(t.count(2))

#find index of 1 from start
print(t.index(1))
#find index of 1 from 2nd index
print(t.index(1,2))
#find index of 1 from 5th index
#print(t.index(1,5)) 1 is not their in index 5 so error shows




