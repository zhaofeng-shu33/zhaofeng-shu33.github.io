# Deploying_Wordpress_on_Windows_Server

## 2018/1/14

## Version

* IIS8.5 on Windows Server 2012(x64)
* php-7.2.1
* mysql-5.7.20
* wordpress-4.9.1

## Step

* download php zip file from official website and extract it to disk, add the `path_to_php_extract_dir/bin` to `sys_path`
* edit `php.ini` , change the following configurations:

```INI
; change the default data zone to local
date.timezone = "Asia/Shanghai"
; configure extension dir
extension_dir = "path_to_php_extension_dir"
; configure doc root
doc_root = "path_to_php_file_root_path"
; also comment out the following extension:
extension = curl
extension = mysqli
extension = pdo_mysql
```

* download mysql zip file from official website and extract it to disk, add the `path_to_mysql_extract_dir/bin` to `sys_path`
* open cmd prompt and initialize the database by `mysqld --initialize`

By doing so, a random password is generated for root user, and the password can be 
found at error log file.

* open the database service by `mysqld`
* close the database service by `mysqladmin -u root -p shutdown`, type the root user password and the service is stopped.
* create a database `XXX` and a new user `YYY` with full privilege on `XXX`

* create a website in IIS Manager, edit the Module Mapping by mapping "*.php" to `FastCgiModule` with executable called `php-cgi.exe`
* grant IIS_USER with appropriate privilege to avoid 401 error.

* download wordpress zip file from official website and extract it to disk.
* copy `wp-config-sample.php` to a new file `wp-config.php` and edit it as follows:

```PHP
define('DB_NAME','XXX');
define('DB_USER','YYY');
define('DB_PASSWORD','password of YYY');
define('DB_HOST','allow only localhost connection to mysql');
```


## Issue remained
During this attempt, I did not configure mysql by `my.ini`, some default setting may be inappropriate, such as log file time_zone.

