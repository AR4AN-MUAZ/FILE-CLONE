#!/data/data/com.termux/files/usr/bin/python
import platform,os,sys
bit = platform.architecture()[0]
if bit == '64bit':
    import myfile
elif bit == '32bit':
    print(" [#] Sorry bit is not frequent right now")
