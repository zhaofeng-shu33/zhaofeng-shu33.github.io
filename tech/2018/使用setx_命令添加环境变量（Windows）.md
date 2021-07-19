# 使用setx 命令添加环境变量（Windows）
2018/11/14

#背景
用GUI的方法可能添加环境变量可能会比较麻烦，为此可采用命令行操作的方式。
#步骤
1. 以管理员身份运行 `cmd` 输入 `setx /M "%path%" "%path%[new_path];"。其中 `\M` 开关表示添加系统变量，由于 `%path%` 本身是系统变量和用户变量拼起来的，不能用此方法添加用户变量。
详见[https://superuser.com/questions/601015/how-to-update-the-path-user-environment-variable-from-command-line](https://superuser.com/questions/601015/how-to-update-the-path-user-environment-variable-from-command-line)
1. 设置在新的命令行窗口生效。