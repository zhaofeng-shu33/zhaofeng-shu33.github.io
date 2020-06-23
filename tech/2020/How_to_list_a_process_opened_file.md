# How to list a process opened file
2020/01/13

First use `ps` command to find the pid of the process you would like to monitor.

Then use
```
sudo lsof -p pid -P
```
