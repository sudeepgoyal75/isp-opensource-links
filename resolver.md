# Find commands

```
find ./ -type f -exec sed -i 's/pakistan/india/g' {} \;
```

# Enable docker to user

```
### enabled docker user
sudo usermod -aG docker ${USER}
sudo chmod 666 /var/run/docker.sock
```

# Create empty file

```
fallocate -l 10G empty_10g_file.img
```

# disk  check

```
du -h --max-depth=1 / | grep '[0-9]G\>'
```

# enabled docker user

```
sudo usermod -aG docker ${USER}
sudo chmod 666 /var/run/docker.sock
```

# copy with permissions and mount

```
mkdir /newfolder
mkfs.ext4 /dev/vdd
mount -t ext4 /dev/vdd /newfolder
cp  -rap /data/* /newfolder
```

# in case volume size change run below command to update LVM

```
 resize2fs /dev/vdd
```

# linux grow disk

```
DISK=$1
(
 echo n # new partition
 echo p # primary parition
 echo   # partition number
 echo   # default start sector
 echo   # default end sector
 echo p # print table
 echo w # write table
) | fdisk $DISK

vgextend primary /dev/vda3
lvextend -l+100%FREE /dev/primary/root
resize2fs /dev/mapper/primary-root
exit 0

```

# json convert

```
python -m json.tool
```

# resolver config

```
cat /etc/systemd/resolved.conf
[Resolve]
DNS=8.8.8.8
#FallbackDNS=
Domains=abc.com


```

# DNS resolver status

```
systemd-resolve --status
```
