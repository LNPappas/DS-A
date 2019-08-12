#Data structure = collection of values
    #container, like a file cabininet

#1. How to build data structures <- many are pre-built
#2. How to use data structures    

## Arrays ## <- Lists in Python
    #simplest and most widely used. 
    #least amount of rules

strings = ['a','b','c','d']
#4*4 = 16 bytes of storge
strings.append('e') # <- adds e to end of list O(1)
print(strings)
strings.pop() # <- removes last item from array O(1)
print(strings) 
strings.insert(0, 'z') # <- inserts value at specified index O(n) 
print(strings)
strings.remove('z') # <- remove by value O(n)
print(strings)
strings.pop(2) # <- remove by index O(n) (unless last element, do not need to shift.)
print(strings)






