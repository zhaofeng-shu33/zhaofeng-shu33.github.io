# Build Miktex on Windows
## 2018/4/21

Principle: We try our best not to modify the source code (all CMakeList.txt)
Goal: Run mpm client program to debug(hacking...) its session state.

## Steps
* Add `-DWITH_UI_QT=OFF,-DWITH_UI_MFC=OFF` as we do not need to build UI app, and we do not need Qt5 Dependency.
* Add `C:\cygwin64\bin` to system path to resolve some unix program not found on windows (only needed in the current shell)
* Comment out `xsltproc` on line 884 of the main root `CMakeList.txt`; Add `-DWITH_MIKTEX_DOC=OFF` as We do not need Some Document Build utility.
* CMake uses system icu, manually set icu include directory to `ICU_INCLUDE_DIR:PATH=C:/Program Files (x86)/Windows Kits/10/Include/10.0.16299.0/um` in `CMakeCache.txt` as `FindICU.cmake` script can not find the include directory.
* We do not use `WITH_COM`, set '-DWITH_COM=OFF'

