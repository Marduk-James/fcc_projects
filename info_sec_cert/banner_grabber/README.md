This is a Banner Grabber I am building for the Information Security Certification @freeCodeCamp.org

It's part 5 of the Python for Penetration Testing.

I will try to use this README more as a diary to keep track of problems I run into, things I dont understand, and solutions I find.

1) 
    Traceback (most recent call last):
  File "C:\Users\mjame\OneDrive\Documents\Jim\Coding\fcc_python_for-pen_testing\banner_grabber\banner_grabber.py", line 10, in <module>
    s.connect((ip, int(port)))
  ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

    FIXED: Well, wasn't broken. 
      Instead of using my IP address I used nmap.scanme.org and it worked great!!

      Response was:
      b'SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13\r\n'