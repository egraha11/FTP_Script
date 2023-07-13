from pathlib import Path
import os
import ftplib





FTP_URL = 'ftp://ftp.dlptest.com/'
FTP_User = 'dlpuser'
Password = 'rNrKYTX9g7z3RgJRmxWuGHbeu'

ftp_server = ftplib.FTP(FTP_URL, FTP_User, Password)

ftp_server.encoding = "utf-8"

write_file = input("Enter the file name to which you want to write to: \n")


p = Path(str(os.getcwd())) / write_file


for file_name in p.iterdir():
    if(file_name.is_file()):
        for file_name_2 in p.glob('*.txt'):
            with open(file_name_2, "rb") as file:
                ftp_server.storbinary(f"STOR {filename}", file)
                file.close()

    ftp_server.quit()