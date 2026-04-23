@echo off
cls

echo.
echo --- OS Info ---
systeminfo | findstr /B /C:"OS Name" /C:"OS Version"
ver

echo.
echo --- Processor Info ---
wmic cpu get name, loadpercentage

echo.
echo --- Address Translation (Virtual Memory) Status ---
systeminfo | find "Virtual Memory"

pause
