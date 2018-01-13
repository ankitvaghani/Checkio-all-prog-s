
var1 = 'Hello World!'
var2 = "Python Programming"

print "var1[0]: ", var1[0]
print "var2[1:5]: ", var2[1:15],"..."

import time;  # This is required to include time module.

ticks = time.time()
print "Number of ticks since 12:00am, January 1, 1970:", ticks

localtime = time.localtime(time.time())
print "Local current time :", localtime


localtime = time.asctime( time.localtime(time.time()) )
print "Local current time :", localtime

import calendar
cal = calendar.month(2018, 8)
print "Here is the calendar:"
print cal

print "time.altzone %d " % time.altzone

def procedure():
   time.sleep(2.5)

# measure process time
t0 = time.clock()
procedure()
print time.clock(), "seconds process time"

# measure wall time
t0 = time.time()
procedure()
print time.time() - t0, "seconds wall time"


print "Start : %s" % time.ctime()
time.sleep( 5 )
print "End    : %s" % time.ctime()



def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print "Values inside the function: ", mylist
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print "Values outside the function: ", mylist



def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4]; # This would assig new reference in mylist
   print "Values inside the function: ", mylist
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print "Values outside the function: ", mylist




