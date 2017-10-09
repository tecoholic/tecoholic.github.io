---
title: Live Transit Visualization
author: Arunmozhi
layout: post
permalink: /live-transit-visualization/
categories:
  - Projects
tags:
  - coding
---
After a push from [@logic][1], I started working on a project to show live location of suburban trains based on [transit.js][2]. The idea is to make a map similar to [this][3] for many cities, with a choice of schedules (weekday/sunday). But I found the jQuery plugin, transit.js, too hardcoded and disorganised to perform what I wanted to and also to my taste.

I found other projects like:

  * [LiveBus][4] which does a live status map using SVG maps based on d3.js library and GTFS feeds of the bus data.
  * [TransitLive][5] which uses LeafletJS as the map library with their own OSM tiles. The schdule data seems to come from the backend service.
  * [NextBus][6] which has a textual realtime status and route maps based completely on Google Maps.
  * [King County Metro][7] which again uses Google Maps for the map and a custom way of loading data from its servers. The best map I have seen so far and loads a ton of JS.

Each has its own technology stack solving the same problem.[This blog post][8] details the use of GTFS data or the lack of it for realtime visualization. So the generalized picture seems to be that everyone is rolling out a custom version of their own.

So, I am going to create a simple library that can do this.

Here is the mockup usage of the library:

{% highlight javascript %}
// Create a new livetransit object with the map type
var lt = new LiveTransit();

// Assign a div for the map
var divId = "map";
var mapType = "google";

lt.setupMap(divId, mapType);

// Overloaded to perform both addRoute and initiateMovement
lt.initiateMovement("chennai_velachery.kml", "chennai_velachery_weekday.json");


// ------------------------------------
// other probable cases to deal with
// -----------------------------------
// Specify a different schedule like Sunday/Holiday Schedule
lt.changeSchedule( "chennai_velachery_sunday.json" );
// change the location - city
lt.changeLocation( "new.kml", "new.json" );
{% endhighlight %}

 [1]: https://twitter.com/logic
 [2]: http://onloop.net/transit/ "transit.js"
 [3]: http://onloop.net/chennairail/ "Chennai Rail"
 [4]: https://github.com/PasDeChocolat/LiveBus "LiveBus"
 [5]: https://transitlive.com/ "TransitLive"
 [6]: http://www.nextbus.com/ "NextBus"
 [7]: http://tripplanner.kingcounty.gov/hiwire?.a=iRealTimeDisplay "King County Metro"
 [8]: http://bdon.org/2014/07/13/realtime-transit-data-howto/
