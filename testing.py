def testing_log(command):
	stdin, stdout, stderr=ssh.exec_command(command)
	li=stdout.readlines()
	return (li)


import os
import paramiko
import time
import re


ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.1.249",username='guest',password='guest123',look_for_keys=False)
print("connection established")


n=0
p=0
x=0
timest=time.strftime("%Y.%m.%d - %H:%M:%S")

cc=os.getcwd()
os.chdir('%s'%cc)
h=os.listdir()
#print(h)
fs=open("setup","r")
ds=fs.readlines()
fs.close()
print(ds)
for sd in ds:
	#print(sd)
	d=sd.strip('\n')
	if d=='setup':
		print("IT IS SETUP FILE")
	if d=='config':
		print("IT's A CONFIG FILE")
	if d=='testing.py':
		print("IT IS A PYTHON FILE")
	if d!='setup' and d!='config' and d!='testing.py':
		os.chdir('%s/%s'%(cc,d))
		print("%s"%d)
		z=os.listdir()
		#print(z)
		fd=open('setup','r')
		print("content of setup")
		v=fd.readlines()
		print(v)
		for i in v:
			#print(i)
			os.chdir('%s/%s'%(cc,d))
			b=i.strip('\n')
			#print(b)
			
			bb=b[::-1]
			#print(bb)
			bbb=bb[4:]
			#print(bbb)
			bbbb=bbb[::-1]
			
			fg=open("%s"%b,'r')
			r=fg.read()
			s=""
			found=False
			for line in r:
	    			if ":" in line:
	    				found=True
	    			if found :
	    				s=s+line
			e=s[1:]
			q=e.strip('\n')
			print(q)
			
			try:
				fe=open("%s.exp"%bbbb,"r")
				ex=fe.read()
			except:
				print("%s.exp file not found"%e)
				
				
			ot=testing_log(q)
			os.chdir('%s/%s/log'%(cc,d))
			fff=open("%s.log  %s"%(timest,q),"a+")
			fff.write("##############################  TEST CASE STARTED  ##############################")
			fff.write("\n")
			fff.write("******************************  COMMAND=%s  ******************************" %q)
			fff.write("\n")
			fff.write("\n")
			for bv in ot:
				fff.write("%s" % bv)
			fff.write("\n")
			fff.write("\n")
			fff.write("##############################  TEST CASE  ENDED  ##############################")
			fff.write("\n")
			fff.write("\n")
			fff.close()
			
			os.chdir('%s/log'%cc)		
			n=n+1
			ff=open("%s.log"%timest,"a+")
			ff.write("##############################  TEST CASE %s STARTED  ##############################" %n)
			ff.write("\n")
			ff.write("******************************  COMMAND=%s  ******************************" %q)
			ff.write("\n")
			ff.write("\n")
			for bv in ot:
				ff.write("%s" % bv)
			ff.write("\n")
			ff.write("\n")
			ff.write("##############################  TEST CASE %s ENDED  ##############################" %n)
			ff.write("\n")
			ff.write("\n")
			ff.close()
			
			c=ex.strip('\n')
			m=c.strip(' ')
			#print(m)
			t=str(ot)
			#print(t)
			
			try:
				w=re.compile(m)
				if (w.search(ot)):
					p=p+1
			except:
				print("it's not a regex")
			
			if (m==t):
				print("test case pass")
				p=p+1
				#print(p)
				#print(n)
			
			else:
				print("test case failed")
				x=x+1
				
				
		if ds=="":
			print("no file found")


			
os.chdir('%s/log'%cc)	
v=open("%s.result" %timest,"a+")
v.write(" TOTAL NUMBER OF TEST CASES : %s \n" %n)
v.write(" NUMBER OF TEST CASES PASSED: %s \n" %p)
v.write(" NUMBER OF TEST CASES FAILED: %s \n" %x)

			
			
			
			
			
			
			
			
			
			
			
			
			
			
