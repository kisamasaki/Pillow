from PIL import Image
aoba_im=Image.open('aoba.jpg')
cropped_im=aoba_im.crop((240,25,420,210))
cropped_im.save('cropped.png')