#  for visdrone vehicle datasets:
import argparse
import multiprocessing
import os
import xml.etree.ElementTree
from PIL import Image
import config


def voc2yolo(xml_file):
    in_file = open(f'{config.label_dir}/{xml_file}')

    root = xml.etree.ElementTree.parse(in_file).getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    has_class = False
    for obj in root.iter('object'):
        name = obj.find('name').text
        if name in config.names:
            has_class = True
    if has_class:
        out_file = open(f'{config.save_dir}/{xml_file[:-4]}.txt', 'w')
        for obj in root.iter('object'):
            name = obj.find('name').text
            print('name : ', name)
                # assert obj.find('bndbox') and obj.find('polygon'), 'both bndbox and polygon exists!!!!!!!!!'
            if obj.find('bndbox'):
                xml_box = obj.find('bndbox')
                x1 = float(xml_box.find('xmin').text)
                y1 = float(xml_box.find('ymin').text)
                x4 = float(xml_box.find('xmax').text)
                y4 = float(xml_box.find('ymax').text)
                x2 = x4
                y2 = y1
                x3 = x1
                y3 = y4

                b = [x1, y1, x2, y2, x4, y4, x3, y3]
                # cls_id = config.names.index(obj.find('name').text)
                cls_id = name
                if name == 'feright car' or name == 'feright_car':
                    cls_id = 'feright_car'
                difficult = 0
                out_file.write(" ".join([str(f'{a:.6f}') for a in b]) + ' ' + str(cls_id) + " " +  str(difficult) + '\n')
                
            if obj.find('polygon'):
                xml_box = obj.find('polygon')
                x1 = float(xml_box.find('x1').text)
                y1 = float(xml_box.find('y1').text)
                x2 = float(xml_box.find('x2').text)
                y2 = float(xml_box.find('y2').text)
                x3 = float(xml_box.find('x3').text)
                y3 = float(xml_box.find('y3').text)
                x4 = float(xml_box.find('x4').text)
                y4 = float(xml_box.find('y4').text)
                b = [x1, y1, x2, y2, x3, y3, x4, y4]
                cls_id = name
                if name == 'feright car' or name == 'feright_car':
                    cls_id = 'feright_car'
                difficult = 0
                out_file.write(" ".join([str(f'{a:.6f}') for a in b]) + ' ' + str(cls_id) + " " +  str(difficult) + '\n')

if __name__ == '__main__':

    print('VOC to YOLO')
    xml_files = [name for name in os.listdir(config.label_dir) if name.endswith('.xml')]
    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        pool.map(voc2yolo, xml_files)
    pool.join()