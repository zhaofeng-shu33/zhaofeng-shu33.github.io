# cuda toolkit installation on machine without GPU
2019/12/05

For cross-compilation purpose.
We use `Ubuntu 16.04`.

```shell
echo "deb [ trusted=yes ] http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64 /" > /etc/apt/sources.list.d/cuda.list
apt update
apt install nvidia-cuda-toolkit
```
