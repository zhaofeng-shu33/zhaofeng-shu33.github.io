# 阿里云oss上传文件
2019/12/07

# 方法一
使用 web interface 上传

# 方法二
使用 [oss browser](https://github.com/aliyun/oss-browser) 官方客户端软件上传，支持桌面操作系统，首次打开时输入 appid 和 secret 登陆，预设 oss 路径为 `oss://oef`，地域选深圳。
登陆后可上传文件。

# 方法三
使用 [oss util](https://github.com/aliyun/ossutil) 官方命令行工具上传，可以通过 `cron` 定时任务实现定期上传、备份等。
首先下载 `ossutil64` 这个可执行文件（不同系统名字可能不一样），使用方法为首先创建配置文件（修改id 和 secret）：
```shell
cat <<EOF >> ~/.ossutilconfig
[Credentials]
language=EN
endpoint=http://oss-cn-shenzhen-internal.aliyuncs.com
accessKeyID=aaa
accessKeySecret=aaa
```
然后用`ossutil64 cp local_file oss://oef/remote_dir/`，常用的命令有 `ossutil64 ls oss://oef/`，`ossutil64 mkdir oss://oef/test_dir2` 与Linux `ls`, `cp` 类似命令。
