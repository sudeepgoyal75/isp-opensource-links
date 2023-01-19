# http proxy connect 

```
curl -x <proxy>:<port> google.com
```


# connect 


curl we can use multiple --connect-to..
so for example you can have 

```
--connect-to ::127.0.0.1:8888 --connect-to 10.10.10.10:443
```

This would cause all connections to hit 127.0.0.1:8888 instead of the specified IP (from DNS or direct) BUT 10.10.10.10:443 will use real IP and real port.
