---
layout:     post
title:      Building Extraction from GF-2 Satellite Image Based on Deep Learning Method
subtitle:   Undergraduate Final Thesis
date:       01/06/2020
author:     Jifei Wang
header-img: img/post/0_0.PNG
catalog:   true
tags:
    - Research
---

## Abstract

Building extraction from high-resolution remote sensing images is a long-standing research topic in urban planning, land use analysis, and remote sensing applications. Deep learning has received growing research attention over recent years. Numerous studies show that deep learning methods can accurately extract buildings from remote sensing images. In order to solve the problems of low accuracy and noise of the existing deep learning methods for optical remote sensing images segmentation of complex scenes, this paper proposed an image segmentation algorithm based on improved U-Net network architecture. A Deep Residual U-Net model was constructed by integrated residual blocks and a Hybrid Residual U-Net model was presented to simplify the network structure and increase training efficiency. The method includes the following steps: First, the original GF-2 satellite images are preprocessed and labeled to construct a training imagery dataset. The proposed deep network architecture is then trained with the training dataset to extract buildings at the pixel level. Experimental results show that the Deep Residual U-Net algorithm can improve 2-3% accuracy performance compared with other architectures.

**Keywords:** deep learning, building extraction, deep residual U-Net, high resolution remote sensing image

**The framework of the pixel-level segmentation using deep learning networks.**

![avatar](/img/post/0_1.png)

**Deep Residual U-Net structure**

![avatar](/img/post/0_2.png)

**Hybrid Residual U-Net structure**

![avatar](/img/post/0_3.png)

**Different model segmentation prediction results. (a)RGB image (b)Label image (c)FCN (d)Segnet (e)U-Net (f)Hybrid Residual U-Net (g)Deep Residual U-Net**

![avatar](/img/post/0_4.png)

**Values of evaluation metrics of building extraction results using different methods**

![avatar](/img/post/0_5.png)

Download paper [Here](https://drive.google.com/file/d/1WFY89jp-8v0NVMt-AjcUB2QIzf_GsE0g/view?usp=sharing)
Download dissertation slides(in Chinese) [Here](https://drive.google.com/file/d/1BkeIOiShrLHx60A8D37KG-5026ZqP99T/view?usp=sharing)
