s=input('enter the name:')

initials=''

for c in s:
	if c.isupper():
		initials+=c
print(initials)