print('-'*65)
print('Narrative Bot:')
print()
grade = input('What grade did I receive on my narrative?')
grade = int(grade)
if grade >= 65:
	print('Hugo, your final grade in AP Computer Science is 94%.')
	print('You have excelled in all components of the class!')
	print('I wish you continued success in the next semester of AP Computer Science!')
else:
	print('Hugo, your final grade in AP Computer Science is 62%.')
	print('This is largely a result of missing projects and homework assignments.')
	print('Unfortunately, because this grade is less than a 65, you will have to complete an MBA assignment next semester.')
	print('-'*65)