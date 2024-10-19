---
layout: post
title: "Setting up my HomeServer - Part 1"
date: 2022-11-24 14:29:51
category: General
tags: technology
---

Preamble
--------




I had an old [Intel NUC](https://www.intel.in/content/www/in/en/products/details/nuc.html) lying around that I always wanted to put it to good use. I had set it up as a home media server using [Plex](https://www.plex.tv/) a couple years back, but streaming services and the newer content coupled with 100-300Mbps Fiber Internet connections have kind of made it redundant.




So, when finally a couple of weeks back when I wanted to switch from Twitter to Mastodon, I got the idea to just host an instance for myself. But Mastodon was in Ruby and I was at the time reading through the [ActivityPub Protocol specifications](https://www.w3.org/TR/activitypub/) to see if I can create an account using just a couple of scripts and a bunch of JSON files. I didn't get far in the experiment, but someone ended up finding out [Misskey](https://misskey-hub.net/). I setup a Misskey instance on Digital Ocean and set out to preparing the NUC for a home-server.




Hardware
--------




The NUC I have has a Intel i3 processor with **4 cores** each running at **2.1 GHz** and has 16 GB of RAM and a 128 GB SSD. That's the equivalent of an AWS EC2 Compute optimized *c7g.2xlarge* instance which costs about *0.289 USD/hour* which comes to $200/month (approx). 




**Sidenote:** I know its not apple to apple comparison between a hardware device and a cloud instance, but for my intended purposes, it totally works.




OS
--




I used to have this as an alternate desktop system, so it runs **Ubuntu 22.04** **Desktop Version** with the default Gnome interface. I removed almost all the desktop software and left only the bare minimum necessary to run the OS and the desktop.




I thought about installing Ubuntu Server edition but couldn't find a pendrive. So a stripped down desktop OS will have to do.




Software Deployment
-------------------




Now this I am very particular about.




2. I want to use Infrastructure as Code tools like Terraform as much as possible. This allows storing all the necessary configuration in a repo, so if and when my HDD fails, I can redeploy them again without having to do each and every one of them by hand again.

6. I want to have some form of Web UI that can show the running services and resource consumption, if possible




First up is [YUNOHost](https://yunohost.org/) - It is an OS dedicated to self-hosting and supports a huge number of software and has a nice UI to manage them. But, the ones I want to host (Misskey) aren't there and I don't think storing config as code is an option here.




Next I looked at [docker-compose](https://docs.docker.com/compose/) - I am very familiar with it. The config can be stored as files and reused for redeployment. A lot of software are distributed with docker-compose files themselves. But, there is no web UI by default, and I also don't want to run multiple copies of the same software.[1] 




I have some experience with [Kubernetes](https://kubernetes.io/) - There are lightweight alternatives like K3S, that might be suitable for a single node system. It fulfills the config-as-code and the Web UI requirements. But, the complexity is a bit daunting and the yaml can get a little unwieldy. And also everything needs to be in a container.




Finally I settled on [Nomad](https://www.nomadproject.io/) - It seemed to have a fine balance.




* It can handle docker containers, execute shell scripts, run Java programs..etc.,

* The config is stored in JSON like HCL files, which feels better than the YAML

* It has a web UI to see running services and resource utilization.







Footnotes
---------




[1] - When software are distributed using docker-compose files, they tend to have all the necessary services defined in them. That usually means, along with the core software they also have other things like a database (Postgres/MariaDB), a web server (Nginx/Apache), a cache (Redis/Memcache)..etc., So, when multiple software are deployed with vendor supplied docker-compose files, it ends up running multiple copies of the same services using up unnecessary CPU and memory.



