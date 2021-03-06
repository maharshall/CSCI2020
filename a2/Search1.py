import sys
import time

def buildIndex(filename):
	try:
		f = open(filename, "r")
	except:
		print "Cannot open file %s! Maybe you made a typo :(" % filename
		sys.exit()

	courses = {}

	for line in f.readlines():
		info = line.split("            ")
		courses[info[0]] = info[1] 
	
	return courses

def search(index, keyword):
	for target in index.keys():
		if keyword.lower() in index[target].lower():
			print target, " : ", index[target]

def resetTimer():
  global START
  START = time.time()

def readTimerMilliseconds():
  t = time.time() - START
  return (t * 1000)


#----------------------------------------------
if len(sys.argv[1:]) < 2:
	print "Usage <file> <keyword>"
	sys.exit()

filename = sys.argv[1]
keyword = sys.argv[2]

courses = buildIndex(filename)
resetTimer()
search(courses, keyword)
print "Took %f milliseconds to search for keyword %s" % (readTimerMilliseconds(), keyword)
