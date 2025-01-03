from _LinkedList import LinkedList

def test_append():
    list = LinkedList()
    
    for i in range(10):
        list.append(i**2)
        
    for i in range(10):
        print(list.get(i))
        
    print(list)
test_append()



def test_prepend():
    list = LinkedList()
    
    for i in range(11,100):
        list.append(i)
        
    list.prepend(10000)
    print(list)



    
def test_insert():
    list = LinkedList()
    
    for i in range(10):
        list.append(i)
        
    list.insert(4, 10000)
    print(list)