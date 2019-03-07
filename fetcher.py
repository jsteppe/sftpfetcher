import pysftp
import os

myHostname = input("Server name/IP: ")
myUsername = input("Username: ")
myPassword = input("Password for " + myHostname + ": ")
filename = input("Full path of the file you want to transfer from the remote machine: ")
home_dir = input("Local directory: ")
file_basename = os.path.basename(filename)

with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp:

    print("Connection succesfully established. File transferred.")
    
    remoteFilePath = filename
    localFilePath = home_dir + file_basename

    sftp.get(remoteFilePath, localFilePath)
