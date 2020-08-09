# 内网ssh穿透
2019/04/10

公司服务器没有公网IP，只有内网IP，利用自己的阿里云服务器（有公网ip）做ssh内网穿透，使得外网可访问。方法如下：

环境：
公司服务器和阿里云服务器均为 Ubuntu 操作系统，
需要修改阿里云服务器的 sshd_config 的相关配置与 公司服务器 ssh_config 的相关配置使得

1. sshd server 支持 remote port forwarding
1. 会话不会自动断开

具体操作见 [ssh preventing timeout](https://bjornjohansen.no/ssh-timeout).

首先配置公司服务器可以ssh无密登录阿里云服务器，具体方法是用基于密匙的方法，见 [ssh keys](https://help.ubuntu.com/community/SSH/OpenSSH/Keys)。

然后在公司用工作站ssh登录公司服务器, 在公司服务器上登录阿里云服务器，后面一个登录需要用 nohup 处理，避免前一个会话断开后导致后一个登录会话失效，后面一个完整的ssh登录语句为：

```shell
nohup ssh -tt -R aliyun_server_port_number:company_server_intranet_ip_address:company_server_ssh_port_number aliyun_server_username@aliyun_server_domain_name 2>&1 &
```
后面一个登录不会打开新的 terminal。退出前一个ssh会话。用如下的方法测试公司服务器ssh内网穿透（在工作站上）
```shell
ssh -p aliyun_server_port_number aliyun_server_username@aliyun_server_domain_name
```
参考：
1. [ssh tunneling example](https://www.ssh.com/ssh/tunneling/example)
1. [ssh port forwarding](https://help.ubuntu.com/community/SSH/OpenSSH/PortForwarding)