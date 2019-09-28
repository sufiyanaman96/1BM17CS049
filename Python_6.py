import sys
class validity :
  def __init__(self,stack,o,c,s) :
    self.stack=stack
    self.o=o
    self.c=c
    self.s=s
  def check(self) :
    for i in self.s:
      if i in self.o :
        self.stack.append(i)
      elif i in self.c :
        ch=self.stack[len(self.stack)-1]
        ch1=self.c[self.o.index(ch)]
        if ch1==i : 
          self.stack.pop()
        else : 
          print("invalid")
          sys.exit()



s=input()
stack=[]		
o=['(','[','{']
c=[')',']','}']	

obj=validity(stack,o,c,s)
obj.check()

if len(obj.stack)==0 : print("validate")
