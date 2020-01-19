# -*- coding: latin-1 -*-

#
#
#
#
#   19_jun_2018   Ver1
#
#   v1_1  - work as a subroutines  24-06-2018
#   v1_2 - added num_lines + Histogram
#   v15 - compiled VCForPython27.msi  required Microsoft Visual C++ Compiler for Python 2.7
#       https://www.microsoft.com/en-us/download/details.aspx?id=44266
#
#   C:\Python27\Scripts>pyinstaller.exe --onefile  V14.py
#
#
#

import time
import calendar
import getopt
import re
import datetime
# from datetime import datetime as dt
# from dateutil.parser import parse
#import pandas as pd
import math
import matplotlib
from pylab import *
#import numpy as np
#import datefinder
#import dateparser
#import re
import os


# ===============================================
#   05/13/2016 15:05:26
test_datetime = '05/13/2016 10:05:26'
datepattern = '%m/%d/%Y %H:%M:%S'
datepattern_1 = '%Y-%m-%d %H:%M:%S'

utc_epoch = calendar.timegm(time.strptime(test_datetime, datepattern))


# print test_datetime
# print utc_epoch
# ===============================================





# def uptime_analyses(array_uptime):
#    for line in array_uptime:
# match = re.search('\d{4}-\d{2}-\d{2}', line)

#        print (line)
#       if "Disk soft media error" not in line:
#           array_b.append(line)
# file_out2.write(line)


# ===============================================
#
#     write_analyses_file(name):
#
# ===============================================
def write_analyses_file(name):
    print " write_analyses_file  write to file " + name
#    file_name = open('{}.txt'.format(name), 'w')
    ii = 0
    rs_name =  name.strip('\n')
    file_name = open( Unity_Parsed_Log + rs_name  + '.txt', 'w')
    for line in array_a:
        # array.append(line)
        if rs_name in line:
            ii = ii +1
            file_name.write(line)

    file_name = close('{}.txt'.format(name))
    """

    testing

    print " write ---> " + name, ii
    file_array_a = open('array_a', 'w')

    for line in array_a:
        file_array_a.write(line)

    exit(0)
    """
# ===============================================

# ===============================================
#
#     Plot_analyses_file(name):
#
# ===============================================
def plot_analyses_file(name):
    file_name = open('{}.txt'.format(name), 'w')

    for line in array_a:
        # array.append(line)
        if name in line:
            file_name.write(line)


# ===============================================

# ===============================================
#
#     Clean_log
#
# =============================================
def clean_log(name):
    global array_shorten
    global array_b
    i_clean = 0
    array_shorten = array_b
    array_b = []

    rs_name = name.strip('\n')

    for line in array_shorten:
        # array.append(line)
        i_clean = i_clean + 1
        if rs_name not in line:
            array_b.append(line)
            #file_out2.write(line)
    print "   cleaned --> " + name, i_clean

# =============================================

# ===============================================
file_in = open('TRiiAGE_SPlogs.txt', 'r')
# ===============================================

Log_parsing_Config_dir = 'Unity_Log_parsing_Config\\'

Unity_Parsed_Log_dir = 'Unity_Parsed_Log'
if not os.path.exists(Unity_Parsed_Log_dir):
    os.makedirs(Unity_Parsed_Log_dir)


Unity_Parsed_Log = 'Unity_Parsed_Log\\'

file_Delete = open(Log_parsing_Config_dir + 'Delete_List.txt', 'r')
file_Parse = open(Log_parsing_Config_dir + 'Parse_List.txt', 'r')
# ===============================================
#file_array_alive = open('TRiiAGE_SPlogs_f.txt', 'w')
# ===============================================
#file_disk_softmedia = open('disk_softmedia.txt', 'w')
# ===============================================
file_out2 = open('TRiiAGE_SPlogs_filtered.txt', 'w')
# ===============================================
# file_cache = open('cache.txt', 'w')
# ===============================================


# =============================================

print "  open files "

file_Log_parsing = open(Unity_Parsed_Log + 'Log_parsing_process.txt', 'w')
file_Log_parsing.write(" " + '\n')
file_Log_parsing.write(" " + '\n')
file_Log_parsing.write(" " + '\n')
n_start = datetime.datetime.now()
file_Log_parsing.write("   Log parsing Start time:   %s" % n_start)
file_Log_parsing.write(" " + '\n')
file_Log_parsing.write(" " + '\n')
# =============================================
#
#   write files
#   feel arrays
#
# =============================================
array_a = []
line_time = []
array_b = []
# array_uptime = []
num_lines = 0

#   @@@@@@@@@@@@@@@@@@@@@@

date_new = ""
date_old = ""

Delete_list = []
Parse_List = []

# =============================================
#
#   delete / parse  read
#
# =============================================

for line in file_Delete:
    Delete_list.append(line)
    num_lines = num_lines + 1


for line in file_Parse:
    Parse_List.append(line)
    num_lines = num_lines + 1


# =============================================
#
#  END  delete / parse  read
#
# =============================================

for line in file_in:
    array_b.append(line)
    date_old = date_new
    #    matches = list(datefinder.find_dates(line))
    #    date = matches[0]
    #    print date

    #    utc_epoch = calendar.timegm(time.strptime(test_datetime, datepattern))

    #    print " line", num_lines, " date ", date, " old ", date_old, " new ", date_new, " d ",d
    num_lines = num_lines + 1

    # file_out.write(line)
