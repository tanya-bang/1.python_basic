# node에 해당하는 애들 만들거임 (ppt자료)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # 다음 node의 주소를 저장
        
class LinkedList:
    def __init__(self):
        self.__head = None # 첫번째 node의 주소를 저장. (캡슐화 필요해서 __붙임)
        self.__length = 0 # 리스트의 길이를 알기위한 length

    def append(self, data):
        node = Node(data)

        if(self.__head == None): 
            self.__head = node
            self.__length += 1
            return
        
        prev = self.__head #(노드를 저장.)
                
        while(prev.next): 
            prev = prev.next 
                    
        prev.next = node
        self.__length += 1

    def get(self, idx):
        if(idx <0 or idx >= self.__length):
            raise IndexError(f'length : {self.__length}')
        
        if(idx == 0):
            return self.__head.data
        
        prev = self.__head
        for _ in range(0, idx):
            prev = prev.next
            
        return prev.data
    
    def __str__(self):
        node = self.__head
        if(not node):
            return 'empty list'
        
        res = '['
        
        while(node.next):
            res += str(node.data) + ' , '
            node = node.next
            
        res += str(node.data)
        res += ']'
        
        return res
    
    
    # list의 가장 앞에 노드를 추가
    def prepend(self,data): #데이터 앞에 추가
        node = self.__head          
    
    # 인자로 전달받은 i에 노드를 추가   
    def insert(self, i, data):
        pass
    
    
    
    def pop(self):
        """가장 뒤에 있는 요소를 반환하고 삭제
        """
        pass
    
    # 매개변수로 전달받은 data를 삭제하고 성공여부를 T/F로 반환
    
    def remove(self, data): # index가 아닌 data로 삭제해서 data.
        node = self.__head
        if(node.data == data):
            self.__head = node.next
            self.__length -=1
            return True
        
        while(node.next):
            current = node.next
            if(current.data == data):
                node.next = current.next
                self.__length -= 1
                return True
            
            node = current
            
        return False