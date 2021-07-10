# Windows学习"Network Analysis in Python"
2019/03/29

原代码仓库的地址为 [Network Analysis in Python](https://github.com/nderzsy/Network-Analysis-in-Python---Tutorial-JupyterCon18-ODSCEast18).

主要按照里面的README.md 进行操作，全部仓库有100MB以上。考虑到数据比较大，再加上我对原笔记文件有修改，建议从我用 gitee 导入的国内站点下载这个仓库：[gitee](https://gitee.com/freewind201301/Network-Analysis-in-Python---Tutorial-JupyterCon18-ODSCEast18)

安装完conda 后安装 jupyter，最近好像有个bug， notebook 这个包5.7.6版本出了点问题，建议安装5.7.4，用下面的命令：
```shell
conda install notebook=5.7.4
```
运行后还要按 Ctrl +Shift + R 才能在浏览器看到结果，详见[issue](https://github.com/jupyter/notebook/issues/4488) 的讨论。

其他注意事项：
1. jupyter 启动要在仓库的根目录下，否则数据文件的路径可能会有问题。
1. 安装包的时候建议先把 jupyter 关掉，否则可能会出问题。
