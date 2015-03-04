import shlex
from subprocess import Popen, PIPE
import subprocess
import os
def runModule(hostname):
        strCmd = "openssl.exe";
        strArgs = "s_client -connect " + hostname +":443 -cipher EXPORT";
        strFullCmd = "\"" + os.path.dirname(os.path.abspath("__file__"))+"\\"+ strCmd+"\"" +" "+  strArgs;
        
        args = shlex.split(strFullCmd)
        #print("Running Command.......");
        #proc = Popen(args, stdout=PIPE, stderr=PIPE,shell=True);
        #output = str(subprocess.check_output(strFullCmd));
        ps = subprocess.Popen(strFullCmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT);
        output = ps.communicate()[0];   
        #output, err = proc.communicate();
       
        return output;
import sys   
def FreakFilter(output):
    
    if ("alert handshake failure" in str(output)):
        return "Host is Safe";
    else:
        return "Host is Vulnerable";
    

def main():
    output = runModule(sys.argv[1]);
    print(FreakFilter(output));
main();