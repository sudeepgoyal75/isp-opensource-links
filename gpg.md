# import
gpg --import sudeep.gpg

# encrypt
gpg --output sudeep.txt.gpg --encrypt --recipient your.friend@yourfriendsdomain.com  sudeep.txt


# decrypt
gpg --output sudeep.txt --decrypt sudeep.txt.gpg

# document
https://www.gnupg.org/gph/en/manual/x110.html
