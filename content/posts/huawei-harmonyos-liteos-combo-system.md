---
title: Huawei - HarmonyOS & LiteOS combo system
date: '2021-12-29T08:49:28'
slug: huawei-harmonyos-liteos-combo-system
categories:
  - General
---

I recently bought a smart watch that will let me go for a run without 350 grams of electronics (my phone) jiggling in my pocket at every step. It is a [Honor Magic Watch 2](https://amzn.to/3z5F1lF). It's probably the cheap & beast option (costs about 12K) which supports onboard music storage. Now, I can go for a run with just watch and Bluetooth earphones :)




### The LiteOS




Now the watch doesn't support 3rd party apps like the pricier WearOS ones like the [Samsung Galaxy Watches](https://amzn.to/3qzZGKu). How to make this thing smarter? Google lookup revealed that this thing is basically a clone of Huawei Watch 2 and they both run an operating system called [LiteOS](https://www.huawei.com/en/technology-insights/publications/huawei-tech/84/lite-os-smart-iot) - which is a low power IoT OS developed by Huawei for its smart devices. The cool thing is, the OS is actually Open Source - <https://github.com/LiteOS/LiteOS> (BSD-3 Licensed).




While it might be OpenSource, it still doesn't solve "making it smarter".




* The watch's source code is not open source - just the OS
* There is no SDK to develop apps, so there is no documented way to know it's APIs




### HarmonyOS




Unsurprisingly Huawei is aware of the problem and they have been developing more modern OS called [HarmonyOS](https://www.harmonyos.com/en/), which will allow them to overcome this. HarmonyOS is being positioned as an alternate to Android for cross device integration. It runs on everything from watches, phones, tablets, to TVs. 




How did Huawei develop such an OS so fast? [Turns out it is just a fork of Android](https://www.techadvisor.com/news/software/harmony-os-3798558/) that has been rebranded/code obfuscated... or whatever. Basically a copy. 




### The Battery




One of the good thing about the LiteOS watches is their battery life. They are rated for 7 - 4 days of usage. Having used it for a week now, I will say it is kind of true. Even with GPS + Bluetooth Music on for 40 mins a day, it can still go for 4 days.




Now if Google's WearOS can only provide a battery life of 24 - 48 hours, how can HarmonyOS which is a clone be any better? 




### Enter the combo OS




Huawei has done what we Linux users have been doing for decades - dual booting OS. Well, not exactly, but close. So the newer watches like Huawei Watch 3, come with [both LiteOS and HarmonyOS loaded onto them](https://www.wired.co.uk/article/huawei-harmony-os-20-tablets-watches).




For "smarter" requirements, HarmonyOS takes over, and for essentials, the LiteOS subs in. It is kind of a smart solution. With this combo solution, Huawei seems to bringing the best of both worlds to their watches.




##### Sidenote




The Honor watch also has a Huawei designed custom chip called Kirin which runs the LiteOS. So they could be going Apple's way in Chip + Kernel + OS level integration. 