# =============================================
#   numbering from 0 to end ...
# =============================================
num_lines = num_lines - 2

# =============================================

# =============================================
array_a = array_b
# =============================================

for line in array_a:
    # array.append(line)
    if "The array is alive" in line:
        file_array_alive.write(line)
# =============================================
#
#       Disk soft media error  & Soft SCSI Bus Error
#
#        zerodisk
#
# =============================================

for line in array_a:
    # array.append(line)
    if "Disk soft media error" in line:
        file_disk_softmedia.write(line)
    if "Soft SCSI Bus Error" in line:
        file_disk_softmedia.write(line)
    if "zerodisk" in line:
        file_disk_softmedia.write(line)
# =============================================
# =============================================

for line in array_a:
    # array.append(line)
    if "Unit Shutdown for Trespass" in line:
        file_disk_softmedia.write(line)
# =============================================
#
#       cache
#
# =============================================
"""
file_cache = open('cache.txt', 'w')

for line in array_a:
    # array.append(line)
    if "Cache" in line:
        file_cache.write(line)
    if "cache" in line:
        file_cache.write(line)

"""
# =============================================
#
#       Power & Battery & SPS
#
# =============================================
"""
file_Power = open('Power.txt', 'w')

for line in array_a:
    # array.append(line)
    if "Power" in line:
        file_Power.write(line)
    if "Battery" in line:
        file_Power.write(line)
    if "SPS" in line:
        file_Power.write(line)
"""

# =============================================
# =============================================
# =============================================
#
#   Psrsing LOG
#
# =============================================
# =============================================


for line in Parse_List:
    print " write_analyses_file " + line
    write_analyses_file(line)

"""

# uptime_analyses(array_uptime)
write_analyses_file("LUN")
write_analyses_file("oldest archive file")
write_analyses_file("Trespass")
write_analyses_file("snapshot")
write_analyses_file("The system uptime")
write_analyses_file("Relocation")
write_analyses_file("Time Synchronization")

 """
# =============================================
# =============================================
#
#   Cleaning LOG
#
# =============================================
# =============================================


array_b = array_a

for line in Delete_list:
    print " delete --> "  + line
    clean_log(line)

'''
clean_log("Authentication session")
clean_log("Authentication successful")
clean_log("Operation Create Replica")
clean_log("has received a notification")
clean_log("Operation Evacuate Slices")
clean_log("System: Lun:")
clean_log("System: CBFS")
clean_log("System: file mode")
clean_log("System: Operation")
clean_log("Unit Shutdown for Trespass")
clean_log("MiddleRedirector")
clean_log("called by")
clean_log("Microsoft-Windows-Security-Audit")
clean_log("Microsoft-Windows-Kernel-General")
clean_log("Microsoft-Windows-User Profiles")
clean_log("NTP Time Synchronization")
clean_log("Audit Logging Service")
clean_log("Service Control Manager")
clean_log("SSH connection")
clean_log("Power")
clean_log("Battery")
clean_log("SPS")
clean_log("Relocation")
clean_log("relocation")
clean_log("uptime")
clean_log("Informational message")
clean_log("The array is alive")
clean_log("Rule exec")
clean_log("LUN")
clean_log("oldest archive file was deleted")
clean_log("Trespass")
clean_log("snapshot")
clean_log("Disk soft media error")
clean_log("CRU Ready")
clean_log("Soft SCSI Bus Error")
clean_log("Cache")
clean_log("cache")
clean_log("Unit Shutdown for Trespass")
clean_log("Soft Media Error")
clean_log("Sector Reconstructed")

'''

# =============================================
#
#   write result file
#
# =============================================

for line in array_b:
    file_out2.write(line)

# =============================================


# =============================================
file_Log_parsing.write(" " + '\n')
file_Log_parsing.write(" " + '\n')
file_Log_parsing.write(" IASYNB " + '\n')
file_Log_parsing.write(" Unity log parsing tool " + '\n')
file_Log_parsing.write(" Ver-03 " + '\n')
file_Log_parsing.write(" " + '\n')

n_end = datetime.datetime.now()
file_Log_parsing.write("   Log parsing End time:   %s" % n_end)
file_Log_parsing.write(" " + '\n')

n_delta = n_end - n_start

file_Log_parsing.write("   Log parsing delta:   %s" % n_delta)
file_Log_parsing.write(" " + '\n')
file_Log_parsing.write(" " + '\n')
file_Log_parsing.write("  Lines in LOG %s " % num_lines + '\n')
file_Log_parsing.write(" " + '\n')
file_Log_parsing.write(" " + '\n')
file_Log_parsing.write("  line 1  %s" % array_a[0])
file_Log_parsing.write("  line  %s" % num_lines)
file_Log_parsing.write(" " + '\n')
file_Log_parsing.write(" " + '\n')
file_Log_parsing.write("   Log parsing End time:   %s" % n_end)
#file_Log_parsing.write("  last line   %s" % array_a[num_lines])

# file_Log_parsing.write("  line  %s" %num_lines %array_a[num_lines-1])
# =============================================

# =============================================
#  simple histogram
# =============================================
# hist(randn(10000), bins=30)
# show()
# =============================================



# from pylab import *

file_in.close()
#file_out.close()
