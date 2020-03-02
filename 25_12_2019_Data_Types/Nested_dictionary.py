#this program only prints the value of the nested dictionary
data = {"x" : {"y" : {"z" : "1Rivet"},
		"m" : "css",
		"l" :{"a" : "valsad" }}
		}

#stores the type of dictionary in variable t
#t=type(dict())

def dict_values(di):
	for v in di.values():
		#checks the type of v. whether it is dictionary or not
		# if(type(v)!=t):
		# 	print(v)
		if isinstance(v, dict):
			dict_values(v)
		else:
			print(v)
dict_values(data)
