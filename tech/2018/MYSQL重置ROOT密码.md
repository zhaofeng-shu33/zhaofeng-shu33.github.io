# MYSQL重置ROOT密码
2018/11/11

#背景
mysql 服务器长时间未使用，管理员当时设置的root 密码忘记，需要重置 root 密码，并加以妥善保存。

#步骤
1. 关闭 mysql 服务 `systemctl stop mysql`
1. 以跳过密码验证的方式启动 mysql 服务`mysqld --skip-grant-tables`
1. 本地登陆后设置新的root 密码 `update mysql.user set authentication_string = password('123') where User = 'root'` 并且 'flush privileges'
1. 以需要密码验证的方式重启 mysql 服务