---
layout:     post
title:      Tropical Tree Species Identification Using 2D and 3D Aerial Data
subtitle:   GE5219 Spatial Programming Group6
date:       26/04/2021
author:     Jifei Wang
header-img: img/post/3_0.png
catalog:   true
tags:
    - Coursework
---

## Abstract

Tree species identification is an important topic in forestry studies, including forest inventory, forest health monitoring and plant ecology. Forest restoration and management activities usually require spatial analysis of tree canopy cover and tree height to identify forest types and tree species across large areas. The complexities and heterogeneity of tropical forest composition make tree species classification a challenging task in tropical forest studies. This project combines aerial optical images and 3D point cloud data collected from the Unmanned Aerial Vehicles ([UAVs](https://www.sciencedirect.com/topics/engineering/unmanned-aerial-vehicles)) to identify tree species and forest types in tropical areas using highly efficient segmentation algorithms and machine learning classification models. The tree species identification was performed by three steps: First, we generated canopy height model ([CHM](https://www.earthdefine.com/chm/#:~:text=The%20Canopy%20Height%20Model%20(CHM,a%20CHM%20is%20LIDAR%20data.)) from point cloud data. The missing height values were interpolated using the K-nearest neighborhood ([KNN](http://scholarpedia.org/article/K-nearest_neighbor)) algorithm. Second, tree crown segmentation methods based on multiresolution segmentation ([MRS](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4183749/#:~:text=Although%20multiresolution%20segmentation%20(MRS)%20is,which%20reduces%20the%20classification%20accuracy.)) and watershed algorithm were applied for delineating individual tree crowns. Finally, object-level features were extracted for classification to increase accuracy in forest tree species identification. The classification results of tropical tree species proved that object-based classification techniques using a small size of samples for training are effective in the applications of tropical forest identification. The overall accuracy and kappa coefficient for classification results based on Random Forest([RF](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)) model can reach 0.74 and 0.68 respectively.

![avatar](/img/post/3_1.png)
**Study area**

![avatar](/img/post/3_2.png)
**Dataset**

## Introduction
The application of UAV provides opportunities to incorporate multisource information in tree species classification. The change of canopy height derived from DAP point clouds reflects tree structure and helps identify the peak and range of each tree crown. The differences in spectral characteristics between individual trees and backgrounds can be used to classify diverse tree species. The purpose of individual tree species classification is to identify tree canopy based on different spectral and structural information ([Ramiya et al., 2019](https://doi.org/10.1016/j.rsase.2019.100242); [Yun et al., 2021](https://doi.org/10.1016/j.rse.2021.112307 )). The main steps of individual tree classification methods include individual tree crown segmentation and individual tree species classification ([Yun et al., 2021](https://doi.org/10.1016/j.rse.2021.112307 )). Multiresolution segmentation algorithms (MRS), region growth, and spectral clustering algorithms are widely used in individual tree crown detection based on multispectral images ([Apostol et al., 2020](https://doi.org/10.1016/j.rse.2021.112307 ); [Erikson, 2004](https://doi.org/10.1016/j.rse.2004.04.006 ); [Yurtseven et al., 2019](https://doi.org/10.1016/j.measurement.2019.05.092 )). Watershed and nearest neighbor algorithms were applied in many researches concerning DAP point cloud segmentation ([Kopačková-Strnadová et al., 2021](https://doi.org/10.3390/rs13040705); [Li et al., 2012](https://doi.org/10.14358/pers.78.1.75 ); [Miraki et al., 2021](https://doi.org/10.1016/j.ecoinf.2020.101207 ); [Reitberger et al., 2009](https://doi.org/https://doi.org/10.1016/j.isprsjprs.2009.04.002 ); [Silva et al., 2016](https://doi.org/10.1080/07038992.2016.1196582 )). To identify tree species in heterogenous forest areas, the accurate delineation of tree crowns is essential for tree species classification. Both 2D and 3D characteristics of tree structures and canopies are considered. The 2D indices include spectral features, textural features, TCT components, and Vegetation indexes can be calculated from multispectral images. The 3D indices such as tree height, treetops can be directly derived from DAP point clouds. Thus, the classification is conducted by combing spectral and structural features to improve performance.

In this project, we realized individual tree species identification using the chestnut dataset, which contains multispectral imagery and DAP point cloud. The individual tree was segmented based on Canopy Height Model (CHM) derived from point cloud data and tree species classification was performed on object-level using various features generated from multispectral image and point cloud data. The individual tree species classification was implemented based on the following methods:

- Object-based Segmentation: Watershed segmentation, Multiresolution segmentation.
- 3D information projection: Triangular algorithm, Pit-free algorithm, K-nearest Neighbor (KNN) imputation algorithm.
- Texture metrics extraction: Gray-level Co-occurrence Matrix (GLCM) algorithm.
- Dimensional reduction: Principal Component Analysis (PCA), Linear Discriminant Analysis (LDA).
- Classification: Support Vector Machine (SVM) classifier, Random Forest (RF) classifier.

![avatar](/img/post/3_4.png)
![avatar](/img/post/3_5.png)
**Tree species classification maps**

## Contributions

The previous studies concerning tree species classification using UAV datasets have been carried out in forests with less diverse species structures, for example, boreal and temperate forests. In this study, we based our research on simultaneously acquired multi-source images and point clouds from UAVs, and implemented individual tree detection algorithms and a machine learning approach to identify the tree species in tropical forests in Singapore, Chestnut National Park. The results demonstrated that a combination of spectral texture and structural metrics can improve classification accuracy. The logical framework was proved effective in 2D and 3D data fusion and tree types identification. The results from comparative analysis also proved that MRS segmentation performed better than other segmentation methods and OA of the Random Forest classifier is higher than SVM in this scenario. The experimental work could provide an insightful technical flow in forest inventory research in tropical forests. Also, this study highlighted that the combination of UAV images and 3D point clouds has broad potential for application in forest classification, object detection, and other related fields.

**Github repository** [Tree species classification](https://github.com/Wang-Jifei/tree_species_classification)

**ArcGIS Story Map** [Here](https://arcg.is/0TKjyO0)

**Download Full Project Report** [Here](https://drive.google.com/file/d/1wG8kzegdccw7UNkr5v5WCJ3k9fa8yvT_/view?usp=sharing)
