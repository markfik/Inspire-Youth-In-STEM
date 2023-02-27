'''
filename = 'C:\\Users\\user\\Documents\\Inspire-Youth-In-STEM\\Week-4\\text.txt','r+w'

#exception handling
try:
    with open(filename,'r+w',encoding=None) as f_obj:
        contents =f_obj.read()
        print(contents)

except FileExistsError:
    msg ="sorry the file: "+filename+" doesn`t exist"

print(filename)
'''

file_name =open("C:\\Users\\user\\Documents\\Inspire-Youth-In-STEM\\Week-4\\text.txt",'r')
print(file_name.readlines())