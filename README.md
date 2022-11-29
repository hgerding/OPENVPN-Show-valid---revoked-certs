# Easy-rsa / OPENVPN Show valid - revoked certs

Purpose: show the revoked and valid certs for openvpn/ easyrsa.

to make it easy for people to quickly check a server cert.

This script works with Openvpn at the linux command line 
    The script is generic python so it will work on other platforms as well.

this script is simple ie not fancy modify as you will (you can do this one line with a grep and awk if you want)

You can pass the index.txt on the commands line using the -f option

otherwise you run it at the command line with just -r or -v

Usage: /root/bin/ovpn-show-certs -hrv
-h this help
-d Debug
-r revoked list
-v show valid certs
-f file-index.txt (needs to be combined with -r or a -v)

example:
ovpn-show-certs -r
Cert: /CN=clientcert1 Is Revoked on: 2022-10-12 17:58:31 GMT/Zulu time
Cert: /CN=\x0D Is Revoked on: 2022-02-07 17:53:29 GMT/Zulu time
Cert: /CN=clientcert2-test Is Revoked on: 2022-02-15 23:55:30 GMT/Zulu time

ovpn-show-certs -v
Cert: /CN=ServerCert1 Is VALID and expires on: 2024-04-21 06:55:35 GMT/Zulu time
Cert: /CN=ServerCert1 Is VALID and expires on: 2024-04-21 07:09:56 GMT/Zulu time
Cert: /CN=clientcert3 Is VALID and expires on: 2024-04-21 16:49:35 GMT/Zulu time
Cert: /CN=client_other_cert Is VALID and expires on: 2024-04-21 16:50:18 GMT/Zulu time

this is the command line to use if you want to specify the file index.txt with location
ovpn-show-certs -f /etc/easy-rsa/pki/index.txt -r

More info:
You can edit the file and change the following file to hard wire a new file location in.

indexfile = '/etc/easy-rsa/pki/index.txt'

the date time format is
220215235530Z which is YYMMDDHHmmSS and z for ZULU/GMT timezone 

the script assumes a "z" and it is always printed in GMT

