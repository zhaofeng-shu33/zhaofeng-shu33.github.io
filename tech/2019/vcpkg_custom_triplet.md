# vcpkg custom triplet
2019/04/25

需求是要弄一个用 pip 发布的python 包，使用 boost-python 桥接 原C++代码，发布时不想带 boost-python 的运行时库，因此需要弄静态的 boost-python库，在 Windows平台下使用vcpkg 的自定义 triplet实现。
在 vcpkg\triplets 根目录下新建 `x64-windows-dynamic.cmake`
```cmake
set(VCPKG_TARGET_ARCHITECTURE x64)
set(VCPKG_CRT_LINKAGE dynamic)
set(VCPKG_LIBRARY_LINKAGE static)
if(PORT MATCHES "python3")
    set(VCPKG_LIBRARY_LINKAGE dynamic)
endif()
```
上面的设置使得对python3 这个port完全动态编译，这个库是 boost-python 的依赖库；对于 boost库，运行时库是动态的(/MD)，但库本身是静态的，由于vcpkg采用统一的命名规范，与 boost windows平台下库的名称不太一样。
之后使用`vcpkg install boost-python:x64-windows-dynamic`，同样方法安装其他库即可（均为链接动态的CRT和静态的库本身）

初始化cmake 项目时使用
```shell
cmake "-GVisual Studio 15 2017 Win64" -DCMAKE_TOOLCHAIN_FILE=%VCPKG_ROOT%scripts\buildsystems\vcpkg.cmake -DVCPKG_TARGET_TRIPLET=x64-windows-dynamic ..
```
其中`VCPKG_ROOT`是环境变量，指向本机vcpkg的安装目录。

使用custom 的 [setup.py](https://github.com/zhaofeng-shu33/principal_sequence_of_partition/blob/python-setup/setup.py) 进行打包
```shell
python setup.py bdist_wheel
```
输入用户名和密码上传到`pypi.org`
```shell
python -m twine uplodat dist\package.whl
```
把 `package.whl`换成你实际的包名。

然后在有相同python版本的windows电脑上（比如都是python3.6）可以用 `pip install package` 进行测试。