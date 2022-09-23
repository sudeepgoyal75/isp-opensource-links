

echo password | mkpasswd -m sha-512 -s

openssl passwd -6 -salt xyz  yourpass
