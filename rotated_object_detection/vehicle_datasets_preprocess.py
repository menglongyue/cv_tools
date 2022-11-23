import cv2
import os

'''
去除vehicle dataset中img的外圈padding的白色条状
'''

img_path = '/Users/huangquanjin/Data/oriented_car_detection/val/valimg'
label_path = '/Users/huangquanjin/Data/oriented_car_detection/val/valyololabel'
img_save_path = '/Users/huangquanjin/Data/oriented_car_detection/val/val_img_process'
label_save_path = '/Users/huangquanjin/Data/oriented_car_detection/val/valyololabel_process'

for label_name in os.listdir(label_path):
    img_stem = label_name.split('.')[0]
    img_name = img_stem + '.jpg'
    img_path_ = os.path.join(img_path, img_name)
    label_path_ = os.path.join(label_path, label_name)
    img = cv2.imread(img_path_)
    img_ = img[100:612, 100:740, :]
    
    cv2.imwrite(img_save_path + '/' + img_name, img_)
    
    with open(label_path_, 'r') as f:
        label_info = f.readlines()
        with open(label_save_path + '/' + label_name, 'w') as f1:
            for label in label_info:
                label = label.strip().split(' ')
                bbox_new = [(float(x)-100) for x in label[:8]]
                
                if bbox_new[0] < 0:
                    bbox_new[0] = 0
                elif bbox_new[0] > 640:
                    bbox_new[0] = 640
                if bbox_new[1] < 0:
                    bbox_new[1] = 0
                elif bbox_new[1] > 512:
                    bbox_new[1] = 512
                    
                if bbox_new[2] < 0:
                    bbox_new[2] = 0
                elif bbox_new[2] > 640:
                    bbox_new[2] = 640
                if bbox_new[3] < 0:
                    bbox_new[3] = 0
                elif bbox_new[3] > 512:
                    bbox_new[3] = 512
                    
                if bbox_new[4] < 0:
                    bbox_new[4] = 0
                elif bbox_new[4] > 640:
                    bbox_new[4] = 640
                if bbox_new[5] < 0:
                    bbox_new[5] = 0
                elif bbox_new[5] > 512:
                    bbox_new[5] = 512
                    
                if bbox_new[6] < 0:
                    bbox_new[6] = 0
                elif bbox_new[6] > 640:
                    bbox_new[6] = 640
                if bbox_new[7] < 0:
                    bbox_new[7] = 0
                elif bbox_new[7] > 512:
                    bbox_new[7] = 512
                
                for x in bbox_new:
                    f1.write(str(x))
                    f1.write(' ')
                    
                f1.write(label[8])
                f1.write(' ')
                f1.write(label[9])
                f1.write('\n')
            # break
                
            
    
    
