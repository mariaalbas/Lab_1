# Lab 1
Maria Alba Sendra
NIA: 206142

## Introduction
This repository contains the three python scripts requested for exercises 1, 4 and 5. Their respective names are ```rgb_yuv.py```, ```run_length_encoding.py``` and ```dct.py```. A part from these, there are also two folders, _Images_ and _Scripts_, containing the resulting images from exercises 2 and 3 and the screenshots from the terminal showing the command lines used. Each of these exercises are explained below, with some comments explaning the results.

### Exercise 2
We use the command line ```ffmpeg -i lenna.png -vf scale=320:240 lenna_resized.png``` to resize the input image _Lenna.png_ into lower quality. If we compare both images, the input one is 512x512 pixels while the output one is 320x240 pixels, as specified in the command line. Therefore, the resize is done as expected. The resulting image appears in the _Images_ folder, in the file _Lenna_resized.png_.

### Exercise 3
In this case we are asked to transform the input image _Lenna.png_ to bw. For that, we use the command line ```ffmpeg -i lenna.png -vf format=gray lenna_bw.png```. We can see the result in the _Images_ folder, in the file _Lenna_bw.png_.
Secondly, we compress the resulting bw image using the command ```ffmpeg -hide_banner -i lenna_bw.png -compression_level 1 lenna_compressed.png```. If we check the size of both input and output files, we observe that with the lowest compression level, which is 1, we compress from 223.6 kB (original bw image) to 215.8 kB (compressed bw image)
