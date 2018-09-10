# MesoNet

You can find here the implementation of the network architecture and the dataset used in our paper on digital forensics.   

> We present a method to automatically detect face tampering in videos. We particularly focus on two recent approaches used to generate hyper-realistic forged videos: deepfake and face2face. Traditional image forensics techniques are usually not well suited to videos due to their compression that strongly degrades the data. Thus, we follow a deep learning approach and build two networks, both with a low number of layers to focus on mesoscopic properties of the image. We evaluate those fast networks on both an existing dataset and a dataset we have constituted from online videos. Our tests demonstrate a successful detection for more than 98\% for deepfake and 95\% for face2face.

[Link to full paper](https://arxiv.org/abs/1809.00888)

## Requirements

- Python 3.5
- Numpy 1.14.2
- Keras 2.1.5

## Dataset

### Aligned face datasets

|Set|Size of the forged image class|Size of real image class|
|---|---|---|
|Training|5111|7250|
|Validation|2889|4259|

[Training set (~150Mo)](#)

[Validation set (~50Mo)](#)

### Video datasets

[Training + Validation set (~1.4Go)](#)

## Help

## Changelog

- Add preprint link
