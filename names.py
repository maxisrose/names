def names():
	students = [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
	]
	for x in xrange(len(students)):
		print students[x]["first_name"]+" "+students[x]["last_name"]
names()

def dojo():
	users = {
 'Students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
	for x in xrange(len(users)):
 		name = 0
 		teach = users.keys()
	 	print teach[x]
	 	for y in users.itervalues():
	 		for z in xrange(len(y)):
	 			print z
	 			print y[z]
	 			first = y[z]
	 			last = y[z]
	 			print str(z)+" - "+first[first_name]+" "+last[last_name]+" - "+str(len(first[first_name])+len(last[last_name]))
[first_name]
dojo()