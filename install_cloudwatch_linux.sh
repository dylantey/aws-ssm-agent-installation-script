#!/bin/sh
  
osVersion=$(cat /etc/os-release | grep ^NAME)

if [[ "$osVersion" == "NAME=\"SLES\"" ]]; then
  echo "OS: SLES"
  echo "Installing SSM Agent..."
  sudo zypper -n install amazon-ssm-agent > /dev/null 2>&1
  sudo systemctl enable amazon-ssm-agent > /dev/null 2>&1
  echo "Starting SSM Agent..."
  sudo systemctl start amazon-ssm-agent > /dev/null 2>&1

  agentStatus=$(sudo systemctl status amazon-ssm-agent | grep Active)
  if [[ "$agentStatus" == *"Active: active (running)"* ]]; then
    echo "Installation successfully!"
  elif [[ "$agentStatus" == *"Active: inactive"* ]]; then
    echo "Installation failed!"
    exit 1
  else
    echo "Script error"
  fi
else
  echo "Unsupported OS version"
fi
