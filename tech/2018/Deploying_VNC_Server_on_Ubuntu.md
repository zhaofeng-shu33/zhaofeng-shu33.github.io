# Deploying VNC Server on Ubuntu
## 2018/1/3
## Server：Ubuntu 16.04 LTS

## install VNC

    sudo apt-get install vnc4server

## install Gnome Desktop Environment

    sudo apt-get install gnome-panel
    
## start vnc-server service

    vncserver
    
## close vnc-server service
    
    vncserver -kill :[port_number]

## modify ~/.vnc/vncstartup configuration file

Append the following to the last line

```shell
gnome-panel &
gnome-settings-daemon &
metacity &
nautilus &
```

## Unnecessary installation
 
 gnome-core is unnecessary, but I install it.