# WordPress 自动初始化数据库
2018/12/30

# 背景
自动化搭建开发环境、测试、部署如通过网页操作（访问 `/wp-admin/install.php`）相对比较麻烦且在有的场景无法实现。

# 步骤

1. 修改 `wp-config.php` 配置 wordpress 的数据库信息。
2. 在与`wp-config.php` 同级的目录新建`custom_install.php`，输入如下代码：
```php
<?php
define( 'WP_INSTALLING', true );

/** Load WordPress Bootstrap */
require_once( dirname( __FILE__ ) . '/wp-load.php' );

/** Load WordPress Administration Upgrade API */
require_once( ABSPATH . 'wp-admin/includes/upgrade.php' );

/** Load WordPress Translation Install API */
require_once( ABSPATH . 'wp-admin/includes/translation-install.php' );

/** Load wpdb */
require_once( ABSPATH . WPINC . '/wp-db.php' );

define('WP_SITEURL', 'http://localhost/wordpress');
$weblog_title = 'develop';
$user_name = 'zhaofeng_shu33';
$admin_email = '616545598@qq.com';
$public = 1;
$admin_password = 'random_generation_of_password'; // in plain text
$loaded_language = '';
$result = wp_install($weblog_title, $user_name, $admin_email, $public, '', wp_slash( $admin_password ), $loaded_language);
print_r($result);
?>
```
注意在以上设置用户名和密码。

3. 通过命令行或终端运行 `php custom_install.php` 即可完成wordpress数据库的初始化。