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

# extend disk

https://www.cyberciti.biz/faq/howto-add-disk-to-lvm-volume-on-linux-to-increase-size-of-pool/

```
# Pysical device
pvs
pvdisplay

# LVM volume Groups (vg)
vgs
vgdisplay

#  LVM logical volume (lv)
lvs
lvdisplay

# find disk
fdisk -l
fdisk -l | grep '^Disk /dev/'

# Create physical volumes (pv) on new disk named /dev/sdb
 pvcreate /dev/sdb
lvmdiskscan -l

# Add newly created pv named /dev/vdb to an existing lv
vgextend VolGroup00 /dev/sdb

# Finally, you need extend the /dev/ubuntu-box-1-vg/root to create total 45GB (/dev/vdb (5G)+ existing /dev/ubuntu-box-1-vg/root (40G))
lvm lvextend -l +100%FREE /dev/mapper/VolGroup00-rootLV
resize2fs -p /dev/mapper/VolGroup00-rootLV

df -H
```
