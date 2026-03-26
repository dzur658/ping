!macro customInstall
    DetailPrint "Installing Nmap"

    ExecWait '"$INSTDIR\resources\installers\nmap-7.98-setup.exe"'
!macroend

!macro customWelcomePage
  PageEx license
    LicenseText "Important Disclaimer"
    LicenseData "${PROJECT_DIR}\build\disclaimer.txt"
  PageExEnd
!macroend