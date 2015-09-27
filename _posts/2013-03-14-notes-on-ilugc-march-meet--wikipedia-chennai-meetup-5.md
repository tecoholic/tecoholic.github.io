---
layout: post
title: "Notes on ILUGC March Meet and Wikipedia Chennai Meetup 5"
description: "Notes that I took during the ILUGC Monthly Meet where Wikipedia Chennai Meetup was co-held"
category: Notes
tags: [Wikipedia, Tamil, Chennai, ILUGC, Meetup]
---

I attended this meet and kept typing in my observations to keep myself completely concentrated about what is being said.
This has been sitting as a text file in my drive without purpose, so I thought it would be better taken care online.  

    3:50PM: Introduction by T.Shrinivasan
    3.52PM: Technical talk 1: Swift by Yogesh
          OpenStack - Swift - Object Storage Component
          -> public cloud
          -> private cloud, home server, admistration
          -> VMs
          -> Image Server
          -> Volatile machines -> Virtual hard disk -> Block Storage -> Amazom EBS
          -> Authentication Server -> User permissions
          -> Object storage -> data stored in
    
    Slide 1: Introduction
    * Object Storage
    * Analogous to AWS S3
    * API based access only - no mount, no format, no file system - recent developements give a illusion of file system - Pyhton running over Aapache
    * Major Usage - Media and Big Data Storage
    
    Slide 2: Use Cases
    * Media Storage
    * Big Data Storage
    * Backup and archival
    * Conten Delivery
    * Data distribution
    
    Slide 3: Features
    * REST based API
    * versioning
    * Scalable and distributed
    * Redunant( Replications ) - Minimum of 3
    * Streaming Support
    * Cheap( community Servers )
    
    Slide 4: Components
    * Proxy Server - gateway to use the system - autheticates using authetication server
    * Account Server - holds info about containers
    * Container Server - hold info about object
    * Object Server -  holds the actual data
    * Rings - Hashing of the data
    * Caching Server - caching data and authetication code
    
    Slide 5: Contribution
    * Contibutor's License agreement
    * Fork from Github / Pull Request
    * Patches / Bug Fixes
    * Python
    
    Slide 6: Getting Help
    * Mailing Lists
    * Blogs & Social Media
    * Documentation
    * IRC
    * Meetups - meetup.com
    
    4.26PM: Wikimedia India Chapter - Bala Jeyaraman (SodaBottle)
            Overview about the Wikipedia related talks
            * Introduction to Bala and Surya Prakash
    
    4.31PM: State of Tamil Wikipedia - Surya Prakash
        * What is Wikipedia? - Online Refrence Wikipedia
        * Contributors and what they do?
        * Statistics about the Wikipedia usage
        * Contibutors - Who they are? What they do? 
        * Edits - What are wikipedia edits?
        * What do you achieve by editing wikipedia?
            - Writing style and fluentcy
            - Team work and co-operation
            - Critical thinking and analysis
            - Global Society
        * Other Wikipedia Projects
            - Wiki Source
            - Wiki Books
            - WikiPedia
            - Wikimedia Commons
            - Wiki News
            - Wiki Quotes
            - Wiktionary
        * What wikipedia is not?
            - a dictionary
            - a text book
            - an archive
            - an advertisement board
            - a chat room
            - a blog
            - a campign tool
            - a correction tool
            - a research publication
            - an experimental tool
        * User Contibution
            - Writing a new article
            - Translation from other language wikipedia articles
            - Structuring the esssays 
            - Wikifying the content
            - Referencing
            - Updating the content
            - Administartion work ( by Administrators )
            - Introducing Wikipedia to others
            - Coding by Programmers
            - Adding Media
            - User Opinions
            - Verification of work
            - Graphic Files & Sound files
        * Tamil Input in Tamil Wikipedia
    
    5.02PM: Copyright of Content contributed to Wikipedia - BalaJeyaraman answering to queries
    
    5.21PM: State of Wikimedia India Chapter - Bala Jeyaraman
    
    5.35PM: Interactive session
    
    6.30PM: Exchanged pleasentaries and dispersed. Two college students tugged around me and I ended up talking non-stop 30-40mins about coding and GSoC
    
