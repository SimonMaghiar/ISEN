import paramiko

# ssh root@209.97.128.189
# olivierRoot
def SSH_Pong(host, username, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect(host, username = username, password=password)
    if (client.get_transport().is_active()):
        print("0 OK")
    client.close()