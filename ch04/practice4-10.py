def addComma(list1):
	out = ''
	for i in range(len(list1)):
		if(i == (len(list1) - 1)):
			out = out + ', and ' + list1[i]
			return out
		elif(i == 0):
			out = list1[i]
		else:
			out = out + ', ' + list1[i]

spam = ['apples','bananas','tofu','cats']
print(spam)
spam = addComma(spam)
print(spam)
