from PIL import Image


im_file = 'data/page_01.png'
im = Image.open(im_file)

# print size
print(im.size)

# display image
im.show()

# rotate and show
# im.rotate(90).show() # results in badly cropped image

# save a file
im.save("temp/page_01.png")