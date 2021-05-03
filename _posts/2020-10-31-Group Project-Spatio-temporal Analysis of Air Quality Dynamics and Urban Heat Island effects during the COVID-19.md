---
layout:     post
title:      Spatiotemporal Analysis of Air Quality Dynamics and Urban Heat Island effects during the COVID-19
subtitle:   GE5228 Big Spatial Data and Analytics Group2
date:       31/10/2020
author:     Jifei Wang
header-img: img/post/1_0.png
catalog:   true
tags:
    - Coursework

---

## Abstract

The outbreak of novel coronavirus pneumonia is the most serious global issue in 2020, causing enormous impacts on various aspects of human society from public health to economic growth. The ecological environment has also been affected due to the transformation of human activities during the epidemic period. The implementation of the ‘Lockdown’ and ‘Stay-in-Home’ policies have reduced the pollution emissions from transport and commercial areas, thus altered the urban environment. Based on the analysis of the temporal and spatial distribution of the COVID-19, we studied the changes of the air and thermal environment in Wuhan City and New York City in 2020. Combining spatial interpolation and spatial clustering analysis, we further analyzed the dynamics of air pollution and urban heat island effect to evaluate environmental variations.
![avatar](/img/post/1_1.png)

## Introduction

To investigate the consequences of epidemic control strategies and understand the environmental changes during the disease outbreak, we focused our research on two typical cities, Wuhan City and New York City, which are both epicentres in the global pandemic. The primary purpose of our project is to make a temporal and spatial comparison of air pollution (i.e. PM2.5) and thermal environment variations (i.e., land surface temperature) in the metropolitan urban area. Using geospatial analysis tools and remote sensing data, we further explore the consequences of COVID-19 based on the distribution characteristics of disease mapping.

The objectives of our project are summarized as follows:

1. To understand the temporal and spatial distribution of COVID-19 cases in the two cities during the outbreak.
2. To assess the influence of epidemic spread based on the air quality level using critical air quality indicators, e.g. PM2.5, NO2, CO, SO2, O3.
3. To investigate the spatial pattern of air pollutants and understand the Urban Heat Island phenomenon under the impact of COVID-19 spread.
   ![avatar](/img/post/1_2.png)

## Data and Method

### Study Area

