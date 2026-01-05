import os
for dirname, _,filename in os.walk('.'):
	for filename in filename:
		print(os.path.join(dirname, filename))