import paramiko
def led():

    ip_address = "raspberrypi.local"  # Replace with the IP address of your Raspberry Pi
    username = "pi"  # Replace with your Raspberry Pi username
    password = "1234567890"  # Replace with your Raspberry Pi password

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip_address, username=username, password=password)

    stdin, stdout, stderr = ssh.exec_command("python conn.py")
    print(stdout.read().decode())

    ssh.close()
