# How to install non-free software for debian buster
2020/01/14

Add the following line to the `/etc/apt/sources.list`.
```
deb [ trusted=yes ] https://apt.atzlinux.com/debian buster non-free
```
Then run `apt update` and use `apt search linuxqq`.

See [official website](https://www.atzlinux.com) for detail.