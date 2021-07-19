# Linux OS 上使用 Windows VPN 客户端
2019/08/07

# windows proxy server 与 proxychains 配合
## 背景
* 假如你的工作站用 Linux 操作系统，公司提供的VPN只有 Windows 客户端，则你无法使用自己的电脑连接。

## Solution
提出如下的解决方案：通过 windows 虚拟机与特定的网络配置实现。下面假设你的操作系统是 CentOS 7，上面用 VMWare 安装了 Win10。

### Path
1. linux os 可以通过 wine 运行 windows exe，但对于涉及复杂网络配置的 vpn client, wine 的思路应该是行不通的，即使可以运行，linux os 也无法利用 client 弄出来的 network adapter。
1. windows 虚拟机的思路很容易想到，但如何将 windows 作为网关是一个难题。 win 10 虚拟机不是 win server，自带的 network 模块受限制，比如有名的 RRAS(routing and remote access service)虽然可以开启服务但无法使用管理工具，因此笔者在一番尝试下发现行不通。
1. 于是采用 windows proxy server 的方法， 同样因为 IIS 作 proxy 功能太弱，笔者费了一番功夫找到了一个开源的 cross-platform 的 proxy server 名字叫 [3proxy](https://github.com/z3APA3A/3proxy)，这个项目文档做的不好，经过一番探索才跑起来 server。
1.  linux os 如何使用搭建好的 proxy server 也是个难题，CentOS 7 实际并没有 system proxy 这一概念，有的 network client 是不会用你设置好的 http proxy 环境变量的。为此，只能在底层做一些改动强制软件如 matlab 使用 proxy。笔者找到了一个开源的 UNIX 平台的 [proxychains4](https://github.com/rofl0r/proxychains-ng)

### 最终网络结构
eth0 是一个内网
* Linux OS 192.168.0.254 （Win10的网关和DNS服务器）
* Win10 192.168.0.1 （运行 3proxy service 和 VPN客户端）

在其他机器上（非Win10），通过 3proxy 可访问到内网，假设 10.8.4.170 是内网对外提供HTTP服务的 IP 地址。

```shell
curl --socks 192.168.0.1:1080 10.8.4.170
curl --proxy 192.168.0.1:3128 10.8.4.170
```
curl 客户端通过命令行参数可以指定 proxy server，但 matlab 不行。

### 具体步骤

1. 首先要在管理节点安装 VMWare Win10 虚拟机，配置网络环境为 Bridge，使用管理节点的 etho adapter，这里可能需要解锁 vmware 的一个高级功能 `/usr/lib/vmware/bin/vmware-netcfg`。配置静态ip, network mask, gateway, dns server ip ， 然后确保 win10 可以上外网. 打开 win10 icmp firewall 的限制。在管理节点可以 ping 通 192.168.0.1。

1. 然后在 Win10 上安装 3proxy pre-built binary. 完成相关的配置，其中的要点有：取消 proxy 密码限制，打开对 3proxy service 的 firewall restriction。在管理节点使用 curl 命令测试 proxy server 是否正常。

1. 在管理节点编译安装 proxychains，修改 `/etc/proxychains.conf`，其中的要点有取消对 dns 请求的代理，对 localhost 的代理。

### Reference
[在 Linux 上使用深信服 VPN](http://kingsamchen.github.io/2019/02/23/using-sangfor-vpn-on-linux/)