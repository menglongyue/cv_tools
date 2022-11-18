# cv_tools
this repository contains data processing tools in CV, including object detection, oriented object detection, segmentation, change detection, gan, video classification etc.   

Object Detection:

- Convert datasets format from voc  to yolo or yolo to voc.
- Convert datasets from yolo to coco or coco to yolo.
- Visualizing data in voc or yolo or coco format.



Rotated Object Detection:

- Visualizing dota datasets or data submission datasets: for checking whether the gt is right.

  ```python
  # DOTA format: 
  	imgname score x1 y1 x2 y2 x3 y3 x4 y4
  
  # DOTA submission format: 
  	x1 y1 x2 y2 x3 y3 x4 y4 class_name difficult
  ```

  | ![00194](https://typora-images-1302473945.cos.ap-chengdu.myqcloud.com/images/202211181526270.jpg) | ![00196](https://typora-images-1302473945.cos.ap-chengdu.myqcloud.com/images/202211181526495.jpg) |
  | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | ![00448](https://typora-images-1302473945.cos.ap-chengdu.myqcloud.com/images/202211181527139.jpg) | ![00476](https://typora-images-1302473945.cos.ap-chengdu.myqcloud.com/images/202211181527689.jpg) |
  
  