Wuhan City, located in Hubei Province, was the earliest outbreak region in China. The Yangtze River flows through the center of the city, dividing the central urban area of Wuhan into three regions. The city has a population of over 11 million and underwent a lockdown from January 23 to April 8. Until September 8, there were 68,139 cases in total in Wuhan during the epidemic outbreak ([Peng et al., 2020](https://doi.org/10.3390/ijgi9060402)). The geographic location of Wuhan is 113°41’20” E ~ 115°6’40” E, 29°58’30” N ~ 31°20’25” N.

 ![avatar](/img/post/1_3.png)

New York City, located at the southern tip of the U.S state of New York, became the center of the epidemic at the end of March 2020. New York City has a highly dense population of 8.3 million people spread across five boroughs interconnected by a subway system that also extends into neighboring areas ([U.S. Census Bureau, 2020](https://www.census.gov/quickfacts/newyorkcitynewyork)). According to the New York City had 445,071 cases as of September 8, 2020. The geographic location of New York City is 73°41’50” W ~ 74°15’25” W, 40°29’30” S ~ 40°55’10” S.

![avatar](/img/post/1_4.png)

### Data

In our project, the comprehensive analysis of various environmental factors influenced by COVID-19 control strategies is based on multi-source data:

- The COVID-19 cases,     population composition, and hospital assistance data.
- The daily air quality data     of the Wuhan City and New York City.
- Satellite imagery data     covers the study area

The COVID-19 data for Wuhan is accumulated from the Wuhan Health Commission [website](http://wjw.wuhan.gov.cn/xwzx_28/), and the New York data is from NYC Health [website](https://www1.nyc.gov/site/doh/covid/covid-19-). The COVID-19 cases data in Wuhan is collected from 23rd Jan to 28th May, while the cases data in New York City is from 1st Mar to 17th Jun. The daily AQI data of Wuhan, from 1 January 2016 to 31 September 2020, is provided by the [China National Environmental Monitoring Centre](http://www.cnemc.cn/). The daily AQI data of New York, from 1 January 2016 to 31 September 2020, is provided by the United States Environmental Protection Agency ([EPA](https://www.epa.gov/outdoor-air-quality-data)).

The Landsat 8 satellite images for the year 2019, 2020 are provided by the U.S. Geological Survey ([USGS](https://glovis.usgs.gov/app)). Due to the limitation of image quality and vacancy of data, we selected the image with little cloud cover over the study area before and after the pandemic outbreak. The Landsat 8 satellite comprises the camera of the Operational Land Imager (OLI) and the Thermal Infrared Sensor (TIRS) which can be used to study earth surface temperature and is used to study global warming ([Roy et al., 2014](https://doi.org/10.1016/j.rse.2014.02.001)). In this study, we used Landsat8 Level L1B data to calculate Land Surface Temperature (LST) to monitor the dynamics of Urban Heat Island (UHI).

![avatar](/img/post/1_5.png)

### Methods

### Spatial autocorrelation algorithm

Moran’s I statistic measures the spatial autocorrelation and is calculated as follows:

![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image002.png)            (1)

where ![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image004.png) and ![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image006.png) were the region indexes and ![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image008.png) indicated the adjacency between area ![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image004.png) and area ![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image006.png). This study considered different types of adjacency newly confirmed cases in areas ![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image004.png) and ![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image006.png), respectively, and ![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image010.png) was the average of the number of newly confirmed cases in the entire region. A value of 0 indicated that there was no spatial autocorrelation in the data. A positive Moran’s I value indicated the clustering of similar values, whereas a negative Moran’s I value indicated the clustering of dissimilar values. The larger the absolute Moran’s I value, the stronger the spatial autocorrelation ([Kang et al., 2020](https://doi.org/10.1016/j.ijid.2020.03.076)).

### Cluster analysis model

#### Hotspot analysis

The Hot Spot Analysis tool calculates the Getis-Ord Gi* statistic (pronounced G-i-star) for each feature in a dataset. The resultant z-scores and p-values tell you where features with either high or low values cluster spatially. This tool works by looking at each feature within the context of neighbouring features. A feature with a high value is interesting but may not be a statistically significant hot spot ([Andy, M., 2005](https://esripress.esri.com/display/index.cfm?fuseaction=display&websiteID=86&moduleID=0)). The hotspots of COVID-19 positive cases are mapped using Getis-Ord Gi* statistic algorithm to find the cluster patterns of disease outbreak and spread.

#### Cluster and Outlier Analysis (Anselin Local Moran's I)

Based on Moran’s I statistic, the Cluster and Outlier Analysis tool identifies spatial clusters of features with high or low values. A positive value for I indicates that a feature has neighbouring features with similarly high or low attribute values; this feature is part of a cluster. A negative value for I indicates that a feature has neighbouring features with dissimilar values; this feature is an outlier. In either instance, the p-value for the feature must be small enough for the cluster or outlier to be considered statistically significant (Anselin, Luc, 1995).

### Spatial interpretation method

Ordinary kriging is a geostatistical interpolation method base on spatially dependent variance, which used to find the best linear unbiased estimate(Belkhiri, Tiri, & Mouni, 2020). The general form of Ordinary kriging equation can be written as :

![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image012.png)             (2)

In order to achieve unbiased estimations in kriging the following set of equations should be solved simultaneously:

![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image014.png)     (3)

Where ![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image016.png) is the estimated value of variable Z at location ![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image018.png);![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image020.png) is known value at location ![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image022.png);![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image024.png) is the weight associated with the data;![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image026.png) is the Lagrange coefficient; ![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image028.png)is the value of variogram corresponding to a vector with origin in ![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image022.png) and extremity in ![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image030.png); and n is the number of sampling points used in estimation.



### LST retrieval algorithm

Urban Heat Island is one of the most typical anthropogenic environmental characteristics in the urban area, During COVID-19 spread. The lockdown and ‘stay-in-home’ protocols changed the tracks and forms of human activity. Therefore, the urban environment is altered from both social and geographical aspects. To discover the vague change of urban ecology under anti-pandemic regulations, we collected temporal Landsat 8 OLI/TIRS images to evaluate the Land surface Temperature (LST) change between 2019 and 2020.



At present, there are mainly three surface temperature inversion algorithms: atmospheric correction method (also known as Radiative Transfer Equation, RTE), single-channel algorithm and split-window algorithm. In this study, the LST retrieval process is based on atmospheric correction method, using Landsat8 TIRS inversion of surface temperature. First, the atmospheric effect on the surface thermal radiation is estimated and then subtracted from the total amount of thermal radiation observed by satellite sensors to obtain the surface thermal radiation intensity, which is then converted to the corresponding surface temperature.



The specific implementation is as follows: the thermal infrared radiation brightness value ![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image032.png) received by the satellite sensor is composed of three parts: atmospheric upwelling radiation brightness![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image034.png), the true radiation brightness of the ground reaches the energy of the satellite sensor after passing through the atmosphere and the energy reflected by the atmosphere as it radiates down to the ground ([Wang et al., 2016](https://doi.org/10.1002/2016JD025270))..



By building Radiative Transfer Equation, the LST is obtained from the following expression:

![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image036.png)(4)

![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image038.png)(5)

![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image040.png)(6)

where ![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image042.png) is the at-sensor radiance or Top of Atmospheric (TOA) radiance, i.e., the radiance measured by the sensor, ![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image044.png)is the blackbody radiance of channel ![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image004.png), ![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image046.png)and ![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image048.png) are the atmospheric transmittance and land surface emissivity of channel![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image050.png), and the ![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image052.png) and ![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image054.png) are the atmospheric upwelling and downwelling radiance of channel ![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image004.png), respectively, ![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image056.png) and ![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image058.png) are the Planck’s radiation constants, for TIRS Band 10 data, the values is ![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image060.png) and 1321.08![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image062.png), respectively, ![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image064.png) is wavelength. The atmospheric parameters ![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image066.png), ![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image052.png) and ![img](file:///C:/Users/lenovo/AppData/Local/Temp/msohtmlclip1/01/clip_image054.png)can be calculated from in situ radio soundings and using a radiative transfer code like MODTRAN.

![avatar](/img/post/1_6.png "LST retrieval workflow")

## Results and Analysis

### COVID-19 cases spatial analysis

#### COVID-19 cases distribution in China and the U.S.

##### Spatial patterns

According to the up-to-date data of total cases in China and the United States, the epidemic spread trend in these two countries has different features. China has controlled the epidemic spread within Hubei province since April 2020, whereas the U.S. is still under stressful coronavirus impacts. Most cases in China concentrate in Hubei province and Hongkong. Since Wuhan is the original outbreak city of COVID-19 in China, the death and positive cases mainly distributed in the urban area of Wuhan City. In the case of the New York State in the U.S., the cases accumulated in several counties. New York City, as one of the earliest regions in the U.S. hit by COVID-19, has an enormous number of the infected population.

##### Autocorrelation analysis

In our experiment, the spatial autocorrelation of COVID-19 cases between cities has been estimated through Moran’I index by using the formula (1). The values of Moran coefficients are around the interval of [0, 1], since there is a positive correlation among the confirmed cases according to the geographical structure, and its spatial distribution has prominent agglomeration characteristics. The increase of confirmed pneumonia cases in one region will inevitably lead to the increasing cases in adjacent areas, which means that a positive spill-over effect occurs. Thus, regions adjacent to COVID-19 hotspots are at higher risk.
