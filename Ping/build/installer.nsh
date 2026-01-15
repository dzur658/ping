!macro customInstall
    DetailPrint "Installing Nmap"

    ExecWait '"$INSTDIR\resources\installers\nmap-7.98-setup.exe"'
!macroend