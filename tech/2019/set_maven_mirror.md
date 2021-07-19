# set maven mirror
2019/09/07

Use browser to browse [aliyun maven mirror](https://maven.aliyun.com/mvn/view)
In `/etc/maven/setting.xml` add the following:
```xml
<mirror>
       <id>aliyun</id>
      <mirrorOf>central</mirrorOf>
      <name>Nexus aliyun</name>
      <url>http://maven.aliyun.com/nexus/content/groups/public</url>
</mirror>
```