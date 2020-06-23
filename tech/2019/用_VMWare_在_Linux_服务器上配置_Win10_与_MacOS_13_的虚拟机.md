# 用 VMWare 在 Linux 服务器上配置 Win10 与 MacOS 13 的虚拟机
2019/07/24

## Win10
出于解决 Windows 上专用框架开发以及测试特定软件的需要，我在 Linux 服务器上用 VMWare 安装了 Win10 与 MacOS 13 的虚拟机。
使用的是 VMWare Player 15，目前实现了 Win10 使用固定的 IP 地址，开放 SSH 与远程桌面默认端口。将 Linux Server 的防火墙打开并做内网穿透便可
实现外网连接 Win10 服务器。注意 VMWare 配置内网穿透的功能在 Player 中找不到，在 CentOS 7 下面可以手动打开打开网络配置器UI

```shell
/usr/lib/vmware/bin/vmware-netcfg
```

## 数量
VMWare Player 不支持同时开两个虚拟机，考虑到对资源的占用（8核8GB内存等），也不方便同时开两个。

## Mac
VMWare Player 锁定了 建 Mac 虚拟机的功能，可以使用开源的方法解锁。具体操作见 [https://github.com/DrDonk/unlocker](https://github.com/DrDonk/unlocker)。
使用这种方法后虽然能建 Mac 虚拟机，但一旦建好后，无法通过 UI 更改 CPU、内存数量等。