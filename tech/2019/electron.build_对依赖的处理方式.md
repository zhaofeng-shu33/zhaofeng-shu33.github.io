# electron.build 对依赖的处理方式
2019/07/17

一个 electron 项目中会有很多 node_modules 依赖，如果依赖是用 `npm` 安装的，本身会带有大量的 Symbol Link. electron.build 并不是直接把 项目的 node_modules 目录拷贝过去，而是将所有的 Symbol Link 恢复成实际的文件。
另外，它只对 `package.json` 的 `dependency` 字段进行处理，因此有可能出现在调试模式程序可以运行，打包会不能运行的状况，有可能是 `require(module_name)` 引起的 not found. 打包程序的报错要结合日志进行分析。

如果想绕过 electron.build 对依赖的处理，可以在 `package.json` 的 `extraResources` 字段指定额外的内容
```JSON
 "extraResources": [
{
  "from": "./server",
  "to": "./server"
 }]
```
这时 server 目录下的内容便会直接 copy 到 目标目录下而不会有筛选。