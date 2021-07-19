# make bootable win10 on debian buster
2020/05/27


It seems that `cp a.iso /dev/sdb` or `dd if=a.iso of=/dev/sdb` not works for win iso image.
Since it formats the disk as UDF file system.

We have a `win.im` which is larger than 4GB, fat32 format does not allow this. Therefore we use exFat.
We don't use NTFS since many old machines do not recognize this format when they are on boot loading stage.

We use MBR partition table, which can be created by GUI program `gnome-disk-utility`.

Unfortunately, there is no GUI to format the usb as exfat format. We need to use command line to do this, see
https://newtocode.wordpress.com/2014/02/12/format-usb-as-exfat-in-ubuntu-13-10-terminal/ for detail.

After successfully formatting the disk, we follow https://itsfoss.com/bootable-windows-usb-linux/ to copy all files 
of iso to the usb disk.
