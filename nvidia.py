import os

os.system('clear')

driver = input("Do you want to install legacy NVIDIA drivers? (Y/n): ").strip().lower()

if driver in ["y", "Y", "yes", "Yes"]:
    os.system('sh apt-sid.sh')
    os.system('systemctl reboot')
elif driver in ["n", "N", "no", "No"]:
    os.system('systemctl reboot')
else:
    os.system('sh apt-sid.sh')
    os.system('systemctl reboot')

exit()
