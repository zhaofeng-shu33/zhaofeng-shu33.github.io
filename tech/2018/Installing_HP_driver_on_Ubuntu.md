# Installing HP driver on Ubuntu

## 2018/4/11

## Version

* Ubuntu 16.04
* HP LaserJet Pro MFP m226dw

## Step

* download the latest hplib from ![https://sourceforge.net/projects/hplip/](https://sourceforge.net/projects/hplip/)
* `chmod a+x your_installer`
* Run the installer, also need to install a lot of depedency.
* (for my printer) install HPLIP Binary Plug-In:`hp-plugin`
* restart my computer, I found a desktop toolbox(HP Device Manager) on the upper-right corner.
* Open the device manager, add new HP printer, enter the printer ip address manually and send the test page to the printer



## Issue remained
The ip address of the printer is not fixed in my lab. For other students who use ubuntu, they have to figure out ip first.


