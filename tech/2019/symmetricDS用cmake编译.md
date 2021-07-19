# symmetricDS用cmake编译
2019/05/03

[symmetricDS](http://www.symmetricds.org) 是同步数据库的软件，client 端提供了 C语言的库，默认是用 Eclipse 构建，也可以自己写CMakeLists 构建，下面是在Ubuntu 系统编译并运行成功的步骤：
## 依赖
根据[symmetric-client-clib](https://github.com/JumpMind/symmetric-ds/tree/3.10/symmetric-client-clib) 可以用 apt-get 安装一些依赖，LibCSV 的包名是 `libcsv-dev`，此外还要安装 `libzip-dev`，完整的命令为
```shell
sudo apt-get install libcsv-dev libzip-dev libsqlite3-dev libcurl4-gnutls-dev
```
带 dev 表明安装了所需的头文件，因为依赖控制的原因， 相应的运行时库 so 如 libsqlite3.so 也会自动安装。

## 源码
使用 svn 工具下载 symmetric-ds 的 GitHub 子目录，然后下载 symmetric-client-native 的入口文件放到和 libsymmetric.c 同一文件夹下（称为项目根目录）
```shell
svn checkout https://github.com/JumpMind/symmetric-ds/trunk/symmetric-client-clib ./
cd symmetric-client-clib
wget https://github.com/JumpMind/symmetric-ds/raw/3.10/symmetric-client-native/src/SymClientNative.c
wget https://github.com/JumpMind/symmetric-ds/raw/3.10/symmetric-client-native/inc/SymClientNative.h
```

## 构建文件
需要创建两个`CMakeLists.txt`，一个放在项目根目录下面，内容是：
```cmake
cmake_minimum_required(VERSION 3.5) # version is not important
project(symmetricdb LANGUAGES C)
include_directories(${PROJECT_SOURCE_DIR}/inc)
add_subdirectory(src)
add_executable(symclient SymClientNative.c)
find_library(ZIP zip) 
find_library(CURL curl)
find_library(SQLITE sqlite3)
find_library(CSV csv)
target_link_libraries(symclient libsymclient)
target_link_libraries(symclient ${CURL})
target_link_libraries(symclient ${ZIP})
target_link_libraries(symclient ${SQLITE})
target_link_libraries(symclient ${CSV})
```
另一个放到 src 文件夹下，内容是：
```cmake
cmake_minimum_required(VERSION 3.5)
FILE(GLOB_RECURSE filelist ${CMAKE_CURRENT_SOURCE_DIR} *.c)
add_library(libsymclient ${filelist})
```
## 编译
在项目根目录下用 out of source build 的方法进行编译构建：
```shell
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
```