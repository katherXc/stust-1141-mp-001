#!/usr/bin/env python3
print('Hello world')

import psutil

cpu_percent = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu_percent}%")

mem = psutil.virtual_memory()
print(f"Total Memory: {mem.total / (1024**3):.2f} GB")
print(f"Used Memory: {mem.used / (1024**3):.2f} GB")
print(f"Memory Usage: {mem.percent}%")

disk = psutil.disk_usage('/')
print(f"Total Disk Space: {disk.total / (1024**3):.2f} GB")
print(f"Used Disk Space: {disk.used / (1024**3):.2f} GB")
print(f"Disk Usage: {disk.percent}%")

