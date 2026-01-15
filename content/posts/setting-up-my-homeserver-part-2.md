---
title: Setting up my HomeServer - Part 2
date: '2022-11-26T21:15:18'
slug: setting-up-my-homeserver-part-2
categories:
  - Projects
tags:
  - homeserver
  - internet
  - technology
---

In [part 1](https://arunmozhi.in/2022/11/24/setting-up-my-homeserver-part-1/), I wrote about the hardware, operating system and the software deployment method and tools used in my home server. In this one, I am going to cover one topic that I am least experienced in - **Networking**




Problem: Exposing the server to the internet
--------------------------------------------




At the heart of it, this the only thing in *Networking* I really wanted to achieve. Ideally the following is all I should have needed:




2. Login to my router

6. Make the IP of my Intel NUC static, so that DHCP doesn't assign a different value every time it reboots

10. Setup port forwarding for 80 (HTTP) and 443 (HTTPS) in the router to the NUC.

14. Use something like [DuckDNS](https://www.duckdns.org/) to update my domain records to point to my public address.




I did the first 3 steps, and tried to hit my IP. Nothing. After some searching on the internet, I came to realize that my ISP doesn't provide Public IPs for home connections anymore and my router is under some NAT (don't know what it is).




*Before I outline how everything is setup, I want to highlight 2 people and their self-hosting related blogs:*




2. [Abhay Rana aka Nemo's Setup](https://captnemo.in/setup/)

6. [Karan Sharma's setup](https://mrkaran.dev/setup/)




*Their blogs provided a huge amount of inspiration and a number of ideas.*




Solution: Tailscale + OCI Free VM
----------------------------------




After [asking around](https://twitter.com/tecoholic/status/1592471285019611136), I settled on using [Tailscale](https://tailscale.com/) and a free VM on [Oracle Cloud Infrastructure](https://cloud.oracle.com) to route the traffic from the internet to the VM.




Here is how Tailscale helps:




2. All the devices that I install Tailscale in and login becomes a part of my private network.

6. I added my Intel NUC and the Oracle VM to the Tailscale network and added the public IP of the Oracle VM to the DNS records of my domain.

10. Now requests to my domain go to the OCI VM, which then get forwarded to my NUC via the Tailscale network.




![](/img/wp-content/uploads/2022/11/tailscale-networking.png?w=944)


### Some Tips




2. Tailscale has something called MagicDNS which once turned on allows accessing the devices using their name instead of their IPs. This allows configuring things quite easy.

6. Oracle VM's by default have all of their Ports Blocked except for 22 (SSH). So after installing the webserver like Nginx or Apache, 2 things need to be done:
	* Add Ingress Rules allowing traffic to ports 80 and 443 for the Virtual Cloud network that the VM is configured with
	
	* Configure the firewall to open the ports 80 and 443 (ufw allow <port>)




I think there are many ways to forward the requests from one machine to another (OCI Instance to Homeserver in this case). I have currently settled for the most familiar one - **using Nginx as Reverse Proxy.**




There are 2 types of applications I plan to host:




2. Public applications like [Misskey](https://misskey-hub.net/) which are going to be accessed by anyone who wants to.

6. Private applications like [Node-RED](https://nodered.org/) which I am going to access 99.99% from my laptop connected to my home-network.




I deploy my public applications to the Tailscale Network IP in my homer server and make them listed to a specific port. Then, in the [Nginx reverse-proxy configuration](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/) on the OCI VM, I set the **proxy_pass** to something like `http://intel-nuc:<app-port>`. Since I am using Tailscale's magic DNS, I don't have to hard-code IP values here.




For Private applications, I simply run them on the Intel NUC's default local network, which is my router and other things connected to it (including my laptop) and access it locally.




### Up next...




Now that the connectivity is sorted out, the next part is deploying the actual application and related services. I use Nomad to do that. In the next post I will share my "architecture" and how I use Nomad and Terraform to do deployments and some tricks I learnt using them.



