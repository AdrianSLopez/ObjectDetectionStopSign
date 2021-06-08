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
  <p>Ex: <i>opencv_annotation -images=PositiveImages/ -annotations a.txt</i></p>
  <p>- The process of labeling is just creating a box/square around the object you want to detect</p>

  <h2>3. Training</h2>
  <p align="center"><img src="https://github.com/AdrianSLopez/ObjectDetectionStopSign/blob/main/ReadMeMedia/Training.png"></p>
  <p>- Run the following command:</p> 
  <p><i>opencv_createsamples -num (number of objects in your annotations file) -vec samples.vec(name of file that is going to be created) -info (annotations file/.txt file that saved the labeling) -bg (.txt file that has the negative images' filepath)</i></p> 
  <p>Ex: <i>opencv_createsamples -num 145 -vec samples.vec -info a.txt -bg negativeImagesFilePath.txt</i></p>
  <p> What this command basically does is it puts your positive images on top of the negative images. It gives your object different backgrounds.</p>
  <p>- Then Run the final command: </p>
  <p><i>opencv_traincascade -featureType LBP -numPos (85% of positive files that was put in the .vec file; which is the number after -num in the opencv_creatsamples command) -data (filepath to store the file that will be createdd) -bg (.txt file that has the negative images' filepath) -acceptanceRatioBreakValue 0.00001 -vec (.vec file that was created from opencv_createsamples)</i></p>
  <p>Ex: <i>opencv_traincascade -featureType LBP -numPos 123 -data home/CV/Result/ -bg negativeImagesFilePath.txt - acceptanceRatioBreakValue 0.00001 -vec samples.vec</i></p>
  <h1>Result: </h1>
  <p>- "cascade.xml" is created after using <i>opencv_trainscascade</i> command.</p>
  <p>- Used python <a href="https://github.com/AdrianSLopez/ObjectDetectionStopSign/blob/main/Result/detectStopSign.py">code</a> with OpenCV, to use the cascade file on a video, and potentially live through a webcam/camera, and detect Stop Signs.</p>
  <p align="center"><img src="https://github.com/AdrianSLopez/ObjectDetectionStopSign/blob/main/ReadMeMedia/ObjectDetectStopSign.gif"</p>
