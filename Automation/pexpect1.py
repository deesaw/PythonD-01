import pexpect
child = pexpect.spawn("echo1.bat")
child.expect('Enter your age:')
child.sendline(65)
child.expect(pexpect.EOF, timeout=None)
cmd_show_data =  child.before
cmd_output = cmd_show_data.split('\r\n')
for data in cmd_output:
    print data

    