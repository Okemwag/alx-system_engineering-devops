# MY FIRST POSTMORTEM
![403 Error](https://user-images.githubusercontent.com/84608830/154974907-1b361a17-2ad6-43e0-bc1c-65198ddf4819.png)

# An Outage Experience I Had 

From 6PM to 7PM GMT, requests to our servers from all sources were receiving 403 errors. About 78% of our subscribers were trying to access our content but were denied access. This was as a result of an outbreak on the firewall on the load balancer 

## Timeline (All in Greenwich Mean Time)
_5:30 PM_ – Our load balancer was being tuned.  
_5:50 PM_ – We received a complaint from the on-call management system that our site is not responding.  
_5:51 PM_ – The on-call person was trying to find out what was wrong with the load balancer.  
_5:59 PM_ – The on-call engineer escalated the task to other software engineers to check it out as well.  
_6 PM_ – The whole website was not accessible.  
_6:30 PM_ – The engineers found out the issue was with the firewall.  
_6:45 PM_ – Firewall traffic was cleaned up and unused rules were removed from the firewall to prevent accidents.  
_7 PM_ – The issue was completely resolved and the site was up and running.  

## Root cause and resolution
**CAUSE**: The load balancer was tuned and the firewall configuration was unconsciously affected. This caused a block on all ports except port 22.
**RESOLUTION**: The issue was found out and firewall was configured to allow required ports.

## Corrective and preventative measures

The following measures will be put in place to make sure the same thing never repeats itself:  
&nbsp;&nbsp;•&nbsp;&nbsp;&nbsp;&nbsp;The firewall configuration files’ content will always be simple and clear.  
&nbsp;&nbsp;•&nbsp;&nbsp;&nbsp;&nbsp;Burden on the firewall will be reduced by regularly removing unwanted traffic on the firewall.

