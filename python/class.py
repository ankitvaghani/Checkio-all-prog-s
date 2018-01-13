fo = open("../aaa.txt", "r+a")
print "Name of the file: ", fo.name
print "Closed or not : ", fo.closed
print "Opening mode : ", fo.mode
print "Softspace flag : ", fo.softspace

#fo.write( "Python is a great language.\nYeah its great!!\n")

str=fo.read()
print str
fo.close()

class Vector:

   def __init__(self, a, b):

      self.a = a

      self.b = b



   def __str__(self):

      return 'Vector (%d, %d)' % (self.a, self.b)

   

   def __add__(self,other):

      return Vector(self.a + other.a, self.b + other.b)



v1 = Vector(2,10)

v2 = Vector(5,-2)

print v1 + v2


class JustCounter:
   __secretCount = 0
  
   def count(self):
      self.__secretCount += 1
      print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()
#print counter.__secretCount



import re

line = "Cats are smarter than dogs";

matchObj = re.match( r'(.*) dogs', line, re.M|re.I)
if matchObj:
   print "match --> matchObj.group(1) : ", matchObj.group(1)
else:
   print "No match!!"

searchObj = re.search( r'dogs', line, re.M|re.I)
if searchObj:
   print "search --> searchObj.group() : ", searchObj.group()
else:
   print "Nothing found!!"

phone = "2004-959-559 # This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print "Phone Num : ", num

# Remove anything other than digits
num = re.sub(r'\D', "", phone)    
print "Phone Num : ", num
