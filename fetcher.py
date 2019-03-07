import pysftp
import os

def prompts():
    """Asking for the remote machine and remote file parameters"""
    try:
        myHostname = input("Server name/IP: ")
        myUsername = input("Username: ")
        myPassword = input("Password for " + myHostname + ": ")
        remote_file = input("Full path of the file you want to transfer from the remote machine: ")
        home_dir = input("Local directory: ")
        file_basename = os.path.basename(remote_file)

        with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp:

            print("Connection succesfully established. File transferred.")
    
            remoteFilePath = remote_file
            localFilePath = home_dir + file_basename

            sftp.get(remoteFilePath, localFilePath)

            while True:
                cont = input("Continue operations? [y/n]: ")
                if cont == "y":
                    prompts()
                elif cont == "n":
                    quit()
                else:
                    continue
    except KeyboardInterrupt:
        print("Exiting...")

prompts()

