from PIL import Image

from resizeimage import resizeimage

f_name = input("Имя файла\n")

sizes = input("Width Height separate with whitespace\n")

sizes = sizes.split(' ')

sizes = list(map(int,sizes))

fd_img = open(f_name, 'r+b')
img = Image.open(fd_img)
img = resizeimage.resize_cover(img, sizes)
img.save(f"{f_name}-crop.{img.format}", img.format)
fd_img.close()
