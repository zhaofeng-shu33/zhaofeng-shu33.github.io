# Troubleshooting installation of debian os
2020/01/24

After trying debian on an old workstation, I find there are some pitfalls and tricks:
1. It is recommended to install the minimal base system (with no GUI) using the USB installer first. Since installation of GUI is through network and improper configured mirror will dramatically slow down the installation process.
2. Each operating systems need to be installed into a primary partition and set the bootable flag. Do not erase (format) existing partition containing data. 
3. It may not find the grub on your newly installed system. In such case, you need to enter rescue mode by booting from USB and chroot to the root file system of your installation.
4. After entering the console, the network may not work. Check the network device name by `ls /sys/class/net` and set it properly in `/etc/networking/interface`. See [Network Configuration](https://wiki.debian.org/NetworkConfiguration) for detail. After modifying `interface` by `nano`, restarting the service `systemctl restart networking`.
5. Once the external network is ok, please modify `/etc/apt/sources.list` to fast mirror. For example, add `deb http://mirror.tuna.tsinghua.edu.cn buster main` and run `apt update` to update the package meta information. Then you can install softwares as you like. For example, to install the gnome desktop environment. Use `apt install gnome`. It would download around 800 MB packages and be patient for this process.
6. Installing `fcitx` input method. You don't need to reboot the system. Only relogin to the session is needed.