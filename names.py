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
	 	count = 1
	 	for y in users[teach[x]]:
	 		for z in xrange(len(y)-1):
	 			print str(count)+" - "+y["first_name"]+" "+y["last_name"]+" - "+str(len(y["first_name"])+len(y["last_name"]))
	 		count +=1
dojo()