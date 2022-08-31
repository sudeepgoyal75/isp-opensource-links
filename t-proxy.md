# check T-Proxy Rules

```
iptables -t mangle -n -L
```

#  rule with port 

```
iptables -t mangle -A PREROUTING -i <interface> -p tcp --dport 80 -j TPROXY --tproxy-mark 0x1/0x1 --on-port 8080 --on-ip 127.0.0.1 || true
```

# rule with dest IP

```
iptables -t mangle -A  PREROUTING -i <interface> -p tcp -d 90.90.90.90  -j TPROXY --tproxy-mark 0x1/0x1 --on-port 8080 --on-ip 127.0.0.1
```


# for all ports handling 

```
iptables -t mangle -A  PREROUTING -i <interface> -p tcp  -j TPROXY --tproxy-mark 0x1/0x1 --on-port 8080 --on-ip 127.0.0.1
```

# haproxy
- http://www.haproxy.org/download/1.8/doc/proxy-protocol.txt


