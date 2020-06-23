# vcpkg and vs2019
2019/05/09

VS2019 比较新，配合最新的cmake 3.14 可以在msvc toolset v14.2上做一些编译，但一些依赖以及vcpkg 编译系统还不完全支持 v14.2。如果只装了VS2019，可以同时安装v14.2和v14.1的编译工具以支持。

需要使用 custom triplet (See [How to use custom triplet](https://www.cnblogs.com/zhaofeng-shu33/p/10771521.html)，并且做一些处理 （See [add VS150COMNTOOLS](https://github.com/microsoft/vcpkg/issues/6330#issuecomment-490424194) ）。

公共的port中明确说明不会在python中引入更多的build，(see [fix python features](https://github.com/microsoft/vcpkg/pull/3105)） ，当然可以考虑 private port的方法，但很多公有依赖比较难解决，也要相应自己修改。
如果系统中python minor的版本不一致， 用C++ binding 弄的包也是无法在系统中使用的。目前 vcpkg 的 python3  是 3.7版本，系统中需要升级 python 才能保持兼容。