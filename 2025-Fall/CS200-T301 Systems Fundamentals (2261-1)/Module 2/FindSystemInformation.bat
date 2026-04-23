@ECHO OFF
REM === User Info ===
echo --- User Info ---
whoami

REM === OS Info ===
echo --- OS Info ---
systeminfo | findstr /B /C:"OS Name" /C:"OS Version"
systeminfo | findstr /C:"System Type"
systeminfo | findstr /C:"System Manufacturer" /C:"System Model"

REM === Processor Info ===
echo --- Processor Info ---
wmic cpu get name, loadpercentage

REM === Memory Info ===
echo --- Memory Info ---
systeminfo | findstr /C:"Total Physical Memory"
wmic OS get FreePhysicalMemory,TotalVisibleMemorySize /Format:List
wmic memorychip get capacity

REM === Disk Info ===
echo --- Disk Drives ---
wmic diskdrive get name, model, size
echo --- Logical Drives ---
wmic logicaldisk get name,size,freespace

REM === Video Card Info ===
echo --- Video Card ---
wmic path win32_videocontroller get name

@ECHO OFF
ECHO --- Listing All Connected Input Devices ---
ECHO.

ECHO --- KEYBOARDS ---
WMIC PATH Win32_Keyboard GET Description, DeviceID

ECHO.
ECHO --- MICE AND POINTING DEVICES ---
WMIC PATH Win32_PointingDevice GET Manufacturer, Description, DeviceID

pause
