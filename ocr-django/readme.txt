Install Easy ocr

pip install easyocr
(for Windows, please install torch and torchvision first by following the official instruction here https://pytorch.org. On pytorch website, be sure to select the right CUDA version you have. If you intend to run on CPU mode only, select CUDA = None.)

Specify the image name in the readtext function and aslo the imread function for recognition and drawing boxes respectively

run the program with
python detect.py

When you run for the first time, it will download detection models and recognition models and save them in the memory.

The program runs accurately on most of the texts, memes and images.
On the downside, the runtime is much higher (approx 13 secs)
