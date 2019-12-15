# Face detector

Implementation of the MTCNN face detector for Keras in Python3.4+. It is based on the paper *Zhang, K et al. (2016)* [ZHANG2016]_ and MTCNN implementation of [ipazc](https://github.com/ipazc) .

## Prerequisites
* Python 3.4+
* Keras >=2.0.0
* OpenCV >=4.1

### Installing

Currently, this version of the MTCNN implementation is only supported on Python3.4 and onwards. The implementation itself can be installed through pip:

    $ pip install mtcnn

The implementation of MTCNN used in this script also requires OpenCV>=4.1 and Keras>=2.0.0 (and any Tensorflow supported by Keras).
If this is the first time you use tensorflow, you will probably need to install it in your system:



    $ pip install tensorflow

or with `conda`



    $ conda install tensorflow

Note that `tensorflow-gpu` version can be used instead if a GPU device is available on the system, which will speedup the results.

## USAGE

.. code:: python

    >>>import cv2
    >>>from facedetection import find_faces
    >>>from mtcnn import MTCNN
    >>>from PIL import Image, ImageEnhance,ImageDraw, ImageFont

    detector = MTCNN()

    image = 'hoomens.jpg'
    result = find_faces(image,detector)

    for img in result:
        img.show()

The output is just a image with faces detected by our face detector.

## Deployment

I used conda environment, couldn't get it to work with VisualStudio


## Authors

See the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* **Iván de Paz Centeno** - *Initial work* - [ipazc](https://github.com/ipazc)
