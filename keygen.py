#keygen example for Fox Crackme
# https://reverse.put.as/wp-content/uploads/2010/05/3-Fox.zip
# Charles Leerink 2016
#
# Yes I know this is an old one, but hey I did it anyways.....
# Since i'm Learning Python


import hashlib

print "#############################################"
print "#       Fox CrackMe KeyGen Example      #"
print "#############################################"
print ""
print ""

#serial Algo

name = raw_input("Name: ")
sha1 = hashlib.sha1(name)
final_string = sha1.hexdigest()

#just the serial

print "Serial: " + final_string.upper()


#licence file essentials

print ""
print ""
print "Save the below part as <filename.foxlicence> for a valid licence ----------->"
print ""
print"<dict>"
print"	<key>regName</key>"
print"	<string>"+ name + "</string>"
print"	<key>regNumber</key>"
print"	<string>"+ final_string.upper() + "</string>"
print"</dict>"
print"</plist>"
print""
print"STOP COPYING and save for example as: test.foxlicence"
print""






