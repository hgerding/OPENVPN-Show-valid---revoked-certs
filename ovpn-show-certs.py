#!/usr/bin/python
#
#
# Used to display OpenVPN Certs
# By Harm Gerding
#


import sys, getopt
import datetime

indexfile = '/etc/easy-rsa/pki/index.txt'
revoketype="no"
validtype="no"
debug=False

def print_help():
   print("Usage: " + str(sys.argv[0]) + " -hrv")
   print("-h this help")
   print("-d Debug")
   print("-r revoked list")
   print("-v show valid certs")
   print("-f file-index-html (needs to be combined with -r or a -v)")


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