# ObjectDetectionStopSign
A project using OpenCV, Ubuntu, and python for detecting Stop Signs on videos.

#Process

1. Data Collecting    
  <img align="center" src="https://github.com/AdrianSLopez/ObjectDetectionStopSign/blob/main/ReadMeMedia/DataSet.jpg">
   - Collected 150 positive images. *Positive images are images that contain the object you want to label/detect.
   - Resized 150 images to 256x256 pixels.
   - Download Negative images from https://github.com/JoakimSoderberg/haarcascade-negatives/tree/master/images. *Negative images are images that should not contain your object
   

2. Labeling
<p align="center">
  <img src="https://github.com/AdrianSLopez/ObjectDetectionStopSign/blob/main/ReadMeMedia/Labeling.jpg">
</p>
   - Labeled my positive images using the following command:
      - opencv_annotation -images=(filepath of positive images) -annotations (filename of where you want to save the labeling *.txt*) *My annotation file name is a.txt
   - The process of labeling is just creating a box/square around the object you want to detect

3.
  - 


Result: 

![](https://github.com/AdrianSLopez/ObjectDetectionStopSign/blob/main/ReadMeMedia/ObjectDetectStopSign.gif)
