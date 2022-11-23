'''
from pascal_voc_writer import Writer

# Writer(path, width, height)
writer = Writer('path/to/img.jpg', 800, 400)
# ::addObject(name, xmin, ymin, xmax, ymax)
writer.addObject('cat', 100, 100, 200, 200)
# ::save(path)
writer.save('path/to/img.xml')
'''

label_dir = '/Users/huangquanjin/Data/oriented_car_detection/val/vallabel'
image_dir = '/Users/huangquanjin/Data/oriented_car_detection/val/valimg'
save_dir = '/Users/huangquanjin/Data/oriented_car_detection/val/valyololabel'
names = ['car', 'truck', 'bus', 'van', 'feright_car', 'feright car']
