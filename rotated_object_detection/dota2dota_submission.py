
# this scripts convert dota format to dota submission format for visualization
# dota submission format: imgname score x1 y1 x2 y2 x3 y3 x4 y4
# dota format: x1 y1 x2 y2 x3 y3 x4 y4 class_name difficult

import os
dota_labels = '/Users/huangquanjin/Data/oriented_car_detection/val/valyololabel'
dota_submission_labels = '/Users/huangquanjin/Data/oriented_car_detection/val/valimg_dota_submission'

for txt in os.listdir(dota_labels):
    txt_path = os.path.join(dota_labels, txt)
    save_path = os.path.join(dota_submission_labels, txt)
    with open(txt_path, 'r') as f1:
        with open(save_path, 'w') as f2:
            infos = f1.readlines()
            for info in infos:
                
                info_ = info.strip().split(' ')
                print(info_)
                f2.write(txt.split('.')[0] + ' ')
                f2.write(str(float(1)))
                f2.write(' ')
                # print([str(x) for x in info_[:8]])
                f2.write(" ".join([x for x in info_[:8]]) + '\n')
                
