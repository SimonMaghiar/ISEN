from ftplib import FTP
from ftplib import FTP_TLS

#run local FTP server: sudo vsftpd
def FTP_Pong(TLS = False, host = "localhost", user = "anonymous", passwd= "guest"):
    ftp = FTP(host) if not TLS else FTP_TLS(host)
    ftp.login(user=user, passwd=passwd)
    print(ftp.getwelcome())
    ftp.close()