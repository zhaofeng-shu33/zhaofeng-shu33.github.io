# Why php-composer mirror not works
2019/11/05

Php-composer downloads two kinds of files: meta-data and actual packages.
The meta-data of packages is in json format while the actual package is in zip format.
Almost all php composer mirrors have stored the meta-data in their own server. But only partial package zips are stored in it.

Take `https://mirrors.aliyun.com/composer/` for example, if you download `alibabacloud/sdk`, it is quite fast since all the required packages are
stored in aliyun server in the following url format: `https://mirrors.aliyun.com/composer/dists/%package%/%reference%.zip`. The reference is the git commit hash and the package is composed of
a namespace and the package name itself. You can download successfully for example, `https://mirrors.aliyun.com/composer/dists/ralouphie/getallheaders/120b605dfeb996808c31b6477290a714d356e822.zip`.
However, you can not download the following package: `https://mirrors.aliyun.com/composer/dists/jpgraph/jpgraph/e82db7da6a546d3926c24c9a346226da7aa49094.zip`.
The reason is that only partial package zips are stored in aliyun mirror. 