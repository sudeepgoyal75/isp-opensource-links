# import
gpg --import sudeep.gpg

#encrypt
gpg --output sudeep.txt.gpg --encrypt --recipient your.friend@yourfriendsdomain.com  sudeep.txt


# decrypt
gpg --output sudeep.txt --decrypt sudeep.txt.gpg
