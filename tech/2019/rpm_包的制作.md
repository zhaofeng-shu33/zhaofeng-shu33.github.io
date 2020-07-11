# rpm 包的制作
2019/06/09

patch 文件的产生：将上游tarball源码解压到一个目录后，初始化git 仓库并 add 所有的代码，用
`git tag upstream` 命令标识当前的commit，然后修改要patch的文件并commit

可以使用
```shell
git format-patch --no-prefix upstream
```
产生 相应的 patch 文件，之后 mv 到 `$topdir/SOURCES` 目录下面。