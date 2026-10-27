---
title: "Getting VIA to Work With Snap Chromium on Ubuntu"
subtitle: ""
date: 2026-10-27T21:00:00+11:00
lastmod: 2026-10-27T21:00:00+11:00
draft: false
author: "Arunmozhi"
authorLink: ""
description: "Fixing FILE_ERROR_ACCESS_DENIED when connecting a Keychron keyboard to usevia.app from the Chromium snap on Ubuntu."
license: ""
images: []

tags:
    - linux
    - ubuntu
    - snap
    - keychron
    - via
    - udev
categories:
    - Linux

featuredImage: ""
featuredImagePreview: ""

hiddenFromHomePage: false
hiddenFromSearch: false
twemoji: false
lightgallery: true
ruby: true
fraction: true
fontawesome: true
linkToMarkdown: true
rssFullText: false

toc:
  enable: true
  auto: true
  keepStatic: false
code:
  copy: true
  maxShownLines: 50
math:
  enable: false
  # ...
mapbox:
  # ...
share:
  enable: true
  # ...
comment:
  enable: true
  # ...
seo:
  images: []
  # ...
---

My keyboard was acting up today and I had to hit a bunch of keys in frustration, that ended up resetting the custom keymaps I have created using https://usevia.app.
But, I just couldn't get it to work. I remembered it was just using `chmod` to make the `/dev/hidraw{1-4}` read and writable so Chromium can read and write to the USB.
No matter how many times I tried, unplugging & plugging, run chmod, it just refused to work. So, finally with the help of Claude, I was able to get it working.
Here are the notes.
<!--more-->

My system is Ubuntu 26.10 with Chromium installed using the default "Snap" install, and my keyboard is a Keychron K15 Pro.

```bash
# 1. Let the Chromium snap talk to raw USB devices
sudo snap connect chromium:raw-usb

# 2. A udev rule that gives your user access AND tags the device for the snap
echo 'KERNEL=="hidraw*", SUBSYSTEM=="hidraw", ATTRS{idVendor}=="3434", ATTRS{idProduct}=="02f6", MODE="0660", GROUP="plugdev", TAG+="uaccess", TAG+="snap_chromium_chromium"' \
  | sudo tee /etc/udev/rules.d/92-via.rules

# 3. Reload udev
sudo udevadm control --reload-rules && sudo udevadm trigger --subsystem-match=hidraw
```

Then unplug and replug the keyboard, and **fully** quit and restart Chromium. Replace `3434` / `02f6` with your keyboard's
vendor and product IDs (see below).

Use `lsusb` for getting your device and product IDs

```
$ lsusb | grep -i keychron
Bus 003 Device 017: ID 3434:02f6 Keychron Keychron K15 Pro
```
