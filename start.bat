@echo off
taskkill /IM acs* /F
taskkill /IM py.exe /F
taskkill /IM python.exe /F
start updateHD.py
start updateSEMS.py
