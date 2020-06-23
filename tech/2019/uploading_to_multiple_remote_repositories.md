# uploading to multiple remote repositories
2019/12/29

Saving below to a shell script file and execute it under the git local repositories with multiple remote counterpart:
```shell
#!/bin/bash
set -e -x
mapfile -t remote_url < <(git remote)
for i in "${remote_url[@]}"; do
    git push $i master
done
```

Known limitations: 

* single branch support
* single threaded