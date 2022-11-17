from PIL import Image

name_image = '1.jpeg'
cut_x = 200  #pixels for shift-effect
k_eff = 0.7  #transparency
size = (80, 80) #finally size (WxH)
x0, y0 = 0, 0

red, green, blue = Image.open(name_image).split()

coordinates_left = (cut_x, y0, red.width, red.height)
left = red.crop(coordinates_left)

coordinates_right = (x0, y0, red.width - cut_x, red.height)
right = blue.crop(coordinates_right)

coordinates_mid = (cut_x / 2, y0, red.width - (cut_x / 2), red.height)
mid_red = red.crop(coordinates_mid)
mid_blue = blue.crop(coordinates_mid)
mid_green = green.crop(coordinates_mid)

effect_red = Image.blend(left, mid_red, k_eff)
effect_blue = Image.blend(right, mid_blue, k_eff)

art_image = Image.merge("RGB", (effect_red, mid_green, effect_blue))
#art_image.thumbnail(size)
art_image.save('2.jpeg')