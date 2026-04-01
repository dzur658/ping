!macro customInstall
    DetailPrint "Installing Nmap"

    ExecWait '"$INSTDIR\resources\installers\nmap-7.98-setup.exe"'
!macroend

!macro customWelcomePage
  PageEx license
    LicenseText "AI Disclaimer" "Please review the following important informationbefore installing Ping."
    LicenseData "${PROJECT_DIR}\build\disclaimer.txt"
  PageExEnd
!macroend