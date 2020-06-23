# 利用travis自动化构建与部署（文档项目）
2018/12/15

# 背景
保持网站上文档的最新性有比较重要的意义， travis ci 提供了免费的解决方案，本文基于 latex 构建+ aliyun oss 部署对此作了尝试。
项目链接为 [https://travis-ci.org/zhaofeng-shu33/lab2c_presentation_template](https://travis-ci.org/zhaofeng-shu33/lab2c_presentation_template)

# 构建
travis 本身不提供 texlive 的编译环境，需要用脚本安装，为减少每次下载大量包的延时，可采用 cache 的配置方法。为此在 `.travis.yml` 配置文件中通过
判断 `tlmgr` 有没有安装来区分是否是首次构建，从而决定是否需要下载texlive并安装。

## 构建时遇到的问题
texlive 不能很好的解决包依赖的问题，一方面安装了一些在编译过程中没有用到的宏包，另一方面会因为基本 collection 里面没有安装的包而报错。我们采用比较笨的方法是用 tlmgr 安装缺失的宏包。

# 部署
aliyun oss 部署有多种编程语言的sdk可供选择，这里我们使用python sdk。为此需要下载 oss2 的包，同样用 cache 来加快以后的部署速度。
为确保 appsecret 的安全性，采用在travis 项目设置里面配置环境变量的方法，有自动加密的功能。使用时像读取普通环境变量一样读取即可。