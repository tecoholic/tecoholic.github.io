---
layout: post
title: "India Literacy Map with a How-To"
date: 2019-01-01 01:01:51
category: Maps
tags: india map
---
I published the [Tamilnadu district wise literacy](http://arunmozhi.in/2018/12/28/updating-the-wikipedia-tamilnadu-literacy-map/) map some days ago and @tshrinivasan asked if I can write a blog on how to do it, and here it is now.

https://twitter.com/tecoholic/status/1078953714642182144

What are we going to do?
------------------------



We are going to create India's State Wise Literacy Map. It will be a [Choropleth map](https://en.wikipedia.org/wiki/Choropleth_map) ℹ️ just like the Tamilnadu one.

Things we need
--------------


1. QGIS - An Open Source software that will be used to process the geographic data and create the map. Download and install it from <https://qgis.org/> for your operating system.
2. Base map - The digital map of India with its state boundaries as [a shapefile](https://en.wikipedia.org/wiki/Shapefile). ℹ️ You search the internet for "India states shapefile", there are a number of sources where you can find this. I am going to use the one from the [Hindustan Times public repository](https://github.com/HindustanTimesLabs/shapefiles). [shapefiles/india/state_ut/india_2000-2014_state.zip] ⬇️[Download](https://github.com/HindustanTimesLabs/shapefiles/blob/master/india/state_ut/india_2000-2014_state.zip), Unzip the file and keep it ready. I am choosing the pre-Telangana map because the literacy data is from 2011 which is pre-Telangana.
3. Data on literacy levels of the Indian states. An internet search for "India states literacy csv" would give a number of results. I am going to use the one from the Census 2011 website. ⬇️[Download](http://censusindia.gov.in/2011-prov-results/paper2/data_files/india/Statement5_Literate&LitRate_State.xls)


Get the data ready
------------------



We have 2 sources of data:

1. Geographic data which we downloaded from the Hindustan Times
2. The Literacy data from the Census 2011 website



Both the datasets need to be joined to create the map. Let us do that:

1. Open QGIS and create a new project. From menu select *Project -> New Project*
2. Add the map using *Layer -> Add Layer -> Add Vector Layer*. Browse to the location of the downloaded shapefile, select the **india_2000-2014_state.shp**file and click *Add.* ![Add_layer](/img/wp-content/uploads/2019/01/Add_layer.png)
3. You will be asked to select the coordinate system. *Select WGS84* and click *OK*. Once the layer is added close the Add layer button. ![Select CRS](/img/wp-content/uploads/2019/01/Select-CRS.png)
4. Now you should have the map loaded to the main area, and should see the legend entry for the data layer like this. ![Base Map added](/img/wp-content/uploads/2019/01/Base-Map-added.png)
5. Now right click on the layer and select *Open Attribute Table*![Open Attribute Table.png](/img/wp-content/uploads/2019/01/Open-Attribute-Table.png)
6. You will notice it has only two columns - the id and the state name. We are going to create a new column and add the literacy rates from the census data. In the Attribute Table, click the *yellow pencil* icon (first one in the icon bar) to start editing.
7. Click the *Add Column* button and add the literacy column with type decimal. ![Add_column](/img/wp-content/uploads/2019/01/Add_column.png)![literacy column](/img/wp-content/uploads/2019/01/literacy-column.png)
8. Now enter the literacy rates from the excel sheet into the newly added column. **Sidenote:**There is an automated way to combine the data without having to manually enter the data if you have the data in a delimited text file like CSV. It involves adding a something called a Data Layer. We will take the manual route to keep it simple.
9. Once you have added the literacy values. Click Save Edits icon (Ctrl+s).  Now click the "Yellow Pencil" button again to stop editing. This is **very important**. Otherwise, you might unknowingly click at some place and change the geometry of the state boundaries.
10. Now you should have the data in the attribute table like this. ![Attribute Table with Literacy.png](/img/wp-content/uploads/2019/01/Attribute-Table-with-Literacy.png)
11. Close the Attribute Table.


Styling the map
---------------


1. In the *Layers* sidebar right click on the map layer and select *Properties*.
2. In the Properties window, select *Symbology* from the side menu. ![Layer Properties.png](/img/wp-content/uploads/2019/01/Layer-Properties.png)
3. In the Styling window make the following changes. ![Styling.png](/img/wp-content/uploads/2019/01/Styling.png)
	1. A - Change the style from "Single Symbol" to Graduated
	2. B - Select "literacy" as the column
	3. C - Set Precision to your liking (it denotes the decimal points of the values to be shown in the map legend). I prefer 0 or 1 usually.
	4. D - Choose a Color Ramp to your liking. I am choosing the one suitable for Wikipedia based on the [Wikipedia Conventions.](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Maps/Conventions)
	5. E - Set the mode to "Pretty Breaks". Now as soon as you select this, the "Classes" tab right above it should be populated automatically. If not, use F.
	6. F - If your classes didn't appear automatically, click the "Classify" button.
4. Once you are satisfied with the Legend precision and the color ramp, click OK to see your styled Choropleth map. ![styled map.png](/img/wp-content/uploads/2019/01/styled-map.png)


**Note:**The properties dialog provides a huge number of options to do a number of things including labels. Refer to a QGIS manual or tutorials on the web for related information.

Exporting the map
-----------------



Now we have the styled map according to our liking ready. We need to export it to an image so that we can share it across.

1. Click the "New Print Layout" button. Enter a name, I named mine "export" and click ok.![new print layout](/img/wp-content/uploads/2019/01/new-print-layout.png)
2. You will get the Layout window with an empty page. ![empty print layout.png](/img/wp-content/uploads/2019/01/empty-print-layout.png)
3. From the menu, select *Add Item -> Add* map.Click and drag the cursor to the required size. ![map inserted.png](/img/wp-content/uploads/2019/01/map-inserted.png)
4. (Optional) There is a lot of white space around the map inside the box. We can make the map a little bigger by reducing the scale. On the right side switch to the *Item Properties*tab and reduce the value for *Scale.* (Mine was 17485874 and I changed it to 12500000). ![rescaled map.png](/img/wp-content/uploads/2019/01/rescaled-map.png)
5. Click *Add Item -> Add Legend.*Click and drag the cursor to create the Legend. India's maps usually use the Bay of Bengal for that, I am going to do the same. ![Legend Added.png](/img/wp-content/uploads/2019/01/Legend-Added.png)
6. You will notice that the legend title says the layer name. But what we really want it to say is "Literacy Rate". There are two ways to fix that. Choose the one that appeals to you.
	1. On the right in the *Item Properties* tab, under *Main Properties,*you can enter a title as "Literacy Rate"
	2. On the right in the *Item Properties* tab, under *Legend Items, double-click* on the layer name and enter "Literacy Rate"
7. Now there is some extra white space on the right. Let us clean that up. On the right side select *Layout*tab, scroll down to *Resize Layout to content*and click *Resize Layout.*Now the page should have been resized to only the map. ![cropped to content.png](/img/wp-content/uploads/2019/01/cropped-to-content.png)
8. From menu click *Layout -> Export as Image.* Enter the filename in your desired location and save it. You could also export as PDF if you want to print.


**Note:** Apart from just the map and legend you can do a lot more complex things with the layout manager. Again, refer to a QGIS manual and other tutorials on the internet to fully learn about them.

Final Product
-------------


![IndiaLiteracyMap.png](/img/wp-content/uploads/2019/01/IndiaLiteracyMap.png)
