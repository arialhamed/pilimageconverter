from PIL import Image
from os import listdir
from time import sleep

ext_list = ("bmp","dib","eps","gif","ico","msp","pcx","png","ppm","sgi","tga","blp","cur","dds","mpo","pcd","psd","xpm")
the_list = [x for x in listdir('.') if x[len(x)-3:len(x)] in ext_list]

for x in range(len(the_list)):
    print('{}: {}'.format(x+1, the_list[x]))

checklist = [0,0]

while not(checklist[0]):
    print()
    print('Enter index of file displayed above.')
    try:
        file_in = the_list[int(input('>>> '))-1]
        checklist[0] = 1
    except:
        print('Try again, index of file is not valid')

while not(checklist[1]):
    print()
    print('Enter extension to copy file to.')
    ext = input('>>> .')
    if ext in ext_list:
        checklist[1] = 1
    else:
        print('Try again, Extension is not currently valid by program/PIL')

file_proc = file_in[:len(file_in)-4]
img = Image.open(file_in)
print()

try:
    img.save(file_proc+'.'+ext, ext.upper())
    print('Operation successful!')
except:
    print('Operation failed...')
finally:
    sleep(1)
