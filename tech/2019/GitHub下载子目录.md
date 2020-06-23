# GitHub下载子目录
2019/02/04

# 背景
整个Github目录太大，国内网速不好，且其他部分也不需要。

# 方法
把 `/tree/master` 改成 `trunk`。
```shell
svn checkout https://github.com/lodash/lodash/trunk/docs output-dir
```