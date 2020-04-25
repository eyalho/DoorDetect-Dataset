# DoorDetect Dataset
DoorDetect is a dataset of 1,02 images that have been annotated with doors
Total 174 doors..

## Images
The images annotated are from [Open Images Dataset V4](https://storage.googleapis.com/openimages/web/index.html) and [MCIndoor20000 ](https://github.com/bircatmcri/MCIndoor20000).

![alt text](/readme_figures/Fig1.png)



## Labels
1. The object location is specified by the coordinates of its bounding box. Boxes were marked using [Yolo_mark](https://github.com/AlexeyAB/Yolo_mark). There is a .txt file for each image with the same name. Each line in the label file is of the form: `<object-class> <x> <y> <width> <height>`.

Where:
* `<object-class>`: integer number of object. (0) *door*; (1) *handle*; (2) *cabinet door*; (3) *refrigerator door*.
* `<x> <y> <width> <height>`: float values relative to width and height of the image.
* `<x> <y>`: center of the box.

2. annotation file of the form                     
 "[[xmin1, ymin1, width1, height1, idx1], ]"
 (was converted with convert_annotations.py)

![alt text](/readme_figures/Fig3.png)

##  tnesorflow faster rcnn see github eyalho/faster_rcnn


## YOLO with DoorDetect
The dataset can be used for training and testing an object detection CNN such as [YOLO](https://pjreddie.com/darknet/yolo/). Weights for detecting doors and handles with YOLO can be downloaded from: [YOLO_weights](https://drive.google.com/open?id=1i9E9pTPN5MtRxgBJWLnfQl2ypCv92dXk) (mAP=45%). For running YOLO you might also need the network configuration file [yolo-obj.cfg](https://github.com/MiguelARD/DoorDetect-Dataset/blob/master/yolo-obj.cfg) and a text file where the detected classes names and their order is specified [obj.names](https://github.com/MiguelARD/DoorDetect-Dataset/blob/master/obj.names).

![alt text](/readme_figures/Fig4.png)

## Citation
Please cite the paper in your publications if it helps your research.

```
  @misc{arduengo2019robust,
      title={Robust and Adaptive Door Operation with a Mobile Manipulator Robot},
      author={Miguel Arduengo and Carme Torras and Luis Sentis},
      year={2019},
      eprint={1902.09051},
      archivePrefix={arXiv},
      primaryClass={cs.RO}
    }
```

Link to the paper: [Robust and Adaptive Door Operation with a Mobile Manipulator Robot](https://arxiv.org/abs/1902.09051)
