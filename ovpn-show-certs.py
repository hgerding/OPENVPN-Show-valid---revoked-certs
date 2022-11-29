#!/usr/bin/python
#
#
# Used to display OpenVPN Certs
# By Harm Gerding
# ver 1.0
#    
# Copyright (C) 2022  Harm Gerding
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# Usage: /root/bin/ovpn-show-certs -hrv
# -h this help
# -d Debug
# -r revoked list
# -v show valid certs
# -f file-index.txt (needs to be combined with -r or a -v)


import sys, getopt
import datetime

indexfile = '/etc/easy-rsa/pki/index.txt'
revoketype="no"
validtype="no"
debug=False

def print_help():
   print("ovpn-show-cert Copyright (C) 2022  Harm Gerding")
   print("This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.")
   print("This is free software, and you are welcome to redistribute it")
   print("under certain conditions;")
       
   print("Usage: " + str(sys.argv[0]) + " -hrv")
   print("-h this help")
   print("-d Debug")
   print("-r revoked list")
   print("-v show valid certs")
   print("-f file-index.txt (needs to be combined with -r or a -v)")


def main(argv):
   global indexfile
   global revoketype
   global validtype
   global debug

   try:
      opts, args = getopt.getopt(argv,"hdrvf:",["ifile"])
   except getopt.GetoptError:
      print("Invalid Option")
      print_help()
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print_help()
         sys.exit()
      elif opt in ("-d"):
         debug = True
         print("In Debug Mode")
      elif opt in ("-r"):
         revoketype="yes"
      elif opt in ("-v"):
         validtype="yes"
      elif opt in ("-f", "--ifile"):
         indexfile = arg
   if (len(sys.argv)==1):
       print_help()
       sys.exit()

if __name__ == "__main__":
   main(sys.argv[1:])

if (debug==True):
   print('Input file is (after main): ', indexfile)

f = open(indexfile, "rt")

if (debug==True):
   print("Reading File")

while True:
   line=f.readline()
   if not line:
      break
   if (debug==True):
      print("Line:: " + line)
   line_fields = line.split()
   if (debug==True):
      print("Fields: " + str(line_fields))
   if (revoketype=="yes" and line_fields[0]=="R"):
      expiry_time_no_format = line_fields[2]
      expiry_time_no_format = expiry_time_no_format[:-1]
      if (debug==True):
          print("String: " + expiry_time_no_format)
      expiry_time = datetime.datetime.strptime(expiry_time_no_format, "%y%m%d%H%M%S").strftime("%Y-%m-%d %H:%M:%S")
      print("Cert: " + line_fields[5] + " Is Revoked on: " + expiry_time + " GMT/Zulu time")
   if (validtype=="yes" and line_fields[0]=="V"):
      expiry_time_no_format = line_fields[1]
      expiry_time_no_format = expiry_time_no_format[:-1]
      if (debug==True):
          print("String: " + expiry_time_no_format)
      expiry_time = datetime.datetime.strptime(expiry_time_no_format, "%y%m%d%H%M%S").strftime("%Y-%m-%d %H:%M:%S")
      print("Cert: " + line_fields[4] + " Is VALID and expires on: " + expiry_time + " GMT/Zulu time")

f.close()