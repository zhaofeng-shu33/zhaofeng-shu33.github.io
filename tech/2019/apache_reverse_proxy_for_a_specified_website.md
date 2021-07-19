# apache reverse proxy for a specified website
2019/05/19

使用 http://your_server_ip/content 代理 https://target_domain/content
在 apache 配置文件中设置如下：

```
SSLProxyEngine on
ProxyPass "/" "https://target_domain/"
ProxyPassReverse "/" "https://target_domain/"
```

需要使用 a2enmod 启用相关的 module：

```shell
sudo a2enmod ssl proxy proxy_http rewrite deflate headers proxy_connect proxy_html
```

效果是用 http://your_server_ip/content  可以打开  https://target_domain/content 的网页进行浏览，并且html 里的超链接也被rewrite 成 your_server_ip 下面的了，不过 target_domain 里一些和 javascript 相关的功能无法正常使用。