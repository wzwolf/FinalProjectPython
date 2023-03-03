#!/usr/bin/env python3

import shutil
import psutil
import socket
import emails

# warning checks
cpu_usage_percent_warning = 80
disk_usage_percent_warning = 20
disk ="/"
memory_usage_mb_warning = 500
localhost_address_check = "127.0.0.1"

# email settings
sender = "automation@example.com"
recipent = "<username>@example.com"
body = "Please check your system and resolve the issue as soon as possible."

def check_high_cpu_usage(cpu_usage_percent_warning):
    """ CPU usage is over 80%
    return true if cpu is greater than cpu_usage_percent_warning
    return false if cpu is lesser than cpu_usage_percent_warning"""
    cpu_usage = psutil.cpu_percent(1)
    return cpu_usage > cpu_usage_percent_warning

def check_high_disk_usage(disk,disk_usage_percent_warning):
    """ Available disk space is lower than 20%
    return true if disk usage is below warning limit
    return false if disk usage is above warning limit"""
    disk_usage = shutil.disk_usage(disk)
    percent_free = disk_usage.free/disk_usage.total
    return percent_free > disk_usage_percent_warning

def check_high_memory_usage(memory_usage_mb_warning):
    """available memory is less than 500MB"""
    memory_usage = psutil.virtual_memory()
    return memory_usage.available < memory_usage_mb_warning

def check_localhost_issue(localhost_address_check):
    """hostname "localhost" cannot be resolved to "127.0.0.1"""
    localhost = socket.gethostbyname("localhost")
    return localhost != localhost_address_check

def send_error_report(msg):
    """send email """
    email=emails.generate_email(sender,recipent,msg,body,None)
    emails.send_email(email)

if __name__ == "__main__":
    """main function that will email output based on check results"""
    checks = [
        (check_high_cpu_usage,"Error - CPU usage is over 80%", cpu_usage_percent_warning, None),
        (check_high_disk_usage,"Error - Available disk space is less than 20%", disk, disk_usage_percent_warning),
        (check_high_memory_usage,"Error - Available memory is less than 500MB", memory_usage_mb_warning,None),
        (check_localhost_issue,"Error - localhost cannot be resolved to 127.0.0.1", localhost_address_check,None),
        ]
    content = ""
    for check, msg, arg1, arg2 in checks:
        if arg1 == None and arg2 == None:
            if check():
                print(msg)
                send_error_report(msg)
        if arg1 != None and arg2 == None:
            if check(arg1):
                print(msg)
                send_error_report(msg)
        if arg1 != None and arg2 != None:
            if check(arg1, arg2):
                print(msg)
                send_error_report(msg)

    print("server-check is done")

    
        
