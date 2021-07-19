# 使用安装脚本安装Texlive
2018/12/14

# 介绍
TeX Live 是 TUG (TeX User Group) 维护和发布的 TeX 系统，可说是「官方」的 TeX 系统。网上可找到的教程大多是从镜像安装完整版texlive。镜像发布的周期较长，一些包的版本相对较低，如果希望一开始安装的就是最新版本的包并且需要个性化配置，建议使用官方提供的安装脚本(`install-tl`)进行安装。

# 步骤
以下以ubuntu 18.04系统为例，展示从安装脚本安装texlive的全过程。注意 texlive 是跨平台的，主要步骤适应于其他操作系统。

* 首先从官网或其镜像站下载安装脚本。
```shell
export REMOTE_INSTALLER_URL=http://mirror.ctan.org/systems/texlive/tlnet
export INSTALL_PACKAGE=install-tl-unx.tar.gz
wget $REMOTE_INSTALLER_URL/$INSTALL_PACKAGE
```
注意主站 `mirror.ctan.org` 不是一个真实的镜像，它会重定向到一个镜像站，在国内有时重定向的镜像站比较慢，可直接指向某些镜像站，**建议**设置
`export REMOTE_INSTALLER_URL=http://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/tlnet`。

* 解压安装脚本并运行。
```
export INSTALL_DIR=install-texlive
mkdir $INSTALL_DIR
tar -zxvf $INSTALL_PACKAGE -C $INSTALL_DIR --strip-components 1
$INSTALL_DIR/install-tl -repository $REMOTE_INSTALLER_URL -profile tl.profile
```
`install-tl` 的默认方式是文字模式的安装，首次启动会从指定的镜像站下载 `tlpdb` 数据库，数据库目前有11Mb左右，下载完成后出现选项，默认安装 `scheme-full`，即所有的宏包，目前会占用 5GB以上的硬盘空间，可根据提示进行设置以减少首次安装的容量大小。

这里简要介绍下texlive 安装内容的层级，最顶层的是 `scheme`，目前有 full, medium, small, basic, minimal 等; 其次是 `collection`，目前有41个，一个scheme 包含多个 collection; 最小的单元是 `package`，一个 collection 包含多个 package。这里的 package不仅包括宏包，还有可执行程序等。查看各 scheme 和 collection 具体包含内容和简介可以打开下载的 tlpdb 数据库文件（是一个文本文件）查找相应的字段。

为了减轻交互式配置安装的麻烦以及提供自动化安装的需求， 可指定安装需要的 profile 文件，在profile文件中，可指定scheme, collection, tlpdb 的配置信息以及texlive
安装所需要的环境变量。

texlive 默认配置中是安装到 `/usr/local/` 下面，需要对该文件夹有写权限，也可更改至用户目录下面。

* 利用 `tlmgr` 安装新的 `package`.
使用 `tlmgr install pkg` 安装新的包，若同时指定若干个包，包名之间用空格隔开。使用一段时间后，有更新包的需求使用`tlmgr update pkg` 可完成。更多 `tlmgr` 的用法可参考[2]


# 参考
1. [install-tl 用法说明](https://www.tug.org/texlive/doc/install-tl.html)
2. [tlmgr 用法说明](http://tug.org/texlive/doc/tlmgr.html)