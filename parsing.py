import os

os.chdir('/Users/tim/Downloads/test')

# print('\n')
# print(os.getcwd())

print('\n')

for f in os.listdir('/Users/tim/Downloads/test'):

	f_name, f_ext = os.path.splitext(f)
	f_title, f_course, f_num = f_name.split('-') 
	f_title = f_title.strip()
	f_course = f_course.strip()
	f_num = f_num.strip()[1:].zfill(2)		# Grab everything from first element

	new_name = '{}-{}{}'.format(f_num, f_title, f_ext)
	os.rename(f,new_name)
	print('{}-{}-{}{}'.format(f_num, f_course, f_title, f_ext))