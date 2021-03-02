import pexpect
child = pexpect.spawn('ftp ftp.openbsd.org')
print "connected"
child.expect('Name .*: ')
child.sendline('anonymous')
child.expect('Password:')
child.sendline('noah@example.com')
child.expect('ftp> ')
print "logged in"
child.sendline('get robots.txt')
child.expect('ftp> ')
print "got the file"
child.sendline('bye')
child.close()