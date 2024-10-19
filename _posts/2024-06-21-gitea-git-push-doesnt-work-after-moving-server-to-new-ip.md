---
layout: post
title: "Gitea - git push doesn't work after moving server to new IP"
date: 2024-06-21 08:20:15
category: Notes
tags: documentation gitea self-hosting
---

If Gitea is running as a docker container, then there is a SSH Shim script at "/usr/local/bin/gitea" that contains the local IP address of the machine, which might be different from the 127.0.0.1 that's [provided in the documentation](https://docs.gitea.com/installation/install-with-docker).




This script needs to be updated with the new IP address as well.



