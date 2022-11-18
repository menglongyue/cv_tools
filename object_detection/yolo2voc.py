import argparse
import multiprocessing
import os
import xml.etree.ElementTree
from PIL import Image
from pascal_voc_writer import Writer

import config


def yolo2voc(txt_file):
    w, h = Image.open(os.path.join(config.image_dir, f'{txt_file[:-4]}.jpg')).size
    writer = Writer(f'{txt_file[:-4]}.xml', w, h)
    with open(os.path.join(config.label_dir, txt_file)) as f:
        for line in f.readlines():
            label, x_center, y_center, width, height = line.rstrip().split(' ')
            x_min = int(w * max(float(x_center) - float(width) / 2, 0))
            x_max = int(w * min(float(x_center) + float(width) / 2, 1))
            y_min = int(h * max(float(y_center) - float(height) / 2, 0))
            y_max = int(h * min(float(y_center) + float(height) / 2, 1))
            writer.addObject(config.names[int(label)], x_min, y_min, x_max, y_max)
    writer.save(os.path.join(config.label_dir, f'{txt_file[:-4]}.xml'))
    
    

if __name__ == '__main__':
  
    print('YOLO to VOC')
    txt_files = [name for name in os.listdir(config.label_dir) if name.endswith('.txt')]

    with multiprocessing.Pool(os.cpu_count()) as pool:
        pool.map(yolo2voc, txt_files)
    pool.close()

   