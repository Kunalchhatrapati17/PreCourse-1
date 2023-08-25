class myStack:
  #Time and Space complexities
  #Time Complexity:- O(1)
  #Space Complexity:- O(n)
  #Yes, the code is running correctly on leetcode
  '''Problems I faced initially were I thought we could push & pop 
     the elements using self.append(item) but we have to initialize it first and then 
     Insert it as I have displayed in the code, i.e., self.stack_elements.append(item)'''

     #This function is used to initialize an empty list which will be used to perform different operations  
     def __init__(self):
       self.elements_in_stack=[]

     #This isEmpty function would be checking the list to see whether its length is 0 or not. 
     def isEmpty(self):
       return len(self.elements_in_stack)==0

     #This push function would be used to append items to the stack_elements
     def push(self, item):
        self.elements_in_stack.append(item)

     #In this pop function we would be checking if the list is not Empty then we would be returning popped element from the top 
     # else return "Stack is empty" 
     def pop(self):
        if not self.isEmpty():
          return self.elements_in_stack.pop()
        else:
          return "Stack is empty"

     #This peek function we would be checking if the list is not empty then we would be returning the top element from the stack otherwise
     # We would be returning "Stack is empty"
     def peek(self):
        if not self.isEmpty():
          return self.elements_in_stack[-1]
        else:
          return "Stack is empty"
          
     #This size function would return the length of the list   
     def size(self):
         return len(self.elements_in_stack)

     #This function will return all the elements that are there in the list
     def show(self):
        return self.elements_in_stack
         

s = myStack()
s.push('1')
s.push('2')
print(s.pop())
print(s.show())
