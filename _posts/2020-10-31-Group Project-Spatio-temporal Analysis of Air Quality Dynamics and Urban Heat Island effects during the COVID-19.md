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

## Data

#### Study Area

Wuhan City, located in Hubei Province, was the earliest outbreak region in China. The Yangtze River flows through the center of the city, dividing the central urban area of Wuhan into three regions. The city has a population of over 11 million and underwent a lockdown from January 23 to April 8. Until September 8, there were 68,139 cases in total in Wuhan during the epidemic outbreak ([Peng et al., 2020](https://doi.org/10.3390/ijgi9060402)). The geographic location of Wuhan is 113°41’20” E ~ 115°6’40” E, 29°58’30” N ~ 31°20’25” N.

 ![avatar](/img/post/1_3.png)

New York City, located at the southern tip of the U.S state of New York, became the center of the epidemic at the end of March 2020. New York City has a highly dense population of 8.3 million people spread across five boroughs interconnected by a subway system that also extends into neighboring areas ([U.S. Census Bureau, 2020](https://www.census.gov/quickfacts/newyorkcitynewyork)). According to the New York City had 445,071 cases as of September 8, 2020. The geographic location of New York City is 73°41’50” W ~ 74°15’25” W, 40°29’30” S ~ 40°55’10” S.

![avatar](/img/post/1_4.png)

#### Data

In our project, the comprehensive analysis of various environmental factors influenced by COVID-19 control strategies is based on multi-source data:

- The COVID-19 cases,     population composition, and hospital assistance data.
- The daily air quality data     of the Wuhan City and New York City.
- Satellite imagery data     covers the study area

The COVID-19 data for Wuhan is accumulated from the Wuhan Health Commission [website](http://wjw.wuhan.gov.cn/xwzx_28/), and the New York data is from NYC Health [website](https://www1.nyc.gov/site/doh/covid/covid-19-). The COVID-19 cases data in Wuhan is collected from 23rd Jan to 28th May, while the cases data in New York City is from 1st Mar to 17th Jun. The daily AQI data of Wuhan, from 1 January 2016 to 31 September 2020, is provided by the [China National Environmental Monitoring Centre](http://www.cnemc.cn/). The daily AQI data of New York, from 1 January 2016 to 31 September 2020, is provided by the United States Environmental Protection Agency ([EPA](https://www.epa.gov/outdoor-air-quality-data)).

The Landsat 8 satellite images for the year 2019, 2020 are provided by the U.S. Geological Survey ([USGS](https://glovis.usgs.gov/app)). Due to the limitation of image quality and vacancy of data, we selected the image with little cloud cover over the study area before and after the pandemic outbreak. The Landsat 8 satellite comprises the camera of the Operational Land Imager (OLI) and the Thermal Infrared Sensor (TIRS) which can be used to study earth surface temperature and is used to study global warming ([Roy et al., 2014](https://doi.org/10.1016/j.rse.2014.02.001)). In this study, we used Landsat8 Level L1B data to calculate Land Surface Temperature (LST) to monitor the dynamics of Urban Heat Island (UHI).

![avatar](/img/post/1_5.png)



## Results and Analysis

### COVID-19 cases spatial analysis

#### COVID-19 cases distribution in China and the U.S.

##### Spatial patterns

According to the up-to-date data of total cases in China and the United States, the epidemic spread trend in these two countries has different features. China has controlled the epidemic spread within Hubei province since April 2020, whereas the U.S. is still under stressful coronavirus impacts. Most cases in China concentrate in Hubei province and Hongkong. Since Wuhan is the original outbreak city of COVID-19 in China, the death and positive cases mainly distributed in the urban area of Wuhan City. In the case of the New York State in the U.S., the cases accumulated in several counties. New York City, as one of the earliest regions in the U.S. hit by COVID-19, has an enormous number of the infected population.

![avatar](/img/post/1_7.png)

![avatar](/img/post/1_8.png)

##### Autocorrelation analysis

In our experiment, the spatial autocorrelation of COVID-19 cases between cities has been estimated through Moran’I index by using the formula (1). The values of Moran coefficients are around the interval of [0, 1], since there is a positive correlation among the confirmed cases according to the geographical structure, and its spatial distribution has prominent agglomeration characteristics. The increase of confirmed pneumonia cases in one region will inevitably lead to the increasing cases in adjacent areas, which means that a positive spill-over effect occurs. Thus, regions adjacent to COVID-19 hotspots are at higher risk.

![avatar](/img/post/1_9.png)

![avatar](/img/post/1_10.png)

#### COVID-19 cases analysis in Wuhan

The COVID-19 pandemic originated with a cluster of mysterious, suspected pneumonia cases in the city of Wuhan, the capital of Hubei, China in December 2019. The potential disease outbreak soon drew nationwide attention. On 23rd January 2020, the government announced lockdown order in Wuhan City. By 29th January, the virus spread to all provinces of mainland China([Yuan, Li, 28 January 2020](https://www.nytimes.com/2020/01/28/business/china-coronavirus-communist-party.html)). The number of cases increased rapidly in February until the pandemic was under control in early March. By the time Wuhan ended lockdown order, over 2575 died from the coronavirus infection-associated pneumonia, and 50,008 were confirmed to have been infected in Wuhan City.

The outbreak started from the urban districts and gradually spread to the suburban and rural areas across the disease pandemic periods. There were significant geographic differences in rates of confirmed cases, with the highest rates in the urban districts such as Jiangan, Jianghan, Qiaokou and Wuchang district.

![avatar](/img/post/1_11.png)

![avatar](/img/post/1_12.png)

#### COVID-19 cases analysis in New York City

The first case relating to the COVID-19 pandemic was confirmed in New York City in March 2020. At the end of March, the infected cases increased to 33,983 at an unpredictable speed. By April, the city had more confirmed coronavirus cases than China, the U.K., or Iran, and by May, had more cases than any country other than the United States ([NPR., March 24, 2020](https://www.npr.org/2020/03/24/820610818/new-york-city-u-s-epicenter-braces-for-peak)). On 20 March, the governor's office issued an executive order closing down non-essential businesses. The pause order caused the increasing unemployment rate and many social issues, whereas the infected cases of COVID-19 multiplied every day. When the city began its first phase of reopening on 8 June, the total cases had reached 211,728, accounting for 2% of the total population in NYC. From the distribution map in the zip code area, some regions hold a high infected population. To better understand the spatial correlations, the hotspot analysis was imple

![avatar](/img/post/1_13.png)

![avatar](/img/post/1_14.png)

![avatar](/img/post/1_15.png)

### Air quality dynamics analysis

Based on the temporal and spatial analysis of COVID-19 cases in two cities, we executed the evaluation of environmental variables including air pollutants and land surface temperature. Due to the retention of air pollutants, the air pollution dynamics is analysed monthly to compare the air quality during the COVID-19. We chose observation time span of six months. Given that the time of the outbreak in two cities is different, we evaluated the air quality data of Wuhan City and the New York City from from 1st January to 30th June. The monitoring items are PM2.5, PM10, SO2, NO2, CO and O3. The average air quality index (AQI) is a dimensionless index, which is calculated based on an average of six pollutants measured.

#### Air pollutants spatio-temporal patterns in Wuhan

To visually demonstrate of the air pollution variation, we first employed a map tool in AcGIS Pro to graphical depict the distribution of pollutants concentrations. Wuhan contains seventeen sub-districts, which concludes Jiang’an (JA), Jianghan (JH), Qiaokou (QK), Hanyang (HY), Wuhan Economic Technological Development District (WED), Hongshan (HS), East Lake High-Tech Development District (EHD), Wuchang (WC), East-Lake Ecotourism Scenic District (EES), Qingshan (QS), Wuhan Chemical Industry Park (WCIP), Dongxihu (DXH), Xinzhou (XZ), Huangpi (HP), Jiangxia (JX), Caidian(CD), and Hannan(HN). As illustrated in Figure 7-Figure 14, the spatial-temporal distribution of different air pollutants was significantly heterogeneous among districts. Specifically, the concentrations of five air pollutants during the lockdowns appeared to be much lower than concentrations on regular days, which offered supportive evidence of the pollution reduction effects of travel restrictions.

The spatial distribution of six criteria pollutants in Wuhan City from January 2020 to June 2020 is shown in figure 7- figure 14. The concentrations of CO and NO2 have the geographical feature of “low outside and high inside”. JH and WC, which belong to the central urban area of Wuhan City, were the area with the most serious CO and NO2 pollution because of developed traffic and large traffic volume. PM2.5 and PM10 are the highest in QS District because the petroleum and power generation industries in QS District are very developed. Unlike CO and NO2, the concentration of O3 and SO2 at rural area is higher than that at central area. Especially, high concentrations for O3 and SO2 were noticed in the northern part and southern part respectively. This is because the high vegetation rate of suburbs can release a large amount of VOCs, which is conducive to O3 production. At the same time, the NO emitted by vehicles can react with O3, which is equivalent to consuming O3 to a certain extent.

![avatar](/img/post/1_16_1.png)

![avatar](/img/post/1_16_2.png)

![avatar](/img/post/1_16_3.png)

![avatar](/img/post/1_16_4.png)

![avatar](/img/post/1_16_5.png)

![avatar](/img/post/1_16_6.png)

####  Air pollutants spatio-temporal patterns in New York City

The spatial distribution of five criteria pollutants in New York City from January 2020 to June 2020 is shown in below figure. The spatial features of pollution distribution are closely related to urban configuration and land use type. The commercial zones mostly located in Manhattan borough and industrial & manufacturing facilities are separated along the shoreside in Staten Island. The northern and eastern part of New York City like Bronx, Queens and Brooklyn are mostly residential areas.

The eastern part of NYC had lower PM2.5 concentration from February to May in 2020. After the first phase reopening order released, the PM2.5 in residential areas went higher than surrounding areas. Daily temperatures, relative humidity, and wind speed can affect ozone levels. In general, warm, dry weather is more conducive to ozone formation than cool, wet weather. NOx and VOC emissions can also influence ozone levels. The distribution of ozone displayed similar spatial patterns in March and April. In June, the centre of high density ozone moved to eastern part in the urban area.

SO2, NO2 and CO primarily get in the air from the burning of fuel. NO2 forms from emissions from cars, trucks and buses, power plants, and industrial facilities. In NYC, the high concentration of SO2 in the atmosphere clustered in the queen borough from January to May 2020. After the pandemic outbreak, the NO2 and CO pollution concentrated in Staten Island borough where most industrial facilities located.

![avatar](/img/post/1_17_1.png)

![avatar](/img/post/1_17_2.png)

![avatar](/img/post/1_17_3.png)

![avatar](/img/post/1_17_4.png)

![avatar](/img/post/1_17_5.png)

### Urban Heat Island effects during pandemic



The temporal maps of LST distribution are produced to make a comparison between 2019 and 2020 to evaluate the impacts of COVID-19 on the urban thermal environment. Generally, the UHI effect is more significant in summer because of the higher temperature and more CO2 emissions generated from air-conditioning usage.



Wuhan City, known as one of the ‘Stove City’ in China, has obvious UHI effects in central urban area. From the figure 3.16(a), the distribution patterns of LST are similar in February and March. The rural area has a higher temperature than the urban area, which is assumed as a cold island effect caused by the difference in heat emissions in the urban and rural area. Through the comparison of LST in August 2019 and 2020, we found that the UHI effect is severe in 2020. Apart from the influence of global warming, the massive work resumption after months lockdown is likely to be one of the main causes for the increase of temperature in the urban area in Wuhan City.

 ![avatar](/img/post/1_18.png)

Contrary to Wuhan City, the UHI effect in New York City seems to mitigate in 2020 compared with the same time in 2019. Previous studies show that the epidemic influenced normal human activities. The decreased flow in the industrial and commercial area caused lower emission of CO2. Although the change is not significant, it is safe to conclude that the COVID-19 affected the environmental variations in Wuhan City and New York City.

![avatar](/img/post/1_19.png)

## Discussion

Our data and analysis demonstrate the impact of COVID-19 on environmental variations in epi-centre cities. The illustrations of dynamic changes of air pollution level and urban heat island effects in Wuhan and New York City provide information for the study of socio-ecological consequences of an epidemic outbreak. In conclusion, we found that the restrictions on human activities have interactions with the urban environment. The spatial-temporal patterns of air pollutants distribution were modified, especially in Wuhan City. The air quality reached the standard level due to the lockdown order. However, the resumption of industrial production and commercial activities after June 2020 brought a more severe UHI effect in central urban areas. For New York City, air pollution decreases during the outbreak time, but the change is not as significant as in Wuhan City. In addition, the UHI effects in NYC alleviated in 2020 compared with the same time in 2019. The factors contributing to the weaken UHI effects are complicated. Given the global warming tendency, the responses of the local community to COVID-19 are likely to be one of the social factors that influenced the urban thermal environment.



The limitation and future improvements in our study are as follows:

1. The correlation analysis     between COVID-19 cases and air pollutants concentration was not conducted     due to the limited data. With the available long-term data, we can make a     more valid analysis of air quality dynamics in the pandemic period.
2. Social economic data and     human mobility data are supposed to be prompt critical elements for the     investigation of epidemic influence.
3. The air and thermal factors     are inseparable parts for the environmental assessment of urban context,     which directly affects public health and economic development. The     relationship between these two kinds of factors is another meaningful     topic to study.



Our study provides insights for the research of environmental consequences of COVID-19 on a local scale. Despite the initial finding of our analysis, more correlations between critical environmental variables and disease spread can be explored in the future. Since the adaptation to long-last coronavirus crisis will be a new normal for human society, the statistical and quantitative analysis should be conducted to assist the policy-making and environmental protection.
