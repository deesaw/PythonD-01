import ftplib

ftp = ftplib.FTP("ftp.kernel.org")
ftp.login("anonymous", "ftplib-example-1")

#data = []
ftp.cwd('/pub/software/java/jato')
ftp.retrlines('LIST')
#ftp.dir(data.append)



#for line in data:
#    print "-", line

# to download a file named readme
ftp.retrbinary('RETR jato-0.3.tar.xz', open('jato-0.3.tar.xz', 'wb').write)
# to upload a file name python.zip
# ftp.storbinary('STOR python.zip', open(python.zip, "rb"), 1024)

ftp.quit()
