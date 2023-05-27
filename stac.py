class Stack():
	def __init__(self):
		self.items=[]
	

	def push(self,item):
		self.items.append(item)


	def pop(self):
		return self.items.pop()

	
	def printStack(self):
		for x in self.items:
			print(x)


	def isEmpty(self):
		return self.items.size



myStack=Stack()

myStack.push("A")
myStack.push("B")
myStack.push("C")
myStack.printStack()

print("")
myStack.pop()
myStack.printStack()
