#coding:utf-8 
#com.quickfix057.kuaixiustaff
class Fruit:
      def __init__(self, color):
           self.color = color
           print "fruit's color: %s" %self.color
 
      def grow(self):
           print "2"
 
class Apple(Fruit):                               #�̳��˸���
      def __init__(self, color):                  #��ʾ���ø����__init__����
           Fruit.__init__(self, color)
           print "apple's color: %s" % self.color
 
class Banana(Fruit):                              #�̳��˸���
      def __init__(self, color):                  #��ʾ���ø����__init__����
           Fruit.__init__(self, color)
           print "banana's color:%s" % self.color
 
      def grow(self):                             #�����˸����grow����
           print "1"
 
if __name__ == "__main__":
	apple = Apple("red")
	apple.grow()
	banana = Banana("yellow")
	banana.grow()

