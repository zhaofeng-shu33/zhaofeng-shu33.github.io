# Wiki服务器的配置
2018/10/16

本文介绍在Ubuntu Server 上配置Wiki服务器的[MediaWiki 官方参考](https://www.mediawiki.org/wiki/Manual:Installation_requirements),
所用的版本是 Ubuntu 16.04。

## 安装必要的软件
通过命令 `sudo netstat -tulpn | grep :80` 查看原服务器已安装apache2，ubuntu 系统 apache2 的默认安装目录是
`/etc/apache2`，查看其相关的配置文件`/etc/apache2/sites-enabled/*.conf` 找到其静态主页的文件目录是`/var/www/html`，
安装 apache2 此步骤跳过。

通过命令 `sudo apt-get install mariadb-server` 安装数据库 *MariaDB 10.0* 并配置`root`账户的用户名和密码。

通过命令 `sudo apt-get install php7.0 libapache2-mod-php7.0 php7.0-mysql php7.0-xml php7.0-mbstring` 安装 `php7.0`、与 `apache2` server 的绑定、数据库的绑定以及其他php依赖的模块;

## 下载mediawiki 源码并解压

    wget https://releases.wikimedia.org/mediawiki/1.31/mediawiki-1.31.1.tar.gz
    tar -xvzf mediawiki-1.31.1.tar.gz
    rm mediawiki-1.31.1.tar.gz
    mv mediawiki-1.31.1 report
    
## 配置
用浏览器打开 `your_root_url/report/index.php` 按照提示进行进一步配置，生成`LocalSetting.php`文件，上传到服务器上与`index.php`处于同一目录下。

## 调整上传文件大小限制
官方说明：[https://www.mediawiki.org/wiki/Manual:Configuring_file_uploads#Set_maximum_size_for_file_uploads](https://www.mediawiki.org/wiki/Manual:Configuring_file_uploads#Set_maximum_size_for_file_uploads)
总结其主要步骤为：
1. 修改`php.ini` 文件中 `upload_max_filesize`
1. 重启 `apache` （或者其他）
1. 重启 `php-fpm`

## 关于网站迁移
首先要在原来的服务器上进行备份，包括数据库的备份和媒体文件的备份，数据库的备份可采用
```shell
mysqldump -u userid -p dbname > backup.sql
```
具体见 [wiki backup](https://www.mediawiki.org/wiki/Manual:Backing_up_a_wiki)。

媒体文件的备份连同php代码一起备份：
```shell
tar zcvf wiki.tar.gz folder 
```