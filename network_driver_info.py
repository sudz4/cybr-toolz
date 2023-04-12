"""Gather information on your network driver"""
# sometimes useful when setting up stuff on kali
# upon completion ----> this is a very usesful tool.
# i can run collections of bash commands from a python program.

#libs
import subprocess

def run_command(cmd): #cmd: The shell command to run, passed as a string.
    #subprocess.run() is a built-in Python function to run shell commands
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True) #text: When set to True, the output will be returned as a string.
    # stdout: subprocess.PIPE captures the standard output of the command.                  ## shell: When set to True, the command will be executed in a shell, allowing for shell features.
    # stderr: subprocess.PIPE captures the standard error output of the command.

    # .stdout contains the captured standard output of the command.
    return result.stdout.strip() # .strip() removes leading/trailing whitespace before returning the output.

def main():
    # hostname -I
    ip_addresses = run_command("hostname -I")
    print(ip_addresses)

    # ip link show
    ip_link_show = run_command("ip link show")
    print(ip_link_show)

    # lspci | grep -i ethernet
    lspci_ethernet = run_command("lspci | grep -i ethernet")
    print(lspci_ethernet)

    # lspci -v -s 00:05.0
    lspci_details = run_command("lspci -v -s 00:05.0")
    print(lspci_details)

if __name__ == "__main__":
    main()


