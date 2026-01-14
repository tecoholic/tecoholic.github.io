---
title: "Moving back from Mac to Windows + Linux"
date: 2019-12-12T14:02:30
slug: "moving-back-from-mac-to-windows-linux"
categories:
  - General
tags:
  - experience
  - technology
---

> Content Warning: Rant ahead



As my Macbook Air is becoming more and more restrictive to the things I could do, due to low memory of 4 GB and 128GB SSD, I decided to buy a new laptop with better specifications. After some filtering and comparison on Flipkart and Amazon, I finally settled on Lenovo S540 14" with 8 GB RAM and 1TB SSD. It also came fitted with a 2GB Graphics card which I think will help working with ML algorithms easier. While the hardware is great for my requirement, the software is a complete let down.

Issue 1: Windows Font Rendering is Crap
---------------------------------------



The screen is a full HD 1920x1080 display in 14 inches. One would think the display would try to match that of the display of my Macbook Air (1440x900), but nope. Not in a million chance.

The system recommends a scaling of 150% for good results, anything below that the system font Calibri starts breaking down and there seems to be no anti-aliasing effect.

There are a couple of solutions to this problem, like setting the scaling to 100% and increasing the font size separately. This works to a certain degree, but doesn't achieve the smoothness of 150% scale.

Now I have an interface that seems to be adjusted for my Grandma's failing eye sight.

Issue 2: Microsoft loves Linux - My Feet
-----------------------------------------



I think the whole MS loves Linux non-sense started almost the same time I bought a Macbook. So I never experienced what it meant. I now get what it meant, they wanted to sell Linux machines on their Azure cloud and that's about it. Whatever contributions they must have done, should have centered around that goal. Because installing Linux in a Windows 10 machine is more difficult now than it was 5-8 years ago. Back then, it was just a matter of knowing how to partition disks and ability to choose the boot disk. Now I had to:

* Create the bootable disk in a specific format for UEFI compatibility
* Run a command to change the Storage access method from RST to ACHPI
* Go into BIOS and disable Secure Boot, and change the ACHPI
* Boot into Safe Mode so that the disk can work with changed storage
* Finally boot into install disk and install.



What should have taken me 15-30 minutes took me 2 and a half hours.

Issue 3: Windows 10 is a Data Collection Pipeline
-------------------------------------------------



I am really horrified at the number of buttons that I had to turn off during the setup process and I still find as I use the system.

Issue 4: Application Management in Windows
------------------------------------------



Windows Store is a disaster, I don't know what is installed in my system and what isn't. There are tiles for games that aren't installed and there is no way to differentiate between a tile of an installed application and a tile of a shortcut for an application that is recommended for install.

Issue 5: Why are tiles in Start Menu?
-------------------------------------



With 150% scale, it always feels like I am seeing only a part of the actual screen when the tiles come up. I don't understand how MSFT understood that they should go back to the start menu but decided they will keep the tiles nonetheless. Either tile or don't, consistency please, the mashup is nuisance and everybody should just learn to live with it.

Issue 6: Application Management in Ubuntu
-----------------------------------------



So everybody has been bit by the centralised application distribution model. But tell me which serious software actually gets published? At least none of the ones I seem to use, even in the Mac OS ecosystem which started the stores concept. MS Office, Adobe Creative Suite, IDEs like PyCharm, Android Studio, Eclipse, Browsers... everything is package download from vendor sites. But that hasn't stopped Canonical from creating Snap store. Now I seriously don't know why there is a software centre and also a Snap Store and there is good old apt package manager.

The Good Bits in Linux
----------------------



It's been 24 hours of hell with the new system. Yet, not everything is bad.

* Once up and running, I haven't encountered Wifi or Bluetooth driver issues.
* The Kernel seem to be pretty stable.
* Grub has themes and OS selection is stylish.
* Memory usage is pretty low
* Font rendering and antialiasing is spot on. I think I just need some time to get used to 16:10 to 16:9 aspect ratio
* The drivers for the Graphics card are in place
* Tap to click and Natural Scrolling keep my UX is same across both my machines


Conclusion
----------



After a frustrating 24 hours of the setting up the system. I have completely given up on Windows. As ususal Linux will be my primary OS. Will turn to Windows for recording tutorial videos or when collaboration required MS Office, or maybe games. If money wasn't an issue, I don't think I would have moved from Mac to PC at all. Things like 3 finger application switching, desktop switching are still etched in me. So, personally I prefer

1. MacOS
2. Ubuntu
3. Windows... I would try my best not to boot this thing.

