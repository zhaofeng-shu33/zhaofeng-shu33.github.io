# macOS 升级后重装命令行工具的问题
2018/11/05

# 问题背景
最近升级个人macbook 从 10.13 到 10.14 在终端输入 `git` 不能用了，发现是重装操作系统后原来的 **Command Line Tools** 被自动卸载了，
采用 `xcode-select --install` 命令发现 `currently unavailable`. 

# 解决方法
可以从网上下载适配个人 macbook 版本的开发工具，地址为[https://developer.apple.com/download/more/](https://developer.apple.com/download/more/)。需要用自己的 *AppleID* 先登录才可以下载。下载后按照提示安装即可。安装后即可正常使用 `git` 等命令。


# 参考
[stackoverflow](https://apple.stackexchange.com/questions/254380/macos-mojave-invalid-active-developer-path/265049#265049?newreg=dd14b53896074657a35d38937ef4d2e6)