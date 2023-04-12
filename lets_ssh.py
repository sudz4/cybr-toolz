
#libs
import subprocess
import paramiko

#config
from config import REMOTE_HOST_IP
from config import UBUNTU_UN
from config import UBUNTU_PW

def run_remote_command(ssh, cmd):
    stdin, stdout, stderr = ssh.exec_command(cmd)
    return stdout.read().decode('utf-8').strip()

def main():
    #target machine IP and creds
    remote_host = REMOTE_HOST_IP 
    username = UBUNTU_UN    
    password = UBUNTU_PW   

    #connect to the remote machine using SSH
    ssh = paramiko.SSHClient() #implements the SSHv2 protocol
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #allowing you to perform SSH operations like connecting to remote servers
    ssh.connect(remote_host, username=username, password=password) #running commands, and transferring files using SFTP

    # hostname -I
    ip_addresses = run_remote_command(ssh, "hostname -I")
    print(ip_addresses)

    # ip link show
    ip_link_show = run_remote_command(ssh, "ip link show")
    print(ip_link_show)

    # lspci | grep -i ethernet
    lspci_ethernet = run_remote_command(ssh, "lspci | grep -i ethernet")
    print(lspci_ethernet)

    # lspci -v -s 00:05.0
    lspci_details = run_remote_command(ssh, "lspci -v -s 00:05.0")
    print(lspci_details)

    # can just keep adding more commands here... ********************************************* 4 

    # close the SSH connection
    ssh.close()

if __name__ == "__main__":
    main()

    ascii_art = """                               
  _    |_   _  ._   _|_  _   _  | _  
 (_ \/ |_) (/_ |     |_ (_) (_) | /_ 
    /                                
                                    
    """
    print(ascii_art)