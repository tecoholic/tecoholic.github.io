---
title: "Dealing with ghost/outdated service entries in Nomad"
date: 2024-04-03T03:07:14
slug: "dealing-with-ghost-outdated-service-entries-in-nomad"
categories:
  - Notes
tags:
  - homeserver
  - nomad
---

I have run into this issue multiple times with Nomad. For some reason, when jobs are redeployed/restarted, the service registration isn't removed. This causes my Traefik reverse proxy to send requests to a non-existing allocation in Nomad.




Last time this happened, I think I completely nuked the Nomad setup and setup everything from scratch. This time around, I finally figured out the right way to do things.




2. Use `nomad service list` to get a list of the services

6. The use `nomad service info -verbose <service_name>` to get the service registrations for the app having the issue.

10. Open the UI and click on the **Job** > **Services** and click on the allocations to identify the dead allocation

14. Note the allocation ID and get the corresponding **ID** from the service info

18. Finally, remove the ghost entry with `nomad service delete <service-name> <ID>`






