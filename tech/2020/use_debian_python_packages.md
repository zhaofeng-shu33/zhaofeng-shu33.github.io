# Advantages to use debian intepreter packages over package manager itself
2020/6/13

As we can see We know that in debian operating system there are some Python packages packed by debian maintainers. These packages are installed in system level. Generally data science practitioners like to use conda or pip to install their packages. Usually the diversity of packages is: pypi.org > anaconda.cloud > debian source. The reason is obvious: everyone can upload packages to pypi.org, but for some channels of conda (like conda forge), the package requests are reviewed and guided. For debian the reviewing is more strict.

As we can see, the quality of the package is better in debian for other sources. For better quality we mean more clean dependency resolving mechanism, more stable version and there are less bugs within the installation of packages.

Another advantages is convenience. If we require debian 10 and use system level python and packages. We do not need to specify the versions of Python and each packages any more. They are fixed within debian 10. Also, we can omit some dependency packages since the installation is recursive.
The last advantage to use debian Python package is that it is cross-platform. Nowadays as arm computing is emerging, most packages do not have arm version on pypi or anaconda. This is painful for C-binding packages. Such situation brings difficulty for reproducibility on other architecture. But for debian, most packages are multi-arch, which means you can install corresponding packages even if you are using arm machine. This is very helpful and contributes greatly if researchers can use debian system packages.

All above is using python as an example. The same argumentation is suitable for R programming language or others as well.

We have to admit there are some limitations and intrinsic drawback when debian python packages are preferred. For example, many packages may not exist and the version of existing package may be a little bit old. I think this kind of problem can be alleviated if a hybrid solution is used. That is, system package > pypi package. Notice that conda solution is incompatible with system + pypi since they use different python interpreter.