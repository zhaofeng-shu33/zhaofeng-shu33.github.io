# Backup old material
2020/05/11

First use the camera of a smart phone or scanner to prepare the original documents.

Rotate the image if necessary.

If you use the camera, you can rename the file, using

```Python
import os
a = os.listdir('./')
cnt=1
for i in a:
    os.rename(i, '%d.jpg'%cnt)
    cnt+=1
```

Then compress the images to some satisfied level.
You can use [this](https://gist.github.com/zhaofeng-shu33/671f4c0053834198ae1664aca8de1ab7) Python script.

Then convert the images to pdf format if necessary.

```Python
import os
from PIL import Image
a = os.listdir('./')
for i in a:
    im = Image.open(i)
    im.save(i.replace('jpg','pdf'))
```
Merge these pdf to a single pdf file.

Upload necessary files to cloud.