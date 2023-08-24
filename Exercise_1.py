class myStack:
  #Time and Space complexity of each file
  #Time Complexity:- O(1) for every method accept show method as we have to iterate through n elements 
  # Space Complexity:- O(n) as we have to store n no. of elements in the list
     def __init__(self):
       self.elements=[]
         
     def isEmpty(self):
       return if(len.elements)==0
         
     def push(self, item):
         self.elements.append(item)
       
     def pop(self):
         if not self.isEmpty():
            return self.elements.pop()
         else:
             return "Empty Stack"
        
     def peek(self):
        if not self.isEmpty():
          return self.elements.pop[-1]
        else:
          return "Stack empty"
          
     def size(self):
       return len(self.elements)
         
     def show(self):
       return self.elements  

s = myStack()
s.push('1')
s.push('2')
print(s.pop())
print(s.show())
