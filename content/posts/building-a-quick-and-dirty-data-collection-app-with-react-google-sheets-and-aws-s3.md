---
title: Building a quick and dirty data collection app with React, Google Sheets and AWS S3
date: '2020-04-07T10:05:22'
slug: building-a-quick-and-dirty-data-collection-app-with-react-google-sheets-and-aws-s3
categories:
  - Projects
tags:
  - js
  - software
  - technology
  - webapp
---

Covid-19 has created a number of challenges for the society that people are trying to solve with the tools they have. One such challenge was to create an app for data collection from volunteers for food supply requirements for their communities.

This needed a form with the following inputs:

1. Some text inputs like the volunteer's name, his vehicle number, address of delivery..etc.,
2. The location in geographic coordinates so that the delivery person can launch google maps and drive to the place
3. A couple of photos of the closest landmark and the building of delivery.



Multiple ready made solutions like Google Forms, Zoho Forms were attempted, but we hit a block when it came to having a map widget which would let the location to be picked manually, and uploading photos. After an insightful experience with [CovidCrowd](https://github.com/covid19india/CovidCrowd), we were no longer in a mood to build a CRUD app with Database, servers..etc., So the hunt for low to zero maintenance solution resulted in a collection of pieces that work together like an app.

### Piece 1: Google Script Triggers


[Someone has successfully converted a Google Sheet into a writable database (sort of) with some Google Script magic](https://medium.com/@dmccoy/how-to-submit-an-html-form-to-google-sheets-without-google-forms-b833952cc175). This allows any form to be submitted to the Google Sheet and the information would be stored in the columns like in a Database. This solved two issues, no need to have a database or a back-end interface to access the data.

### Piece 2: AWS S3 Uploads from Browser



The AWS JavaScript SDK [allows direct upload of files into buckets from the browser](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/s3-example-photo-album.html) using the Congnito Credentials and Pool ID. Now we can upload the images to the S3 bucket and send the URLs of the images to the Google Sheet.

### Piece 3: HTML 5 Geolocation API and Leaflet JS



Almost 100% of this data collection is going to happen via a mobile phone, to we have a high chance of getting the location directly from the browser using the [browser's native Geolocation API](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API). In a scenario where the device location is not available or user has denied location access, A [LeafletJS](https://leafletjs.com/) widget is embedded in the form with a marker which the user can move to the right location manually. This is also sent to the Google Sheets as a Google Maps URL with the Lat-Long.

### Piece 4: Tying it all together - React



All of this was tied together into a React app using [React hook form](https://react-hook-form.com/) with data validation and custom logic which orchestras the location, file upload ..etc., When the app it built it results in a index.html file and a bunch of static CSS and JS files which can be hosted freely as Github Pages or in an existing server as a subdirectory. Maybe even server over a CDN gzipped files, because there is nothing to be done on the server side.

We even added things like image preview in the form so the user can see the photos he is uploading on the form.

![resource_form](/img/wp-content/uploads/2020/04/resource_form.png)
Architecture Diagram
--------------------


![resource_form_architecture](/img/wp-content/uploads/2020/04/resource_form_architecture.png)
Caveats
-------


1. **Google Script Trigger Limits** - There is a limit to how many times the Google Script can be triggered
2. **AWS Pool ID exposed** - The Pool ID of with write capabilities is exposed to the world. If there is someone smart enough and your S3 bucket could become their free storage or if you have enabled DELETE access, then lose your data as well.
3. **DDOS and Spam** - There are also other considerations like Spamming by watching the Google Script trigger or DDOS by triggering with random requests to the Google Script URL that you exhaust the limits.



All of these are overlooked for now as the volunteers involved are trusted and the URL is not publicly shared. Moreover the entire lifetime of this app might be just a couple of weeks. For now this zero maintenance architecture allows us to collect custom data the we want.

Conclusion
----------



Building this solution showed me how problems can be solved without having to write a CRUD app with a admin dashboard every time. Sometimes a Google Sheet might be all that we need.

Source Code: <https://github.com/tecoholic/ResourceForm>
**PS** Do you know Covid19India.org is just a single Google Sheet and a collection of static files on Github Pages? It servers 150,000 to 300,000 visitors at any given time.
