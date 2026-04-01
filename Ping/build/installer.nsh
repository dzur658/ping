!macro customInstall
    DetailPrint "Installing Nmap"

    ExecWait '"$INSTDIR\resources\installers\nmap-7.98-setup.exe"'
!macroend

!macro customWelcomePage
  !define MUI_WELCOMEPAGE_TITLE "AI Disclaimer"
  !define MUI_WELCOMEPAGE_TEXT "Please review the following important information before installing Ping."
  PageEx license
    LicenseText "If you accept the terms of the agreement, click I Agree to continue. You must accept the agreement to install Ping."
    LicenseData "${PROJECT_DIR}\build\disclaimer.txt"
  PageExEnd
!macroend