# php-fpm重启
2019/04/04

Ubuntu 18.04服务器
修改php init 文件后（/etc/php/7.2/fpm/php.ini）需要重启php-fpm，方法是：
```shell
kill -USR2 `cat /run/php/php7.2-fpm.pid`
```