import paramiko
import shlex
import subprocess

def ssh_command(ip, port, user, passwd, command):
    