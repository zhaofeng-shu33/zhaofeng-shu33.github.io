# node重新加载模块
2019/03/09

```JavaScript
delete require.cache[require.resolve('module name')];
var my_module = require('module name');
```