# may no required

```
fdisk /dev/vda
```

# extend disk

```
vgextend ubuntu-vg  /dev/vda4
lvextend -l+100%FREE /dev/mapper/ubuntu--vg-ubuntu--lv
resize2fs /dev/mapper/ubuntu--vg-ubuntu--lv
```

# disk commands

```
pvs  # list virtual Group (VG)
vgrename -v ubuntu-vg primary # rename virtual group (VG)
lsblk # list virtual group (VG)
```

https://www.redhat.com/sysadmin/create-volume-group#:~:text=A%20volume%20group%20(%20VG%20)%20is,of%20the%20combined%20physical%20devices.
