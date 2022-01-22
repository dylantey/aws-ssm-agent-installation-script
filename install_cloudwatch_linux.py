import os
import sys

stream = os.popen('cat /etc/os-release | grep ^NAME')
output = stream.read().strip()
if output == 'NAME="SLES"':
  print("OS Version is SLES")
  print("Installing SSM Agent...")
  installAgent = os.popen('sudo zypper -n install amazon-ssm-agent')
  enableService = os.popen('sudo systemctl enable amazon-ssm-agent')
  startService = os.popen('sudo systemctl start amazon-ssm-agent')
  statusService = os.popen('sudo systemctl status amazon-ssm-agent')
  statusServiceOutput = statusService.read().strip()

  checkRunning = os.popen('systemctl status amazon-ssm-agent | grep "Active: active"')
  checkRunningOutput = checkRunning.read().strip()
  if "Active: active" not in checkRunningOutput:
    print("Installation failed!")
    sys.exit()
  elif "Active: active" in checkRunningOutput:
    print("Installation successful!")
  else:
    print("Script error")
    sys.exit()
else:
  print("Error")
