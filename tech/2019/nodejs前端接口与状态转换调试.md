# nodejs前端接口与状态转换调试
2019/04/29

和UI无关的逻辑用browser 调有时不太方便，配置 node 命令行调试环境方法如下：
```shell
cnpm install @babel/core @babel/cli @babel/register @babel/polyfill cross-fetch/polyfill
```
因为node 作为commonjs 的环境缺少一些browser 的全局变量（如fetch 等），因此需要装一些 polyfill。

启动 nodejs 前 preload 一些模块：`node -r @babel/register -r @babel/polyfill -r cross-fetch/polyfill`。
这样可以直接 require es6的模块，通过 @babel/register 进行自动转换。

使用 `node inspect test_script.js` 调试脚本 test_script.js，其中 该脚本前几行 load 必须的模块：
```JavaScript
require('@babel/register');
require('@babel/polyfill');
require('cross-fetch/polyfill');
```
在需要调试的代码附近设置 `debugger` 这条语句即可进入，debugger 模式可以与 REPL 模式切换，详见 [Debugger](https://nodejs.org/api/debugger.html).