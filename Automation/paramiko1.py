#paramiko helps in communicating with ssh2 servers.

import paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('127.0.0.1',username='sr',password='ls')

stdin,stdout,stderr=ssh.exec_command('df')

print ('OUTPUT')
for line in stdout:
	print (line)

print ('ERROR')
for line in stderr:
	print(line)

#ssh.close()

ftp = ssh.open_sftp()
ftp.get('Sti_Trace.log', 'paramiko-test.log')
ftp.close()
ssh.close()