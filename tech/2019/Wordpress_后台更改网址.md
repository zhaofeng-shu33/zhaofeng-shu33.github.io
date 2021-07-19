# Wordpress 后台更改网址
2019/02/12

<p>在 `wp_options`&nbsp;数据库执行下面两条命令</p>
<p>```sql</p>
<p>update wp_options set option_value = 'your_new_url' where option_name = 'home';</p>
<p>update wp_options set option_value =&nbsp;'your_new_url' where option_name = 'siteurl';</p>
<p>```</p>
<p>新的URL为wordpress&nbsp;主页的url。</p>