import argparse
from FTP_Pong import FTP_Pong
from HTTP_Pong import HTTP_Pong
from SSH_Pong import SSH_Pong

# Test Commands
# python pong http www.google.fr
# python pong ftp localhost -u anonymous -p guest
# python pong ssh 209.97.128.189 -u root -p olivierRoot

def pong(protocol, host, secure, username, password):
    if protocol == "http":
        HTTP_Pong(host, secure)
    elif protocol == "ftp":
        FTP_Pong(secure, host, username, password)
    elif protocol == "ssh":
        SSH_Pong(host, username, password)

def main():
    protocols = ["http", "ftp", "ssh"]
    
    #Parsing Arguments
    parser = argparse.ArgumentParser(description="Check device")
    parser.add_argument("protocol", choices=protocols, help="The protocol to use")
    parser.add_argument("host", type=str, help="The host to ping")
    parser.add_argument("-s", "--secure", type=bool, default=False, help="Use the secured version of the protocol")
    parser.add_argument("-u", "--username", type=str, default="anonymous", help="Username")
    parser.add_argument("-p", "--password", type=str, default="guest", help="Password")
    args = parser.parse_args()
    
    pong(args.protocol, args.host, args.secure, args.username, args.password)

if __name__ == '__main__':
    main()