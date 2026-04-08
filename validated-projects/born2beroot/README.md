*This project has been created as part of the 42 curriculum by ridias.*
# Born2BeRoot

## Description

The Born2BeRoot is a project that aims to introduce individuals to the world of virtualization.
Students create their first virtual machine in VirtualBox (or UTM if one can't use VirtualBox) through the usage of specific instructions. Then set up an operating system with the implemention of strict rules.


## Instructions

To begin using this project it is needed some sowtware extra: Oracle VM Virtualization, an iso of the OS required to install on the VM.

The installation steps are pretty straignt foward, meaning it's just following the given steps and not installing any GUI or visuals on the VM.

Another step that differs from a simple clean instalation is the use of VLM that helps you create some specific volumes for the bonus part of the project.

After installing the OS on the machine there are some steps to installing all the necessary software for the VM to run, some of the comands are:

- sudo service ufw status (check if the UFW service started)
- sudo ufw status numbered (check UFW active rules)
- sudo service ssh status (check if the SSH service started)
- uname --kernel-version (check the OS)
- getent group sudo user42 (check that the user is within the "sudo" and "user42" group)
- sudo adduser username (create a new user)
- sudo addgroup newgroup (create a new group)
- sudo adduser username newgroup (add newuser to newgroup)
- sudo hostnamectl set-hostname newname (switch hostname to newname, afterwards reboot system so new hostname is displayed)
- lsblk (verify the partitions)
- nano /etc/sudoers.d/sudo_config (check sudo rules)
- cd /var/log/sudo  then  cat sudo_config (check sudo logs)
- sudo ufw allow XXXX (create a new rule for port XXXX, number of choice)
- sudo ufw delete NUMBER_RULE (delete NUMBER_RULE, number of choice based on available ufw numbers)
- ssh newuser@localhost -p 4242 (connect via SSH with newuser in terminal of computer while machine is active)
- sudo crontab -u root -e (check the crontab of script and allows for modification)


## Resources
The references used related to this topic are as follows:
- https://github.com/chlimous/42-born2beroot_guide?tab=readme-ov-file#writing-the-cript
- https://www.youtube.com/watch?v=s2eM7L_etzo
- https://www.youtube.com/watch?v=eDZFMu6_PZk
- https://www.youtube.com/watch?v=3Vw0HlJHLTQ

AI was barely used, it's usage was as a tool to find the usage of a system that were hard to comprehend (AppArmor specifically).

## Project description

#### Chosen OS

For this project I used the Devian OS, for a few reasons, those being that I had previous experience dealing with Debian-based OS like Ubuntu, other reasons is that Rocky linux is a more corporate type of OS, that focus on stability, having few changes from version to version. While the Debian version is more customizable and more aligned with the goal of this project for me.

This choice affected the choise to use AppArmor instead of SELinux, because the Debian OS is automaticly using AppArmor. And after some research it shows that it is not recommended to install SELinux over AppArmor on Debian based OS.
The main diferences are that AppArmor uses a path-based access controll to security policies, while SELinux uses label-based access control, meaning every file process and user is assigned a security context (label) that provides more security in more complex environments.

In regards to the use of firewalls I went with UFW, also because of past experiences with it, but the main diferences are that UFW (Uncomplicated Firewall) is a more minimalistic type of OS focausing on allowing/denying ports, services, or IP addresses. While Firewalld focuses its protections towards zone-based firewalls, this type of approach helps when dealing with multiple networks all with diferent types of security policies.

The use of Virtual box over UTM bases on the fact that my VM was going to run my vm on a "I presume" intel based processor, and also at home I also ran it on Intel based processors. This is relevant because UTM is optimised for Apple Silicon (M1/M2/M3/etc) while Virtual Box can also run Apple Silicon with some adicional costs it is better for Intel based macs.


The main design choices made during the setup are as follows:
#### Partitioning
For partitions, the LVM (Logical Volume Manager) was chosen because it allows for flexible resizing of partitions and a cleaner separation of system components with the filesystem of ext4. It was made with separate logical volumes (/ (root) , /home , /var , /tmp , /srv , /var/log , swap), this improves the security and maintainability and limits the damage if one of the partitions were to fill up.

#### Security policies
- A password policy was implemented following specific conditions: the password must be at least 10 characters long and contain an uppercase letter, a lowercase letter, and a number. It must not contain more than 3 consecutive identical characters, and the password must not include the name of the user. It has to expire every 30 days, with a minimum number of 2 days allowed before the modification of a password, and the user has to receive a warning message 7 days before the password expires.

- The SSH (Secure Shell), a protocol/program for remote access to servers, is installed. This allows for a secure channel with encrypted data exchange between a client and a server, ensuring confidentiality and integrity.

- The UFW (uncomplicated firewall) is a user-friendly front end for managing iptables. It ensures that only the required ports are opened (SSH in this case) and denies all others by default.

UFW and firewalld are both Linux firewall management tools, but they target different audiences and types of environments. UFW is aimed at beginners; for simple desktops and server firewalls, it defaults to Ubuntu, Debian, Kubuntu, and Linux Mint. It simplifies iptables and nftables with easy-to-read syntax with a rule-based configuration style. Unfortunately, it is less flexible for complex scenarios and has static rules. On the other hand, firewalld is aimed for dynamic environments, servers, and laptops needing different profiles; it defaults to RHEL, CentOS, Fedora, and OpenSUSE. It is used for zone-based (public, home, work) and service-based management and supports runtime changes. It works with modern nftables and iptables, it's dynamic and powerful, and it supports rich rules and zones for different network types, but unfortunately, it has a much more rigorous learning curve than UFW. 


#### User management
This machine has a root account, but there is no SSH login associated, and it has limited direct usage. On the other side, there is a normal user who was added to the sudo group (controlled privilege escalation) and other custom groups. The users have sudo configuration associated (password required, limited retry attempts, the logging of sudo commands, and enforced secured path), which makes actions traceable.


#### Services installed
The services installed are SSH (remote administration), UFW (firewall), cron (for scheduled tasks), sudo (privilege management), and a script that runs via cron that shows CPU usage, memory usage, disk usage, CPU usage percentage, last reboot, LVM status, active connections, the number of users, and the number of commands done with sudo.