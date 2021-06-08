# ObjectDetectionStopSign
A project using OpenCV, Ubuntu, and python for detecting Stop Signs on videos.

<h1>Process<h1>
<h2>1. Data Collecting</h2>
  <p align="center"><img src="https://github.com/AdrianSLopez/ObjectDetectionStopSign/blob/main/ReadMeMedia/DataSet.jpg"></p>
   <p>- Collected 150 positive images. *Positive images are images that contain the object you want to label/detect.</p>
   <p>- Resized 150 images to 256x256 pixels.\n</p>
   <p>- Download Negative images from https://github.com/JoakimSoderberg/haarcascade-negatives/tree/master/images. *Negative images are images that should not contain your object</p>
  <p>- Created a txt file that has all the negative images' filepath, by using the following command: </p>
  <p><i>ls (folder that stores all negative images)/* > (.txt file name thats going to be created)</i></p>
  <p>Ex: <i> ls negativeImages/* > negativeImagesFilePath.txt</i><p>

  <h2>2. Labeling</h2>
<p align="center"><img src="https://github.com/AdrianSLopez/ObjectDetectionStopSign/blob/main/ReadMeMedia/Labeling.jpg"></p>
  <p>- Labeled my positive images using the following command:</p>
  <p><i>- opencv_annotation -images=(filepath of positive images) -annotations (.txt filename, thats going to be created, to save the labeling ) *My annotation file name is "a.txt"</i></p>
  <p>- The process of labeling is just creating a box/square around the object you want to detect</p>

<h2>3. Training</h2
  <p align="center"><img src="https://github.com/AdrianSLopez/ObjectDetectionStopSign/blob/main/ReadMeMedia/Training.png"></p>
  <p>- textt</p> 


  <h1>Result: </h1>

<p align="center"><img src="https://github.com/AdrianSLopez/ObjectDetectionStopSign/blob/main/ReadMeMedia/ObjectDetectStopSign.gif"</p>
