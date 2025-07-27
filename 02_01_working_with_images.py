from PIL import Image
im_file = 'data/page_01.png'
im = Image.open(im_file)
print(im.size) # print size
im.show() # display image
im.save("temp/page_01.png") # save a file
im.rotate(90).show() # rotate and show # results in badly cropped image