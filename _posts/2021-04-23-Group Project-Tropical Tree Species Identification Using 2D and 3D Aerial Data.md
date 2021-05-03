---
layout:     post
title:      Tropical Tree Species Identification Using 2D and 3D Aerial Data
subtitle:   GE5219 Spatial Programming Group6
date:       23/04/2021
author:     Jifei Wang
header-img: img/the-first.png
catalog:   true
tags:
    - Coursework
---

## Abstract

Tree species identification is an important topic in forestry studies, including forest inventory, forest health monitoring and plant ecology. Forest restoration and management activities usually require spatial analysis of tree canopy cover and tree height to identify forest types and tree species across large areas. The complexities and heterogeneity of tropical forest composition make tree species classification a challenging task in tropical forest studies. This project combines aerial optical images and 3D point cloud data collected from the Unmanned Aerial Vehicles (UAVs) to identify tree species and forest types in tropical areas using highly efficient segmentation algorithms and machine learning classification models. The tree species identification was performed by three steps: First, we generated canopy height model (CHM) from point cloud data. The missing height values were interpolated using the K-nearest neighborhood (KNN) algorithm. Second, tree crown segmentation methods based on multiresolution segmentation (MRS) and watershed algorithm were applied for delineating individual tree crowns. Finally, object-level features were extracted for classification to increase accuracy in forest tree species identification. The classification results of tropical tree species proved that object-based classification techniques based on small samples are effective in the applications of tropical forest identification.