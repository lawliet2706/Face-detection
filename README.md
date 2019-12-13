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

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system


## Authors

See the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* **Iván de Paz Centeno** - *Initial work* - [ipazc](https://github.com/ipazc)
