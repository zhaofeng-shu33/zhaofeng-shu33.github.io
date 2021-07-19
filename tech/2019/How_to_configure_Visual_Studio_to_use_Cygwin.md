# How to configure Visual Studio to use Cygwin
2019/08/28

Use open folder project, you need to specify it as follows:
```json
{
  "configurations": [
    {
      "inheritEnvironments": [
        "cygwin_64"
      ],
      "name": "x64-Debug",
      "includePath": [
        "${env.INCLUDE}",
        "${workspaceRoot}\\**"
      ],
      "defines": [
      ],
      "intelliSenseMode": "windows-clang-x64",
      "forcedInclude": [ "${env.CYGWIN_ROOT}\\predefined_macro.h" ],
      "environments": [
        {
          "CYGWIN_ROOT": "C:\\cygwin64",
          "BIN_ROOT": "${env.CYGWIN_ROOT}\\bin",
          "environment": "cygwin_64",
          "INCLUDE": "${env.CYGWIN_ROOT}\\usr\\include;${env.CYGWIN_ROOT}\\lib\\gcc\\x86_64-pc-cygwin\\7.4.0\\include;${env.CYGWIN_ROOT}\\usr\\include\\python2.7;${env.CYGWIN_ROOT}\\usr\\include\\w32api",
          "PATH": "${env.CYGWIN_ROOT}\\bin;${env.PATH}"
        }
      ]
    }
  ]
}
```
See [user defined environment](https://docs.microsoft.com/en-us/cpp/build/cppproperties-schema-reference?view=vs-2019) for detail.

A key step is to specify the predefined macro for cygwin. You need to create a file called `predefined_macro.h`, which is the output of `gcc -dM -E - < /dev/null` in cygwin environment.