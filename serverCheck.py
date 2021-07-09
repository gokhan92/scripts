import urllib.request
import subprocess
import sys

# Ports are handled in ~/.ssh/config since we use OpenSSH
command="service sssd status"

listUrl=["http://server1:port","http://server2:port","http://server3:port","http://server4:port","http://server5:port"]


for i in listURL:
    try:
        resp=urllib.request.urlopen(i).getcode()

        if resp == 200:
            print(i+" Server status "+str(resp))
            ssh = subprocess.Popen(["ssh", "%s" % i, command],
                    shell=False,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE)
            result = ssh.stdout.readlines()
            if result == []:
                error = ssh.stderr.readlines()
                print (sys.stderr, "ERROR: %s" % error)
            else:
                print (result)
    except:

        print("An error occurred in the server " + i + " Please check it")

  #check the error 



#You can add following ssh connection to run the remote commands in the if else control flow
"""
ssh = subprocess.Popen(["ssh", "%s" % i, COMMAND],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
result = ssh.stdout.readlines()
if result == []:
    error = ssh.stderr.readlines()
    print (sys.stderr, "ERROR: %s" % error)
else:
    print (result)
 """
