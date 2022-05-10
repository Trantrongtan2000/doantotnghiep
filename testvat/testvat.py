import image

im=image.open('mau1.jpg')

imbox=im.getbox()
crop=im.crop(imbox)
crop.save('anhcut.jpg')