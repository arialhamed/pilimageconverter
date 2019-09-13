from PIL import Image
from os import listdir

ext_list = (".bmp",".dib",".eps",".gif",".ico",".msp",".pcx",".png",".ppm",".sgi",".tga",".blp",".cur",".dds",".mpo",".pcd",".psd",".xpm")
the_list = [x for x in listdir('.') if x[len(x)-4:len(x)] in ext_list]

for x in range(len(the_list)):
    print('{}: {}'.format(x+1, the_list[x]))

print()
print('Enter index of file displayed above.')
file_in = the_list[int(input('>>> '))-1]

print()
print('Enter extension to copy file to.')
ext = input('>>> .')

file_proc = file_in[:len(file_in)-4]
img = Image.open(file_in)
print()

try:
    img.save(file_proc+'.'+ext, ext.upper())
    print('Operation successful!')
except:
    print('Operation failed...')
