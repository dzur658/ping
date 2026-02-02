You have received the following report for a device with security issues. Walk the user through step-by-step on how to fix them. Provide clear instructions in a friendly format.

Remember:
- Do not use words like "vulnerability," "malicious," "firmware," or "credentials."
- Ensure all IP addresses are formatted as clickable links if the device would likely have a web interface. For example, most routers have web interfaces so in that case a router would be written like so: <a href="http://192.168.1.1">[HOSTNAME]</a>.
- Do not suggest specific examples for passwords or PINs.

## Device Scan Report
The mac vendor has been identified by nmap as: LG Innotek
The hostname has been identified by nmap as: ["LGwebOSTV.localdomain"]
You should refer to the device in your report using the hostname.
IP Address: 192.168.100.10
Nmap has inferred the OS of the device to most likely be: [{"name": "Linux 4.15 - 5.19", "accuracy": "100"}, {"name": "OpenWrt 21.02 (Linux 5.4)", "accuracy": "100"}, {"name": "MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3)", "accuracy": "100"}, {"name": "Linux 4.15 - 5.19", "accuracy": "100"}, {"name": "OpenWrt 21.02 (Linux 5.4)", "accuracy": "100"}, {"name": "MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3)", "accuracy": "100"}, {"name": "Linux 4.15 - 5.19", "accuracy": "100"}, {"name": "OpenWrt 21.02 (Linux 5.4)", "accuracy": "100"}, {"name": "MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3)", "accuracy": "100"}]
The following services have been identified on the device:
<services>
  
  <service>
    - Service ID: 6.0
    - Port Number: 515.0
    - Protocol: tcp
    - State: open
    - Service Name: tcpwrapped
    - Service Product (if applicable): 
    - Service Version (if applicable): 
  </service>

  
  <service>
    - Service ID: 7.0
    - Port Number: 1174.0
    - Protocol: tcp
    - State: open
    - Service Name: upnp
    - Service Product (if applicable): LG WebOS TV upnpd
    - Service Version (if applicable): 
  </service>

  
  <service>
    - Service ID: 8.0
    - Port Number: 1186.0
    - Protocol: tcp
    - State: open
    - Service Name: upnp
    - Service Product (if applicable): Platinum unpnd
    - Service Version (if applicable): 1.0.4.9
  </service>

  
  <service>
    - Service ID: 9.0
    - Port Number: 2030.0
    - Protocol: tcp
    - State: open
    - Service Name: upnp
    - Service Product (if applicable): Platinum unpnd
    - Service Version (if applicable): 1.0.4.9
  </service>

  
  <service>
    - Service ID: 10.0
    - Port Number: 3000.0
    - Protocol: tcp
    - State: open
    - Service Name: tcpwrapped
    - Service Product (if applicable): 
    - Service Version (if applicable): 
  </service>

  
  <service>
    - Service ID: 11.0
    - Port Number: 3001.0
    - Protocol: tcp
    - State: open
    - Service Name: http
    - Service Product (if applicable): LG smart TV http service
    - Service Version (if applicable): 
  </service>

  
  <service>
    - Service ID: 12.0
    - Port Number: 7000.0
    - Protocol: tcp
    - State: open
    - Service Name: rtsp
    - Service Product (if applicable): AirTunes rtspd
    - Service Version (if applicable): 377.40.00
  </service>

  
  <service>
    - Service ID: 13.0
    - Port Number: 8008.0
    - Protocol: tcp
    - State: open
    - Service Name: http
    - Service Product (if applicable): 
    - Service Version (if applicable): 
  </service>

  
  <service>
    - Service ID: 14.0
    - Port Number: 8009.0
    - Protocol: tcp
    - State: open
    - Service Name: ajp13
    - Service Product (if applicable): 
    - Service Version (if applicable): 
  </service>

  
  <service>
    - Service ID: 15.0
    - Port Number: 8443.0
    - Protocol: tcp
    - State: open
    - Service Name: https-alt
    - Service Product (if applicable): 
    - Service Version (if applicable): 
  </service>

  
  <service>
    - Service ID: 16.0
    - Port Number: 9080.0
    - Protocol: tcp
    - State: open
    - Service Name: glrpc
    - Service Product (if applicable): 
    - Service Version (if applicable): 
  </service>

  
</services>

The following vulnerabilities have been identified on the device:
<vulnerabilities>
  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-1999-0316
    - Vulnerability Description: Buffer overflow in Linux splitvt command gives root access to local users.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-1999-0470
    - Vulnerability Description: A weak encryption algorithm is used for passwords in Novell Remote.NLM, allowing them to be easily decrypted.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-1999-0476
    - Vulnerability Description: A weak encryption algorithm is used for passwords in SCO TermVision, allowing them to be easily decrypted by a local user.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-1999-1353
    - Vulnerability Description: Nosque MsgCore 2.14 stores passwords in cleartext: (1) the administrator password in the AdmPasswd registry key, and (2) user passwords in the Userbase.dbf data file, which could allow local users to gain privielges.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-1999-1495
    - Vulnerability Description: xtvscreen in SuSE Linux 6.0 allows local users to overwrite arbitrary files via a symlink attack on the pic000.pnm file.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-1999-1576
    - Vulnerability Description: Buffer overflow in Adobe Acrobat ActiveX control (pdf.ocx, PDF.PdfCtrl.1) 1.3.188 for Acrobat Reader 4.0 allows remote attackers to execute arbitrary code via the pdf.setview method.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-0082
    - Vulnerability Description: WebTV email client allows remote attackers to force the client to send email without the user's knowledge via HTML.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-0467
    - Vulnerability Description: Buffer overflow in Linux splitvt 1.6.3 and earlier allows local users to gain root privileges via a long password in the screen locking function.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-0830
    - Vulnerability Description: annclist.exe in webTV for Windows allows remote attackers to cause a denial of service by via a large, malformed UDP packet to ports 22701 through 22705.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-0991
    - Vulnerability Description: Buffer overflow in Hilgraeve, Inc. HyperTerminal client on Windows 98, ME, and 2000 allows remote attackers to execute arbitrary commands via a long telnet URL, aka the "HyperTerminal Buffer Overflow" vulnerability.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-1022
    - Vulnerability Description: The mailguard feature in Cisco Secure PIX Firewall 5.2(2) and earlier does not properly restrict access to SMTP commands, which allows remote attackers to execute restricted commands by sending a DATA command before sending the restricted commands.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0111
    - Vulnerability Description: Format string vulnerability in splitvt before 1.6.5 allows local users to execute arbitrary commands via the -rcfile command line argument.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0112
    - Vulnerability Description: Multiple buffer overflows in splitvt before 1.6.5 allow local users to execute arbitrary commands.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0552
    - Vulnerability Description: ovactiond in HP OpenView Network Node Manager (NNM) 6.1 and Tivoli Netview 5.x and 6.x allows remote attackers to execute arbitrary commands via shell metacharacters in a certain SNMP trap message.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0782
    - Vulnerability Description: KDE ktvision 0.1.1-271 and earlier allows local attackers to gain root privileges via a symlink attack on a user configuration file.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-1272
    - Vulnerability Description: wmtv 0.6.5 and earlier does not properly drop privileges, which allows local users to execute arbitrary commands via the -e (external command) option.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0011
    - Vulnerability Description: Information leak in doeditvotes.cgi in Bugzilla before 2.14.1 may allow remote attackers to more easily conduct attacks on the login.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0059
    - Vulnerability Description: The decompression algorithm in zlib 1.1.3 and earlier, as used in many different utilities and packages, causes inflateEnd to release certain memory more than once (a "double free"), which may allow local and remote attackers to execute arbitrary code via a block of malformed compression data.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0209
    - Vulnerability Description: Nortel Alteon ACEdirector WebOS 9.0, with the Server Load Balancing (SLB) and Cookie-Based Persistence features enabled, allows remote attackers to determine the real IP address of a web server with a half-closed session, which causes ACEdirector to send packets from the server without changing the address to the virtual IP address.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0247
    - Vulnerability Description: Buffer overflows in wmtv 0.6.5 and earlier may allow local users to gain privileges.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0248
    - Vulnerability Description: wmtv 0.6.5 and earlier allows local users to modify arbitrary files via a symlink attack on a configuration file.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0460
    - Vulnerability Description: Bitvise WinSSHD before 2002-03-16 allows remote attackers to cause a denial of service (resource exhaustion) via a large number of incomplete connections that are not properly terminated, which are not properly freed by SSHd.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0491
    - Vulnerability Description: admin.php in AlGuest 1.0 guestbook checks for the existence of the admin cookie to authenticate the AlGuest administrator, which allows remote attackers to bypass the authentication and gain privileges by setting the admin cookie to an arbitrary value.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0631
    - Vulnerability Description: Unknown vulnerability in nveventd in NetVisualyzer on SGI IRIX 6.5 through 6.5.16 allows local users to write arbitrary files and gain root privileges.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0838
    - Vulnerability Description: Buffer overflow in (1) gv 3.5.8 and earlier, (2) gvv 1.0.2 and earlier, (3) ggv 1.99.90 and earlier, (4) gnome-gv, and (5) kghostview in kdegraphics 2.2.2 and earlier, allows attackers to execute arbitrary code via a malformed (a) PDF or (b) PostScript file, which is processed by an unsafe call to sscanf.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0862
    - Vulnerability Description: The (1) CertGetCertificateChain, (2) CertVerifyCertificateChainPolicy, and (3) WinVerifyTrust APIs within the CryptoAPI for Microsoft products including Microsoft Windows 98 through XP, Office for Mac, Internet Explorer for Mac, and Outlook Express for Mac, do not properly verify the Basic Constraints of intermediate CA-signed X.509 certificates, which allows remote attackers to spoof the certificates of trusted sites via a man-in-the-middle attack for SSL sessions, as originally reported for Internet Explorer and IIS.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0954
    - Vulnerability Description: The encryption algorithms for enable and passwd commands on Cisco PIX Firewall can be executed quickly due to a limited number of rounds, which make it easier for an attacker to decrypt the passwords using brute force techniques.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0971
    - Vulnerability Description: Vulnerability in VNC, TightVNC, and TridiaVNC allows local users to execute arbitrary code as LocalSystem by using the Win32 Messaging System to bypass the VNC GUI and access the "Add new clients" dialogue box.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1154
    - Vulnerability Description: anlgform.pl in Analog before 5.23 does not restrict access to the PROGRESSFREQ progress update command, which allows remote attackers to cause a denial of service (disk consumption) by using the command to report updates more frequently and fill the web server error log.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1187
    - Vulnerability Description: Cross-site scripting vulnerability (XSS) in Internet Explorer 5.01 through 6.0 allows remote attackers to read and execute files on the local system via web pages using the <frame> or <iframe> element and javascript, aka "Frames Cross Site Scripting," as demonstrated using the PrivacyPolicy.dlg resource.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1223
    - Vulnerability Description: Buffer overflow in DSC 3.0 parser from GSview, as used in KGhostView in KDE 1.1 and KDE 3.0.3a, may allow attackers to cause a denial of service or execute arbitrary code via a modified .ps (PostScript) input file.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1336
    - Vulnerability Description: TightVNC before 1.2.6 generates the same challenge string for multiple connections, which allows remote attackers to bypass VNC authentication by sniffing the challenge and response of other users.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1493
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in Lycos HTMLGear guestbook allows remote attackers to inject arbitrary script via (1) STYLE attributes or (2) SRC attributes in an IMG tag.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1572
    - Vulnerability Description: Signed integer overflow in the bttv_read function in the bttv driver (bttv-driver.c) in Linux kernel before 2.4.20 has unknown impact and attack vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1697
    - Vulnerability Description: Electronic Code Book (ECB) mode in VTun 2.0 through 2.5 uses a weak encryption algorithm that produces the same ciphertext from the same plaintext blocks, which could allow remote attackers to gain senstive information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1739
    - Vulnerability Description: Alt-N Technologies Mdaemon 5.0 through 5.0.6 uses a weak encryption algorithm to store user passwords, which allows local users to crack passwords.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1848
    - Vulnerability Description: TightVNC before 1.2.4 running on Windows stores unencrypted passwords in the password text control of the WinVNC Properties dialog, which could allow local users to access passwords.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1910
    - Vulnerability Description: Click2Learn Ingenium Learning Management System 5.1 and 6.1 uses weak encryption for passwords (reversible algorithm), which allows attackers to obtain passwords.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-2018
    - Vulnerability Description: sastcpd in SAS/Base 8.0 might allow local users to gain privileges by setting the netencralg environment variable, which causes a segmentation fault.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-2401
    - Vulnerability Description: NT Virtual DOS Machine (NTVDM.EXE) in Windows 2000, NT and XP does not verify user execution permissions for 16-bit executable files, which allows local users to bypass the loader and execute arbitrary programs.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-0032
    - Vulnerability Description: Memory leak in libmcrypt before 2.5.5 allows attackers to cause a denial of service (memory exhaustion) via a large number of requests to the application, which causes libmcrypt to dynamically load algorithms via libtool.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-0036
    - Vulnerability Description: ml85p, as included in the printer-drivers package for Mandrake Linux, allows local users to overwrite arbitrary files via a symlink attack on temporary files with predictable filenames of the form "mlg85p%d".
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-0141
    - Vulnerability Description: The PNG deflate algorithm in RealOne Player 6.0.11.x and earlier, RealPlayer 8/RealPlayer Plus 8 6.0.9.584, and other versions allows remote attackers to corrupt the heap and overwrite arbitrary memory via a PNG graphic file format containing compressed data using fixed trees that contain the length values 286-287, which are treated as a very large length.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-0147
    - Vulnerability Description: OpenSSL does not use RSA blinding by default, which allows local and remote attackers to obtain the server's private key by determining factors using timing differences on (1) the number of extra reductions during Montgomery reduction, and (2) the use of different integer multiplication algorithms ("Karatsuba" and normal).
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-0204
    - Vulnerability Description: KDE 2 and KDE 3.1.1 and earlier 3.x versions allows attackers to execute arbitrary commands via (1) PostScript (PS) or (2) PDF files, related to missing -dPARANOIDSAFER and -dSAFER arguments when using the kghostview Ghostscript viewer.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-0350
    - Vulnerability Description: The control for listing accessibility options in the Accessibility Utility Manager on Windows 2000 (ListView) does not properly handle Windows messages, which allows local users to execute arbitrary code via a "Shatter" style message to the Utility Manager that references a user-controlled callback function.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-0356
    - Vulnerability Description: Multiple off-by-one vulnerabilities in Ethereal 0.9.11 and earlier allow remote attackers to cause a denial of service and possibly execute arbitrary code via the (1) AIM, (2) GIOP Gryphon, (3) OSPF, (4) PPTP, (5) Quake, (6) Quake2, (7) Quake3, (8) Rsync, (9) SMB, (10) SMPP, and (11) TSP dissectors, which do not properly use the tvb_get_nstringz and tvb_get_nstringz0 functions.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-0431
    - Vulnerability Description: The tvb_get_nstringz0 function in Ethereal 0.9.12 and earlier does not properly handle a zero-length buffer size, with unknown consequences.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-0522
    - Vulnerability Description: Multiple SQL injection vulnerabilities in ProductCart 1.5 through 2 allow remote attackers to (1) gain access to the admin control panel via the idadmin parameter to login.asp or (2) gain other privileges via the Email parameter to Custva.asp.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-0692
    - Vulnerability Description: KDM in KDE 3.1.3 and earlier uses a weak session cookie generation algorithm that does not provide 128 bits of entropy, which allows attackers to guess session cookies via brute force methods and gain access to the user session.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-0885
    - Vulnerability Description: Xscreensaver 4.14 contains certain debugging code that should have been omitted, which causes Xscreensaver to create temporary files insecurely in the (1) apple2, (2) xanalogtv, and (3) pong screensavers, and allows local users to overwrite arbitrary files via a symlink attack.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-0971
    - Vulnerability Description: GnuPG (GPG) 1.0.2, and other versions up to 1.2.3, creates ElGamal type 20 (sign+encrypt) keys using the same key component for encryption as for signing, which allows attackers to determine the private key from a signature.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-1334
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in Kai Blankenhorn Bitfolge simple and nice index file (aka snif) before 1.2.7 allows remote attackers to inject arbitrary web script or HTML via unspecified vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-1335
    - Vulnerability Description: Directory traversal vulnerability in Kai Blankenhorn Bitfolge simple and nice index file (aka snif) before 1.2.5 allows remote attackers to download files from locations above the snif directory.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-1342
    - Vulnerability Description: Trend Micro Virus Control System (TVCS) 1.8 running with IIS allows remote attackers to cause a denial of service (memory consumption) in IIS via multiple URL requests for ActiveSupport.exe.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-1344
    - Vulnerability Description: Trend Micro Virus Control System (TVCS) Log Collector allows remote attackers to obtain usernames, encrypted passwords, and other sensitive information via a URL request for getservers.exe with the action parameter set to "selects1", which returns log files.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-1391
    - Vulnerability Description: RTS CryptoBuddy 1.0 and 1.2 uses a weak encryption algorithm for the passphrase and generates predictable keys, which makes it easier for attackers to guess the passphrase.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-1447
    - Vulnerability Description: IBM WebSphere Advanced Server Edition 4.0.4 uses a weak encryption algorithm (XOR and base64 encoding), which allows local users to decrypt passwords when the configuration file is exported to XML.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-1480
    - Vulnerability Description: MySQL 3.20 through 4.1.0 uses a weak algorithm for hashed passwords, which makes it easier for attackers to decrypt the password via brute force methods.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-1483
    - Vulnerability Description: FlashFXP 1.4 uses a weak encryption algorithm for user passwords, which allows attackers to decrypt the passwords and gain access.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-0395
    - Vulnerability Description: The xatitv program in the gatos package does not properly drop root privileges when the configuration file does not exist, which allows local users to execute arbitrary commands via shell metacharacters in a system call.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-0459
    - Vulnerability Description: The Clear Channel Assessment (CCA) algorithm in the IEEE 802.11 wireless protocol, when using DSSS transmission encoding, allows remote attackers to cause a denial of service via a certain RF signal that causes a channel to appear busy (aka "jabber"), which prevents devices from transmitting data.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-0705
    - Vulnerability Description: Multiple cross-site scripting (XSS) vulnerabilities in (1) editcomponents.cgi, (2) editgroups.cgi, (3) editmilestones.cgi, (4) editproducts.cgi, (5) editusers.cgi, and (6) editversions.cgi in Bugzilla 2.16.x before 2.16.6, and 2.18 before 2.18rc1, allow remote attackers to execute arbitrary JavaScript as other users via a URL parameter.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-0766
    - Vulnerability Description: NGSEC StackDefender 2.0 allows attackers to cause a denial of service (system crash) via an invalid address for the BaseAddress parameter to the hooks for the (1) ZwAllocateVirtualMemory or (2) ZwProtectVirtualMemory functions.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-1113
    - Vulnerability Description: SQL injection vulnerability in SQLgrey Postfix greylisting service before 1.2.0 allows remote attackers to execute arbitrary SQL commands via the (1) sender or (2) recipient e-mail addresses.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-1280
    - Vulnerability Description: The gui_popup_view_fly function in gui_tview_popup.c for junkie 0.3.1 allows remote malicious FTP servers to execute arbitrary commands via shell metacharacters in a filename.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-1717
    - Vulnerability Description: Multiple buffer overflows in the psscan function in ps.c for gv (ghostview) allow remote attackers to execute arbitrary code via a Postscript file with a long (1) BoundingBox, (2) comment, (3) Orientation, (4) PageOrder, or (5) Pages value.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-1779
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in board.php for ThWboard before beta 2.84 allows remote attackers to inject arbitrary web script or HTML via the lastvisited parameter.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-1860
    - Vulnerability Description: Buffer overflow in Check Point SmartDashboard in Check Point NG AI R54 and R55 allows remote authenticated users to cause a denial of service (server disconnect) and possibly execute arbitrary code via a large filter on a column when using SmartView Tracker.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-1861
    - Vulnerability Description: Invision NetSupport School Pro uses a weak encryption algorithm to encrypt passwords, which allows local users to obtain passwords.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2007
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in modules.php in NukeJokes 1.7 and 2 Beta allows remote attackers to inject arbitrary HTML or web script via the (1) cat parameter in a CatView function or (2) jokeid parameter in a JokeView function.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2009
    - Vulnerability Description: NukeJokes 1.7 and 2 Beta allows remote attackers to obtain the full path of the server via (1) a direct call to mainfunctions.php, (2) an invalid jokeid parameter in a JokeView function or (3) an invalid cat parameter in a CatView function, which reveals the path in a PHP error message.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2134
    - Vulnerability Description: Oracle toplink mapping workBench uses a weak encryption algorithm for passwords, which allows local users to decrypt the passwords.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2138
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in AWSguest.php in AllWebScripts MySQLGuest allows remote attackers to inject arbitrary HTML and PHP code via the (1) Name, (2) Email, (3) Homepage or (4) Comments field.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2174
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in Custva.asp in EarlyImpact ProductCart allows remote attackers to inject arbitrary Javascript via the redirectUrl parameter.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2551
    - Vulnerability Description: Multiple SQL injection vulnerabilities in Layton HelpBox 3.0.1 allow remote attackers to execute arbitrary SQL commands via (1) the sys_comment_id parameter in editcommentenduser.asp, (2) the sys_suspend_id parameter in editsuspensionuser.asp, (3) the table parameter in export_data.asp, (4) the sys_analgroup parameter in manageanalgrouppreference.asp, (5) the sys_asset_id parameter in quickinfoassetrequests.asp, (6) the sys_eusername parameter in quickinfoenduserrequests.asp, and the sys_request_id parameter in (7) requestauditlog.asp, (8) requestcommentsenduser.asp, (9) selectrequestapplytemplate.asp, and (10) selectrequestlink.asp, resulting in an ability to create a new HelpBox user account and read, modify, or delete data from the backend database.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2682
    - Vulnerability Description: PeerSec MatrixSSL before 1.1 does not implement RSA blinding, which allows context-dependent attackers to obtain the server's private key by determining factors using timing differences on (1) the number of extra reductions during Montgomery reduction, and (2) the use of different integer multiplication algorithms ("Karatsuba" and normal), a related issue to CVE-2003-0147.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2686
    - Vulnerability Description: Directory traversal vulnerability in the vfs_getvfssw function in Solaris 2.6, 7, 8, and 9 allows local users to load arbitrary kernel modules via crafted (1) mount or (2) sysfs system calls.  NOTE: this might be the same issue as CVE-2004-1767, but there are insufficient details to be sure.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2761
    - Vulnerability Description: The MD5 Message-Digest Algorithm is not collision resistant, which makes it easier for context-dependent attackers to conduct spoofing attacks, as demonstrated by attacks on the use of MD5 in the signature algorithm of an X.509 certificate.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-0016
    - Vulnerability Description: Buffer overflow in the exported_display function in xatitv in gatos before 0.0.5 allows local users to execute arbitrary code.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-0661
    - Vulnerability Description: SQL injection vulnerability in the getwbbuserdata function in session.php for Woltlab Burning Board 2.0.3 through 2.3.0 allows remote attackers to execute arbitrary SQL commands via the (1) userid or (2) lastvisit cookie.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-1009
    - Vulnerability Description: Multiple buffer overflows in BakBone NetVault 6.x and 7.x allow (1) remote attackers to execute arbitrary code via a modified computer name and length that leads to a heap-based buffer overflow, or (2) local users to execute arbitrary code via a long Name entry in the configure.cfg file.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-1132
    - Vulnerability Description: LG U8120 mobile phone allows remote attackers to cause a denial of service (device crash) via a malformed MIDI file.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-1372
    - Vulnerability Description: nvstatsmngr.exe process in BakBone NetVault 7.1 does not properly drop privileges before opening files, which allows local users to gain privileges via the Help menu.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-1480
    - Vulnerability Description: Directory traversal vulnerability in RaidenFTPD before 2.4.2241 allows remote attackers to read arbitrary files via a "..\\" (dot dot backslash) in the urlget site command.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-1547
    - Vulnerability Description: Heap-based buffer overflow in the demo version of Bakbone Netvault, and possibly other versions, allows remote attackers to execute arbitrary commands via a large packet to port 20031.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-1600
    - Vulnerability Description: A "mathematical flaw" in the implementation of the El Gamal signature algorithm for LibTomCrypt 1.0 to 1.0.2 allows attackers to generate valid signatures without having the private key.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-1865
    - Vulnerability Description: Multiple SQL injection vulnerabilities in Calendarix Advanced 1.5 allow remote attackers to execute arbitrary SQL commands via the catview parameter to (1) cal_week.php, (2) cal_cat.php, or (3) cal_day.php, or (4) id parameter to cal_pophols.php.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-2359
    - Vulnerability Description: The AES-XCBC-MAC algorithm in IPsec in FreeBSD 5.3 and 5.4, when used for authentication without other encryption, uses a constant key instead of the one that was assigned by the system administrator, which can allow remote attackers to spoof packets to establish an IPsec session.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-2455
    - Vulnerability Description: Greasemonkey before 0.3.5 allows remote web servers to (1) read arbitrary files via a GET request to a file:// URL in the GM_xmlhttpRequest API function, (2) list installed scripts using GM_scripts, or obtain sensitive information via (3) GM_setValue and GM_getValue.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-2506
    - Vulnerability Description: Algorithmic complexity vulnerability in CoreFoundation in Mac OS X 10.3.9 and 10.4.2 allows attackers to cause a denial of service (CPU consumption) via crafted Gregorian dates.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-2856
    - Vulnerability Description: Stack-based buffer overflow in the WinACE UNACEV2.DLL third-party compression utility before 2.6.0.0, as used in multiple products including (1) ALZip 5.51 through 6.11, (2) Servant Salamander 2.0 and 2.5 Beta 1, (3) WinHKI 1.66 and 1.67, (4) ExtractNow 3.x, (5) Total Commander 6.53, (6) Anti-Trojan 5.5.421, (7) PowerArchiver before 9.61, (8) UltimateZip 2.7,1, 3.0.3, and 3.1b, (9) Where Is It (WhereIsIt) 3.73.501, (10) FilZip 3.04, (11) IZArc 3.5 beta3, (12) Eazel 1.0, (13) Rising Antivirus 18.27.21 and earlier, (14) AutoMate 6.1.0.0, (15) BitZipper 4.1 SR-1, (16) ZipTV, and other products, allows user-assisted attackers to execute arbitrary code via a long filename in an ACE archive.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-2946
    - Vulnerability Description: The default configuration on OpenSSL before 0.9.8 uses MD5 for creating message digests instead of a more cryptographically strong algorithm, which makes it easier for remote attackers to forge certificates with a valid certificate authority signature.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-3063
    - Vulnerability Description: SQL injection vulnerability in MailGust 1.9 allows remote attackers to execute arbitrary SQL commands via the email field on the password reminder page.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-3261
    - Vulnerability Description: getversions.php in versatileBulletinBoard (vBB) 1.0.0 RC2 lists the versions of all installed scripts, which allows remote attackers to obtain sensitive information via a direct request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-3530
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in Antville 1.1 allows remote attackers to inject arbitrary web script or HTML via the notfound.skin error document.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-3740
    - Vulnerability Description: Multiple SQL injection vulnerabilities in PHP-Fusion 6.00.206 and earlier allow remote attackers to execute arbitrary SQL commands via (1) the forum_id parameter to options.php or (2) lastvisited parameter to viewforum.php.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-3800
    - Vulnerability Description: Macromedia Contribute Publishing Server (CPS) before 1.11 uses a weak algorithm to encrypt user password in connection keys that use shared FTP login credentials, which allows attackers to obtain sensitive information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-3822
    - Vulnerability Description: Multiple SQL injection vulnerabilities in vTiger CRM 4.2 and earlier allow remote attackers to execute arbitrary SQL commands via the (1) username in the login form or (2) record parameter, as demonstrated in the EditView action for the Contacts module.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-4033
    - Vulnerability Description: Nodezilla 0.4.13-corno-fulgure does not properly protect the evl_data directory, which could allow them to be shared when they are not protected by PRIVATEDATADIR in nodezilla.ini, which allows remote attackers to obtain sensitive information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-4505
    - Vulnerability Description: Unquoted Windows search path vulnerability in McAfee VirusScan Enterprise 8.0i (patch 11) and CMA 3.5 (patch 5) might allow local users to gain privileges via a malicious "program.exe" file in the C: folder, which is run by naPrdMgr.exe when it attempts to execute EntVUtil.EXE under an unquoted "Program Files" path.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-4564
    - Vulnerability Description: The Internet Key Exchange version 1 (IKEv1) implementation in ADTRAN NetVanta before 10.03.03.E might allow remote attackers to cause a denial of service via crafted IKE packets, as demonstrated by the PROTOS ISAKMP Test Suite for IKEv1.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-4565
    - Vulnerability Description: Format string vulnerability in the Internet Key Exchange version 1 (IKEv1) implementation in ADTRAN NetVanta before 10.03.03.E might allow remote attackers to have an unknown impact via format string specifiers in crafted IKE packets, as demonstrated by the PROTOS ISAKMP Test Suite for IKEv1.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-4566
    - Vulnerability Description: Buffer overflow in the Internet Key Exchange version 1 (IKEv1) implementation in ADTRAN NetVanta before 10.03.03.E might allow remote attackers to have an unknown impact via crafted IKE packets, as demonstrated by the PROTOS ISAKMP Test Suite for IKEv1.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-4726
    - Vulnerability Description: MUTE 0.4 uses improper flood protection algorithms, which allows remote attackers to obtain sensitive information (privacy leak and search result data) by controlling a drop chain neighbor that is near the end of a message chain.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-4839
    - Vulnerability Description: PureTLS before 0.9b5 does not clear optional Extensions and Algorithm.Parameters values before parsing, which might trigger an information leak of values from earlier certificates.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-4848
    - Vulnerability Description: Buffer overflow in the decompression algorithm in Research in Motion BlackBerry Enterprise Server 4.0 SP1 and earlier before 20050607 might allow remote attackers to execute arbitrary code via certain data packets.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-0446
    - Vulnerability Description: Unspecified vulnerability in WeBWorK 2.1.3 and 2.2-pre1 allows remote privilged attackers to execute arbitrary commands as the web server via unknown attack vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-0487
    - Vulnerability Description: Multiple unspecified vulnerabilities in Tumbleweed MailGate Email Firewall (EMF) 6.x allow remote attackers to (1) trigger temporarily incorrect processing of an e-mail message under "extremely heavy loads" and (2) cause an "increased number of missed spam" during "spam outbreaks."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-0492
    - Vulnerability Description: Multiple SQL injection vulnerabilities in Calendarix allow remote attackers to execute arbitrary SQL commands via (1) the catview parameter in cal_functions.inc.php and (2) the login parameter in cal_login.php.  NOTE: the catview vector might overlap CVE-2005-1865.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-0937
    - Vulnerability Description: U.N.U. Mailgust 1.9 allows remote attackers to obtain sensitive information via a direct request to index.php with method=showfullcsv, which reveals the POP3 server configuration, including account name and password.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-1142
    - Vulnerability Description: Unspecified vulnerability in Ravenous Web Server before 0.7.1 allows remote attackers to access arbitrary rvplg files, with unknown impact.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-1759
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in allgemein_transfer.php in SWSoft Confixx 3.1.2 allows remote attackers to inject arbitrary web script or HTML via the jahr parameter.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-1900
    - Vulnerability Description: Multiple buffer overflows in World Wide Web Consortium (W3C) Amaya 9.4, and possibly other versions including 8.x before 8.8.5, allow remote attackers to execute arbitrary code via a long value in (1) the COMPACT attribute of the COLGROUP element, (2) the ROWS attribute of the TEXTAREA element, and (3) the COLOR attribute of the LEGEND element
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-2255
    - Vulnerability Description: Multiple SQL injection vulnerabilities in Creative Community Portal 1.1 and earlier allow remote attackers to execute arbitrary SQL commands via the (1) article_id parameter to (a) ArticleView.php, (2) forum_id parameter to (b) DiscView.php or (c) Discussions.php, (3) event_id parameter to (d) EventView.php, (4) AddVote and (5) answer_id parameter to (e) PollResults.php, or (7) mid parameter to (f) DiscReply.php.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-2407
    - Vulnerability Description: Stack-based buffer overflow in (1) WeOnlyDo wodSSHServer ActiveX Component 1.2.7 and 1.3.3 DEMO, as used in other products including (2) FreeSSHd 1.0.9 and (3) freeFTPd 1.0.10, allows remote attackers to execute arbitrary code via a long key exchange algorithm string.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-2482
    - Vulnerability Description: Heap-based buffer overflow in the TZipTV component in (1) ZipTV for Delphi 7 2006.1.26 and for C++ Builder 2006-1.16, (2) PentaZip 8.5.1.190 and PentaSuite-PRO 8.5.1.221, and possibly other products, allows user-assisted attackers to execute arbitrary code via an ARJ archive with a long header. NOTE: the ACE archive vector is covered by CVE-2005-2856.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-2488
    - Vulnerability Description: Multiple cross-site scripting (XSS) vulnerabilities in Spymac WebOS (WOS) 5.0 allow remote attackers to inject arbitrary web script or HTML via the (1) del_folder, (2) nick, or (3) action parameters to (a) notes/index.php, (4) curr parameter to (b) ipod/get_ipod.php, and in (c) login.php.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-2808
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in Lycos Tripod htmlGEAR guestGEAR (aka Guest Gear) allows remote attackers to inject arbitrary web script or HTML via a guestbook post containing a javascript URI in the SRC attribute of the BR element after an extra "iframe" tagname within that element, followed by a double ">", which might bypass cleansing operations.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-2975
    - Vulnerability Description: Multiple cross-site scripting (XSS) vulnerabilities in pblguestbook.php in PBL Guestbook 1.31 allow remote attackers to inject arbitrary web script or HTML via javascript in the SRC attribute of IMG tags in the (1) name, (2) email, and (3) website parameter, which bypasses XSS protection mechanisms that check for SCRIPT tags but not IMG.  NOTE: portions of this description's details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-3092
    - Vulnerability Description: PhpMyFactures 1.2 and earlier allows remote attackers to bypass authentication and modify data via direct requests with modified parameters to (1) /tva/ajouter_tva.php, (2) /remises/ajouter_remise.php, (3) /pays/ajouter_pays.php, (4) /pays/modifier_pays.php, (5) /produits/ajouter_cat.php, (6) /produits/ajouter_produit.php, (7) /clients/ajouter_client.php, (8) /clients/modifier_client.php.  NOTE: the provenance of this information is unknown
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-3252
    - Vulnerability Description: Buffer overflow in the Online Registration Facility for Algorithmic Research PrivateWire VPN software up to 3.7 allows remote attackers to execute arbitrary code via a long GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-3379
    - Vulnerability Description: Algorithmic complexity vulnerability in Hiki Wiki 0.6.0 through 0.6.5 and 0.8.0 through 0.8.5 allows remote attackers to cause a denial of service (CPU consumption) by performing a diff between large, crafted pages that trigger the worst case.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-3380
    - Vulnerability Description: Algorithmic complexity vulnerability in FreeStyle Wiki before 3.6.2 allows remote attackers to cause a denial of service (CPU consumption) by performing a diff between large, crafted pages that trigger the worst case.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-3511
    - Vulnerability Description: Internet Explorer 6 on Windows XP SP2 allows remote attackers to cause a denial of service (crash) by setting the fonts property of the HtmlDlgSafeHelper object, which triggers a null dereference.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-3561
    - Vulnerability Description: BT Voyager 2091 Wireless firmware 2.21.05.08m_A2pB018c1.d16d and earlier, and 3.01m and earlier, allow remote attackers to bypass the authentication process and gain sensitive information, such as configuration information via (1) /btvoyager_getconfig.sh, PPP crendentials via (2) btvoyager_getpppcreds.sh, and decode configuration credentials via (3) btvoyager_decoder.c.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-3617
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in pblguestbook.php in Pixelated By Lev (PBL) Guestbook 1.32 and earlier allows remote attackers to inject arbitrary web script or HTML via the (1) name, (2) message (aka comments), (3) website, and (4) email parameters, which bypasses XSS protection mechanisms that check for SCRIPT tags but not others, as demonstrated by a javascript URI in an onMouseOver attribute and the src attribute in an iframe tag.  NOTE: some vectors might overlap CVE-2006-2975, although the use of alternate manipulations makes it unclear.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-3618
    - Vulnerability Description: SQL injection vulnerability in pblguestbook.php in Pixelated By Lev (PBL) Guestbook 1.32 and earlier allows remote attackers to execute arbitrary SQL commands via the (1) name, (2) email, (3) website, (4) comments, (5) rate, and (6) private parameters.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-4596
    - Vulnerability Description: PHP remote file inclusion in MyBace Light Skrip, when register_globals is enabled, allows remote attackers to execute arbitrary PHP code via the (1) hauptverzeichniss parameter in includes/login_check.php and the (2) template_back parameter in admin/login/content/user_daten.php.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-4790
    - Vulnerability Description: verify.c in GnuTLS before 1.4.4, when using an RSA key with exponent 3, does not properly handle excess data in the digestAlgorithm.parameters field when generating a hash, which allows remote attackers to forge a PKCS #1 v1.5 signature that is signed by that RSA key and prevents GnuTLS from correctly verifying X.509 and other certificates that use PKCS, a variant of CVE-2006-4339.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-4880
    - Vulnerability Description: David Bennett PHP-Post (PHPp) 1.0 and earlier allows remote attackers to obtain sensitive information via a direct request for (1) footer.php, (2) template.php, or (3) lastvisit.php, which reveals the installation path in various error messages.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-4942
    - Vulnerability Description: Moodle before 1.6.2, when the configuration lacks (1) algebra or (2) tex filters, allows remote authenticated users to write LaTeX or MimeTeX output files to the top level of the dataroot directory via (a) filter/algebra/pix.php or (b) filter/tex/pix.php.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-5455
    - Vulnerability Description: Cross-site request forgery (CSRF) vulnerability in editversions.cgi in Bugzilla before 2.22.1 and 2.23.x before 2.23.3 allows user-assisted remote attackers to create, modify, or delete arbitrary bug reports via a crafted URL.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-5777
    - Vulnerability Description: Creasito E-Commerce Content Manager 1.3.08 allows remote attackers to bypass authentication and perform privileged functions via a non-empty finame parameter to (1) addnewcont.php, (2) adminpassw.php, (3) amministrazione.php, (4) artins.php, (5) bgcolor.php, (6) cancartcat.php, (7) canccat.php, (8) cancelart.php, (9) cancontsit.php, (10) chanpassamm.php, (11) dele.php, (12) delecat.php, (13) delecont.php, (14) emailall.php, (15) gestflashtempl.php, (16) gestmagart.php, (17) gestmagaz.php, (18) gestpre.php, (19) input.php, (20) input3.php, (21) insnucat.php, (22) instempflash.php, (23) mailfc.php, (24) modfdati.php, (25) rescont4.php, (26) ricordo1.php, (27) ricordo4.php, (28) tabcatalg.php, (29) tabcont.php, (30) tabcont3.php, (31) tabstile.php, (32) tabstile3.php, (33) testimmg.php, and (34) update.php in admin/.  NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-5954
    - Vulnerability Description: SQL injection vulnerability in page.asp in NetVIOS 2.0 and earlier allows remote attackers to execute arbitrary SQL commands via the NewsID parameter.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-5980
    - Vulnerability Description: adm_lgn_admin.asp in Renasoft NetJetServer 2.5.3.939, and possibly earlier, does not properly perform login authentication, which allows remote attackers to obtain administrative privileges.  NOTE: the provenance of this information is unknown
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-6028
    - Vulnerability Description: Directory traversal vulnerability in textview.php in Anton Vlasov DoSePa 1.0.4 allows remote attackers to read arbitrary files via a .. (dot dot) sequence or absolute file path in the file parameter.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-6102
    - Vulnerability Description: Integer overflow in the ProcDbeGetVisualInfo function in the DBE extension for X.Org 6.8.2, 6.9.0, 7.0, and 7.1, and XFree86 X server, allows local users to execute arbitrary code via a crafted X protocol request that triggers memory corruption during processing of unspecified data structures.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-6158
    - Vulnerability Description: Multiple cross-site scripting (XSS) vulnerabilities in (a) PMOS Help Desk 2.4, formerly (b) InverseFlow Help Desk 2.31 and also sold as (c) Ace Helpdesk 2.31, allow remote attackers to inject arbitrary web script or HTML via the (1) id or email parameter to ticketview.php, or (2) the email parameter to ticket.php.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-6285
    - Vulnerability Description: ** DISPUTED **  PHP remote file inclusion vulnerability in index.php in Kai Blankenhorn Bitfolge simple and nice index file (aka snif) 1.5.2 and earlier allows remote attackers to execute arbitrary PHP code via a URL in the externalConfig parameter.  NOTE: CVE and other third parties dispute this vulnerability because $externalConfig is defined before use.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-6396
    - Vulnerability Description: Stack-based buffer overflow in BlazeVideo HDTV Player 2.1, and possibly earlier, allows remote attackers to execute arbitrary code via a long filename in a PLF playlist, a different product than CVE-2006-6199.  NOTE: it was later reported that 3.5 is also affected.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-6488
    - Vulnerability Description: Stack-based buffer overflow in the DoModal function in the Dialog Wrapper Module ActiveX control (DlgWrapper.dll) before 8.4.166.0, as used by ICONICS OPC Enabled Gauge, Switch, and Vessel ActiveX, allows remote attackers to execute arbitrary code via a long (1) FileName or (2) Filter argument.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-6674
    - Vulnerability Description: Ozeki HTTP-SMS Gateway 1.0, and possibly earlier, stores usernames and passwords in plaintext in the HKLM\Software\Ozeki\SMSServer\CurrentVersion\Plugins\httpsmsgate registry key, which allows local users to obtain sensitive information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-6753
    - Vulnerability Description: Event Viewer (eventvwr.exe) in Microsoft Windows does not properly display log data that contains '%' (percent) characters, which might make it impossible to use Event Viewer to determine the actual data that triggered an event, and might produce long strings that are not properly handled by certain processes that rely on Event Viewer.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-6791
    - Vulnerability Description: SQL injection vulnerability in SelGruFra.asp in chatwm 1.0 allows remote attackers to execute arbitrary SQL commands via the (1) txtUse and (2) txtPas parameters.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-6860
    - Vulnerability Description: Buffer overflow in the sendToMythTV function in MythControlServer.c in MythControl 1.0 and earlier allows remote attackers to execute arbitrary code via a crafted sendStr string to the Bluetooth interface.  NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-6931
    - Vulnerability Description: Algorithmic complexity vulnerability in Snort before 2.6.1, during predicate evaluation in rule matching for certain rules, allows remote attackers to cause a denial of service (CPU consumption and detection outage) via crafted network traffic, aka a "backtracking attack."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-7160
    - Vulnerability Description: The Sandbox.sys driver in Outpost Firewall PRO 4.0, and possibly earlier versions, does not validate arguments to hooked SSDT functions, which allows local users to cause a denial of service (crash) via invalid arguments to the (1) NtAssignProcessToJobObject,, (2) NtCreateKey, (3) NtCreateThread, (4) NtDeleteFile, (5) NtLoadDriver, (6) NtOpenProcess, (7) NtProtectVirtualMemory, (8) NtReplaceKey, (9) NtTerminateProcess, (10) NtTerminateThread, (11) NtUnloadDriver, and (12) NtWriteVirtualMemory functions.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-7239
    - Vulnerability Description: The _gnutls_x509_oid2mac_algorithm function in lib/gnutls_algorithms.c in GnuTLS before 1.4.2 allows remote attackers to cause a denial of service (crash) via a crafted X.509 certificate that uses a hash algorithm that is not supported by GnuTLS, which triggers a NULL pointer dereference.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-0356
    - Vulnerability Description: The Common Controls Replacement Project (CCRP) FolderTreeview (FTV) ActiveX control (ccrpftv6.ocx) allows remote attackers to cause a denial of service (Internet Explorer 7 crash) via a long CCRP.RootFolder property value.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-0449
    - Vulnerability Description: Multiple buffer overflows in LGSERVER.EXE in CA BrightStor ARCserve Backup for Laptops and Desktops r11.0 through r11.1 SP1, Mobile Backup r4.0, Desktop and Business Protection Suite r2, and Desktop Management Suite (DMS) r11.0 and r11.1 allow remote attackers to execute arbitrary code via crafted packets to TCP port (1) 1900 or (2) 2200.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-0524
    - Vulnerability Description: The LG Chocolate KG800 phone allows remote attackers to cause a denial of service (continual modal dialogs and UI unavailability) by repeatedly trying to OBEX push a file over Bluetooth, as demonstrated by ussp-push.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-0672
    - Vulnerability Description: LGSERVER.EXE in BrightStor Mobile Backup 4.0 allows remote attackers to cause a denial of service (disk consumption and daemon hang) via a value of 0xFFFFFF7F at a certain point in an authentication negotiation packet, which writes a large amount of data to a .USX file in CA_BABLDdata\Server\data\transfer\.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-0673
    - Vulnerability Description: LGSERVER.EXE in BrightStor ARCserve Backup for Laptops & Desktops r11.1 allows remote attackers to cause a denial of service (daemon crash) via a value of 0xFFFFFFFF at a certain point in an authentication negotiation packet, which results in an out-of-bounds read.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-0709
    - Vulnerability Description: cmdmon.sys in Comodo Firewall Pro (formerly Comodo Personal Firewall) 2.4.16.174 and earlier does not validate arguments that originate in user mode for the (1) NtCreateSection, (2) NtOpenProcess, (3) NtOpenSection, (4) NtOpenThread, and (5) NtSetValueKey hooked SSDT functions, which allows local users to cause a denial of service (system crash) and possibly gain privileges via invalid arguments.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-0756
    - Vulnerability Description: Chicken of the VNC (cotv) 2.0 allows remote attackers to cause a denial of service (application crash) via a large computer-name size value in a ServerInit packet, which triggers a failed malloc and a resulting NULL dereference.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-0883
    - Vulnerability Description: Directory traversal vulnerability in portalgroups/portalgroups/getfile.cgi in IP3 NetAccess before firmware 4.1.9.6 allows remote attackers to read arbitrary files via a .. (dot dot) in the filename parameter.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-0977
    - Vulnerability Description: IBM Lotus Domino R5 and R6 WebMail, with "Generate HTML for all fields" enabled, stores HTTPPassword hashes from names.nsf in a manner accessible through Readviewentries and OpenDocument requests to the defaultview view, a different vector than CVE-2005-2428.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-1163
    - Vulnerability Description: SQL injection vulnerability in printview.php in webSPELL 4.01.02 and earlier allows remote attackers to execute arbitrary SQL commands via the topic parameter, a different vector than CVE-2007-1019, CVE-2006-5388, and CVE-2006-4783.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-1327
    - Vulnerability Description: The SILC_SERVER_CMD_FUNC function in apps/silcd/command.c in silc-server 1.0.2 allows remote attackers to cause a denial of service (NULL dereference and daemon crash) via a request without a cipher algorithm and an invalid HMAC algorithm.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-1538
    - Vulnerability Description: ** DISPUTED **  McAfee VirusScan Enterprise 8.5.0.i uses insecure permissions for certain Windows Registry keys, which allows local users to bypass local password protection via the UIP value in (1) HKEY_LOCAL_MACHINE\SOFTWARE\McAfee\DesktopProtection or (2) HKEY_LOCAL_MACHINE\SOFTWARE\Network Associates\TVD\VirusScan Entreprise\CurrentVersion.  NOTE: this issue has been disputed by third-party researchers, stating that the default permissions for HKEY_LOCAL_MACHINE\SOFTWARE does not allow for write access and the product does not modify the inherited permissions. There might be an interaction error with another product.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-1566
    - Vulnerability Description: SQL injection vulnerability in News/page.asp in NetVIOS Portal allows remote attackers to execute arbitrary SQL commands via the NewsID parameter.  NOTE: this issue might be the same as CVE-2006-5954.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-1623
    - Vulnerability Description: Multiple cross-site scripting (XSS) vulnerabilities in realGuestbook 5.01, when register_globals is enabled, allow remote attackers to inject arbitrary web script or HTML via the (1) bg_color_1, (2) fs_menu, (3) fc_menu, (4) ff_menu, (5) bg_color_2, (6) fs_normal, (7) fc_normal, and (8) ff_normal parameters to welcome_admin.php
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-1624
    - Vulnerability Description: Multiple SQL injection vulnerabilities in realGuestbook 5.01 allow remote attackers to execute arbitrary SQL commands via the (1) name, (2) email, (3) homepage, and (4) text parameters to save_entry.php, as reachable through add_entry.php
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-1625
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in save_entry.php in realGuestbook 5.01 allows remote attackers to inject arbitrary web script or HTML via the homepage parameter, as reachable through add_entry.php.  NOTE: the original report stated that the vulnerability was in add_entry.php, which does not receive the input data.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-1652
    - Vulnerability Description: OpenID allows remote attackers to forcibly log a user into an OpenID enabled site, divulge the user's personal information to this site, and add it site to the trusted sites list via a crafted web page, related to cached tokens.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-1880
    - Vulnerability Description: Integer overflow in the _NtSetValueKey function in klif.sys in Kaspersky Anti-Virus, Anti-Virus for Workstations, Anti-Virus for File Server 6.0, and Internet Security 6.0 before Maintenance Pack 2 build 6.0.2.614 allows context-dependent attackers to execute arbitrary code via a large, unsigned "data size argument," which results in a heap overflow.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-1987
    - Vulnerability Description: ** DISPUTED **  Multiple PHP remote file inclusion vulnerabilities in PHPEcho CMS 2.0 allow remote attackers to execute arbitrary PHP code via a URL in the (1) _plugin_file parameter to smarty/internals/core.load_pulgins.php or the (2) root_path parameter to index.php.  NOTE: CVE disputes (1) because the inclusion occurs within a function that is not called during a direct request. CVE disputes (2) because root_path is defined in config.php before use.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-2216
    - Vulnerability Description: The tblinf32.dll (aka vstlbinf.dll) ActiveX control for Internet Explorer 5.01, 6 SP1, and 7 uses an incorrect IObjectsafety implementation, which allows remote attackers to execute arbitrary code by requesting the HelpString property, involving a crafted DLL file argument to the TypeLibInfoFromFile function, which overwrites the HelpStringDll property to call the DLLGetDocumentation function in another DLL file, aka "ActiveX Object Vulnerability."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-2279
    - Vulnerability Description: The Scheduler Service (VxSchedService.exe) in Symantec Storage Foundation for Windows 5.0 allows remote attackers to bypass authentication and execute arbitrary code via certain requests to the service socket that create (1) PreScript or (2) PostScript registry values under Veritas\VxSvc\CurrentVersion\Schedules specifying future command execution.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-2494
    - Vulnerability Description: Multiple stack-based buffer overflows in the PowerPointOCX ActiveX control in PowerPointViewer.ocx 3.1.0.3 allow remote attackers to cause a denial of service (Internet Explorer 7 crash) via a long (1) DoOleCommand, (2) FTPDownloadFile, (3) FTPUploadFile, (4) HttpUploadFile, (5) Save, (6) SaveWebFile, (7) HttpDownloadFile, (8) Open, or (9) OpenWebFile property value.  NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-2930
    - Vulnerability Description: The (1) NSID_SHUFFLE_ONLY and (2) NSID_USE_POOL PRNG algorithms in ISC BIND 8 before 8.4.7-P1 generate predictable DNS query identifiers when sending outgoing queries such as NOTIFY messages when answering questions as a resolver, which allows remote attackers to poison DNS caches via unknown vectors.  NOTE: this issue is different from CVE-2007-2926.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-2938
    - Vulnerability Description: Buffer overflow in the BaseRunner ActiveX control in the Ademco ATNBaseLoader100 Module (ATNBaseLoader100.dll) 5.4.0.6, when Internet Explorer 6 is used, allows remote attackers to execute arbitrary code via a long argument to the (1) Send485CMD method, and possibly the (2) SetLoginID, (3) AddSite, (4) SetScreen, and (5) SetVideoServer methods.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-2955
    - Vulnerability Description: Multiple unspecified "input validation error" vulnerabilities in multiple ActiveX controls in NavComUI.dll, as used in multiple Norton AntiVirus, Internet Security, and System Works products for 2006, allows remote attackers to execute arbitrary code via (1) the AnomalyList property to AxSysListView32 and (2) Anomaly property to AxSysListView32OAA.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-3216
    - Vulnerability Description: Multiple buffer overflows in the LGServer component of CA (Computer Associates) BrightStor ARCserve Backup for Laptops and Desktops r11.1 allow remote attackers to execute arbitrary code via crafted arguments to the (1) rxsAddNewUser, (2) rxsSetUserInfo, (3) rxsRenameUser, (4) rxsSetMessageLogSettings, (5) rxsExportData, (6) rxsSetServerOptions, (7) rxsRenameFile, (8) rxsACIManageSend, (9) rxsExportUser, (10) rxsImportUser, (11) rxsMoveUserData, (12) rxsUseLicenseIni, (13) rxsLicGetSiteId, (14) rxsGetLogFileNames, (15) rxsGetBackupLog, (16) rxsBackupComplete, (17) rxsSetDataProtectionSecurityData, (18) rxsSetDefaultConfigName, (19) rxsGetMessageLogSettings, (20) rxsHWDiskGetTotal, (21) rxsHWDiskGetFree, (22) rxsGetSubDirs, (23) rxsGetServerDBPathName, (24) rxsSetServerOptions, (25) rxsDeleteFile, (26) rxsACIManageSend, (27) rxcReadBackupSetList, (28) rxcWriteConfigInfo, (29) rxcSetAssetManagement, (30) rxcWriteFileListForRestore, (31) rxcReadSaveSetProfile, (32) rxcInitSaveSetProfile, (33) rxcAddSaveSetNextAppList, (34) rxcAddSaveSetNextFilesPathList, (35) rxcAddNextBackupSetIncWildCard, (36) rxcGetRevisions, (37) rxrAddMovedUser, (38) rxrSetClientVersion, or (39) rxsSetDataGrowthScheduleAndFilter commands.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-3259
    - Vulnerability Description: Calendarix 0.7.20070307 allows remote attackers to obtain sensitive information via (1) an invalid month[] parameter to calendar.php, (2) an invalid catview[] parameter to cal_week.php in a week operation, (3) an invalid ycyear[] parameter to yearcal.php, or (4) a direct request to cal_functions.inc.php, which reveals the installation path in various error messages.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-3339
    - Vulnerability Description: Multiple cross-site scripting (XSS) vulnerabilities in forum/include/error/autherror.cfm in FuseTalk Basic, Standard, Enterprise, and ColdFusion allow remote attackers to inject arbitrary web script or HTML via the (1) FTVAR_LINKP and (2) FTVAR_URLP parameters to (a) forum/include/error/autherror.cfm, and the (3) FTVAR_SCRIPTRUN parameter to (b) forum/include/common/comfinish.cfm and (c) blog/include/common/comfinish.cfm.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-3603
    - Vulnerability Description: SQL injection vulnerability in the dashboard (include/utils/SearchUtils.php) in vtiger CRM before 5.0.3 allows remote authenticated users to execute arbitrary SQL commands via the assigned_user_id parameter in a Potentials ListView action to index.php.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-3619
    - Vulnerability Description: Directory traversal vulnerability in login.php in Maia Mailguard 1.0.2 and earlier allows remote attackers to read arbitrary files via a .. (dot dot) in the lang parameter.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-3620
    - Vulnerability Description: Multiple directory traversal vulnerabilities in Maia Mailguard 1.0.2 and earlier might allow remote attackers to read arbitrary files via a .. (dot dot) in the (1) prevlang and (2) super parameters to (a) php/login.php
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-3705
    - Vulnerability Description: SQL injection vulnerability in FuseTalk 2.0 allows remote attackers to execute arbitrary SQL commands via the FTVAR_SUBCAT (txForumID) parameter to forum/index.cfm and possibly other unspecified components, related to forum/include/error/forumerror.cfm.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-3800
    - Vulnerability Description: Unspecified vulnerability in the Real-time scanner (RTVScan) component in Symantec AntiVirus Corporate Edition 9.0 through 10.1 and Client Security 2.0 through 3.1, when the Notification Message window is enabled, allows local users to gain privileges via crafted code.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-3803
    - Vulnerability Description: The SMTP ALG in Clavister CorePlus before 8.80.04, and 8.81.00, does not properly parse SMTP commands in certain circumstances, which allows remote attackers to bypass address blacklists.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-3804
    - Vulnerability Description: The AntiVirus engine in the HTTP-ALG in Clavister CorePlus before 8.81.00 and 8.80.03 might allow remote attackers to bypass scanning via small files.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-3911
    - Vulnerability Description: Multiple heap-based buffer overflows in (1) clsscheduler.exe (aka scheduler client) and (2) srvscheduler.exe (aka scheduler server) in BakBone NetVault Reporter 3.5 before Update4 allow remote attackers to execute arbitrary code via long filename arguments in HTTP requests.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-3986
    - Vulnerability Description: file.cgi in Secure Computing SecurityReporter (aka Network Security Analyzer) 4.6.3 allows remote attackers to bypass authentication via a name parameter that specifies the eventcache directory and a non-GIF file, which causes the $dontvalidate variable to be set to true. NOTE: a separate traversal vulnerability could be leveraged to download arbitrary files.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-4034
    - Vulnerability Description: Stack-based buffer overflow in the YDPCTL.YDPControl.1 (aka Yahoo! Installer Plugin for Widgets) ActiveX control before 2007.7.13.3 (20070620) in YDPCTL.dll in Yahoo! Widgets before 4.0.5 allows remote attackers to execute arbitrary code via a long argument to the GetComponentVersion method.  NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-4264
    - Vulnerability Description: Multiple cross-site scripting (XSS) vulnerabilities in index.php in Kai Blankenhorn Bitfolge simple and nice index file (aka snif) 1.5.2 and earlier allow remote attackers to inject arbitrary web script or HTML via the (1) path and (2) download parameters.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-4384
    - Vulnerability Description: Multiple PHP remote file inclusion vulnerabilities in depouilg.php3 in Stephane Pineau VOTE 1c allow remote attackers to execute arbitrary PHP code via a URL in the (1) NomVote and (2) FilePalHex parameters.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-4537
    - Vulnerability Description: Heap-based buffer overflow in the Huffman decompression algorithm implemented in Skulltag 0.97d-beta4.1 and earlier allows remote attackers to execute arbitrary code via a crafted UDP packet.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-4570
    - Vulnerability Description: Algorithmic complexity vulnerability in the MCS translation daemon in mcstrans 0.2.3 allows local users to cause a denial of service (temporary daemon outage) via a large range of compartments in sensitivity labels.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-4580
    - Vulnerability Description: Buffer underflow in redlight.sys in BufferZone 2.1 and 2.5 allows local users to cause a denial of service (crash) and possibly execute arbitrary code by sending a small buffer size value to the FsSetVolumeInformation IOCTL handler code with a FsSetDirectoryInformation subcode containing a large buffer.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-4591
    - Vulnerability Description: vstor-ws60.sys in VMWare Workstation 6.0 allows local users to cause a denial of service (host operating system crash) and possibly gain privileges by sending a small file buffer size value to the FsSetVolumeInformation IOCTL handler with an FsSetFileInformation subcode.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-4675
    - Vulnerability Description: Heap-based buffer overflow in the QuickTime VR extension 7.2.0.240 in QuickTime.qts in Apple QuickTime before 7.3 allows remote attackers to execute arbitrary code via a QTVR (QuickTime Virtual Reality) movie file containing a large size field in the atom header of a panorama sample atom.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-4967
    - Vulnerability Description: Online Armor Personal Firewall 2.0.1.215 does not properly validate certain parameters to System Service Descriptor Table (SSDT) function handlers, which allows local users to cause a denial of service (crash) and possibly gain privileges via unspecified kernel SSDT hooks for Windows Native API functions including (1) NtAllocateVirtualMemory, (2) NtConnectPort, (3) NtCreateFile, (4) NtCreateKey, (5) NtCreatePort, (6) NtDeleteFile, (7) NtDeleteValueKey, (8) NtLoadKey, (9) NtOpenFile, (10) NtOpenProcess, (11) NtOpenThread, (12) NtResumeThread, (13) NtSetContextThread, (14) NtSetValueKey, (15) NtSuspendProcess, (16) NtSuspendThread, and (17) NtTerminateThread.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-4969
    - Vulnerability Description: Process Monitor 1.22 does not properly validate certain parameters to System Service Descriptor Table (SSDT) function handlers, which allows local users to cause a denial of service (crash) and possibly gain privileges via unspecified kernel SSDT hooks for Windows Native API functions including (1) NtCreateKey, (2) NtDeleteValueKey, (3) NtLoadKey, (4) NtOpenKey, (5) NtQueryValueKey, (6) NtSetValueKey, and (7) NtUnloadKey.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-4970
    - Vulnerability Description: ProcessGuard 3.410 does not properly validate certain parameters to System Service Descriptor Table (SSDT) function handlers, which allows local users to cause a denial of service (crash) and possibly gain privileges via kernel SSDT hooks for Windows Native API functions including (1) NtCreateFile, (2) NtCreateKey, (3) NtDeleteValueKey, (4) NtOpenFile, (5) NtOpenKey, and (6) NtSetValueKey.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-5039
    - Vulnerability Description: Ghost Security Suite beta 1.110 does not properly validate certain parameters to System Service Descriptor Table (SSDT) function handlers, which allows local users to cause a denial of service (crash) and possibly gain privileges via the (1) NtCreateKey, (2) NtDeleteValueKey, (3) NtQueryValueKey, (4) NtSetSystemInformation, and (5) NtSetValueKey kernel SSDT hooks.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-5040
    - Vulnerability Description: Ghost Security Suite alpha 1.200 does not properly validate certain parameters to System Service Descriptor Table (SSDT) function handlers, which allows local users to cause a denial of service (crash) and possibly gain privileges via the (1) NtCreateKey, (2) NtCreateThread, (3) NtDeleteValueKey, (4) NtQueryValueKey, (5) NtSetSystemInformation, and (6) NtSetValueKey kernel SSDT hooks.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-5558
    - Vulnerability Description: Integer overflow in the LG Mobile handset allows remote attackers to cause a denial of service (reboot) via a crafted HTTP packet.  NOTE: as of 20071016, the only disclosure is a vague pre-advisory with no actionable information. However, since it is from a well-known researcher, it is being assigned a CVE identifier for tracking purposes.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-5602
    - Vulnerability Description: Multiple stack-based buffer overflows in SwiftView Viewer before 8.3.5, as used by SwiftView and SwiftSend, allow remote attackers to execute arbitrary code via unspecified vectors to the (1) svocx.ocx ActiveX control or the (2) npsview.dll plugin for Mozilla and Firefox.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-5982
    - Vulnerability Description: Multiple cross-site scripting (XSS) vulnerabilities in X7 Chat 2.0.4, 2.0.5, and possibly other versions allow remote attackers to inject arbitrary web script or HTML via the (1) room parameter to sources/frame.php, the (2) theme_c parameter to help/index.php, or the (3) INSTALL_X7CHATVERSION parameter to upgradev1.php.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-6067
    - Vulnerability Description: Algorithmic complexity vulnerability in the regular expression parser in TCL before 8.4.17, as used in PostgreSQL 8.2 before 8.2.6, 8.1 before 8.1.11, 8.0 before 8.0.15, and 7.4 before 7.4.19, allows remote authenticated users to cause a denial of service (memory consumption) via a crafted "complex" regular expression with doubly-nested states.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-6253
    - Vulnerability Description: Multiple buffer overflows in Adobe Form Designer 5.0 and Form Client 5.0 allow remote attackers to execute arbitrary code via unknown vectors in the (1) Adobe File Dialog Button (FileDlg.dll) and the (2) Adobe Copy to Server Object (SvrCopy.dll) ActiveX controls.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-6254
    - Vulnerability Description: Stack-based buffer overflow in the SAP Business Objects BusinessObjects RptViewerAX ActiveX control in RptViewerAX.dll in Business Objects 6.5 before CHF74 allows remote attackers to execute arbitrary code via unspecified vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-6260
    - Vulnerability Description: The installation process for Oracle 10g and llg uses accounts with default passwords, which allows remote attackers to obtain login access by connecting to the Listener.  NOTE: at the end of the installation, if performed using the Database Configuration Assistant (DBCA), most accounts are disabled or their passwords are changed.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-6262
    - Vulnerability Description: A certain ActiveX control in axvlc.dll in VideoLAN VLC 0.8.6 before 0.8.6d allows remote attackers to execute arbitrary code via crafted arguments to the (1) addTarget, (2) getVariable, or (3) setVariable function, resulting from a "bad initialized pointer," aka a "recursive plugin release vulnerability."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-6337
    - Vulnerability Description: Unspecified vulnerability in the bzip2 decompression algorithm in nsis/bzlib_private.h in ClamAV before 0.92 has unknown impact and remote attack vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-6429
    - Vulnerability Description: Multiple integer overflows in X.Org Xserver before 1.4.1 allow context-dependent attackers to execute arbitrary code via (1) a GetVisualInfo request containing a 32-bit value that is improperly used to calculate an amount of memory for allocation by the EVI extension, or (2) a request containing values related to pixmap size that are improperly used in management of shared memory by the MIT-SHM extension.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-6523
    - Vulnerability Description: Algorithmic complexity vulnerability in Opera 9.50 beta and 9.x before 9.25 allows remote attackers to cause a denial of service (CPU consumption) via a crafted bitmap (BMP) file that triggers a large number of calculations and checks.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-6624
    - Vulnerability Description: Directory traversal vulnerability in printview.php in PNphpBB2 1.2i and earlier allows remote attackers to include and execute arbitrary local files via a .. (dot dot) in the phpEx parameter.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-6640
    - Vulnerability Description: Creammonkey 0.9 through 1.1 and GreaseKit 1.2 through 1.3 does not properly prevent access to dangerous functions, which allows remote attackers to read the configuration, modify the configuration, or send an HTTP request via the (1) GM_addStyle, (2) GM_log, (3) GM_openInTab, (4) GM_setValue, (5) GM_getValue, or (6) GM_xmlhttpRequest function within a web page on which a userscript is configured.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-6683
    - Vulnerability Description: The browser plugin in VideoLAN VLC 0.8.6d allows remote attackers to overwrite arbitrary files via (1) the :demuxdump-file option in a filename in a playlist, or (2) a EXTVLCOPT statement in an MP3 file, possibly an argument injection vulnerability.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-6700
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in cgi-bin/bgplg in the web interface for the BGPD daemon in OpenBSD 4.1 allows remote attackers to inject arbitrary web script or HTML via the cmd parameter.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-0162
    - Vulnerability Description: misc.c in splitvt 1.6.6 and earlier does not drop group privileges before executing xprop, which allows local users to gain privileges.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-0429
    - Vulnerability Description: SQL injection vulnerability in index.php in AlstraSoft Forum Pay Per Post Exchange 2.0 allows remote attackers to execute arbitrary SQL commands via the catid parameter in a forum_catview action.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-0519
    - Vulnerability Description: SQL injection vulnerability in index.php in the Atapin Jokes (com_jokes) 1.0 component for Mambo and Joomla! allows remote attackers to execute arbitrary SQL commands via the cat parameter in a CatView action.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-0558
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in Uniwin eCart Professional before 2.0.16 allows remote attackers to inject arbitrary web script or HTML via the rp parameter to cartView.asp and unspecified other components.  NOTE: the provenance of this information is unknown
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-1099
    - Vulnerability Description: _macro_Getval in wikimacro.py in MoinMoin 1.5.8 and earlier does not properly enforce ACLs, which allows remote attackers to read protected pages.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-1146
    - Vulnerability Description: A certain pseudo-random number generator (PRNG) algorithm that uses XOR and 3-bit random hops (aka "Algorithm X3"), as used in OpenBSD 2.8 through 4.2, allows remote attackers to guess sensitive values such as DNS transaction IDs by observing a sequence of previously generated values.  NOTE: this issue can be leveraged for attacks such as DNS cache poisoning against OpenBSD's modification of BIND.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-1147
    - Vulnerability Description: A certain pseudo-random number generator (PRNG) algorithm that uses XOR and 2-bit random hops (aka "Algorithm X2"), as used in OpenBSD 2.6 through 3.4, Mac OS X 10 through 10.5.1, FreeBSD 4.4 through 7.0, and DragonFlyBSD 1.0 through 1.10.1, allows remote attackers to guess sensitive values such as IP fragmentation IDs by observing a sequence of previously generated values.  NOTE: this issue can be leveraged for attacks such as injection into TCP packets and OS fingerprinting.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-1148
    - Vulnerability Description: A certain pseudo-random number generator (PRNG) algorithm that uses ADD with 0 random hops (aka "Algorithm A0"), as used in OpenBSD 3.5 through 4.2 and NetBSD 1.6.2 through 4.0, allows remote attackers to guess sensitive values such as (1) DNS transaction IDs or (2) IP fragmentation IDs by observing a sequence of previously generated values.  NOTE: this issue can be leveraged for attacks such as DNS cache poisoning, injection into TCP packets, and OS fingerprinting.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-1328
    - Vulnerability Description: Buffer overflow in the LGServer service in CA ARCserve Backup for Laptops and Desktops r11.0 through r11.5, and Suite 11.1 and 11.2, allows remote attackers to execute arbitrary code via unspecified "command arguments."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-1420
    - Vulnerability Description: Integer overflow in residue partition value (aka partvals) evaluation in Xiph.org libvorbis 1.2.0 and earlier allows remote attackers to execute arbitrary code via a crafted OGG file, which triggers a heap overflow.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-1423
    - Vulnerability Description: Integer overflow in a certain quantvals and quantlist calculation in Xiph.org libvorbis 1.2.0 and earlier allows remote attackers to cause a denial of service (crash) or execute arbitrary code via a crafted OGG file with a large virtual space for its codebook, which triggers a heap overflow.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-1505
    - Vulnerability Description: PHP remote file inclusion vulnerability in the SSTREAMTV custompages (com_custompages) 1.1 and earlier component for Joomla! allows remote attackers to execute arbitrary PHP code via a URL in the cpage parameter to index.php.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-1608
    - Vulnerability Description: SQL injection vulnerability in postview.php in Clever Copy 3.0 allows remote attackers to execute arbitrary SQL commands via the ID parameter, a different vector than CVE-2008-0363 and CVE-2006-0583.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-1637
    - Vulnerability Description: PowerDNS Recursor before 3.1.5 uses insufficient randomness to calculate (1) TRXID values and (2) UDP source port numbers, which makes it easier for remote attackers to poison a DNS cache, related to (a) algorithmic deficiencies in rand and random functions in external libraries, (b) use of a 32-bit seed value, and (c) choice of the time of day as the sole seeding information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-1678
    - Vulnerability Description: Memory leak in the zlib_stateful_init function in crypto/comp/c_zlib.c in libssl in OpenSSL 0.9.8f through 0.9.8h allows remote attackers to cause a denial of service (memory consumption) via multiple calls, as demonstrated by initial SSL client handshakes to the Apache HTTP Server mod_ssl that specify a compression algorithm.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-1771
    - Vulnerability Description: Integer overflow in the ws_getpostvars function in Firefly Media Server (formerly mt-daapd) 0.2.4.1 (0.9~r1696-1.2 on Debian) allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via an HTTP POST request with a large Content-Length.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-2124
    - Vulnerability Description: SQL injection vulnerability in modules/print.asp in fipsASP fipsCMS allows remote attackers to execute arbitrary SQL commands via the lg parameter.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-2362
    - Vulnerability Description: Multiple integer overflows in the Render extension in the X server 1.4 in X.Org X11R7.3 allow context-dependent attackers to execute arbitrary code via a (1) SProcRenderCreateLinearGradient, (2) SProcRenderCreateRadialGradient, or (3) SProcRenderCreateConicalGradient request with an invalid field specifying the number of bytes to swap in the request data, which triggers heap memory corruption.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-2429
    - Vulnerability Description: Multiple SQL injection vulnerabilities in Calendarix Basic 0.8.20071118 allow remote attackers to execute arbitrary SQL commands via (1) the catsearch parameter to cal_search.php or (2) the catview parameter to cal_cat.php.  NOTE: vector 1 might overlap CVE-2007-3183.3, and vector 2 might overlap CVE-2005-1865.2.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-3129
    - Vulnerability Description: Multiple SQL injection vulnerabilities in index.php in Catviz 0.4 beta 1 allow remote attackers to execute arbitrary SQL commands via the (1) foreign_key_value paramter in the news page and (2) webpage parameter in the webpage_multi_edit form.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-3134
    - Vulnerability Description: Multiple unspecified vulnerabilities in GraphicsMagick before 1.2.4 allow remote attackers to cause a denial of service (crash, infinite loop, or memory consumption) via (a) unspecified vectors in the (1) AVI, (2) AVS, (3) DCM, (4) EPT, (5) FITS, (6) MTV, (7) PALM, (8) RLA, and (9) TGA decoder readers
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-3172
    - Vulnerability Description: Opera allows web sites to set cookies for country-specific top-level domains that have DNS A records, such as co.tv, which could allow remote attackers to perform a session fixation attack and hijack a user's HTTP session, aka "Cross-Site Cooking."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-3175
    - Vulnerability Description: Integer underflow in rxRPC.dll in the LGServer service in the server in CA ARCserve Backup for Laptops and Desktops 11.0 through 11.5 allows remote attackers to execute arbitrary code or cause a denial of service via a crafted message that triggers a buffer overflow.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-3188
    - Vulnerability Description: libxcrypt in SUSE openSUSE 11.0 uses the DES algorithm when the configuration specifies the MD5 algorithm, which makes it easier for attackers to conduct brute-force attacks against hashed passwords.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-3271
    - Vulnerability Description: Apache Tomcat 5.5.0 and 4.1.0 through 4.1.31 allows remote attackers to bypass an IP address restriction and obtain sensitive information via a request that is processed concurrently with another request but in a different thread, leading to an instance-variable overwrite associated with a "synchronization problem" and lack of thread safety, and related to RemoteFilterValve, RemoteAddrValve, and RemoteHostValve.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-3288
    - Vulnerability Description: The Server Authentication Module in EMC Dantz Retrospect Backup Server 7.5.508 uses a "weak hash algorithm," which makes it easier for context-dependent attackers to recover passwords.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-3433
    - Vulnerability Description: SpeedBit Download Accelerator Plus (DAP) before 8.6.3.9 does not properly verify the authenticity of updates, which allows man-in-the-middle attackers to execute arbitrary code via a Trojan horse update, as demonstrated by evilgrade and DNS cache poisoning.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-3434
    - Vulnerability Description: Apple iTunes before 10.5.1 does not properly verify the authenticity of updates, which allows man-in-the-middle attackers to execute arbitrary code via a Trojan horse update, as demonstrated by evilgrade and DNS cache poisoning.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-3435
    - Vulnerability Description: LinkedIn Browser Toolbar 3.0.3.1100 and earlier does not properly verify the authenticity of updates, which allows man-in-the-middle attackers to execute arbitrary code via a Trojan horse update, as demonstrated by evilgrade and DNS cache poisoning.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-3436
    - Vulnerability Description: The GUP generic update process in Notepad++ before 4.8.1 does not properly verify the authenticity of updates, which allows man-in-the-middle attackers to execute arbitrary code via a Trojan horse update, as demonstrated by evilgrade and DNS cache poisoning.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-3437
    - Vulnerability Description: OpenOffice.org (OOo) before 2.1.0 does not properly verify the authenticity of updates, which allows man-in-the-middle attackers to execute arbitrary code via a Trojan horse update, as demonstrated by evilgrade and DNS cache poisoning.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-3438
    - Vulnerability Description: Apple Mac OS X does not properly verify the authenticity of updates, which allows man-in-the-middle attackers to execute arbitrary code via a Trojan horse update, as demonstrated by evilgrade and DNS cache poisoning.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-3439
    - Vulnerability Description: SpeedBit Video Acceleration before 2.2.1.8 does not properly verify the authenticity of updates, which allows man-in-the-middle attackers to execute arbitrary code via a Trojan horse update, as demonstrated by evilgrade and DNS cache poisoning.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-3440
    - Vulnerability Description: Sun Java 1.6.0_03 and earlier versions, and possibly later versions, does not properly verify the authenticity of updates, which allows man-in-the-middle attackers to execute arbitrary code via a Trojan horse update, as demonstrated by evilgrade and DNS cache poisoning.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-3441
    - Vulnerability Description: Nullsoft Winamp before 5.24 does not properly verify the authenticity of updates, which allows man-in-the-middle attackers to execute arbitrary code via a Trojan horse update, as demonstrated by evilgrade and DNS cache poisoning.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-3442
    - Vulnerability Description: WinZip before 11.0 does not properly verify the authenticity of updates, which allows man-in-the-middle attackers to execute arbitrary code via a Trojan horse update, as demonstrated by evilgrade and DNS cache poisoning.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-3529
    - Vulnerability Description: Heap-based buffer overflow in the xmlParseAttValueComplex function in parser.c in libxml2 before 2.7.0 allows context-dependent attackers to cause a denial of service (crash) or execute arbitrary code via a long XML entity name.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-3624
    - Vulnerability Description: Heap-based buffer overflow in Apple QuickTime before 7.5.5 allows remote attackers to execute arbitrary code or cause a denial of service (application crash) via a QuickTime Virtual Reality (QTVR) movie file with crafted panorama atoms.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-3625
    - Vulnerability Description: Stack-based buffer overflow in Apple QuickTime before 7.5.5 allows remote attackers to execute arbitrary code or cause a denial of service (application crash) via a QuickTime Virtual Reality (QTVR) movie file with crafted (1) maxTilt, (2) minFieldOfView, and (3) maxFieldOfView elements in panorama track PDAT atoms.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-3656
    - Vulnerability Description: Algorithmic complexity vulnerability in the WEBrick::HTTPUtils.split_header_value function in WEBrick::HTTP::DefaultFileHandler in WEBrick in Ruby 1.8.5 and earlier, 1.8.6 through 1.8.6-p286, 1.8.7 through 1.8.7-p71, and 1.9 through r18423 allows context-dependent attackers to cause a denial of service (CPU consumption) via a crafted HTTP request that is processed by a backtracking regular expression.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-3933
    - Vulnerability Description: Wireshark (formerly Ethereal) 0.10.14 through 1.0.2 allows attackers to cause a denial of service (crash) via a packet with crafted zlib-compressed data that triggers an invalid read in the tvb_uncompress function.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-4105
    - Vulnerability Description: JRequest in Joomla! 1.5 before 1.5.7 does not sanitize variables that were set with JRequest::setVar, which allows remote attackers to conduct "variable injection" attacks and have unspecified other impact.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-4376
    - Vulnerability Description: SQL injection vulnerability in index.php in Live TV Script allows remote attackers to execute arbitrary SQL commands via the mid parameter.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-4539
    - Vulnerability Description: Heap-based buffer overflow in the Cirrus VGA implementation in (1) KVM before kvm-82 and (2) QEMU on Debian GNU/Linux and Ubuntu might allow local users to gain privileges by using the VNC console for a connection, aka the LGD-54XX "bitblt" heap overflow.  NOTE: this issue exists because of an incorrect fix for CVE-2007-1320.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-4589
    - Vulnerability Description: Heap-based buffer overflow in the tvtumin.sys kernel driver in Lenovo Rescue and Recovery 4.20, including 4.20.0511 and 4.20.0512, allows local users to execute arbitrary code via a long file name.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-4683
    - Vulnerability Description: The dissect_btacl function in packet-bthci_acl.c in the Bluetooth ACL dissector in Wireshark 0.99.2 through 1.0.3 allows remote attackers to cause a denial of service (application crash or abort) via a packet with an invalid length, related to an erroneous tvb_memcpy call.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-4865
    - Vulnerability Description: Untrusted search path vulnerability in valgrind before 3.4.0 allows local users to execute arbitrary programs via a Trojan horse .valgrindrc file in the current working directory, as demonstrated using a malicious --db-command options.  NOTE: the severity of this issue has been disputed, but CVE is including this issue because execution of a program from an untrusted directory is a common scenario.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-4972
    - Vulnerability Description: mailgo in mgt 2.31 allows local users to overwrite arbitrary files via a symlink attack on a /tmp/mailgo##### temporary file.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-5033
    - Vulnerability Description: The chip_command function in drivers/media/video/tvaudio.c in the Linux kernel 2.6.25.x before 2.6.25.19, 2.6.26.x before 2.6.26.7, and 2.6.27.x before 2.6.27.3 allows attackers to cause a denial of service (NULL function pointer dereference and OOPS) via unknown vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-5065
    - Vulnerability Description: TlGuestBook 1.2 allows remote attackers to bypass authentication and gain administrative access by setting the tlGuestBook_login cookie to admin.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-5194
    - Vulnerability Description: SQL injection vulnerability in checkavail.php in SoftVisions Software Online Booking Manager (obm) 2.2 allows remote attackers to execute arbitrary SQL commands via the id parameter.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-5200
    - Vulnerability Description: SQL injection vulnerability in the Xe webtv (com_xewebtv) component for Joomla! allows remote attackers to execute arbitrary SQL commands via the id parameter in a detail action to index.php.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-5306
    - Vulnerability Description: SQL injection vulnerability in admin/index.php in PG Real Estate Solution allows remote attackers to execute arbitrary SQL commands via the login_lg parameter (username).  NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-5307
    - Vulnerability Description: SQL injection vulnerability in admin/index.php in PG Roommate Finder Solution allows remote attackers to execute arbitrary SQL commands via the login_lg parameter.  NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-5409
    - Vulnerability Description: Unspecified vulnerability in the pdf.xmd module in (1) BitDefender Free Edition 10 and Antivirus Standard 10, (2) BullGuard Internet Security 8.5, and (3) Software602 Groupware Server 6.0.08.1118 allows remote attackers to cause a denial of service (application crash) or possibly execute arbitrary code via a crafted PDF file, possibly related to included compressed streams that were processed with the ASCIIHexDecode filter.  NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-5807
    - Vulnerability Description: Multiple cross-site scripting (XSS) vulnerabilities in TestLink before 1.8 RC1 allow remote attackers to inject arbitrary web script or HTML via (1) Testproject Names and (2) Testplan Names in planEdit.php, and possibly (3) Testcaseprefixes in projectview.tpl.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-5818
    - Vulnerability Description: Directory traversal vulnerability in index.php in eDreamers eDContainer 2.22, when magic_quotes_gpc is disabled, allows remote attackers to include and execute arbitrary local files via a .. (dot dot) in the lg parameter.  NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-5819
    - Vulnerability Description: Directory traversal vulnerability in eDNews_archive.php in eDreamers eDNews 2, when magic_quotes_gpc is disabled, allows remote attackers to include and execute arbitrary local files via a .. (dot dot) in the lg parameter.  NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-6285
    - Vulnerability Description: SQL injection vulnerability in index.php in PHP TV Portal 2.0 and earlier allows remote attackers to execute arbitrary SQL commands via the mid parameter.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-6387
    - Vulnerability Description: Quick Tree View .NET 3.1 stores sensitive information under the web root with insufficient access control, which allows remote attackers to download the database file via a direct request to qtv.mdb.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-6641
    - Vulnerability Description: Multiple SQL injection vulnerabilities in Shader TV (Beta) allow remote authenticated administrators to execute arbitrary SQL commands via the sid parameter to (1) kanal.asp, (2) google.asp, and (3) hakk.asp in yonet/
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-6827
    - Vulnerability Description: The ListView control in the Client GUI (AClient.exe) in Symantec Altiris Deployment Solution 6.x before 6.9.355 SP1 allows local users to gain SYSTEM privileges and execute arbitrary commands via a "Shatter" style attack on the "command prompt" hidden GUI button to (1) overwrite the CommandLine parameter to cmd.exe to use SYSTEM privileges and (2) modify the DLL that is loaded using the LoadLibrary API function.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-6927
    - Vulnerability Description: Multiple cross-site scripting (XSS) vulnerabilities in autoinstall4imagesgalleryupgrade.php in the Fantastico De Luxe Module for cPanel allow remote attackers to inject arbitrary web script or HTML via the (1) localapp, (2) updatedir, (3) scriptpath_show, (4) domain_show, (5) thispage, (6) thisapp, and (7) currentversion parameters in an Upgrade action.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-7029
    - Vulnerability Description: Unrestricted file upload vulnerability in usercp.php in AlilG Application AliBoard Beta allows remote authenticated users to execute arbitrary code by uploading a file with an executable extension as an avatar, then accessing it via a direct request to the file in uploads/avatars/.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-7045
    - Vulnerability Description: AJ Square Free Polling Script (AJPoll) Database version allows remote attackers to bypass authentication and reset poll votes via a direct request to admin/resetvote.php.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-7122
    - Vulnerability Description: Multiple insecure method vulnerabilities in an ActiveX control in (epRegPro.ocx) in Evans Programming Registry Pro allow remote attackers to read and modify sensitive registry keys via the (1) About, (2) CreateKey, (3) DeleteBranch, (4) DeleteKey, (5) DeleteValue, (6) EnumKeys, (7) EnumValues, (8) QueryType, (9) QueryValue, (10) RenameKey, and (11) SetValue methods.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-0002
    - Vulnerability Description: Heap-based buffer overflow in Apple QuickTime before 7.6 allows remote attackers to cause a denial of service (application termination) and possibly execute arbitrary code via a QTVR movie file with crafted THKD atoms.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-0049
    - Vulnerability Description: Belgian eID middleware (eidlib) 2.6.0 and earlier does not properly check the return value from the OpenSSL EVP_VerifyFinal function, which allows remote attackers to bypass validation of the certificate chain via a malformed SSL/TLS signature for DSA and ECDSA keys, a similar vulnerability to CVE-2008-5077.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-0388
    - Vulnerability Description: Multiple integer signedness errors in (1) UltraVNC 1.0.2 and 1.0.5 and (2) TightVnc 1.3.9 allow remote VNC servers to cause a denial of service (heap corruption and application crash) or possibly execute arbitrary code via a large length value in a message, related to the (a) ClientConnection::CheckBufferSize and (b) ClientConnection::CheckFileZipBufferSize functions in ClientConnection.cpp.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-0450
    - Vulnerability Description: Stack-based buffer overflow in BlazeVideo HDTV Player 3.5 and earlier allows remote attackers to execute arbitrary code via a long string in a playlist (aka .plf) file.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-0568
    - Vulnerability Description: The RPC Marshalling Engine (aka NDR) in Microsoft Windows 2000 SP4, XP SP2 and SP3, Server 2003 SP2, Vista Gold, SP1, and SP2, and Server 2008 SP2 does not properly maintain its internal state, which allows remote attackers to overwrite arbitrary memory locations via a crafted RPC message that triggers incorrect pointer reading, related to "IDL interfaces containing a non-conformant varying array" and FC_SMVARRAY, FC_LGVARRAY, FC_VARIABLE_REPEAT, and FC_VARIABLE_OFFSET, aka "RPC Marshalling Engine Vulnerability."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-0586
    - Vulnerability Description: Integer overflow in the gst_vorbis_tag_add_coverart function (gst-libs/gst/tag/gstvorbistag.c) in vorbistag in gst-plugins-base (aka gstreamer-plugins-base) before 0.10.23 in GStreamer allows context-dependent attackers to execute arbitrary code via a crafted COVERART tag that is converted from a base64 representation, which triggers a heap-based buffer overflow.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-0699
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in pagesUTF8/auftrag_allgemeinauftrag.jsp in Plunet BusinessManager 4.1 and earlier allows remote authenticated users to inject arbitrary web script or HTML via the (1) QUB and (2) Bez74 parameters.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-0803
    - Vulnerability Description: SmoothWall SmoothGuardian, as used in SmoothWall Firewall, NetworkGuardian, and SchoolGuardian 2008, when transparent interception mode is enabled, uses the HTTP Host header to determine the remote endpoint, which allows remote attackers to bypass access controls for Flash, Java, Silverlight, and probably other technologies, and possibly communicate with restricted intranet sites, via a crafted web page that causes a client to send HTTP requests with a modified Host header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-0819
    - Vulnerability Description: sql/item_xmlfunc.cc in MySQL 5.1 before 5.1.32 and 6.0 before 6.0.10 allows remote authenticated users to cause a denial of service (crash) via "an XPath expression employing a scalar expression as a FilterExpr with ExtractValue() or UpdateXML()," which triggers an assertion failure.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-1190
    - Vulnerability Description: Algorithmic complexity vulnerability in the java.util.regex.Pattern.compile method in Sun Java Development Kit (JDK) before 1.6, when used with spring.jar in SpringSource Spring Framework 1.1.0 through 2.5.6 and 3.0.0.M1 through 3.0.0.M2 and dm Server 1.0.0 through 1.0.2, allows remote attackers to cause a denial of service (CPU consumption) via serializable data with a long regex string containing multiple optional groups, a related issue to CVE-2004-2540.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-1370
    - Vulnerability Description: Stack-based buffer overflow in ape_plugin.plg in Xilisoft Video Converter 3.1.53.0704n and 5.1.23.0402 allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via a long string in a .cue file.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-1428
    - Vulnerability Description: Multiple cross-site scripting (XSS) vulnerabilities in ccLgView.exe in the Symantec Log Viewer, as used in Symantec AntiVirus (SAV) before 10.1 MR8, Symantec Endpoint Protection (SEP) 11.0 before 11.0 MR1, Norton 360 1.0, and Norton Internet Security 2005 through 2008, allow remote attackers to inject arbitrary web script or HTML via a crafted e-mail message, related to "two parsing errors."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-1457
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in player.php in Nuke Evolution Xtreme 2.x allows remote attackers to inject arbitrary web script or HTML via the defaultVisualExt parameter.  NOTE: the provenance of this information is unknown
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-1748
    - Vulnerability Description: Multiple directory traversal vulnerabilities in index.php in Catviz 0.4.0 Beta 1 allow remote attackers to read arbitrary files via a .. (dot dot) in the (1) webpages_form or (2) userman_form parameter.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-1749
    - Vulnerability Description: Multiple cross-site scripting (XSS) vulnerabilities in index.php in Catviz 0.4.0 beta 1 allow remote attackers to inject arbitrary web script or HTML via the (1) userman_form and (2) webpages_form parameters.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-2101
    - Vulnerability Description: Directory traversal vulnerability in archive.php in TorrentVolve 1.4, when register_globals is enabled, allows remote attackers to delete arbitrary files via a .. (dot dot) in the deleteTorrent parameter.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-2155
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in report/ReportViewAction.do in WebNMS Free Edition 5 allows remote attackers to inject arbitrary web script or HTML via the type parameter.  NOTE: the provenance of this information is unknown
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-2172
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in forum/radioandtv.php in the Radio and TV Player addon for vBulletin allows remote registered users to inject arbitrary web script or HTML via the station parameter.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-2275
    - Vulnerability Description: Directory traversal vulnerability in frontend/x3/stats/lastvisit.html in cPanel allows remote attackers to read arbitrary files via a .. (dot dot) in the domain parameter.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-2339
    - Vulnerability Description: SQL injection vulnerability in index.php in Rentventory allows remote attackers to execute arbitrary SQL commands via the product parameter.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-2437
    - Vulnerability Description: Multiple cross-site scripting (XSS) vulnerabilities in index.php in Rentventory 1.0.1 allow remote attackers to inject arbitrary web script or HTML via the (1) username (aka Login) and (2) password parameters in a login action.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-2924
    - Vulnerability Description: Multiple SQL injection vulnerabilities in Videos Broadcast Yourself 2 allow remote attackers to execute arbitrary SQL commands via the (1) UploadID parameter to videoint.php, and possibly the (2) cat_id parameter to catvideo.php and (3) uid parameter to cviewchannels.php.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-2950
    - Vulnerability Description: Heap-based buffer overflow in the GIFLZWDecompressor::GIFLZWDecompressor function in filter.vcl/lgif/decode.cxx in OpenOffice.org (OOo) before 3.2 allows remote attackers to cause a denial of service (application crash) or possibly execute arbitrary code via a crafted GIF file, related to LZW decompression.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-2970
    - Vulnerability Description: Stack-based buffer overflow in the GetUiDllVersion function in an ActiveX control in UiCheck.dll before 1.0.0.7 in UiTV UiPlayer, as used in BaiduX and other products, allows remote attackers to execute arbitrary code via the filename parameter.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-2973
    - Vulnerability Description: Google Chrome before 2.0.172.43 does not prevent SSL connections to a site with an X.509 certificate signed with the (1) MD2 or (2) MD4 algorithm, which makes it easier for man-in-the-middle attackers to spoof arbitrary HTTPS servers via a crafted certificate, a related issue to CVE-2009-2409.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-3045
    - Vulnerability Description: Opera before 10.00 trusts root X.509 certificates signed with the MD2 algorithm, which makes it easier for man-in-the-middle attackers to spoof arbitrary SSL servers via a crafted server certificate.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-3086
    - Vulnerability Description: A certain algorithm in Ruby on Rails 2.1.0 through 2.2.2, and 2.3.x before 2.3.4, leaks information about the complexity of message-digest signature verification in the cookie store, which might allow remote attackers to forge a digest via multiple attempts.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-3149
    - Vulnerability Description: Directory traversal vulnerability in _css/js.php in Elgg 1.5, when magic_quotes_gpc is disabled, allows remote attackers to read arbitrary files via a .. (dot dot) in the js parameter.  NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-3251
    - Vulnerability Description: include/utils/ListViewUtils.php in vtiger CRM before 5.1.0 allows remote authenticated users to bypass intended access restrictions and read the (1) visibility, (2) location, and (3) recurrence fields of a calendar via a custom view.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-3448
    - Vulnerability Description: npvmgr.exe in BakBone NetVault Backup 8.22 Build 29 allows remote attackers to cause a denial of service (daemon crash) via a packet to (1) TCP or (2) UDP port 20031 with a large value in an unspecified size field, which is not properly handled in a malloc operation.  NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-3511
    - Vulnerability Description: Multiple PHP remote file inclusion vulnerabilities in justVisual 1.2 allow remote attackers to execute arbitrary PHP code via a URL in the fs_jVroot parameter to (1) sites/site/pages/index.php, (2) sites/test/pages/contact.php, (3) system/pageTemplate.php, and (4) system/utilities.php.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-3622
    - Vulnerability Description: Algorithmic complexity vulnerability in wp-trackback.php in WordPress before 2.8.5 allows remote attackers to cause a denial of service (CPU consumption and server hang) via a long title parameter in conjunction with a charset parameter composed of many comma-separated "UTF-8" substrings, related to the mb_convert_encoding function in PHP.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-3633
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in the t3lib_div::quoteJSvalue API function in TYPO3 4.0.13 and earlier, 4.1.x before 4.1.13, 4.2.x before 4.2.10, and 4.3.x before 4.3beta2 allows remote attackers to inject arbitrary web script or HTML via unspecified vectors related to the sanitizing algorithm.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-3695
    - Vulnerability Description: Algorithmic complexity vulnerability in the forms library in Django 1.0 before 1.0.4 and 1.1 before 1.1.1 allows remote attackers to cause a denial of service (CPU consumption) via a crafted (1) EmailField (email address) or (2) URLField (URL) that triggers a large amount of backtracking in a regular expression.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-3812
    - Vulnerability Description: Heap-based buffer overflow in OtsAV DJ trial version 1.85.64.0, Radio trial version 1.85.64.0, TV trial version 1.85.64.0, and Free version 1.77.001 allows remote attackers to execute arbitrary code via a long playlist in an Ots File List (.ofl) file.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-4006
    - Vulnerability Description: Stack-based buffer overflow in the TEA decoding algorithm in RhinoSoft Serv-U FTP server 7.0.0.1, 9.0.0.5, and other versions before 9.1.0.0 allows remote attackers to execute arbitrary code via a long hexadecimal string.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-4237
    - Vulnerability Description: Multiple cross-site scripting (XSS) vulnerabilities in TestLink before 1.8.5 allow remote attackers to inject arbitrary web script or HTML via (1) the req parameter to login.php, and allow remote authenticated users to inject arbitrary web script or HTML via (2) the key parameter to lib/general/staticPage.php, (3) the tableName parameter to lib/attachments/attachmentupload.php, or the (4) startDate, (5) endDate, or (6) logLevel parameter to lib/events/eventviewer.php
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-4238
    - Vulnerability Description: Multiple SQL injection vulnerabilities in TestLink before 1.8.5 allow remote authenticated users to execute arbitrary SQL commands via (1) the Test Case ID field to lib/general/navBar.php or (2) the logLevel parameter to lib/events/eventviewer.php.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-4269
    - Vulnerability Description: The password hash generation algorithm in the BUILTIN authentication functionality for Apache Derby before 10.6.1.0 performs a transformation that reduces the size of the set of inputs to SHA-1, which produces a small search space that makes it easier for local and possibly remote attackers to crack passwords by generating hash collisions, related to password substitution.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-4482
    - Vulnerability Description: Buffer overflow in MediaServer.exe in TVersity 1.6 allows remote attackers to execute arbitrary code via unspecified vectors, as demonstrated by the vd_tversity module in VulnDisco Pack Professional 8.11.  NOTE: as of 20091229, this disclosure has no actionable information. However, because the VulnDisco Pack author is a reliable researcher, the issue is being assigned a CVE identifier for tracking purposes.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-4717
    - Vulnerability Description: Multiple cross-site scripting (XSS) vulnerabilities in Gonafish WebStatCaffe allow remote attackers to inject arbitrary web script or HTML via the (1) host parameter to stat/host.php, nodayshow parameter to (2) mostvisitpage.php and (3) visitorduration.php in stat/, (4) nopagesmost parameter to stat/mostvisitpagechart.php, and date parameter to (5) pageviewers.php, (6) pageviewerschart.php, and (7) referer.php in stat/.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-4842
    - Vulnerability Description: Multiple cross-site scripting (XSS) vulnerabilities in ToutVirtual VirtualIQ Pro 3.5 build 8691 allow remote attackers to inject arbitrary web script or HTML via the (1) addNewDept, (2) deptId, or (3) deptDesc parameter to tvserver/server/user/addDepartment.jsp
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-4843
    - Vulnerability Description: ToutVirtual VirtualIQ Pro before 3.5 build 8691 does not require administrative authentication for JBoss console access, which allows remote attackers to execute arbitrary commands via requests to (1) the JMX Management Console or (2) the Web Console.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-4844
    - Vulnerability Description: ToutVirtual VirtualIQ Pro 3.2 build 7882 does not restrict access to the /status URI on port 9080, which allows remote attackers to obtain sensitive Tomcat information via a direct request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-4845
    - Vulnerability Description: The configuration page in ToutVirtual VirtualIQ Pro 3.2 build 7882 contains cleartext SSH credentials, which allows remote attackers to obtain sensitive information by reading the username and password fields.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-4848
    - Vulnerability Description: Multiple cross-site scripting (XSS) vulnerabilities in ToutVirtual VirtualIQ Pro 3.2 build 7882 and 3.5 build 8691 allow remote attackers to inject arbitrary web script or HTML via the (1) userId parameter to tvserver/server/user/setPermissions.jsp, (2) deptName parameter to tvserver/server/user/addDepartment.jsp, (3) ID parameter to tvserver/server/inventory/inventoryTabs.jsp, (4) reportName parameter to tvserver/reports/virtualIQAdminReports.do, or (5) middleName parameter in a save action to tvserver/user/user.do.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-4849
    - Vulnerability Description: Multiple cross-site request forgery (CSRF) vulnerabilities in ToutVirtual VirtualIQ Pro 3.2 build 7882 and 3.5 build 8691 allow remote attackers to hijack the authentication of administrators for requests that (1) create a new user account via a save action to tvserver/user/user.do, (2) shutdown a virtual machine, (3) start a virtual machine, (4) restart a virtual machine, or (5) schedule an activity.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-5071
    - Vulnerability Description: Unspecified vulnerability in Palm Pre WebOS before 1.2.1 has unknown impact and attack vectors related to an "included contact template file."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-5097
    - Vulnerability Description: Palm Pre WebOS 1.1 and earlier processes JavaScript in email messages, which allows remote attackers to execute arbitrary JavaScript, as demonstrated by reading PalmDatabase.db3.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-5098
    - Vulnerability Description: The LunaSysMgr process in Palm Pre WebOS 1.1 and earlier, when not viewing web pages in landscape mode, allows remote attackers to cause a denial of service (crash) via a web page containing a long string following a refresh tag, which triggers a floating point exception.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-5102
    - Vulnerability Description: SQL injection vulnerability in default.asp in ATCOM Netvolution 1.0 ASP allows remote attackers to execute arbitrary SQL commands via the bpe_nid parameter.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-5103
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in ATCOM Netvolution 1.0 ASP allows remote attackers to inject arbitrary web script or HTML via the email variable.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-0039
    - Vulnerability Description: The Application-Level Gateway (ALG) on the Apple Time Capsule, AirPort Extreme Base Station, and AirPort Express Base Station with firmware before 7.5.2 modifies PORT commands in incoming FTP traffic, which allows remote attackers to use the device's IP address for arbitrary intranet TCP traffic by leveraging write access to an intranet FTP server.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-0232
    - Vulnerability Description: The kernel in Microsoft Windows NT 3.1 through Windows 7, including Windows 2000 SP4, Windows XP SP2 and SP3, Windows Server 2003 SP2, Windows Vista Gold, SP1, and SP2, and Windows Server 2008 Gold and SP2, when access to 16-bit applications is enabled on a 32-bit x86 platform, does not properly validate certain BIOS calls, which allows local users to gain privileges by crafting a VDM_TIB data structure in the Thread Environment Block (TEB), and then calling the NtVdmControl function to start the Windows Virtual DOS Machine (aka NTVDM) subsystem, leading to improperly handled exceptions involving the #GP trap handler (nt!KiTrap0D), aka "Windows Kernel Exception Handler Vulnerability."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-0331
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in the TV21 Talkshow (tv21_talkshow) extension 1.0.1 and earlier for TYPO3 allows remote attackers to inject arbitrary web script or HTML via unspecified vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-0332
    - Vulnerability Description: SQL injection vulnerability in the TV21 Talkshow (tv21_talkshow) extension 1.0.1 and earlier for TYPO3 allows remote attackers to execute arbitrary SQL commands via unspecified vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-0635
    - Vulnerability Description: SQL injection vulnerability in the plgSearchEventsearch::onSearch method in eventsearch.php in the JEvents Search plugin 1.5 through 1.5.3 for Joomla! allows remote attackers to execute arbitrary SQL commands via unspecified vectors.  NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-0923
    - Vulnerability Description: Race condition in workspace/krunner/lock/lockdlg.cc in the KRunner lock module in kdebase in KDE SC 4.4.0 allows physically proximate attackers to bypass KScreenSaver screen locking and access an unattended workstation by pressing the Enter key at a certain time, related to multiple forked processes.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-0928
    - Vulnerability Description: OpenSSL 0.9.8i on the Gaisler Research LEON3 SoC on the Xilinx Virtex-II Pro FPGA uses a Fixed Width Exponentiation (FWE) algorithm for certain signature calculations, and does not verify the signature before providing it to a caller, which makes it easier for physically proximate attackers to determine the private key via a modified supply voltage for the microprocessor, related to a "fault-based attack."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-1236
    - Vulnerability Description: The protocolIs function in platform/KURLGoogle.cpp in WebCore in WebKit before r55822, as used in Google Chrome before 4.1.249.1036 and Flock Browser 3.x before 3.0.0.4112, does not properly handle whitespace at the beginning of a URL, which allows remote attackers to conduct cross-site scripting (XSS) attacks via a crafted javascript: URL, as demonstrated by a \x00javascript:alert sequence.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-1268
    - Vulnerability Description: Directory traversal vulnerability in index.php in justVisual CMS 2.0, when magic_quotes_gpc is disabled, allows remote attackers to include and execute arbitrary local files directory traversal sequences in the p parameter.  NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-1470
    - Vulnerability Description: Directory traversal vulnerability in the Web TV (com_webtv) component 1.0 for Joomla! allows remote attackers to read arbitrary files and possibly have unspecified other impact via a .. (dot dot) in the controller parameter to index.php.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-1537
    - Vulnerability Description: Multiple directory traversal vulnerabilities in phpCDB 1.0 and earlier allow remote attackers to include and execute arbitrary local files via a .. (dot dot) in the lang_global parameter to (1) firstvisit.php, (2) newfolder.php, (3) showfolders.php, (4) newlang.php, (5) showinnerfolder.php, (6) writecode.php, and (7) showcode.php.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-2468
    - Vulnerability Description: The S2 Security NetBox 2.x and 3.x, as used in the Linear eMerge 50 and 5000 and the Sonitrol eAccess, uses a weak hash algorithm for storing the Administrator password, which makes it easier for context-dependent attackers to obtain privileged access by recovering the cleartext of this password.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-2498
    - Vulnerability Description: The psh_glyph_find_strong_points function in pshinter/pshalgo.c in FreeType before 2.4.0 does not properly implement hinting masks, which allows remote attackers to cause a denial of service (heap memory corruption and application crash) or possibly execute arbitrary code via a crafted font file that triggers an invalid free operation.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-2648
    - Vulnerability Description: The implementation of the Unicode Bidirectional Algorithm (aka Bidi algorithm or UBA) in Google Chrome before 5.0.375.99 allows remote attackers to cause a denial of service (memory corruption) or possibly have unspecified other impact via unknown vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-2909
    - Vulnerability Description: SQL injection vulnerability in ttvideo.php in the TTVideo (com_ttvideo) component 1.0 for Joomla! allows remote attackers to execute arbitrary SQL commands via the cid parameter in a video action to index.php.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-2967
    - Vulnerability Description: The loginDefaultEncrypt algorithm in loginLib in Wind River VxWorks before 6.9 does not properly support a large set of distinct possible passwords, which makes it easier for remote attackers to obtain access via a (1) telnet, (2) rlogin, or (3) FTP session.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-2978
    - Vulnerability Description: Cisco Unified Wireless Network (UWN) Solution 7.x before 7.0.98.0 does not use an adequate message-digest algorithm for a self-signed certificate, which allows remote attackers to bypass intended access restrictions via vectors involving collisions, aka Bug ID CSCtd67660.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-3128
    - Vulnerability Description: Untrusted search path vulnerability in TeamViewer 5.0.8703 and earlier allows local users, and possibly remote attackers, to execute arbitrary code and conduct DLL hijacking attacks via a Trojan horse dwmapi.dll that is located in the same folder as a .tvs or .tvc file.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-3167
    - Vulnerability Description: The nsTreeContentView function in Mozilla Firefox before 3.5.12 and 3.6.x before 3.6.9, Thunderbird before 3.0.7 and 3.1.x before 3.1.3, and SeaMonkey before 2.0.7 does not properly handle node removal in XUL trees, which allows remote attackers to execute arbitrary code via vectors involving access to deleted memory, related to a "dangling pointer vulnerability."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-3329
    - Vulnerability Description: mshtmled.dll in Microsoft Internet Explorer 7 and 8 allows remote attackers to execute arbitrary code via a crafted Microsoft Office document that causes the HtmlDlgHelper class destructor to access uninitialized memory, aka "Uninitialized Memory Corruption Vulnerability."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-3397
    - Vulnerability Description: Untrusted search path vulnerability in PGP Desktop 9.9.0 Build 397, 9.10.x, 10.0.0 Build 2732, and probably other versions allows local users, and possibly remote attackers, to execute arbitrary code and conduct DLL hijacking attacks via a Trojan horse tsp.dll or tvttsp.dll that is located in the same folder as a .p12, .pem, .pgp, .prk, .prvkr, .pubkr, .rnd, or .skr file.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-3404
    - Vulnerability Description: Multiple SQL injection vulnerabilities in eshtery CMS (aka eshtery.com) allow remote attackers to execute arbitrary SQL commands via the (1) Criteria field in an unspecified form related to catlgsearch.aspx or (2) user name to an unspecified form related to adminlogin.aspx.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-3614
    - Vulnerability Description: named in ISC BIND 9.x before 9.6.2-P3, 9.7.x before 9.7.2-P3, 9.4-ESV before 9.4-ESV-R4, and 9.6-ESV before 9.6-ESV-R3 does not properly determine the security status of an NS RRset during a DNSKEY algorithm rollover, which might allow remote attackers to cause a denial of service (DNSSEC validation error) by triggering a rollover.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-3679
    - Vulnerability Description: Oracle MySQL 5.1 before 5.1.49 allows remote authenticated users to cause a denial of service (mysqld daemon crash) via certain arguments to the BINLOG command, which triggers an access of uninitialized memory, as demonstrated by valgrind.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-3802
    - Vulnerability Description: Integer signedness error in Apple QuickTime before 7.6.9 allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted panorama atom in a QuickTime Virtual Reality (QTVR) movie file.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-3804
    - Vulnerability Description: The JavaScript implementation in WebKit in Apple Safari before 5.0.3 on Mac OS X 10.5 through 10.6 and Windows, and before 4.1.3 on Mac OS X 10.4, uses a weak algorithm for generating values of random numbers, which makes it easier for remote attackers to track a user by predicting a value, a related issue to CVE-2008-5913 and CVE-2010-3171.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-4025
    - Vulnerability Description: Unspecified vulnerability in Doc Viewer in HP Palm webOS 1.4.1 allows remote attackers to execute arbitrary code via a crafted document, as demonstrated by a Word document.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-4026
    - Vulnerability Description: Unspecified vulnerability in the service API in HP Palm webOS 1.4.1 allows local users to gain privileges by leveraging the ability to perform certain service calls.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-4027
    - Vulnerability Description: Unspecified vulnerability in the camera application in HP Palm webOS 1.4.1 allows local users to overwrite arbitrary files via unknown vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-4079
    - Vulnerability Description: The ivtvfb_ioctl function in drivers/media/video/ivtv/ivtvfb.c in the Linux kernel before 2.6.36-rc8 does not properly initialize a certain structure member, which allows local users to obtain potentially sensitive information from kernel stack memory via an FBIOGET_VBLANK ioctl call.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-4109
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in the Contacts Application in HP Palm webOS before 2.0 allows remote attackers to inject arbitrary web script or HTML via a crafted vCard file.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-4302
    - Vulnerability Description: /opt/rv/Versions/CurrentVersion/Mcu/Config/Mcu.val in Cisco Unified Videoconferencing (UVC) System 5110 and 5115, when the Linux operating system is used, uses a weak hashing algorithm for the (1) administrator and (2) operator passwords, which makes it easier for local users to obtain sensitive information by recovering the cleartext values, aka Bug ID CSCti54010.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-4407
    - Vulnerability Description: Multiple cross-site scripting (XSS) vulnerabilities in index.php in AlGuest 1.1c-patched allow remote attackers to inject arbitrary web script or HTML via the (1) nome (nickname), (2) messaggio (message), and (3) link (homepage) parameters.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-4472
    - Vulnerability Description: Unspecified vulnerability in the Java Runtime Environment (JRE) in Oracle Java SE and Java for Business 6 Update 23 and earlier allows remote attackers to affect availability, related to XML Digital Signature and unspecified APIs.  NOTE: the previous information was obtained from the February 2011 CPU.  Oracle has not commented on claims from a downstream vendor that this issue involves the replacement of the "XML DSig Transform or C14N algorithm implementations."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-4618
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in the Algis Info aiContactSafe component before 2.0.14 for Joomla! allows remote attackers to inject arbitrary web script or HTML via unspecified vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-4966
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in default.asp in ATCOM Netvolution allows remote attackers to inject arbitrary web script or HTML via the query parameter in a Search action.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-4967
    - Vulnerability Description: SQL injection vulnerability in default.asp in ATCOM Netvolution 2.5.6 allows remote attackers to execute arbitrary SQL commands via the artID parameter.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-5208
    - Vulnerability Description: Multiple untrusted search path vulnerabilities in the (1) Presentation, (2) Writer, and (3) Spreadsheets components in Kingsoft Office 2010 6.6.0.2477 allow local users to gain privileges via a Trojan horse plgpf.dll file in the current working directory, as demonstrated by a directory that contains a .xls, .ppt, .rtf, or .doc file.  NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-5217
    - Vulnerability Description: Multiple untrusted search path vulnerabilities in TuneUp Utilities 2009 8.0.3310 and 2010 9.0.4600 allow local users to gain privileges via a Trojan horse (1) wscapi.dll or (2) vclib32.dll file in the current working directory, as demonstrated by a directory that contains a .tvs file.  NOTE: the provenance of this information is unknown
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-5235
    - Vulnerability Description: Untrusted search path vulnerability in IZArc Archiver 4.1.2 allows local users to gain privileges via a Trojan horse ztv7z.dll file in the current working directory, as demonstrated by a directory that contains a .arj file.  NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-5278
    - Vulnerability Description: Directory traversal vulnerability in manager/controllers/default/resource/tvs.php in MODx Revolution 2.0.2-pl, and possibly earlier, when magic_quotes_gpc is disabled, allows remote attackers to read arbitrary files via a .. (dot dot) in the class_key parameter.  NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-0009
    - Vulnerability Description: Best Practical Solutions RT 3.x before 3.8.9rc2 and 4.x before 4.0.0rc4 uses the MD5 algorithm for password hashes, which makes it easier for context-dependent attackers to determine cleartext passwords via a brute-force attack on the database.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-0032
    - Vulnerability Description: Untrusted search path vulnerability in DirectShow in Microsoft Windows Vista SP1 and SP2, Windows 7 Gold and SP1, Windows Server 2008 R2 and R2 SP1, and Windows Media Center TV Pack for Windows Vista allows local users to gain privileges via a Trojan horse DLL in the current working directory, as demonstrated by a directory that contains a Digital Video Recording (.dvr-ms), Windows Recorded TV Show (.wtv), or .mpg file, aka "DirectShow Insecure Library Loading Vulnerability."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-0042
    - Vulnerability Description: SBE.dll in the Stream Buffer Engine in Windows Media Player and Windows Media Center in Microsoft Windows XP SP2 and SP3, Windows XP Media Center Edition 2005 SP3, Windows Vista SP1 and SP2, Windows 7 Gold and SP1, and Windows Media Center TV Pack for Windows Vista does not properly parse Digital Video Recording (.dvr-ms) files, which allows remote attackers to execute arbitrary code via a crafted file, aka "DVR-MS Vulnerability."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-0043
    - Vulnerability Description: Kerberos in Microsoft Windows XP SP2 and SP3 and Server 2003 SP2 supports weak hashing algorithms, which allows local users to gain privileges by operating a service that sends crafted service tickets, as demonstrated by the CRC32 algorithm, aka "Kerberos Unkeyed Checksum Vulnerability."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-0162
    - Vulnerability Description: Wi-Fi in Apple iOS before 4.3 and Apple TV before 4.2 does not properly perform bounds checking for Wi-Fi frames, which allows remote attackers to cause a denial of service (device reset) via unspecified traffic on the local wireless network.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-1180
    - Vulnerability Description: Multiple stack-based buffer overflows in the iriap_getvaluebyclass_indication function in net/irda/iriap.c in the Linux kernel before 2.6.39 allow remote attackers to cause a denial of service (memory corruption) or possibly have unspecified other impact by leveraging connectivity to an IrDA infrared network and sending a large integer value for a (1) name length or (2) attribute length.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-1209
    - Vulnerability Description: IBM WebSphere Application Server (WAS) 6.1 before 6.1.0.39 and 7.0 before 7.0.0.17 uses a weak WS-Security XML encryption algorithm, which makes it easier for remote attackers to obtain plaintext data from a (1) JAX-RPC or (2) JAX-WS Web Services request via unspecified vectors related to a "decryption attack."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-1323
    - Vulnerability Description: Yamaha RTX, RT, SRT, RTV, RTW, and RTA series routers with firmware 6.x through 10.x, and NEC IP38X series routers with firmware 6.x through 10.x, do not properly handle IP header options, which allows remote attackers to cause a denial of service (device reboot) via a crafted option that triggers access to an invalid memory location.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-1418
    - Vulnerability Description: The stateless address autoconfiguration (aka SLAAC) functionality in the IPv6 networking implementation in Apple iOS before 4.3 and Apple TV before 4.2 places the MAC address into the IPv6 address, which makes it easier for remote IPv6 servers to track users by logging source IPv6 addresses.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-1737
    - Vulnerability Description: Multiple cross-site scripting (XSS) vulnerabilities in the Email application in HP Palm webOS 1.4.5 and 1.4.5.1 allow remote attackers to inject arbitrary web script or HTML via unspecified vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-1738
    - Vulnerability Description: HP Palm webOS 1.4.5 and 1.4.5.1 does not properly restrict Plug-in Development Kit (PDK) applications, which allows local users to gain privileges by leveraging unintended filesystem write access.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-1823
    - Vulnerability Description: The vold volume manager daemon on Android 3.0 and 2.x before 2.3.4 trusts messages that are received from a PF_NETLINK socket, which allows local users to execute arbitrary code and gain root privileges via a negative index that bypasses a maximum-only signed integer check in the DirectVolume::handlePartitionAdded method, which triggers memory corruption, as demonstrated by Gingerbreak.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-1945
    - Vulnerability Description: The elliptic curve cryptography (ECC) subsystem in OpenSSL 1.0.0d and earlier, when the Elliptic Curve Digital Signature Algorithm (ECDSA) is used for the ECDHE_ECDSA cipher suite, does not properly implement curves over binary fields, which makes it easier for context-dependent attackers to determine private keys via a timing attack and a lattice calculation.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-2009
    - Vulnerability Description: Untrusted search path vulnerability in Windows Media Center in Microsoft Windows Vista SP2 and Windows 7 Gold and SP1, and Windows Media Center TV Pack for Windows Vista, allows local users to gain privileges via a Trojan horse DLL in the current working directory, aka "Media Center Insecure Library Loading Vulnerability."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-2082
    - Vulnerability Description: The vulnerable-passwords script in Best Practical Solutions RT 3.x before 3.8.12 and 4.x before 4.0.6 does not update the password-hash algorithm for disabled user accounts, which makes it easier for context-dependent attackers to determine cleartext passwords, and possibly use these passwords after accounts are re-enabled, via a brute-force attack on the database.  NOTE: this vulnerability exists because of an incomplete fix for CVE-2011-0009.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-2174
    - Vulnerability Description: Double free vulnerability in the tvb_uncompress function in epan/tvbuff.c in Wireshark 1.2.x before 1.2.17 and 1.4.x before 1.4.7 allows remote attackers to cause a denial of service (application crash) via a packet with malformed data that uses zlib compression.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-2408
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in the Contacts application in HP Palm webOS 3.x before 3.0.2 allows remote attackers to inject arbitrary web script or HTML via unspecified vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-2409
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in the Calendar application in HP Palm webOS 3.x before 3.0.2 allows remote attackers to inject arbitrary web script or HTML via unspecified vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-2475
    - Vulnerability Description: Format string vulnerability in ECTrace.dll in the iMailGateway service in the Internet Mail Gateway in OneBridge Server and DMZ Proxy in Sybase OneBridge Mobile Data Suite 5.5 and 5.6 allows remote attackers to execute arbitrary code via format string specifiers in unspecified string fields, related to authentication logging.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-2511
    - Vulnerability Description: Integer overflow in libvirt before 0.9.3 allows remote authenticated users to cause a denial of service (libvirtd crash) and possibly execute arbitrary code via a crafted VirDomainGetVcpus RPC call that triggers memory corruption.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-2642
    - Vulnerability Description: Multiple cross-site scripting (XSS) vulnerabilities in the table Print view implementation in tbl_printview.php in phpMyAdmin before 3.3.10.3 and 3.4.x before 3.4.3.2 allow remote authenticated users to inject arbitrary web script or HTML via a crafted table name.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-3188
    - Vulnerability Description: The (1) IPv4 and (2) IPv6 implementations in the Linux kernel before 3.1 use a modified MD4 algorithm to generate sequence numbers and Fragment Identification values, which makes it easier for remote attackers to cause a denial of service (disrupted networking) or hijack network sessions by predicting these values and sending crafted packets.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-3259
    - Vulnerability Description: The kernel in Apple iOS before 5 and Apple TV before 4.4 does not properly recover memory allocated for incomplete TCP connections, which allows remote attackers to cause a denial of service (resource consumption) by making many connection attempts.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-3340
    - Vulnerability Description: SQL injection vulnerability in ATCOM Netvolution 2.5.8 ASP allows remote attackers to execute arbitrary SQL commands via the Referer HTTP header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-3427
    - Vulnerability Description: The Data Security component in Apple iOS before 5 and Apple TV before 4.4 does not properly restrict use of the MD5 hash algorithm within X.509 certificates, which makes it easier for man-in-the-middle attackers to spoof servers or obtain sensitive information via a crafted certificate.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-3483
    - Vulnerability Description: Wireshark 1.6.x before 1.6.2 allows remote attackers to cause a denial of service (application crash) via a malformed capture file that leads to an invalid root tvbuff, related to a "buffer exception handling vulnerability."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-3487
    - Vulnerability Description: Directory traversal vulnerability in CarelDataServer.exe in Carel PlantVisor 2.4.4 and earlier allows remote attackers to read arbitrary files via a .. (dot dot) in an HTTP GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-3733
    - Vulnerability Description: Elgg 1.7.6 allows remote attackers to obtain sensitive information via a direct request to a .php file, which reveals the installation path in an error message, as demonstrated by vendors/simpletest/test/visual_test.php and certain other files.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-4042
    - Vulnerability Description: An unspecified ActiveX control in SVUIGrd.ocx in ARC Informatique PcVue 6.0 through 10.0, FrontVue, and PlantVue allows remote attackers to execute arbitrary code by using a crafted HTML document to obtain control of a function pointer.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-4043
    - Vulnerability Description: Integer overflow in an unspecified ActiveX control in SVUIGrd.ocx in ARC Informatique PcVue 6.0 through 10.0, FrontVue, and PlantVue allows remote attackers to execute arbitrary code via a large value for an integer parameter, leading to a buffer overflow.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-4044
    - Vulnerability Description: An unspecified ActiveX control in SVUIGrd.ocx in ARC Informatique PcVue 6.0 through 10.0, FrontVue, and PlantVue allows remote attackers to modify files via calls to unknown methods.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-4045
    - Vulnerability Description: Buffer overflow in an unspecified ActiveX control in aipgctl.ocx in ARC Informatique PcVue 6.0 through 10.0, FrontVue, and PlantVue allows remote attackers to cause a denial of service via a crafted HTML document.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-4081
    - Vulnerability Description: crypto/ghash-generic.c in the Linux kernel before 3.1 allows local users to cause a denial of service (NULL pointer dereference and OOPS) or possibly have unspecified other impact by triggering a failed or missing ghash_setkey function call, followed by a (1) ghash_update function call or (2) ghash_final function call, as demonstrated by a write operation on an AF_ALG socket.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-4354
    - Vulnerability Description: crypto/bn/bn_nist.c in OpenSSL before 0.9.8h on 32-bit platforms, as used in stunnel and other products, in certain circumstances involving ECDH or ECDHE cipher suites, uses an incorrect modular reduction algorithm in its implementation of the P-256 and P-384 NIST elliptic curves, which allows remote attackers to obtain the private key of a TLS server via multiple handshake attempts.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-4496
    - Vulnerability Description: Buffer overflow in Aviosoft DTV Player 1.0.1.2 allows remote attackers to execute arbitrary code via a crafted .plf (aka playlist) file.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-4515
    - Vulnerability Description: Siemens WinCC (TIA Portal) 11 uses a reversible algorithm for storing HMI web-application passwords in world-readable and world-writable files, which allows local users to obtain sensitive information by leveraging (1) physical access or (2) Sm@rt Server access.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-4532
    - Vulnerability Description: Absolute path traversal vulnerability in the ALMListView.ALMListCtrl ActiveX control in almaxcx.dll in the graphical user interface in Siemens Automation License Manager (ALM) 2.0 through 5.1+SP1+Upd2 allows remote attackers to overwrite arbitrary files via the Save method.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-4670
    - Vulnerability Description: Multiple cross-site scripting (XSS) vulnerabilities in vTiger CRM 5.2.1 and earlier allow remote attackers to inject arbitrary web script or HTML via the (1) viewname parameter in a CalendarAjax action, (2) activity_mode parameter in a DetailView action, (3) contact_id and (4) parent_id parameters in an EditView action, (5) day, (6) month, (7) subtab, (8) view, and (9) viewOption parameters in the index action, and (10) start parameter in the ListView action to the Calendar module
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-4873
    - Vulnerability Description: Unspecified vulnerability in the server in Certec EDV atvise before 2.1 allows remote attackers to cause a denial of service (daemon crash) via crafted requests to TCP port 4840.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-4880
    - Vulnerability Description: Directory traversal vulnerability in the web server in Certec atvise webMI2ADS (aka webMI) before 2.0.2 allows remote attackers to read arbitrary files via a crafted HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-4881
    - Vulnerability Description: The web server in Certec atvise webMI2ADS (aka webMI) before 2.0.2 does not properly check return values from functions, which allows remote attackers to cause a denial of service (NULL pointer dereference) via a crafted HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-4882
    - Vulnerability Description: The web server in Certec atvise webMI2ADS (aka webMI) before 2.0.2 allows remote attackers to cause a denial of service (application exit) via an unspecified command in an HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-4883
    - Vulnerability Description: The web server in Certec atvise webMI2ADS (aka webMI) before 2.0.2 does not properly validate values in HTTP requests, which allows remote attackers to cause a denial of service (resource consumption) via a crafted request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-5031
    - Vulnerability Description: Multiple SQL injection vulnerabilities in servlet/capexweb.parentvalidatepassword in cApexWEB 1.1 allow remote attackers to execute arbitrary SQL commands via the (1) dfuserid and (2) dfpassword parameters.  NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-5115
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in DLGuard, possibly 4.6 and earlier, allows remote attackers to inject arbitrary web script or HTML via the searchCart parameter to index.php.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-5156
    - Vulnerability Description: Untrusted search path vulnerability in Effective File Search 6.7 allows local users to gain privileges via a Trojan horse ztvunrar36.dll file in the current working directory, as demonstrated by a directory that contains a .efs file.  NOTE: the provenance of this information is unknown
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-0158
    - Vulnerability Description: The (1) ListView, (2) ListView2, (3) TreeView, and (4) TreeView2 ActiveX controls in MSCOMCTL.OCX in the Common Controls in Microsoft Office 2003 SP3, 2007 SP2 and SP3, and 2010 Gold and SP1
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-0378
    - Vulnerability Description: Cisco Adaptive Security Appliances (ASA) 5500 series devices with software 8.0 through 8.4 allow remote attackers to cause a denial of service (connection limit exceeded) by triggering a large number of stale connections that result in an incorrect value for an MPF connection count, aka Bug ID CSCtv19854.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-0667
    - Vulnerability Description: Integer signedness error in Apple QuickTime before 7.7.2 on Windows allows remote attackers to execute arbitrary code or cause a denial of service (application crash) via a crafted QTVR movie file.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-1019
    - Vulnerability Description: Multiple cross-site scripting (XSS) vulnerabilities in XWiki Enterprise 3.4 allow remote attackers to inject arbitrary web script or HTML via the (1) XWiki.XWikiComments_comment parameter to xwiki/bin/commentadd/Main/WebHome, (2) XWiki.XWikiUsers_0_company parameter when editing a user profile, or (3) projectVersion parameter to xwiki/bin/view/DownloadCode/DownloadFeedback.  NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-1148
    - Vulnerability Description: Memory leak in the poolGrow function in expat/lib/xmlparse.c in expat before 2.1.0 allows context-dependent attackers to cause a denial of service (memory consumption) via a large number of crafted XML files that cause improperly-handled reallocation failures when expanding entities.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-1399
    - Vulnerability Description: Unspecified vulnerability in the U+Box 2.0 (lg.uplusbox) application 2.0.2 and 2.0.8.4 for Android has unknown impact and attack vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-1400
    - Vulnerability Description: Unspecified vulnerability in the U+Box 2.0 Pad (lg.uplusbox.pad) application 2.0.8.4 for Android has unknown impact and attack vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-1588
    - Vulnerability Description: Algorithmic complexity vulnerability in the _filter_url function in the text filtering system (modules/filter/filter.module) in Drupal 7.x before 7.14 allows remote authenticated users with certain roles to cause a denial of service (CPU consumption) via a long email address.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-1634
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in video_filter.codecs.inc in the Video Filter module 6.x-2.x and 7.x-2.x for Drupal allows remote attackers to inject arbitrary web script or HTML via the EMBEDLOOKUP parameter for Blip.tv links.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-1653
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in the Taxonomy Views Integrator (TVI) module 6.x-1.x before 6.x-1.3 for Drupal allows remote authenticated users to inject arbitrary web script or HTML via unspecified vectors, related to "views pages."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-1838
    - Vulnerability Description: The web management interface on the LG-Nortel ELO GS24M switch allows remote attackers to bypass authentication, and consequently obtain cleartext credential and configuration information, via a direct request to a configuration web page.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-1990
    - Vulnerability Description: Multiple cross-site scripting (XSS) vulnerabilities in Schneider Electric Kerweb before 3.0.1 and Kerwin before 6.0.1 allow remote attackers to inject arbitrary web script or HTML via (1) the evtvariablename parameter in an evts.xml action to kw.dll, (2) unspecified search fields, or (3) unspecified content-display fields.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-2091
    - Vulnerability Description: Multiple buffer overflows in FlightGear 2.6 and earlier and SimGear 2.6 and earlier allow user-assisted remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via a (1) long string in a rotor tag of an aircraft xml model to the Rotor::getValueforFGSet function in src/FDM/YASim/Rotor.cpp or (2) a crafted UDP packet to the SGSocketUDP::read function in simgear/simgear/simgear/io/sg_socket_udp.cxx.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-2098
    - Vulnerability Description: Algorithmic complexity vulnerability in the sorting algorithms in bzip2 compressing stream (BZip2CompressorOutputStream) in Apache Commons Compress before 1.4.1 allows remote attackers to cause a denial of service (CPU consumption) via a file with many repeating inputs.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-2210
    - Vulnerability Description: The Sony Bravia TV KDL-32CX525 allows remote attackers to cause a denial of service (configuration outage or device crash) via a flood of TCP SYN packets, as demonstrated by hping, a related issue to CVE-1999-0116.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-2378
    - Vulnerability Description: Apache CXF 2.4.5 through 2.4.7, 2.5.1 through 2.5.3, and 2.6.x before 2.6.1, does not properly enforce child policies of a WS-SecurityPolicy 1.1 SupportingToken policy on the client side, which allows remote attackers to bypass the (1) AlgorithmSuite, (2) SignedParts, (3) SignedElements, (4) EncryptedParts, and (5) EncryptedElements policies.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-2414
    - Vulnerability Description: main/manager.c in the Manager Interface in Asterisk Open Source 1.6.2.x before 1.6.2.24, 1.8.x before 1.8.11.1, and 10.x before 10.3.1 and Asterisk Business Edition C.3.x before C.3.7.4 does not properly enforce System class authorization requirements, which allows remote authenticated users to execute arbitrary commands via (1) the originate action in the MixMonitor application, (2) the SHELL and EVAL functions in the GetVar manager action, or (3) the SHELL and EVAL functions in the Status manager action.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-2417
    - Vulnerability Description: PyCrypto before 2.6 does not produce appropriate prime numbers when using an ElGamal scheme to generate a key, which reduces the signature space or public key space and makes it easier for attackers to conduct brute force attacks to obtain the private key.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-2619
    - Vulnerability Description: The Broadcom BCM4325 and BCM4329 Wi-Fi chips, as used in certain Acer, Apple, Asus, Ford, HTC, Kyocera, LG, Malata, Motorola, Nokia, Pantech, Samsung, and Sony products, allow remote attackers to cause a denial of service (out-of-bounds read and Wi-Fi outage) via an RSN 802.11i information element.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-2743
    - Vulnerability Description: Revelation 0.4.13-2 and earlier does not iterate through SHA hashing algorithms for AES encryption, which makes it easier for context-dependent attackers to guess passwords via a brute force attack.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-3018
    - Vulnerability Description: The lockout-recovery feature in the Security Configurator component in ICONICS GENESIS32 9.22 and earlier and BizViz 9.22 and earlier uses an improper encryption algorithm for generation of an authentication code, which allows local users to bypass intended access restrictions and obtain administrative access by predicting a challenge response.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-3287
    - Vulnerability Description: Poul-Henning Kamp md5crypt has insufficient algorithmic complexity and a consequently short runtime, which makes it easier for context-dependent attackers to discover cleartext passwords via a brute-force attack, as demonstrated by an attack using GPU hardware.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-3398
    - Vulnerability Description: Algorithmic complexity vulnerability in Moodle 1.9.x before 1.9.19, 2.0.x before 2.0.10, 2.1.x before 2.1.7, and 2.2.x before 2.2.4 allows remote authenticated users to cause a denial of service (CPU consumption) by using the advanced-search feature on a database activity that has many records.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-3886
    - Vulnerability Description: AirDroid 1.0.4 beta uses the MD5 algorithm for values in the checklogin key parameter and 7bb cookie, which makes it easier for remote attackers to obtain cleartext data by sniffing the local wireless network and then conducting a (1) brute-force attack or (2) rainbow-table attack.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-4193
    - Vulnerability Description: Mozilla Firefox before 16.0.1, Firefox ESR 10.x before 10.0.9, Thunderbird before 16.0.1, Thunderbird ESR 10.x before 10.0.9, and SeaMonkey before 2.13.1 omit a security check in the defaultValue function during the unwrapping of security wrappers, which allows remote attackers to bypass the Same Origin Policy and read the properties of a Location object, or execute arbitrary JavaScript code, via a crafted web site.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-4329
    - Vulnerability Description: The Samsung D6000 TV and possibly other products allow remote attackers to cause a denial of service (continuous restart) via a crafted controller name.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-4330
    - Vulnerability Description: The Samsung D6000 TV and possibly other products allows remote attackers to cause a denial of service (crash) via a long string in certain fields, as demonstrated by the MAC address field, possibly a buffer overflow.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-4618
    - Vulnerability Description: The SIP ALG feature in the NAT implementation in Cisco IOS 12.2, 12.4, and 15.0 through 15.2 allows remote attackers to cause a denial of service (device reload) via transit IP packets, aka Bug ID CSCtn76183.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-4693
    - Vulnerability Description: Invensys Wonderware InTouch 2012 R2 and earlier and Siemens ProcessSuite use a weak encryption algorithm for data in Ps_security.ini, which makes it easier for local users to discover passwords by reading this file.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-4876
    - Vulnerability Description: Stack-based buffer overflow in the UltraMJCam ActiveX Control in TRENDnet SecurView TV-IP121WN Wireless Internet Camera allows remote attackers to execute arbitrary code via a long string to the OpenFileDlg method.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-4899
    - Vulnerability Description: WellinTech KingView 6.5.3 and earlier uses a weak password-hashing algorithm, which makes it easier for local users to discover credentials by reading an unspecified file.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-4960
    - Vulnerability Description: The Huawei NE5000E, MA5200G, NE40E, NE80E, ATN, NE40, NE80, NE20E-X6, NE20, ME60, CX600, CX200, CX300, ACU, WLAN AC 6605, S9300, S7700, S2300, S3300, S5300, S3300HI, S5300HI, S5306, S6300, S2700, S3700, S5700, S6700, AR G3, H3C AR(OEM IN), AR 19, AR 29, AR 49, Eudemon100E, Eudemon200, Eudemon300, Eudemon500, Eudemon1000, Eudemon1000E-U/USG5300, Eudemon1000E-X/USG5500, Eudemon8080E/USG9300, Eudemon8160E/USG9300, Eudemon8000E-X/USG9500, E200E-C/USG2200, E200E-X3/USG2200, E200E-X5/USG2200, E200E-X7/USG2200, E200E-C/USG5100, E200E-X3/USG5100, E200E-X5/USG5100, E200E-X7/USG5100, E200E-B/USG2100, E200E-X1/USG2100, E200E-X2/USG2100, SVN5300, SVN2000, SVN5000, SVN3000, NIP100, NIP200, NIP1000, NIP2100, NIP2200, and NIP5100 use the DES algorithm for stored passwords, which makes it easier for context-dependent attackers to obtain cleartext passwords via a brute-force attack.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-5134
    - Vulnerability Description: Heap-based buffer underflow in the xmlParseAttValueComplex function in parser.c in libxml2 2.9.0 and earlier, as used in Google Chrome before 23.0.1271.91 and other products, allows remote attackers to cause a denial of service or possibly execute arbitrary code via crafted entities in an XML document.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-5227
    - Vulnerability Description: SQL injection vulnerability in administrer/tva.php in Peel SHOPPING 2.8 and 2.9 allows remote attackers to execute arbitrary SQL commands via the id parameter.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-5370
    - Vulnerability Description: JRuby computes hash values without properly restricting the ability to trigger hash collisions predictably, which allows context-dependent attackers to cause a denial of service (CPU consumption) via crafted input to an application that maintains a hash table, as demonstrated by a universal multicollision attack against the MurmurHash2 algorithm, a different vulnerability than CVE-2011-4838.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-5371
    - Vulnerability Description: Ruby (aka CRuby) 1.9 before 1.9.3-p327 and 2.0 before r37575 computes hash values without properly restricting the ability to trigger hash collisions predictably, which allows context-dependent attackers to cause a denial of service (CPU consumption) via crafted input to an application that maintains a hash table, as demonstrated by a universal multicollision attack against a variant of the MurmurHash2 algorithm, a different vulnerability than CVE-2011-4815.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-5372
    - Vulnerability Description: Rubinius computes hash values without properly restricting the ability to trigger hash collisions predictably, which allows context-dependent attackers to cause a denial of service (CPU consumption) via crafted input to an application that maintains a hash table, as demonstrated by a universal multicollision attack against the MurmurHash3 algorithm.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-5373
    - Vulnerability Description: Oracle Java SE 7 and earlier, and OpenJDK 7 and earlier, computes hash values without properly restricting the ability to trigger hash collisions predictably, which allows context-dependent attackers to cause a denial of service (CPU consumption) via crafted input to an application that maintains a hash table, as demonstrated by a universal multicollision attack against the MurmurHash3 algorithm, a different vulnerability than CVE-2012-2739.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-5770
    - Vulnerability Description: The SSL configuration in IBM Tivoli Application Dependency Discovery Manager (TADDM) 7.2.x before 7.2.1.4 supports the MD5 hash algorithm, which makes it easier for man-in-the-middle attackers to spoof servers and decrypt network traffic via a brute-force attack.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-5777
    - Vulnerability Description: Eval injection vulnerability in the ReplaceListVars function in the template parser in e/class/connect.php in EmpireCMS 6.6 allows user-assisted remote attackers to execute arbitrary PHP code via a crafted template.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-5906
    - Vulnerability Description: Multiple cross-site scripting (XSS) vulnerabilities in GreenBrowser 6.1.0117 and 6.1.0216 allow remote attackers to inject arbitrary web script or HTML via (1) the URI in an about: page or (2) the last visited URL in the LastVisitWriteEn function in function.js.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-5951
    - Vulnerability Description: Unspecified vulnerability in IBM Tivoli NetView 1.4, 5.1 through 5.4, and 6.1 on z/OS allows local users to gain privileges by leveraging access to the normal Unix System Services (USS) security level.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-6557
    - Vulnerability Description: Multiple cross-site scripting (XSS) vulnerabilities in the AboutMe plugin 1.1.1 for Vanilla Forums allow remote attackers to inject arbitrary web script or HTML via the (1) AboutMe/RealName, (2) AboutMe/Name, (3) AboutMe/Quote, (4) AboutMe/Loc, (5) AboutMe/Emp, (6) AboutMe/JobTit, (7) AboutMe/HS, (8) AboutMe/Col, (9) AboutMe/Bio, (10) AboutMe/Inter, (11) AboutMe/Mus, (12) AboutMe/Gam, (13) AboutMe/Mov, (14) AboutMe/FTV, or (15) AboutMe/Bks parameter to the Edit My Details page.  NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-6561
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in engine/lib/views.php in Elgg before 1.8.5 allows remote attackers to inject arbitrary web script or HTML via the view parameter to index.php.  NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-6562
    - Vulnerability Description: engine/lib/users.php in Elgg before 1.8.5 does not properly specify permissions for the useradd action, which allows remote attackers to create arbitrary accounts.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-6563
    - Vulnerability Description: engine/lib/access.php in Elgg before 1.8.5 does not properly clear cached access lists during plugin boot, which allows remote attackers to read private entities via unspecified vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-0148
    - Vulnerability Description: The Data Camouflage (aka FairCom Standard Encryption) algorithm in FairCom c-treeACE does not ensure that a decryption key is needed for accessing database contents, which allows context-dependent attackers to read cleartext database records by copying a database to another system that has a certain default configuration.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-0176
    - Vulnerability Description: The publickey_from_privatekey function in libssh before 0.5.4, when no algorithm is matched during negotiations, allows remote attackers to cause a denial of service (NULL pointer dereference and crash) via a "Client: Diffie-Hellman Key Exchange Init" packet.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-0229
    - Vulnerability Description: The ProcessSSDPRequest function in minissdp.c in the SSDP handler in MiniUPnP MiniUPnPd before 1.4 allows remote attackers to cause a denial of service (service crash) via a crafted request that triggers a buffer over-read.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-0230
    - Vulnerability Description: Stack-based buffer overflow in the ExecuteSoapAction function in the SOAPAction handler in the HTTP service in MiniUPnP MiniUPnPd 1.0 allows remote attackers to execute arbitrary code via a long quoted method.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-0523
    - Vulnerability Description: IBM WebSphere Commerce Enterprise 5.6.x through 5.6.1.5, 6.0.x through 6.0.0.11, and 7.0.x through 7.0.0.7 does not use a suitable encryption algorithm for storefront web requests, which allows remote attackers to obtain sensitive information via a padding oracle attack that targets certain UTF-8 processing of the krypto parameter, and leverages unspecified browser access or traffic-log access.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-0941
    - Vulnerability Description: EMC RSA Authentication API before 8.1 SP1, RSA Web Agent before 5.3.5 for Apache Web Server, RSA Web Agent before 5.3.5 for IIS, RSA PAM Agent before 7.0, and RSA Agent before 6.1.4 for Microsoft Windows use an improper encryption algorithm and a weak key for maintaining the stored data of the node secret for the SecurID Authentication API, which allows local users to obtain sensitive information via cryptographic attacks on this data.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-0964
    - Vulnerability Description: The kernel in Apple iOS before 6.1 and Apple TV before 5.2 does not properly validate copyin and copyout arguments, which allows local users to bypass intended pointer restrictions and access locations in the first kernel-memory page by specifying a length of less than one page.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-0977
    - Vulnerability Description: dyld in Apple iOS before 6.1.3 and Apple TV before 5.2.1 does not properly manage the state of file loading for Mach-O executable files, which allows local users to bypass intended code-signing requirements via a file that contains overlapping segments.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-0978
    - Vulnerability Description: The ARM prefetch abort handler in the kernel in Apple iOS before 6.1.3 and Apple TV before 5.2.1 does not ensure that it has been invoked in an abort context, which makes it easier for local users to bypass the ASLR protection mechanism via crafted code.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-0981
    - Vulnerability Description: The IOUSBDeviceFamily driver in the USB implementation in the kernel in Apple iOS before 6.1.3 and Apple TV before 5.2.1 accesses pipe object pointers that originated in userspace, which allows local users to gain privileges via crafted code.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-1122
    - Vulnerability Description: Cisco NX-OS on the Nexus 7000, when a certain Overlay Transport Virtualization (OTV) configuration is used, allows remote attackers to cause a denial of service (M1-Series module reload) via crafted packets, aka Bug ID CSCud15673.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-1166
    - Vulnerability Description: Cisco IOS XE 3.2 through 3.4 before 3.4.5S, and 3.5 through 3.7 before 3.7.1S, on 1000 series Aggregation Services Routers (ASR), when VRF-aware NAT and SIP ALG are enabled, allows remote attackers to cause a denial of service (card reload) by sending many SIP packets, aka Bug ID CSCuc65609.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-1461
    - Vulnerability Description: The ExecuteSoapAction function in the SOAPAction handler in the HTTP service in MiniUPnP MiniUPnPd 1.0 allows remote attackers to cause a denial of service (NULL pointer dereference and service crash) via a SOAPAction header that lacks a # (pound sign) character, a different vulnerability than CVE-2013-0230.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-1462
    - Vulnerability Description: Integer signedness error in the ExecuteSoapAction function in the SOAPAction handler in the HTTP service in MiniUPnP MiniUPnPd 1.0 allows remote attackers to cause a denial of service (incorrect memory copy) via a SOAPAction header that lacks a " (double quote) character, a different vulnerability than CVE-2013-0230.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-1585
    - Vulnerability Description: epan/tvbuff.c in Wireshark 1.6.x before 1.6.13 and 1.8.x before 1.8.5 does not properly validate certain length values for the MS-MMC dissector, which allows remote attackers to cause a denial of service (application crash) via a malformed packet.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-1697
    - Vulnerability Description: The XrayWrapper implementation in Mozilla Firefox before 22.0, Firefox ESR 17.x before 17.0.7, Thunderbird before 17.0.7, and Thunderbird ESR 17.x before 17.0.7 does not properly restrict use of DefaultValue for method calls, which allows remote attackers to execute arbitrary JavaScript code with chrome privileges via a crafted web site that triggers use of a user-defined (1) toString or (2) valueOf method.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-1699
    - Vulnerability Description: The Internationalized Domain Name (IDN) display algorithm in Mozilla Firefox before 22.0 does not properly handle the .com, .name, and .net top-level domains, which allows remote attackers to spoof the address bar via unspecified homograph characters.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-1982
    - Vulnerability Description: Multiple integer overflows in X.org libXext 1.3.1 and earlier allow X servers to trigger allocation of insufficient memory and a buffer overflow via vectors related to the (1) XcupGetReservedColormapEntries, (2) XcupStoreColors, (3) XdbeGetVisualInfo, (4) XeviGetVisualInfo, (5) XShapeGetRectangles, and (6) XSyncListSystemCounters functions.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-2566
    - Vulnerability Description: The RC4 algorithm, as used in the TLS protocol and SSL protocol, has many single-byte biases, which makes it easier for remote attackers to conduct plaintext-recovery attacks via statistical analysis of ciphertext in a large number of sessions that use the same plaintext.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-2784
    - Vulnerability Description: Triangle Research International (aka Tri) Nano-10 PLC devices with firmware before r81 use an incorrect algorithm for bounds checking of data in Modbus/TCP packets, which allows remote attackers to cause a denial of service (networking outage) via a crafted packet to TCP port 502.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-2953
    - Vulnerability Description: IBM InfoSphere Optim Data Growth for Oracle E-Business Suite 6.x, 7.x, and 9.x before 9.1.0.3 relies on the MD5 algorithm for signatures in X.509 certificates, which makes it easier for man-in-the-middle attackers to spoof SSL servers via a crafted certificate.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-3076
    - Vulnerability Description: The crypto API in the Linux kernel through 3.9-rc8 does not initialize certain length variables, which allows local users to obtain sensitive information from kernel stack memory via a crafted recvmsg or recvfrom system call, related to the hash_recvmsg function in crypto/algif_hash.c and the skcipher_recvmsg function in crypto/algif_skcipher.c.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-3562
    - Vulnerability Description: Multiple integer signedness errors in the tvb_unmasked function in epan/dissectors/packet-websocket.c in the Websocket dissector in Wireshark 1.8.x before 1.8.7 allow remote attackers to cause a denial of service (application crash) via a malformed packet.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-3666
    - Vulnerability Description: The LG Hidden Menu component for Android on the LG Optimus G E973 allows physically proximate attackers to execute arbitrary commands by entering USB Debugging mode, using Android Debug Bridge (adb) to establish a USB connection, dialing 3845#*973#, modifying the WLAN Test Wi-Fi Ping Test/User Command tcpdump command string, and pressing the CANCEL button.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-3672
    - Vulnerability Description: The mm_decode_inter function in mmvideo.c in libavcodec in FFmpeg before 1.2.1 does not validate the relationship between a horizontal coordinate and a width value, which allows remote attackers to cause a denial of service (out-of-bounds array access and application crash) via crafted American Laser Games (ALG) MM Video data.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-4687
    - Vulnerability Description: flowd in Juniper Junos 10.4 before 10.4S14, 11.2 and 11.4 before 11.4R6-S2, and 12.1 before 12.1R6 on SRX devices, when certain Application Layer Gateways (ALGs) are enabled, allows remote attackers to cause a denial of service (daemon crash) via crafted TCP packets, aka PRs 727980, 806269, and 835593.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-4688
    - Vulnerability Description: flowd in Juniper Junos 10.4 before 10.4R11 on SRX devices, when the MSRPC Application Layer Gateway (ALG) is enabled, allows remote attackers to cause a denial of service (daemon crash) via crafted MSRPC requests, aka PR 772834.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-4890
    - Vulnerability Description: The DMCRUIS/0.1 web server on the Samsung PS50C7700 TV allows remote attackers to cause a denial of service (daemon crash) via a long URI to TCP port 5600.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-0779
    - Vulnerability Description: PlatinumFTP 1.0.18, and possibly earlier versions, allows remote attackers to cause a denial of service (server crash) via multiple connection attempts with a \ (backslash) in the username.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-0779
    - Vulnerability Description: PlatinumFTP 1.0.18, and possibly earlier versions, allows remote attackers to cause a denial of service (server crash) via multiple connection attempts with a \ (backslash) in the username.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-1999-0437
    - Vulnerability Description: Remote attackers can perform a denial of service in WebRamp systems by sending a malicious string to the HTTP port.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-1999-0867
    - Vulnerability Description: Denial of service in IIS 4.0 via a flood of HTTP requests with malformed headers.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-1999-0923
    - Vulnerability Description: Sample runnable code snippets in ColdFusion Server 4.0 allow remote attackers to read files, conduct a denial of service, or use the server as a proxy for other HTTP calls.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-1999-0928
    - Vulnerability Description: Buffer overflow in SmartDesk WebSuite allows remote attackers to cause a denial of service via a long URL.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-1999-0929
    - Vulnerability Description: Novell NetWare with Novell-HTTP-Server or YAWN web servers allows remote attackers to conduct a denial of service via a large number of HTTP GET requests.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-1999-0970
    - Vulnerability Description: The OmniHTTPD visadmin.exe program allows a remote attacker to conduct a denial of service via a malformed URL which causes a large number of temporary files to be created.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-1999-1030
    - Vulnerability Description: counter.exe 2.70 allows a remote attacker to cause a denial of service (hang) via an HTTP request that ends in %0A (newline), which causes a malformed entry in the counter log that produces an access violation.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-1999-1068
    - Vulnerability Description: Oracle Webserver 2.1, when serving PL/SQL stored procedures, allows remote attackers to cause a denial of service via a long HTTP GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-1999-1207
    - Vulnerability Description: Buffer overflow in web-admin tool in NetXRay 2.6 allows remote attackers to cause a denial of service, and possibly execute arbitrary commands, via a long HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-1999-1283
    - Vulnerability Description: Opera 3.2.1 allows remote attackers to cause a denial of service (application crash) via a URL that contains an extra / in the http:// tag.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-1999-1343
    - Vulnerability Description: HTTP server for Xerox DocuColor 4 LP allows remote attackers to cause a denial of service (hang) via a long URL that contains a large number of . characters.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-1999-1412
    - Vulnerability Description: A possible interaction between Apple MacOS X release 1.0 and Apache HTTP server allows remote attackers to cause a denial of service (crash) via a flood of HTTP GET requests to CGI programs, which generates a large number of processes.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-1999-1416
    - Vulnerability Description: AnswerBook2 (AB2) web server dwhttpd 3.1a4 allows remote attackers to cause a denial of service (resource exhaustion) via an HTTP POST request with a large content-length.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-1999-1417
    - Vulnerability Description: Format string vulnerability in AnswerBook2 (AB2) web server dwhttpd 3.1a4 allows remote attackers to cause a denial of service and possibly execute arbitrary commands via encoded % characters in an HTTP request, which is improperly logged.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-1999-1523
    - Vulnerability Description: Buffer overflow in Sambar Web Server 4.2.1 allows remote attackers to cause a denial of service, and possibly execute arbitrary commands, via a long HTTP GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-1999-1533
    - Vulnerability Description: Eicon Technology Diva LAN ISDN modem allows a remote attacker to cause a denial of service (hang) via a long password argument to the login.htm file in its HTTP service.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-1999-1535
    - Vulnerability Description: Buffer overflow in AspUpload.dll in Persits Software AspUpload before 1.4.0.2 allows remote attackers to cause a denial of service, and possibly execute arbitrary commands, via a long argument in the HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-1999-1537
    - Vulnerability Description: IIS 3.x and 4.x does not distinguish between pages requiring encryption and those that do not, which allows remote attackers to cause a denial of service (resource exhaustion) via SSL requests to the HTTPS port for normally unencrypted files, which will cause IIS to perform extra work to send the files over SSL.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-1999-1548
    - Vulnerability Description: Cabletron SmartSwitch Router (SSR) 8000 firmware 2.x can only handle 200 ARP requests per second allowing a denial of service attack to succeed with a flood of ARP requests exceeding that limit.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-0023
    - Vulnerability Description: Buffer overflow in Lotus Domino HTTP server allows remote attackers to cause a denial of service via a long URL.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-0064
    - Vulnerability Description: cgiproc CGI script in Nortel Contivity HTTP server allows remote attackers to cause a denial of service via a malformed URL that includes shell metacharacters.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-0243
    - Vulnerability Description: AnalogX SimpleServer:WWW HTTP server 1.03 allows remote attackers to cause a denial of service via a short GET request to cgi-bin.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-0290
    - Vulnerability Description: Buffer overflow in Webstar HTTP server allows remote attackers to cause a denial of service via a long GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-0299
    - Vulnerability Description: Buffer overflow in WebObjects.exe in the WebObjects Developer 4.5 package allows remote attackers to cause a denial of service via an HTTP request with long headers such as Accept.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-0359
    - Vulnerability Description: Buffer overflow in Trivial HTTP (THTTPd) allows remote attackers to cause a denial of service or execute arbitrary commands via a long If-Modified-Since header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-0380
    - Vulnerability Description: The IOS HTTP service in Cisco routers and switches running IOS 11.1 through 12.1 allows remote attackers to cause a denial of service by requesting a URL that contains a %% string.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-0395
    - Vulnerability Description: Buffer overflow in CProxy 3.3 allows remote users to cause a denial of service via a long HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-0417
    - Vulnerability Description: The HTTP administration interface to the Cayman 3220-H DSL router allows remote attackers to cause a denial of service via a long username or password.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-0470
    - Vulnerability Description: Allegro RomPager HTTP server allows remote attackers to cause a denial of service via a malformed authentication request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-0484
    - Vulnerability Description: Buffer overflow in Small HTTP Server allows remote attackers to cause a denial of service via a long GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-0529
    - Vulnerability Description: Net Tools PKI Server allows remote attackers to cause a denial of service via a long HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-0571
    - Vulnerability Description: LocalWEB HTTP server 1.2.0 allows remote attackers to cause a denial of service via a long GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-0593
    - Vulnerability Description: WinProxy 2.0 and 2.0.1 allows remote attackers to cause a denial of service by sending an HTTP GET request without listing an HTTP version number.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-0643
    - Vulnerability Description: Buffer overflow in WebActive HTTP Server 1.00 allows remote attackers to cause a denial of service via a long URL.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-0732
    - Vulnerability Description: Worm HTTP server allows remote attackers to cause a denial of service via a long URL.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-0766
    - Vulnerability Description: Buffer overflow in vqSoft vqServer 1.4.49 allows remote attackers to cause a denial of service or possibly gain privileges via a long HTTP GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-0775
    - Vulnerability Description: Buffer overflow in RobTex Viking server earlier than 1.06-370 allows remote attackers to cause a denial of service or execute arbitrary commands via a long HTTP GET request, or long Unless-Modified-Since, If-Range, or If-Modified-Since headers.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-0830
    - Vulnerability Description: annclist.exe in webTV for Windows allows remote attackers to cause a denial of service by via a large, malformed UDP packet to ports 22701 through 22705.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-0838
    - Vulnerability Description: Fastream FUR HTTP server 1.0b allows remote attackers to cause a denial of service via a long GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-0859
    - Vulnerability Description: The web configuration server for NTMail V5 and V6 allows remote attackers to cause a denial of service via a series of partial HTTP requests.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-0894
    - Vulnerability Description: HTTP server on the WatchGuard SOHO firewall does not properly restrict access to administrative functions such as password resets or rebooting, which allows attackers to cause a denial of service or conduct unauthorized activities.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-0895
    - Vulnerability Description: Buffer overflow in HTTP server on the WatchGuard SOHO firewall allows remote attackers to cause a denial of service and possibly execute arbitrary code via a long GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-0897
    - Vulnerability Description: Small HTTP Server 2.03 and earlier allows remote attackers to cause a denial of service by repeatedly requesting a URL that references a directory that does not contain an index.html file, which consumes memory that is not released after the request is completed.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-0899
    - Vulnerability Description: Small HTTP Server 2.01 allows remote attackers to cause a denial of service by connecting to the server and sending out multiple GET, HEAD, or POST requests and closing the connection before the server responds to the requests.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-0908
    - Vulnerability Description: BrowseGate 2.80 allows remote attackers to cause a denial of service and possibly execute arbitrary commands via long Authorization or Referer MIME headers in the HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-0939
    - Vulnerability Description: Samba Web Administration Tool (SWAT) in Samba 2.0.7 allows remote attackers to cause a denial of service by repeatedly submitting a nonstandard URL in the GET HTTP request and forcing it to restart.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-0984
    - Vulnerability Description: The HTTP server in Cisco IOS 12.0 through 12.1 allows local users to cause a denial of service (crash and reload) via a URL containing a "?/" string.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-1048
    - Vulnerability Description: Directory traversal vulnerability in the logfile service of Wingate 4.1 Beta A and earlier allows remote attackers to read arbitrary files via a .. (dot dot) attack via an HTTP GET request that uses encoded characters in the URL.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-1049
    - Vulnerability Description: Allaire JRun 3.0 http servlet server allows remote attackers to cause a denial of service via a URL that contains a long string of "." characters.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-1078
    - Vulnerability Description: ICQ Web Front HTTPd allows remote attackers to cause a denial of service by requesting a URL that contains a "?" character.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-1154
    - Vulnerability Description: RHConsole in RobinHood 1.1 web server in BeOS r5 pro and earlier allows remote attackers to cause a denial of service via long HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-1155
    - Vulnerability Description: RHDaemon in RobinHood 1.1 web server in BeOS r5 pro and earlier allows remote attackers to cause a denial of service via long HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-1168
    - Vulnerability Description: IBM HTTP Server 1.3.6 (based on Apache) allows remote attackers to cause a denial of service and possibly execute arbitrary commands via a long GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2000-1242
    - Vulnerability Description: The HTTP service in American Power Conversion (APC) PowerChute uses a default username and password, which allows remote attackers to gain system access.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0122
    - Vulnerability Description: Kernel leak in AfpaCache module of the Fast Response Cache Accelerator (FRCA) component of IBM HTTP Server 1.3.x and Websphere 3.52 allows remote attackers to cause a denial of service via a series of malformed HTTP requests that generate a "bad request" error.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0129
    - Vulnerability Description: Buffer overflow in Tinyproxy HTTP proxy 1.3.3 and earlier allows remote attackers to cause a denial of service and possibly execute arbitrary commands via a long connect request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0171
    - Vulnerability Description: Buffer overflow in SlimServe HTTPd 1.0 allows remote attackers to cause a denial of service, and possibly execute arbitrary commands, via a long GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0227
    - Vulnerability Description: Buffer overflow in BiblioWeb web server 2.0 allows remote attackers to cause a denial of service and possibly execute arbitrary commands via a long HTTP GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0252
    - Vulnerability Description: iPlanet (formerly Netscape) Enterprise Server 4.1 allows remote attackers to cause a denial of service via a long HTTP GET request that contains many "/../" (dot dot) sequences.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0257
    - Vulnerability Description: Buffer overflow in Easycom/Safecom Print Server Web service, version 404.590 and earlier, allows remote attackers to execute arbitrary commands via (1) a long URL or (2) a long HTTP header field such as "Host:".
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0275
    - Vulnerability Description: Moby Netsuite Web Server 1.02 allows remote attackers to cause a denial of service, and possibly execute arbitrary commands, via a long HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0277
    - Vulnerability Description: Buffer overflow in ext.dll in BadBlue 1.02.07 Personal Edition allows remote attackers to cause a denial of service and possibly execute arbitrary commands via a long HTTP GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0282
    - Vulnerability Description: SEDUM 2.1 HTTP server allows remote attackers to cause a denial of service and possibly execute arbitrary commands via a long HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0285
    - Vulnerability Description: Buffer overflow in A1 HTTP server 1.0a allows remote attackers to cause a denial of service and possibly execute arbitrary commands via a long HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0298
    - Vulnerability Description: Buffer overflow in WebReflex 1.55 HTTPd allows remote attackers to cause a denial of service, and possibly execute arbitrary commands, via a long HTTP GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0327
    - Vulnerability Description: iPlanet Web Server Enterprise Edition 4.1 and earlier allows remote attackers to retrieve sensitive data from memory allocation pools, or cause a denial of service, via a URL-encoded Host: header in the HTTP request, which reveals memory in the Location: header that is returned by the server.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0367
    - Vulnerability Description: Mirabilis ICQ WebFront Plug-in ICQ2000b Build 3278 allows a remote attacker to create a denial of service via HTTP URL requests containing a large number of % characters.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0385
    - Vulnerability Description: GoAhead webserver 2.1 allows remote attackers to cause a denial of service via an HTTP request to the /aux directory.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0386
    - Vulnerability Description: AnalogX SimpleServer:WWW 1.08 allows remote attackers to cause a denial of service via an HTTP request to the /aux directory.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0394
    - Vulnerability Description: Remote manager service in Website Pro 3.0.37 allows remote attackers to cause a denial of service via a series of malformed HTTP requests to the /dyn directory.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0433
    - Vulnerability Description: Buffer overflow in Savant 3.0 web server allows remote attackers to cause a denial of service, and possibly execute arbitrary commands, via a long Host HTTP header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0447
    - Vulnerability Description: Web configuration server in 602Pro LAN SUITE allows remote attackers to cause a denial of service, and possibly execute arbitrary commands, via a long HTTP request containing "%2e" (dot dot) characters.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0448
    - Vulnerability Description: Web configuration server in 602Pro LAN SUITE allows remote attackers to cause a denial of service via an HTTP GET HTTP request to the aux directory, and possibly other directories with legacy DOS device names.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0460
    - Vulnerability Description: Websweeper 4.0 does not limit the length of certain HTTP headers, which allows remote attackers to cause a denial of service (memory exhaustion) via an extremely large HTTP Referrer: header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0472
    - Vulnerability Description: Hursley Software Laboratories Consumer Transaction Framework (HSLCTF) HTTP object allows remote attackers to cause a denial of service (crash) via an extremely long HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0493
    - Vulnerability Description: Small HTTP server 2.03 allows remote attackers to cause a denial of service via a URL that contains an MS-DOS device name such as aux.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0558
    - Vulnerability Description: T. Hauck Jana Webserver 2.01 beta 1 and earlier allows a remote attacker to create a denial of service via a URL request which includes a MS-DOS device name (i.e. GET /aux HTTP/1.0).
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0600
    - Vulnerability Description: Lotus Domino R5 prior to 5.0.7 allows a remote attacker to create a denial of service via repeated URL requests with the same HTTP headers, such as (1) Accept, (2) Accept-Charset, (3) Accept-Encoding, (4) Accept-Language, and (5) Content-Type.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0601
    - Vulnerability Description: Lotus Domino R5 prior to 5.0.7 allows a remote attacker to create a denial of service via HTTP requests containing certain combinations of UNICODE characters.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0606
    - Vulnerability Description: Vulnerability in iPlanet Web Server 4.X in HP-UX 11.04 (VVOS) with VirtualVault A.04.00 allows a remote attacker to create a denial of service via the HTTPS service.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0613
    - Vulnerability Description: Omnicron Technologies OmniHTTPD Professional 2.08 and earlier allows a remote attacker to create a denial of service via a long POST URL request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0616
    - Vulnerability Description: Faust Informatics Freestyle Chat server prior to 4.1 SR3 allows a remote attacker to create a denial of service via a URL request which includes a MS-DOS device name (e.g., GET /aux HTTP/1.0).
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0636
    - Vulnerability Description: Buffer overflows in Raytheon SilentRunner allow remote attackers to (1) cause a denial of service in the collector (cle.exe) component of SilentRunner 2.0 via traffic containing long passwords, or (2) execute arbitrary commands via long HTTP queries in the Knowledge Browser component in SilentRunner 2.0 and 2.0.1.  NOTE: It is highly likely that this candidate will be split into multiple candidates.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0647
    - Vulnerability Description: Orange Web Server 2.1, based on GoAhead, allows a remote attacker to perform a denial of service via an HTTP GET request that does not include the HTTP version.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0649
    - Vulnerability Description: Personal Web Sharing 1.5.5 allows a remote attacker to cause a denial of service via a long HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0665
    - Vulnerability Description: Internet Explorer 6 and earlier allows remote attackers to cause certain HTTP requests to be automatically executed and appear to come from the user, which could allow attackers to gain privileges or execute operations within web-based services, aka the "HTTP Request Encoding vulnerability."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0747
    - Vulnerability Description: Buffer overflow in iPlanet Web Server (iWS) Enterprise Edition 4.1, service packs 3 through 7, allows remote attackers to cause a denial of sevice and possibly execute arbitrary code via a long method name in an HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0777
    - Vulnerability Description: Omnicron OmniHTTPd 2.0.8 allows remote attackers to cause a denial of service (memory exhaustion) via a series of requests for PHP scripts.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-0852
    - Vulnerability Description: TUX HTTP server 2.1.0-2 in Red Hat Linux allows remote attackers to cause a denial of service via a long Host: header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-1064
    - Vulnerability Description: Cisco 600 series routers running CBOS 2.0.1 through 2.4.2ap allows remote attackers to cause a denial of service via multiple connections to the router on the (1) HTTP or (2) telnet service, which causes the router to become unresponsive and stop forwarding packets.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-1067
    - Vulnerability Description: Buffer overflow in AOLserver 3.0 allows remote attackers to cause a denial of service, and possibly execute arbitrary code, via an HTTP request with a long Authorization header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-1083
    - Vulnerability Description: Icecast 1.3.7, and other versions before 1.3.11 with HTTP server file streaming support enabled allows remote attackers to cause a denial of service (crash) via a URL that ends in . (dot), / (forward slash), or \ (backward slash).
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-1186
    - Vulnerability Description: Microsoft IIS 5.0 allows remote attackers to cause a denial of service via an HTTP request with a content-length value that is larger than the size of the request, which prevents IIS from timing out the connection.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-1245
    - Vulnerability Description: Opera 5.0 for Linux does not properly handle malformed HTTP headers, which allows remote attackers to cause a denial of service, possibly with a header whose value is the same as a MIME header name.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-1251
    - Vulnerability Description: SmallHTTP 1.204 through 3.00 beta 8 allows remote attackers to cause a denial of service via multiple long URL requests.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-1293
    - Vulnerability Description: Buffer overflow in web server of 3com HomeConnect Cable Modem External with USB (#3CR29223) allows remote attackers to cause a denial of service (crash) via a long HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-1304
    - Vulnerability Description: Buffer overflow in SHOUTcast Server 1.8.2 allows remote attackers to cause a denial of service (crash) via several HTTP requests with a long (1) user-agent or (2) host HTTP header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-1337
    - Vulnerability Description: Beck IPC GmbH IPC@CHIP Embedded-Webserver allows remote attackers to cause a denial of service via a long HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-1342
    - Vulnerability Description: Apache before 1.3.20 on Windows and OS/2 systems allows remote attackers to cause a denial of service (GPF) via an HTTP request for a URI that contains a large number of / (slash) or other characters, which causes certain functions to dereference a null pointer.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2001-1496
    - Vulnerability Description: Off-by-one buffer overflow in Basic Authentication in Acme Labs thttpd 1.95 through 2.20 allows remote attackers to cause a denial of service and possibly execute arbitrary code.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0057
    - Vulnerability Description: XMLHTTP control in Microsoft XML Core Services 2.6 and later does not properly handle IE Security Zone settings, which allows remote attackers to read arbitrary files by specifying a local file as an XML Data Source.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0099
    - Vulnerability Description: Buffer overflow in Michael Lamont Savant Web Server 3.0 allows remote attackers to cause a denial of service (crash) via a long HTTP request to the cgi-bin directory in which the CGI program name contains a large number of . (dot) characters.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0123
    - Vulnerability Description: MDG Computer Services Web Server 4D WS4D/eCommerce 3.0 and earlier, and possibly 3.5.3, allows remote attackers to cause a denial of service and possibly execute arbitrary commands via a long HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0124
    - Vulnerability Description: MDG Computer Services Web Server 4D/eCommerce 3.5.3 allows remote attackers to exploit directory traversal vulnerability via a ../ (dot dot) containing URL-encoded slashes in the HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0133
    - Vulnerability Description: Buffer overflows in Avirt Gateway Suite 4.2 allow remote attackers to cause a denial of service and possibly execute arbitrary code via (1) long header fields to the HTTP proxy, or (2) a long string to the telnet proxy.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0150
    - Vulnerability Description: Buffer overflow in Internet Information Server (IIS) 4.0, 5.0, and 5.1 allows remote attackers to spoof the safety check for HTTP headers and cause a denial of service or execute arbitrary code via HTTP header field values.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0200
    - Vulnerability Description: Cyberstop Web Server for Windows 0.1 allows remote attackers to cause a denial of service via an HTTP request for an MS-DOS device name.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0201
    - Vulnerability Description: Cyberstop Web Server for Windows 0.1 allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via a long HTTP GET request, possibly triggering a buffer overflow.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0289
    - Vulnerability Description: Buffer overflow in Phusion web server 1.0 allows remote attackers to cause a denial of service and execute arbitrary code via a long HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0291
    - Vulnerability Description: Dino's Webserver 1.2 allows remote attackers to cause a denial of service (CPU consumption) and possibly execute arbitrary code via several large HTTP requests within a short time.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0297
    - Vulnerability Description: Buffer overflow in ScriptEase MiniWeb Server 0.95 allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via a long URL in an HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0298
    - Vulnerability Description: ScriptEase MiniWeb Server 0.95 allows remote attackers to cause a denial of service (crash) via certain HTTP GET requests containing (1) a %2e%2e (encoded dot-dot), (2) several /../ (dot dot) sequences, (3) a missing URI, or (4) several ../ in a URI that does not begin with a / (slash) character.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0335
    - Vulnerability Description: Buffer overflow in Galacticomm Worldgroup web server 3.20 and earlier allows remote attackers to cause a denial of service, and possibly execute arbitrary code, via a long HTTP GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0386
    - Vulnerability Description: The administration module for Oracle Web Cache in Oracle9iAS (9i Application Suite) 9.0.2 allows remote attackers to cause a denial of service (crash) via (1) an HTTP GET request containing a ".." (dot dot) sequence, or (2) a malformed HTTP GET request with a chunked Transfer-Encoding with missing data.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0392
    - Vulnerability Description: Apache 1.3 through 1.3.24, and Apache 2.0 through 2.0.36, allows remote attackers to cause a denial of service and possibly execute arbitrary code via a chunk-encoded HTTP request that causes Apache to use an incorrect size.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0448
    - Vulnerability Description: Xerver Free Web Server 2.10 and earlier allows remote attackers to cause a denial of service (crash) via an HTTP request that contains many "C:/" sequences.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0460
    - Vulnerability Description: Bitvise WinSSHD before 2002-03-16 allows remote attackers to cause a denial of service (resource exhaustion) via a large number of incomplete connections that are not properly terminated, which are not properly freed by SSHd.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0496
    - Vulnerability Description: The HTTP server for SouthWest Talker server 1.0.0 allows remote attackers to cause a denial of service (server crash) via a malformed URL to port 5002.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0541
    - Vulnerability Description: Buffer overflow in Tivoli Storage Manager TSM (1) Server or Storage Agents 3.1 through 5.1, and (2) the TSM Client Acceptor Service 4.2 and 5.1, allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via a long HTTP GET request to port 1580 or port 1581.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0559
    - Vulnerability Description: Buffer overflows in PL/SQL module 3.0.9.8.2 in Oracle 9i Application Server 1.0.2.x allow remote attackers to cause a denial of service or execute arbitrary code via (1) a long help page request without a dadname, which overflows the resulting HTTP Location header, (2) a long HTTP request to the plsql module, (3) a long password in the HTTP Authorization, (4) a long Access Descriptor (DAD) password in the addadd form, or (5) a long cache directory name.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0566
    - Vulnerability Description: PL/SQL module 3.0.9.8.2 in Oracle 9i Application Server 1.0.2.x allows remote attackers to cause a denial of service (crash) via an HTTP Authorization header without an authentication type.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0578
    - Vulnerability Description: Buffer overflow in 4D WebServer 6.7.3 allows remote attackers to cause a denial of service and possibly execute arbitrary code via an HTTP request with Basic Authentication containing a long (1) user name or (2) password.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0602
    - Vulnerability Description: Snapgear Lite+ firewall 1.5.4 and 1.5.3 allows remote attackers to cause a denial of service (crash) via a large number of connections to (1) the HTTP web management port, or (2) the PPTP port.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0663
    - Vulnerability Description: Buffer overflow in HTTP Proxy for Symantec Norton Personal Internet Firewall 3.0.4.91 and Norton Internet Security 2001 allows remote attackers to cause a denial of service and possibly execute arbitrary code via a large outgoing HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0692
    - Vulnerability Description: Buffer overflow in SmartHTML Interpreter (shtml.dll) in Microsoft FrontPage Server Extensions (FPSE) 2000 and 2002 allows remote attackers to cause a denial of service (CPU consumption) or run arbitrary code, respectively, via a certain type of web file request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0717
    - Vulnerability Description: PHP 4.2.0 and 4.2.1 allows remote attackers to cause a denial of service and possibly execute arbitrary code via an HTTP POST request with certain arguments in a multipart/form-data form, which generates an error condition that is not properly handled and causes improper memory to be freed.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0748
    - Vulnerability Description: LabVIEW Web Server 5.1.1 through 6.1 allows remote attackers to cause a denial of service (crash) via an HTTP GET request that ends in two newline characters, instead of the expected carriage return/newline combinations.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0792
    - Vulnerability Description: The web management interface for Cisco Content Service Switch (CSS) 11000 switches allows remote attackers to cause a denial of service (soft reset) via (1) an HTTPS POST request, or (2) malformed XML data.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0839
    - Vulnerability Description: The shared memory scoreboard in the HTTP daemon for Apache 1.3.x before 1.3.27 allows any user running as the Apache UID to send a SIGUSR1 signal to any process as root, resulting in a denial of service (process kill) or possibly other behaviors that would not normally be allowed, by modifying the parent[].pid and parent[].last_rtime segments in the scoreboard.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0876
    - Vulnerability Description: Web server for Shambala 4.5 allows remote attackers to cause a denial of service (crash) via a malformed HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0945
    - Vulnerability Description: Buffer overflow in SeaNox Devwex allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via a long HTTP GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0966
    - Vulnerability Description: Buffer overflow in 4D web server 6.7.3 allow remote attackers to cause a denial of service and possibly execute arbitrary code via a long HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-0968
    - Vulnerability Description: Buffer overflow in AnalogX SimpleServer:WWW 1.16 and earlier allows remote attackers to cause a denial of service (crash) and execute code via a long HTTP request method name.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1001
    - Vulnerability Description: Buffer overflows in AnalogX Proxy before 4.12 allows remote attackers to cause a denial of service and possibly execute arbitrary code via (1) a long HTTP request to TCP port 6588 or (2) a SOCKS 4A request to TCP port 1080 with a long DNS hostname.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1011
    - Vulnerability Description: Buffer overflow in web server for Tivoli Management Framework (TMF) Endpoint 3.6.x through 3.7.1, before Fixpack 2, allows remote attackers to cause a denial of service or execute arbitrary code via a long HTTP GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1012
    - Vulnerability Description: Buffer overflow in web server for Tivoli Management Framework (TMF) ManagedNode 3.6.x through 3.7.1 allows remote attackers to cause a denial of service or execute arbitrary code via a long HTTP GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1023
    - Vulnerability Description: BadBlue server allows remote attackers to cause a denial of service (crash) via an HTTP GET request without a URI.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1032
    - Vulnerability Description: Buffer overflow in KeyFocus (KF) web server 1.0.5 and earlier allows remote attackers to cause a denial of service and possibly execute arbitrary code via a malformed HTTP header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1035
    - Vulnerability Description: Omnicron OmniHTTPd 2.09 allows remote attackers to cause a denial of service (crash) via an HTTP request with a long, malformed HTTP 1version number.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1052
    - Vulnerability Description: Jigsaw 2.2.1 on Windows systems allows remote attackers to use MS-DOS device names in HTTP requests to (1) cause a denial of service using the "con" device, or (2) obtain the physical path of the server using two requests to the "aux" device.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1061
    - Vulnerability Description: Multiple buffer overflows in Thomas Hauck Jana Server 2.x through 2.2.1, and 1.4.6 and earlier, allow remote attackers to cause a denial of service and possibly execute arbitrary code via (1) an HTTP GET request with a long major version number, (2) an HTTP GET request to the HTTP proxy on port 3128 with a long major version number, (3) a long OK reply from a POP3 server, and (4) a long SMTP server response.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1068
    - Vulnerability Description: The web server for D-Link DP-300 print server allows remote attackers to cause a denial of service (hang) via a large HTTP POST request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1077
    - Vulnerability Description: IPSwitch IMail Web Calendaring service (iwebcal) allows remote attackers to cause a denial of service (crash) via an HTTP POST request without a Content-Length field.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1142
    - Vulnerability Description: Heap-based buffer overflow in the Remote Data Services (RDS) component of Microsoft Data Access Components (MDAC) 2.1 through 2.6, and Internet Explorer 5.01 through 6.0, allows remote attackers to execute code via a malformed HTTP request to the Data Stub.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1147
    - Vulnerability Description: The HTTP administration interface for HP Procurve 4000M Switch firmware before C.09.16, with stacking features and remote administration enabled, does not authenticate requests to reset the device, which allows remote attackers to cause a denial of service via a direct request to the device_reset CGI program.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1153
    - Vulnerability Description: IBM Websphere 4.0.3 allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via an HTTP request with long HTTP headers, such as "Host".
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1154
    - Vulnerability Description: anlgform.pl in Analog before 5.23 does not restrict access to the PROGRESSFREQ progress update command, which allows remote attackers to cause a denial of service (disk consumption) by using the command to report updates more frequently and fill the web server error log.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1169
    - Vulnerability Description: IBM Web Traffic Express Caching Proxy Server 3.6 and 4.x before 4.0.1.26 allows remote attackers to cause a denial of service (crash) via an HTTP request to helpout.exe with a missing HTTP version number, which causes ibmproxy.exe to crash.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1212
    - Vulnerability Description: Buffer overflow in RadioBird Software WebServer 4 Everyone 1.23 and 1.27, and other versions before 1.30, allows remote attackers to cause a denial of service (crash) via a long HTTP GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1222
    - Vulnerability Description: Buffer overflow in the embedded HTTP server for Cisco Catalyst switches running CatOS 5.4 through 7.3 allows remote attackers to cause a denial of service (reset) via a long HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1223
    - Vulnerability Description: Buffer overflow in DSC 3.0 parser from GSview, as used in KGhostView in KDE 1.1 and KDE 3.0.3a, may allow attackers to cause a denial of service or execute arbitrary code via a modified .ps (PostScript) input file.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1236
    - Vulnerability Description: The remote management web server for Linksys BEFSR41 EtherFast Cable/DSL Router before firmware 1.42.7 allows remote attackers to cause a denial of service (crash) via an HTTP request to Gozila.cgi without any arguments.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1368
    - Vulnerability Description: Common Unix Printing System (CUPS) 1.1.14 through 1.1.17 allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code by causing negative arguments to be fed into memcpy() calls via HTTP requests with (1) a negative Content-Length value or (2) a negative length in a chunked transfer encoding.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1501
    - Vulnerability Description: The MPS functionality in Enterasys SSR8000 (Smart Switch Router) before firmware 8.3.0.10 allows remote attackers to cause a denial of service (crash) via multiple port scans to ports 15077 and 15078.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1531
    - Vulnerability Description: The administrative web interface (STEMWADM) for SurfControl SuperScout Email Filter allows remote attackers to cause a denial of service (crash) via an HTTP request without a Content-Length parameter.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1556
    - Vulnerability Description: Cisco ONS15454 and ONS15327 running ONS before 3.4 allows attackers to cause a denial of service (reset) via an HTTP request to the TCC, TCC+ or XTC, in which the request contains an invalid CORBA Interoperable Object Reference (IOR).
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1557
    - Vulnerability Description: Cisco ONS15454 and ONS15327 running ONS before 3.4 allows attackers to cause a denial of service (reset to TCC, TCC+, TCCi or XTC) via a malformed HTTP request that does not contain a leading / (slash) character.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1596
    - Vulnerability Description: Cisco SN 5420 Storage Router 1.1(5) and earlier allows remote attackers to cause a denial of service (router crash) via an HTTP request with large headers.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1624
    - Vulnerability Description: Buffer overflow in Lotus Domino web server before R5.0.10, when logging to DOMLOG.NSF, allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via a long HTTP Authenticate header containing certain non-ASCII characters.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1663
    - Vulnerability Description: The Post_Method function in method.c for Monkey HTTP Daemon before 0.5.1 allows remote attackers to cause a denial of service (crash) via a POST request with an invalid or missing Content-Length header value.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1793
    - Vulnerability Description: HTTP Server mod_ssl module running on HP-UX 11.04 with Virtualvault OS (VVOS) 4.5 through 4.6 closes the connection when the Apache server times out during an SSL request, which may allow attackers to cause a denial of service.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1828
    - Vulnerability Description: Savant Webserver 3.1 allows remote attackers to cause a denial of service (crash) via an HTTP GET request with a negative Content-Length value.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1850
    - Vulnerability Description: mod_cgi in Apache 2.0.39 and 2.0.40 allows local users and possibly remote attackers to cause a denial of service (hang and memory consumption) by causing a CGI script to send a large amount of data to stderr, which results in a read/write deadlock between httpd and the CGI script.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1862
    - Vulnerability Description: SmartMail Server 2.0 allows remote attackers to cause a denial of service (crash) by sending data and closing the connection before all the data has been sent.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1865
    - Vulnerability Description: Buffer overflow in the Embedded HTTP server, as used in (1) D-Link DI-804 4.68, Dl-704 V2.56b6, and Dl-704 V2.56b5 and (2) Linksys Etherfast BEFW11S4 Wireless AP + Cable/DSL Router 1.37.2 through 1.42.7 and Linksys WAP11 1.3 and 1.4, allows remote attackers to cause a denial of service (crash) via a long header, as demonstrated using the Host header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1895
    - Vulnerability Description: The servlet engine in Jakarta Apache Tomcat 3.3 and 4.0.4, when using IIS and the ajp1.3 connector, allows remote attackers to cause a denial of service (crash) via a large number of HTTP GET requests for an MS-DOS device such as AUX, LPT1, CON, or PRN.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1897
    - Vulnerability Description: MyWebServer LLC MyWebServer 1.0.2 allows remote attackers to cause a denial of service (crash) via a long HTTP request, possibly triggering a buffer overflow.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1905
    - Vulnerability Description: Buffer overflow in the web server of Polycom ViaVideo 2.2 and 3.0 allows remote attackers to cause a denial of service (crash) via a long HTTP GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1906
    - Vulnerability Description: The web server for Polycom ViaVideo 2.2 and 3.0 allows remote attackers to cause a denial of service (CPU consumption) by sending incomplete HTTP requests and leaving the connections open.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1907
    - Vulnerability Description: TelCondex SimpleWebServer 2.06.20817 allows remote attackers to cause a denial of service (crash) via a long HTTP GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1908
    - Vulnerability Description: Microsoft IIS 5.0 and 5.1 allows remote attackers to cause a denial of service (CPU consumption) via an HTTP request with a Host header that contains a large number of "/" (forward slash) characters.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1941
    - Vulnerability Description: Buffer overflow in RadioBird WebServer 4 Everyone 1.28 allows remote attackers to cause a denial of service (crash) via a long HTTP GET request with the Host header set.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1945
    - Vulnerability Description: Buffer overflow in SmartMail Server 1.0 Beta 10 allows remote attackers to cause a denial of service (crash) via a long request to (1) TCP port 25 (SMTP) or (2) TCP port 110 (POP3).
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1973
    - Vulnerability Description: Buffer overflow in CHttpServer::OnParseError in the ISAPI extension (Isapi.cpp) when built using Microsoft Foundation Class (MFC) static libraries in Visual C++ 5.0, and 6.0 before SP3, as used in multiple products including BadBlue, allows remote attackers to cause a denial of service (access violation and crash) and possibly execute arbitrary code via a long query string that causes a parsing error.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1992
    - Vulnerability Description: Buffer overflow in jrun.dll in ColdFusion MX, when used with IIS 4 or 5, allows remote attackers to cause a denial of service in IIS via (1) a long template file name or (2) a long HTTP header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-1994
    - Vulnerability Description: advserver.exe in Advanced Web Server (AdvServer) Professional 1.030000 allows remote attackers to cause a denial of service via multiple HTTP requests containing a single carriage return/line feed (CRLF) sequence.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-2025
    - Vulnerability Description: Lotus Domino server 5.0.9a and earlier allows remote attackers to cause a denial of service by exhausting the number of working threads via a large number of HTTP requests for (1) an MS-DOS device name and (2) an MS-DOS device name with a large number of characters appended to the device name.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-2030
    - Vulnerability Description: Stack-based buffer overflow in SQLData Enterprise Server 3.0 allows remote attacker to execute arbitrary code and cause a denial of service via a long HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-2081
    - Vulnerability Description: cphost.dll in Microsoft Site Server 3.0 allows remote attackers to cause a denial of service (disk consumption) via an HTTP POST of a file with a long TargetURL parameter, which causes Site Server to abort and leaves the uploaded file in c:\temp.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-2140
    - Vulnerability Description: Buffer overflow in Cisco PIX Firewall 5.2.x to 5.2.8, 6.0.x to 6.0.3, 6.1.x to 6.1.3, and 6.2.x to 6.2.1 allows remote attackers to cause a denial of service via HTTP traffic authentication using (1) TACACS+ or (2) RADIUS.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-2146
    - Vulnerability Description: cgitest.exe in Savant Web Server 3.1 and earlier allows remote attackers to cause a denial of service (crash) via a long HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-2149
    - Vulnerability Description: Buffer overflow in Lucent Access Point 300, 600, and 1500 Service Routers allows remote attackers to cause a denial of service (reboot) via a long HTTP request to the administrative interface.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-2241
    - Vulnerability Description: Buffer overflow in httpd32.exe in Deerfield VisNetic WebSite before 3.5.15 allows remote attackers to cause a denial of service (crash) via a long HTTP OPTIONS request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-2258
    - Vulnerability Description: Moby NetSuite allows remote attackers to cause a denial of service (crash) via an HTTP POST request with a (1) large integer or (2) non-numeric value in the Content-Length header, which causes an access violation after a failed atoi function call.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-2272
    - Vulnerability Description: Tomcat 4.0 through 4.1.12, using mod_jk 1.2.1 module on Apache 1.3 through 1.3.27, allows remote attackers to cause a denial of service (desynchronized communications) via an HTTP GET request with a Transfer-Encoding chunked field with invalid values.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-2286
    - Vulnerability Description: The parse-get function in utils.c for apt-www-proxy 0.1 allows remote attackers to cause a denial of service (crash) via an empty HTTP request, which causes a null dereference.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-2295
    - Vulnerability Description: Buffer overflow in Pico Server (pServ) 2.0 beta 1 through beta 5 allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via (1) a 1024-byte TCP stream message, which triggers an off-by-one buffer overflow, or (2) a long method name in an HTTP request, (3) a long version number in an HTTP request, (4) a long User-Agent header, or (5) a long file path.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-2317
    - Vulnerability Description: Memory leak in the (1) httpd, (2) nntpd, and (3) vpn driver in VelociRaptor 1.0 allows remote attackers to cause a denial of service (memory consumption) via an unknown method.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-2400
    - Vulnerability Description: Buffer overflow in the httpdProcessRequest function in LibHTTPD 1.2 allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via a long HTTP POST request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-2406
    - Vulnerability Description: Buffer overflow in HTTP server in LiteServe 2.0, 2.0.1 and 2.0.2 allows remote attackers to cause a denial of service (hang) via a large number of percent characters (%) in an HTTP GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-2414
    - Vulnerability Description: Opera 6.0.3, when using Squid 2.4 for HTTPS proxying, does not properly handle when accepting a non-global certificate authority (CA) certificate from a site and establishing a subsequent HTTPS connection, which allows remote attackers to cause a denial of service (crash).
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-2421
    - Vulnerability Description: acWEB 1.14 allows remote attackers to cause a denial of service (crash) via an HTTP request for a MS-DOS device name such as COM2.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-2428
    - Vulnerability Description: webs.c in GoAhead WebServer before 2.1.4 allows remote attackers to cause a denial of service (NULL pointer dereference and daemon crash) via an HTTP POST request that contains a Content-Length header but no body data.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2002-2429
    - Vulnerability Description: webs.c in GoAhead WebServer before 2.1.4 allows remote attackers to cause a denial of service (daemon crash) via an HTTP POST request that contains a negative integer in the Content-Length header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-0016
    - Vulnerability Description: Apache before 2.0.44, when running on unpatched Windows 9x and Me operating systems, allows remote attackers to cause a denial of service or execute arbitrary code via an HTTP request containing MS-DOS device names.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-0032
    - Vulnerability Description: Memory leak in libmcrypt before 2.5.5 allows attackers to cause a denial of service (memory exhaustion) via a large number of requests to the application, which causes libmcrypt to dynamically load algorithms via libtool.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-0123
    - Vulnerability Description: Buffer overflow in Web Retriever client for Lotus Notes/Domino R4.5 through R6 allows remote malicious web servers to cause a denial of service (crash) via a long HTTP status line.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-0180
    - Vulnerability Description: Lotus Domino Web Server (nhttp.exe) before 6.0.1 allows remote attackers to cause a denial of service via an incomplete POST request, as demonstrated using the h_PageUI form.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-0181
    - Vulnerability Description: Lotus Domino Web Server (nhttp.exe) before 6.0.1 allows remote attackers to cause a denial of service via a "Fictionary Value Field POST request" as demonstrated using the s_Validation form with a long, unknown parameter name.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-0315
    - Vulnerability Description: Snowblind Web Server 1.0 allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via a long HTTP request, which may trigger a buffer overflow.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-0356
    - Vulnerability Description: Multiple off-by-one vulnerabilities in Ethereal 0.9.11 and earlier allow remote attackers to cause a denial of service and possibly execute arbitrary code via the (1) AIM, (2) GIOP Gryphon, (3) OSPF, (4) PPTP, (5) Quake, (6) Quake2, (7) Quake3, (8) Rsync, (9) SMB, (10) SMPP, and (11) TSP dissectors, which do not properly use the tvb_get_nstringz and tvb_get_nstringz0 functions.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-0409
    - Vulnerability Description: Buffer overflow in BRS WebWeaver 1.04 and earlier allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via a long HTTP (1) POST or (2) HEAD request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-0421
    - Vulnerability Description: Apple QuickTime / Darwin Streaming Server before 4.1.3f allows remote attackers to cause a denial of service (crash) via an MS-DOS device name (e.g. AUX) in a request to HTTP port 1220, a different vulnerability than CVE-2003-0502.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-0502
    - Vulnerability Description: Apple QuickTime / Darwin Streaming Server before 4.1.3g allows remote attackers to cause a denial of service (crash) via a .. (dot dot) sequence followed by an MS-DOS device name (e.g. AUX) in a request to HTTP port 1220, a different vulnerability than CVE-2003-0421.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-0807
    - Vulnerability Description: Buffer overflow in the COM Internet Services and in the RPC over HTTP Proxy components for Microsoft Windows NT Server 4.0, NT 4.0 Terminal Server Edition, 2000, XP, and Server 2003 allows remote attackers to cause a denial of service via a crafted request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-0824
    - Vulnerability Description: Unknown vulnerability in the SmartHTML interpreter (shtml.dll) in Microsoft FrontPage Server Extensions 2000 and 2002, and Microsoft SharePoint Team Services 2002, allows remote attackers to cause a denial of service (response failure) via a certain request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-0866
    - Vulnerability Description: The Catalina org.apache.catalina.connector.http package in Tomcat 4.0.x up to 4.0.3 allows remote attackers to cause a denial of service via several requests that do not follow the HTTP protocol, which causes Tomcat to reject later requests.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-0904
    - Vulnerability Description: Microsoft Exchange 2003 and Outlook Web Access (OWA), when configured to use NTLM authentication, does not properly reuse HTTP connections, which can cause OWA users to view mailboxes of other users when Kerberos has been disabled as an authentication method for IIS 6.0, e.g. when SharePoint Services 2.0 is installed.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-0973
    - Vulnerability Description: Unknown vulnerability in mod_python 3.0.x before 3.0.4, and 2.7.x before 2.7.9, allows remote attackers to cause a denial of service (httpd crash) via a certain query string.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-1001
    - Vulnerability Description: Buffer overflow in the Cisco Firewall Services Module (FWSM) in Cisco Catalyst 6500 and 7600 series devices allows remote attackers to cause a denial of service (crash and reload) via HTTP auth requests for (1) TACACS+ or (2) RADIUS authentication.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-1084
    - Vulnerability Description: Monit 1.4 to 4.1 allows remote attackers to cause a denial of service (daemon crash) via an HTTP POST request with a negative Content-Length field.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-1085
    - Vulnerability Description: The HTTP server in the Thomson TWC305, TWC315, and TCW690 cable modem ST42.03.0a allows remote attackers to cause a denial of service (unstable service) via a long GET request, possibly caused by a buffer overflow.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-1159
    - Vulnerability Description: Plug and Play Web Server Proxy 1.0002c allows remote attackers to cause a denial of service (server crash) via an invalid URI in an HTTP GET request to TCP port 8080.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-1165
    - Vulnerability Description: Buffer overflow in BRS WebWeaver 1.06 and earlier allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via an HTTP request with a long User-Agent header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-1198
    - Vulnerability Description: connection.c in Cherokee web server before 0.4.6 allows remote attackers to cause a denial of service via an HTTP POST request without a Content-Length header field.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-1209
    - Vulnerability Description: The Post_Method function in Monkey HTTP Daemon before 0.6.2 allows remote attackers to cause a denial of service (crash) via a POST request without a Content-Type header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-1228
    - Vulnerability Description: Buffer overflow in the prepare_reply function in request.c for Mathopd 1.2 through 1.5b13, and possibly earlier versions, allows remote attackers to cause a denial of service (server crash) and possibly execute arbitrary code via an HTTP request with a long path.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-1262
    - Vulnerability Description: Buffer overflow in the http_fetch function of HTTP Fetcher 1.0.0 and 1.0.1 allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via a URL request via a long (1) host, (2) referer, or (3) userAgent value.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-1263
    - Vulnerability Description: ICAL.EXE in iCal 3.7 allows remote attackers to cause a denial of service (crash) via a malformed HTTP request, possibly due to an invalid method name.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-1270
    - Vulnerability Description: AN HTTP 1.41e allows remote attackers to cause a denial of service (borken pipe) via an HTTP request to aux.cgi with a long argument, possibly triggering a buffer overflow or MS-DOS device vulnerability.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-1321
    - Vulnerability Description: Buffer overflow in Avant Browser 8.02 allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via a long URL in an HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-1342
    - Vulnerability Description: Trend Micro Virus Control System (TVCS) 1.8 running with IIS allows remote attackers to cause a denial of service (memory consumption) in IIS via multiple URL requests for ActiveSupport.exe.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-1364
    - Vulnerability Description: Aprelium Technologies Abyss Web Server 1.1.2, and possibly other versions before 1.1.4, allows remote attackers to cause a denial of service (crash) via an HTTP GET message with empty (1) Connection or (2) Range fields.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-1397
    - Vulnerability Description: The PluginContext object of Opera 6.05 and 7.0 allows remote attackers to cause a denial of service (crash) via an HTTP request containing a long string that gets passed to the ShowDocument method.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-1490
    - Vulnerability Description: SonicWall Pro running firmware 6.4.0.1 allows remote attackers to cause a denial of service (device reset) via a long HTTP POST to the internal interface, possibly due to a buffer overflow.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-1497
    - Vulnerability Description: Buffer overflow in the system log viewer of Linksys BEFSX41 1.44.3 allows remote attackers to cause a denial of service via an HTTP request with a long Log_Page_Num variable.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-1510
    - Vulnerability Description: TinyWeb 1.9 allows remote attackers to cause a denial of service (CPU consumption) via a ".%00." in an HTTP GET request to the cgi-bin directory.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-1558
    - Vulnerability Description: Buffer overflow in httpd.c of fnord 1.6 allows remote attackers to create a denial of service (crash) and possibly execute arbitrary code via a long CGI request passed to the do_cgi function.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-1567
    - Vulnerability Description: The undocumented TRACK method in Microsoft Internet Information Services (IIS) 5.0 returns the content of the original request in the body of the response, which makes it easier for remote attackers to steal cookies and authentication credentials, or bypass the HttpOnly protection mechanism, by using TRACK to read the contents of the HTTP headers that are returned in the response, a technique that is similar to cross-site tracing (XST) using HTTP TRACE.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-1569
    - Vulnerability Description: GoAhead WebServer before 2.1.5 on Windows 95, 98, and ME allows remote attackers to cause a denial of service (daemon crash) via an HTTP request with a (1) con, (2) nul, (3) clock$, or (4) config$ device name in a path component, different vectors than CVE-2001-0385.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2003-1582
    - Vulnerability Description: Microsoft Internet Information Services (IIS) 6.0, when DNS resolution is enabled for client IP addresses, allows remote attackers to inject arbitrary text into log files via an HTTP request in conjunction with a crafted DNS response, as demonstrated by injecting XSS sequences, related to an "Inverse Lookup Log Corruption (ILLC)" issue.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-0006
    - Vulnerability Description: Multiple buffer overflows in Gaim 0.75 and earlier, and Ultramagnetic before 0.81, allow remote attackers to cause a denial of service and possibly execute arbitrary code via (1) cookies in a Yahoo web connection, (2) a long name parameter in the Yahoo login web page, (3) a long value parameter in the Yahoo login page, (4) a YMSG packet, (5) the URL parser, and (6) HTTP proxy connect.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-0049
    - Vulnerability Description: Helix Universal Server/Proxy 9 and Mobile Server 10 allow remote attackers to cause a denial of service via certain HTTP POST messages to the Administration System port.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-0095
    - Vulnerability Description: McAfee ePolicy Orchestrator agent allows remote attackers to cause a denial of service (memory consumption and crash) and possibly execute arbitrary code via an HTTP POST request with an invalid Content-Length value, possibly triggering a buffer overflow.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-0096
    - Vulnerability Description: Unknown vulnerability in mod_python 2.7.9 allows remote attackers to cause a denial of service (httpd crash) via a certain query string, a variant of CAN-2003-0973.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-0113
    - Vulnerability Description: Memory leak in ssl_engine_io.c for mod_ssl in Apache 2 before 2.0.49 allows remote attackers to cause a denial of service (memory consumption) via plain HTTP requests to the SSL port of an SSL-enabled server.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-0245
    - Vulnerability Description: Web Crossing 4.x and 5.x allows remote attackers to cause a denial of service (crash) by sending a HTTP POST request with a large or negative Content-Length, which causes an integer divide-by-zero.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-0264
    - Vulnerability Description: palmhttpd for PalmOS allows remote attackers to cause a denial of service (crash) by establishing two simultaneous HTTP connections, which exceeds the PalmOS accept queue.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-0276
    - Vulnerability Description: The get_real_string function in Monkey HTTP Daemon (monkeyd) 0.8.1 and earlier allows remote attackers to cause a denial of service (crash) via an HTTP request with a sequence of "%" characters and a missing Host field.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-0292
    - Vulnerability Description: Buffer overflow in KarjaSoft Sami HTTP Server 1.0.4 allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via a long HTTP GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-0313
    - Vulnerability Description: Buffer overflow in PSOProxy 0.91 allows remote attackers to cause a denial of service and possibly execute arbitrary code via a long HTTP request, as demonstrated using a long (1) GET argument or (2) method name.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-0331
    - Vulnerability Description: Heap-based buffer overflow in Dell OpenManage Web Server 3.4.0 allows remote attackers to cause a denial of service (crash) via a HTTP POST with a long application variable.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-0459
    - Vulnerability Description: The Clear Channel Assessment (CCA) algorithm in the IEEE 802.11 wireless protocol, when using DSSS transmission encoding, allows remote attackers to cause a denial of service via a certain RF signal that causes a channel to appear busy (aka "jabber"), which prevents devices from transmitting data.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-0492
    - Vulnerability Description: Heap-based buffer overflow in proxy_util.c for mod_proxy in Apache 1.3.25 to 1.3.31 allows remote attackers to cause a denial of service (process crash) and possibly execute arbitrary code via a negative Content-Length HTTP header field, which causes a large amount of data to be copied.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-0493
    - Vulnerability Description: The ap_get_mime_headers_core function in Apache httpd 2.0.49 allows remote attackers to cause a denial of service (memory exhaustion), and possibly an integer signedness error leading to a heap-based buffer overflow on 64 bit systems, via long header lines with large numbers of space or tab characters.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-0551
    - Vulnerability Description: Cisco CatOS 5.x before 5.5(20) through 8.x before 8.2(2) and 8.3(2)GLX, as used in Catalyst switches, allows remote attackers to cause a denial of service (system crash and reload) by sending invalid packets instead of the final ACK portion of the three-way handshake to the (1) Telnet, (2) HTTP, or (3) SSH services, aka "TCP-ACK DoS attack."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-0604
    - Vulnerability Description: The HTTP client and server in giFT-FastTrack 0.8.6 and earlier allows remote attackers to cause a denial of service (crash), possibly via an empty search query, which triggers a NULL dereference.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-0610
    - Vulnerability Description: The Web administration interface in Microsoft MN-500 Wireless Router allows remote attackers to cause a denial of service (connection refusal) via a large number of open HTTP connections.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-0611
    - Vulnerability Description: Web-Based Administration in Netgear FVS318 VPN Router allows remote attackers to cause a denial of service (no new connections) via a large number of open HTTP connections.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-0684
    - Vulnerability Description: WebSphere Edge Component Caching Proxy in WebSphere Edge Server 5.02, with the JunctionRewrite directive enabled, allows remote attackers to cause a denial of service via an HTTP GET request without any parameters.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-0740
    - Vulnerability Description: The HTTP server in Lexmark T522 and possibly other models allows remote attackers to cause a denial of service (server crash, reload, or hang) via an HTTP header with a long Host field, possibly triggering a buffer overflow.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-0766
    - Vulnerability Description: NGSEC StackDefender 2.0 allows attackers to cause a denial of service (system crash) via an invalid address for the BaseAddress parameter to the hooks for the (1) ZwAllocateVirtualMemory or (2) ZwProtectVirtualMemory functions.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-0786
    - Vulnerability Description: The IPv6 URI parsing routines in the apr-util library for Apache 2.0.50 and earlier allow remote attackers to cause a denial of service (child process crash) via a certain URI, as demonstrated using the Codenomicon HTTP Test Tool.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-0799
    - Vulnerability Description: The HTTP daemon in Ipswitch WhatsUp Gold 8.03 and 8.03 Hotfix 1 allows remote attackers to cause a denial of service (server crash) via a GET request containing an MS-DOS device name, as demonstrated using "prn.htm".
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-0931
    - Vulnerability Description: MySQL MaxDB before 7.5.00.18 allows remote attackers to cause a denial of service (crash) via an HTTP request to webdbm with high ASCII values in the Server field, which triggers an assert error in the IsAscii7 function.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-0942
    - Vulnerability Description: Apache webserver 2.0.52 and earlier allows remote attackers to cause a denial of service (CPU consumption) via an HTTP GET request with a MIME header containing multiple lines with a large number of space characters.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-0983
    - Vulnerability Description: The CGI module in Ruby 1.6 before 1.6.8, and 1.8 before 1.8.2, allows remote attackers to cause a denial of service (infinite loop and CPU consumption) via a certain HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-1034
    - Vulnerability Description: Buffer overflow in the http_open function in Kaffeine before 0.5, whose code is also used in gxine before 0.3.3, allows remote attackers to cause a denial of service (application crash) and possibly execute arbitrary code via a long Content-Type header for a Real Audio Media (.ram) playlist file.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-1101
    - Vulnerability Description: mailpost.exe in MailPost 5.1.1sv, and possibly earlier versions, allows remote attackers to cause a denial of service (server crash), leak sensitive pathname information in the resulting error message, and execute a cross-site scripting (XSS) attack via an HTTP request that contains a / (backslash) and arbitrary webscript before the requested file, which leaks the pathname and does not quote the script in the resulting Visual Basic error message.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-1113
    - Vulnerability Description: SQL injection vulnerability in SQLgrey Postfix greylisting service before 1.2.0 allows remote attackers to execute arbitrary SQL commands via the (1) sender or (2) recipient e-mail addresses.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-1141
    - Vulnerability Description: The HTTP dissector in Ethereal 0.10.1 through 0.10.7 allows remote attackers to cause a denial of service (application crash) via a certain packet that causes the dissector to access previously-freed memory.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-1169
    - Vulnerability Description: MaxDB WebTools 7.5.00.18 and earlier allows remote attackers to cause a denial of service (application crash) via an HTTP GET request for a file that does not exist, followed by two carriage returns, which causes a NULL dereference.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-1514
    - Vulnerability Description: 04WebServer 1.42 allows remote attackers to cause a denial of service (fail to restart properly) via an HTTP request for an MS-DOS device name such as COM2.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-1606
    - Vulnerability Description: slxweb.dll in SalesLogix 6.1 allows remote attackers to cause a denial service (application crash) via an invalid HTTP request, which might also leak sensitive information in the ErrorLogMsg cookie.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-1680
    - Vulnerability Description: application.cgi in the Pingtel Xpressa handset running firmware 2.1.11.24 allows remote authenticated users to cause a denial of service (VxWorks OS crash) via a long HTTP GET request, possibly triggering a buffer overflow.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-1706
    - Vulnerability Description: The U.S. Robotics USR808054 wireless access point allows remote attackers to cause a denial of service (device crash) and possibly execute arbitrary code via an HTTP GET request with a long version string.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-1727
    - Vulnerability Description: BadBlue 2.5 allows remote attackers to cause a denial of service (refuse HTTP connections) via a large number of connections from the same IP address.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-1744
    - Vulnerability Description: Easy File Sharing (EFS) Webserver 1.25 allows remote attackers to cause a denial of service (CPU consumption or crash) via many large HTTP requests.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-1749
    - Vulnerability Description: Attack Mitigator IPS 5500 3.11.008, and possibly other versions, when configured in a one-armed routing configuration, allows remote attackers to cause a denial of service (CPU consumption) via a large number of HTTP requests.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-1804
    - Vulnerability Description: wMCam server 2.1.348 allows remote attackers to cause a denial of service (no new connections) via multiple malformed HTTP requests without the GET command.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-1860
    - Vulnerability Description: Buffer overflow in Check Point SmartDashboard in Check Point NG AI R54 and R55 allows remote authenticated users to cause a denial of service (server disconnect) and possibly execute arbitrary code via a large filter on a column when using SmartView Tracker.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-1973
    - Vulnerability Description: DiGi Web Server allows remote attackers to cause a denial of service (CPU consumption) via an HTTP GET request that contains a large number of / (slash) characters, which consumes resources when DiGi converts the slashes to \ (backslash) characters.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2029
    - Vulnerability Description: The Util_DecodeHTTPAuth function in BNBT BitTorrent Tracker Beta 7.5 Release 2 and earlier allows remote attackers to cause a denial of service (crash) via a Basic Authorization HTTP request with a "A==" value.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2033
    - Vulnerability Description: Orenosv 0.5.9f allows remote attackers to cause a denial of service (crash) via a long HTTP GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2035
    - Vulnerability Description: MiniShare 1.3.2 allows remote attackers to cause a denial of service (crash) via a malformed HTTP GET or HEAD request without the proper number of trailing CRLF sequences.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2045
    - Vulnerability Description: The HTTP administration interface on Conceptronic CADSLR1 ADSL router running firmware 3.04n allows remote attackers to cause a denial of service (device reboot) via an HTTP request with a long username.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2086
    - Vulnerability Description: Stack-based buffer overflow in results.stm for Sambar Server before the 6.0 production release allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via an HTTP POST request with a long query parameter.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2101
    - Vulnerability Description: The sysinfo script in GeoHttpServer allows remote attackers to cause a denial of service (crash) via a long pwd parameter, possibly triggering a buffer overflow.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2107
    - Vulnerability Description: Finjan SurfinGate 6.0 and 7.0, when running in proxy mode, does not authenticate FHTTP commands on TCP port 3141, which allows remote attackers to use the finjan-parameter-type header to (1) restart the service, (2) use the getlastmsg command to view log information, or (3) use the online command to force a policy update from the database server.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2117
    - Vulnerability Description: Tiny Server 1.1 allows remote attackers to cause a denial of service (crash) via malformed HTTP requests such as (1) a GET request without the HTTP version (HTTP/1.1), or (2) a request without GET or the HTTP version.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2120
    - Vulnerability Description: Reptile Web Server allows remote attackers to cause a denial of service (CPU consumption) via multiple incomplete GET requests without the HTTP version.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2129
    - Vulnerability Description: SurfNOW 2.2 allows remote attackers to cause a denial of service (crash) via a series of long HTTP GET requests, possibly triggering a buffer overflow.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2217
    - Vulnerability Description: Multiple unknown vulnerabilities in yhttpd in yChat before 0.7 allow remote attackers to cause a denial of service (segmentation fault) via unknown vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2224
    - Vulnerability Description: Appfoundry Message Foundry 2.75 .0003 allows remote attackers to cause a denial of service (crash) via an HTTP GET request that contains MS-DOS device names such as com1.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2315
    - Vulnerability Description: Mbedthis AppWeb HTTP server before 1.0.2 allows remote attackers to cause a denial of service (crash) via an empty OPTIONS request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2316
    - Vulnerability Description: Mbedthis AppWeb HTTP server before 1.0.2 allows remote attackers to cause a denial of service (crash) via a GET request containing an MS-DOS device name such as COM1.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2327
    - Vulnerability Description: Vizer Web Server 1.9.1 allows remote attackers to cause a denial of service (crash) via multiple malformed requests including (1) requests without GET, (2) GET requests without HTTP, (3) or long GET requests.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2330
    - Vulnerability Description: ColdFusion MX 6.1 and 6.1 J2EE allows remote attackers to cause a denial of service via an HTTP request containing a large number of form fields.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2381
    - Vulnerability Description: HttpRequest.java in Jetty HTTP Server before 4.2.19 allows remote attackers to cause denial of service (memory usage and application crash) via HTTP requests with a large Content-Length.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2424
    - Vulnerability Description: BEA WebLogic Server and WebLogic Express 8.1 through 8.1 SP2 allow remote attackers to cause a denial of service (network port comsumption) via unknown actions in HTTPS sessions, which prevents the server from releasing the network port when the session ends.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2478
    - Vulnerability Description: Unspecified vulnerability in Jetty HTTP Server, as used in (1) IBM Trading Partner Interchange before 4.2.4, (2) CA Unicenter Web Services Distributed Management (WSDM) before 3.11, and possibly other products, allows remote attackers to read arbitrary files via a .. (dot dot) in the URL.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2496
    - Vulnerability Description: The HTTP daemon in OpenText FirstClass 7.1 and 8.0 allows remote attackers to cause a denial of service (service availability loss) via a large number of POST requests to /Search.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2517
    - Vulnerability Description: myServer 0.7.1 allows remote attackers to cause a denial of service (crash) via a long HTTP POST request in a View=Logon operation to index.html.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2534
    - Vulnerability Description: Fastream NETFile Server 7.1.2 does not properly handle keep-alive connection timeouts and does not close the connection after a HEAD request, which allows remote attackers to perform a denial of service (connection consumption) by sending a large number HTTP HEAD requests.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2549
    - Vulnerability Description: Nortel Wireless LAN (WLAN) Access Point (AP) 2220, 2221, and 2225 allow remote attackers to cause a denial of service (service crash) via a TCP request with a large string, followed by 8 newline characters, to (1) the Telnet service on TCP port 23 and (2) the HTTP service on TCP port 80, possibly due to a buffer overflow.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2583
    - Vulnerability Description: SMTP service in SmarterTools SmarterMail 1.6.1511 and 1.6.1529 allows remote attackers to cause a denial of service (CPU consumption) via a large number of simultaneous open connections to TCP port 25.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2587
    - Vulnerability Description: login.aspx in SmarterTools SmarterMail 1.6.1511 and 1.6.1529 allows remote attackers to cause a denial of service via a long txtusername parameter, possibly due to a buffer overflow.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2589
    - Vulnerability Description: Gaim before 0.82 allows remote servers to cause a denial of service (application crash) via a long HTTP Content-Length header, which causes Gaim to abort when attempting to allocate memory.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2614
    - Vulnerability Description: Buffer overflow in MyWeb 3.3 allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via a long HTTP GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2726
    - Vulnerability Description: HTTPMail service in MailEnable Professional 1.18 does not properly handle arguments to the Authorization header, which allows remote attackers to cause a denial of service (null dereference and application crash).  NOTE: This is a different vulnerability than CVE-2005-1348.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2727
    - Vulnerability Description: Buffer overflow in MEHTTPS (HTTPMail) of MailEnable Professional 1.5 through 1.7 allows remote attackers to cause a denial of service (application crash) via a long HTTP GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2004-2762
    - Vulnerability Description: The server in IBM Tivoli Storage Manager (TSM) 4.2.x on MVS, 5.1.9.x before 5.1.9.1, 5.1.x before 5.1.10, 5.2.2.x before 5.2.2.3, 5.2.x before 5.2.3, 5.3.x before 5.3.0, and 6.x before 6.1, when the HTTP communication method is enabled, allows remote attackers to cause a denial of service (daemon crash or hang) via unspecified HTTP traffic, as demonstrated by the IBM port scanner 1.3.1.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-0049
    - Vulnerability Description: Windows SharePoint Services and SharePoint Team Services for Windows Server 2003 does not properly validate an HTTP redirection query, which allows remote attackers to inject arbitrary HTML and web script via a cross-site scripting (XSS) attack, or to spoof the web cache.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-0081
    - Vulnerability Description: MySQL MaxDB 7.5.0.0, and other versions before 7.5.0.21, allows remote attackers to cause a denial of service (crash) via an HTTP request with invalid headers.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-0294
    - Vulnerability Description: minis.php in Minis 0.2.1 allows remote attackers to cause a denial of service (infinite loop) via an HTTP request for a file that the web server does not have permission to read, as demonstrated using the month parameter.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-0334
    - Vulnerability Description: Linksys PSUS4 running firmware 6032 allows remote attackers to cause a denial of service (device crash) via an HTTP POST request containing an unknown parameter without a value.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-0451
    - Vulnerability Description: Sami HTTP Server 1.0.5 allows remote attackers to cause a denial of service via an HTTP request containing two CRLF sequences, which triggers a NULL dereference.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-0478
    - Vulnerability Description: Multiple buffer overflows in TrackerCam 5.12 and earlier allow remote attackers to cause a denial of service and possibly execute arbitrary code via (1) an HTTP request with a long User-Agent header or (2) a long argument to an arbitrary PHP script.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-0575
    - Vulnerability Description: Buffer overflow in Stormy Studios Knet 1.04c and earlier allows remote attackers to cause a denial of service and possibly execute arbitrary code via a long HTTP GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-0657
    - Vulnerability Description: Directory traversal vulnerability in Computalynx CProxy 3.3.x and 3.4.x through 3.4.4 allows remote attackers to read arbitrary files or cause a denial of service (application crash) via a .. (dot dot) in an HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-0734
    - Vulnerability Description: PY Software Active Webcam WebServer (webcam.exe) 5.5 allows remote attackers to cause a denial of service (memory exhaustion and process crash) via a large number of HTTP requests.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-0807
    - Vulnerability Description: Multiple buffer overflows in Cain & Abel before 2.67 allow remote attackers to cause a denial of service (application crash) and possibly execute arbitrary code via (1) an IKE packet with a large ID field that is not properly handled by the PSK sniffer filter, (2) the HTTP sniffer filter, or the (3) POP3, (4) SMTP, (5) IMAP, (6) NNTP, or (7) TDS sniffer filters.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-0874
    - Vulnerability Description: Multiple buffer overflows in the (1) AIM, (2) MSN, (3) RSS, and other plug-ins for Trillian 2.0 allow remote web servers to cause a denial of service (application crash) via a long string in an HTTP 1.1 response header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-0875
    - Vulnerability Description: Multiple buffer overflows in the Yahoo plug-in for Trillian 2.0, 3.0, and 3.1 allow remote web servers to cause a denial of service (application crash) via a long string in an HTTP 1.1 response header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-0923
    - Vulnerability Description: The SmartScan feature in the Auto-Protect module for Symantec Norton AntiVirus 2004 and 2005, as also used in Internet Security 2004/2005 and System Works 2004/2005, allows attackers to cause a denial of service (CPU consumption and system crash) by renaming a file on a network share.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-0943
    - Vulnerability Description: Cisco VPN 3000 series Concentrator running firmware 4.1.7.A and earlier allows remote attackers to cause a denial of service (device reload or drop user connection) via a crafted HTTPS packet.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-0986
    - Vulnerability Description: NLSCCSTR.DLL in the web service in IBM Lotus Domino Server 6.5.1, 6.0.3, and possibly other versions allows remote attackers to cause a denial of service (deep recursion and nHTTP.exe process crash) via a long GET request containing UNICODE decimal value 430 characters, which causes the stack to be exhausted.  NOTE: IBM has reported that it is unable to replicate this issue.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-1122
    - Vulnerability Description: Format string vulnerability in cgi.c for Monkey daemon (monkeyd) before 0.9.1 allows remote attackers to cause a denial of service and possibly execute arbitrary code via an HTTP GET request containing double-encoded format string specifiers (aka "double expansion error").
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-1132
    - Vulnerability Description: LG U8120 mobile phone allows remote attackers to cause a denial of service (device crash) via a malformed MIDI file.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-1340
    - Vulnerability Description: The HTTP proxy service in Server Admin for Mac OS X 10.3.9 does not restrict access when it is enabled, which allows remote attackers to use the proxy.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-1385
    - Vulnerability Description: Safari 1.3 allows remote attackers to cause a denial of service (application crash) via a long https URL that triggers a NULL pointer dereference.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-1517
    - Vulnerability Description: Unknown vulnerability in Cisco Firewall Services Module (FWSM) 2.3.1 and earlier, when using URL, FTP, or HTTPS filtering exceptions, allows certain TCP packets to bypass access control lists (ACLs).
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-1666
    - Vulnerability Description: Multiple buffer overflows in Orenosv HTTP/FTP Server 0.8.1 allow remote authenticated users to cause a denial of service (server crash) and possibly execute arbitrary code via long arguments to FTP commands such as MKD, RMD, or DELE, which are processed by the (1) ftp_xlate_path, (2) ftp_is_canonical, or (3) os_fn_nativize functions, or (4) a long SSI command that is processed by the parse_cmd function in cgissi.exe.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-1667
    - Vulnerability Description: DataTrac Activity Console 1.1 allows remote attackers to cause a denial of service via a long HTTP GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-1836
    - Vulnerability Description: NEXTWEB (i)Site allows remote attackers to cause a denial of service (error 500) via a crafted HTTP request, possibly involving wildcard requests for .jsp files.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-2201
    - Vulnerability Description: Unknown vulnerability in the MicroServer Web Server for Xerox WorkCentre Pro Color 2128, 2636, and 3545, version 0.001.04.044 through 0.001.04.504, allow attackers to cause a denial of service or access files via crafted HTTP requests.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-2222
    - Vulnerability Description: Unknown vulnerability in the HTTPMail service in MailEnable Professional before 1.6 has unknown impact and attack vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-2361
    - Vulnerability Description: Unknown vulnerability in the (1) AgentX dissector, (2) PER dissector, (3) DOCSIS dissector, (4) SCTP graphs, (5) HTTP dissector, (6) DCERPC, (7) DHCP, (8) RADIUS dissector, (9) Telnet dissector, (10) IS-IS LSP dissector, or (11) NCP dissector in Ethereal 0.8.19 through 0.10.11 allows remote attackers to cause a denial of service (application crash or abort) via unknown attack vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-2455
    - Vulnerability Description: Greasemonkey before 0.3.5 allows remote web servers to (1) read arbitrary files via a GET request to a file:// URL in the GM_xmlhttpRequest API function, (2) list installed scripts using GM_scripts, or obtain sensitive information via (3) GM_setValue and GM_getValue.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-2506
    - Vulnerability Description: Algorithmic complexity vulnerability in CoreFoundation in Mac OS X 10.3.9 and 10.4.2 allows attackers to cause a denial of service (CPU consumption) via crafted Gregorian dates.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-2646
    - Vulnerability Description: Unknown vulnerability in Xerox MicroServer Web Server in Document Centre 220 through 265, 332 and 340, 420 through 490, and 535 through 555 allows remote attackers to cause a denial of service or read files via unknown vectors involving crafted HTTP requests.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-2728
    - Vulnerability Description: The byte-range filter in Apache 2.0 before 2.0.54 allows remote attackers to cause a denial of service (memory consumption) via an HTTP header with a large Range field.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-2729
    - Vulnerability Description: The HTTP proxy in Astaro Security Linux 6.0 does not properly filter HTTP CONNECT requests to localhost, which allows remote attackers to bypass firewall rules and connect to local services.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-2806
    - Vulnerability Description: client.cpp in BNBT EasyTracker 7.7r3.2004.10.27 and earlier allows remote attackers cause a denial of service (application hang) via an HTTP header containing only a ":" (colon), possibly leading to an integer signedness error due to a missing field name or value.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-2874
    - Vulnerability Description: The is_path_absolute function in scheduler/client.c for the daemon in CUPS before 1.1.23 allows remote attackers to cause a denial of service (CPU consumption by tight loop) via a "..\.." URL in an HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-2912
    - Vulnerability Description: Linksys WRT54G router allows remote attackers to cause a denial of service (CPU consumption and server hang) via an HTTP POST request with a negative Content-Length value.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-2922
    - Vulnerability Description: Heap-based buffer overflow in the embedded player in multiple RealNetworks products and versions including RealPlayer 10.x, RealOne Player, and Helix Player allows remote malicious servers to cause a denial of service (crash) and possibly execute arbitrary code via a chunked Transfer-Encoding HTTP response in which either (1) the chunk header length is specified as -1, (2) the chunk header with a length that is less than the actual amount of sent data, or (3) a missing chunk header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-3033
    - Vulnerability Description: Stack-based buffer overflow in vxWeb 1.1.4 allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via a long HTTP GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-3144
    - Vulnerability Description: httpAdapter.c in sblim-sfcb before 0.9.2 allows remote attackers to cause a denial of service via long HTTP headers.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-3145
    - Vulnerability Description: httpAdapter.c in sblim-sfcb before 0.9.2 allows remote attackers to cause a denial of service (resource consumption) by connecting to sblim-sfcb but not sending any data.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-3187
    - Vulnerability Description: The listening daemon in Blue Coat Systems Inc. WinProxy before 6.1a allows remote attackers to cause a denial of service (crash) via a long HTTP request that causes an out-of-bounds read.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-3206
    - Vulnerability Description: iSQL*Plus (isqlplus) for Oracle9i Database Server Release 2 9.0.2.4 allows remote attackers to cause a denial of service (TNS listener stop) via an HTTP request with an sid parameter that contains a STOP command.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-3269
    - Vulnerability Description: Stack-based buffer overflow in help.cgi in the HTTP administrative interface for (1) Sun Java System Directory Server 5.2 2003Q4, 2004Q2, and 2005Q1, (2) Red Hat Directory Server and (3) Certificate Server before 7.1 SP1, (4) Sun ONE Directory Server 5.1 SP4 and earlier, and (5) Sun ONE Administration Server 5.2 allows remote attackers to cause a denial of service (admin server crash), or local users to gain root privileges.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-3322
    - Vulnerability Description: Unspecified vulnerability in Squid on SUSE Linux 9.0 allows remote attackers to cause a denial of service (crash) via HTTPs (SSL).
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-3475
    - Vulnerability Description: Hasbani Web Server (WindWeb) 2.0 allows remote attackers to cause a denial of service (infinite loop) via HTTP crafted GET requests.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-3653
    - Vulnerability Description: Heap-based buffer overflow in the iGateway service for various Computer Associates (CA) iTechnology products, in iTechnology iGateway before 4.0.051230, allows remote attackers to execute arbitrary code via an HTTP request with a negative Content-Length field.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-4147
    - Vulnerability Description: The TCLHTTPd service in Lyris ListManager before 8.9b allows remote attackers to obtain source code for arbitrary .tml (TCL) files via (1) a request with a trailing null byte (%00), which might also require (2) an authentication bypass step that involves a username with a trailing "@" characters.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-4296
    - Vulnerability Description: AppServ Open Project 2.5.3 allows remote attackers to cause a denial of service via a large HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-4332
    - Vulnerability Description: Cisco Clean Access 3.5.5 and earlier on the Secure Smart Manager allows remote attackers to bypass authentication and cause a denial of service or upload files via direct requests to obsolete JSP files including (1) admin/uploadclient.jsp, (2) apply_firmware_action.jsp, and (3) file.jsp.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-4503
    - Vulnerability Description: httprint v202, and possibly other versions before v301, allows remote attackers to cause a denial of service (crash) via a long Server field in an HTTP response.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-4564
    - Vulnerability Description: The Internet Key Exchange version 1 (IKEv1) implementation in ADTRAN NetVanta before 10.03.03.E might allow remote attackers to cause a denial of service via crafted IKE packets, as demonstrated by the PROTOS ISAKMP Test Suite for IKEv1.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-4810
    - Vulnerability Description: Microsoft Internet Explorer 7.0 Beta3 and earlier allows remote attackers to cause a denial of service (crash) via a "text/html" HTML Content-type header sent in response to an XMLHttpRequest (AJAX).
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-4825
    - Vulnerability Description: Cisco Clean Access 3.5.5 and earlier on the Secure Smart Manager allows remote attackers to bypass authentication and cause a denial of service (disk consumption), or make unauthorized files accessible, by uploading files through requests to certain JSP scripts, a related issue to CVE-2005-4332.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-4843
    - Vulnerability Description: The SmartConnect Class control allows remote attackers to cause a denial of service (Internet Explorer crash) by creating a COM object of the class associated with the control's CLSID, which is not intended for use within Internet Explorer.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2005-4857
    - Vulnerability Description: eZ publish 3.5 before 3.5.7, 3.6 before 3.6.5, 3.7 before 3.7.3, and 3.8 before 20051128 allows remote authenticated users to cause a denial of service (Apache httpd segmentation fault) via a request to content/advancedsearch.php with an empty SearchContentClassID parameter, reportedly related to a "memory addressing error".
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-0201
    - Vulnerability Description: Dave Nielsen and Patrick Breitenbach PayPal Web Services (aka PHP Toolkit) 0.50, and possibly earlier versions, allows remote attackers to enter false payment entries into the log file via HTTP POST requests to ipn_success.php.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-0342
    - Vulnerability Description: RockLiffe MailSite HTTP Mail management agent (httpma) 7.0.3.1 allows remote attackers to cause a denial of service (CPU consumption and crash) via a malformed query string containing special characters such as "|".
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-0362
    - Vulnerability Description: TippingPoint Intrusion Prevention System (IPS) TOS before 2.1.4.6324, and TOS 2.2.x before 2.2.1.6506, allow remote attackers to cause a denial of service (CPU consumption) via an unknown vector, probably involving an HTTP request with a negative number in the Content-Length header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-0483
    - Vulnerability Description: Cisco VPN 3000 series concentrators running software 4.7.0 through 4.7.2.A allow remote attackers to cause a denial of service (device reload or user disconnect) via a crafted HTTP packet.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-0784
    - Vulnerability Description: D-Link DWL-G700AP with firmware 2.00 and 2.01 allows remote attackers to cause a denial of service (CAMEO HTTP service crash) via a request composed of "GET" followed by a space and two newlines, possibly triggering the crash due to missing arguments.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-1159
    - Vulnerability Description: Format string vulnerability in Easy File Sharing (EFS) Web Server 3.2 allows remote attackers to cause a denial of service (server crash) and possibly execute arbitrary code via format string specifiers in the query string argument in an HTTP GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-1218
    - Vulnerability Description: Unspecified vulnerability in the HTTP proxy in Novell BorderManager 3.8 and earlier allows remote attackers to cause a denial of service (CPU consumption and ABEND) via unknown attack vectors related to "media streaming over HTTP 1.1".
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-1619
    - Vulnerability Description: IBM WebSphere Application Server 4.0.1 through 4.0.3 allows remote attackers to cause a denial of service (application crash) via an HTTP request with a large header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-1631
    - Vulnerability Description: Unspecified vulnerability in the HTTP compression functionality in Cisco CSS 11500 Series Content Services switches allows remote attackers to cause a denial of service (device reload) via (1) "valid, but obsolete" or (2) "specially crafted" HTTP requests.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-1647
    - Vulnerability Description: An unspecified "logical programming mistake" in SMART SynchronEyes Student and Teacher 6.0, and possibly earlier versions, allows remote attackers to cause a denial of service via a large packet to the Teacher discovery port (UDP port 5496), which causes a thread to terminate and prevents communications on that port.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-1648
    - Vulnerability Description: SMART SynchronEyes Student and Teacher 6.0, and possibly earlier versions, allows remote attackers to cause a denial of service (memory consumption) via a certain packet to the Teacher discovery port that causes SynchronEyes to connect to the attacker's machine and read a value that is used as a parameter to malloc.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-1931
    - Vulnerability Description: The HTTP/XMLRPC server in Ruby before 1.8.2 uses blocking sockets, which allows attackers to cause a denial of service (blocked connections) via a large amount of data.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-2023
    - Vulnerability Description: Integer overflow in the RTSP_msg_len function in rtsp/RTSP_msg_len.c in Fenice 1.10 and earlier allows remote attackers to cause a denial of service (application crash) via a large HTTP Content-Length value, which leads to an invalid memory access.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-2113
    - Vulnerability Description: The embedded HTTP server in Fuji Xerox Printing Systems (FXPS) print engine, as used in products including (1) Dell 3000cn through 5110cn and (2) Fuji Xerox DocuPrint firmware before 20060628 and Network Option Card firmware before 5.13, does not properly perform authentication for HTTP requests, which allows remote attackers to modify system configuration via crafted requests, including changing the administrator password or causing a denial of service to the print server.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-2222
    - Vulnerability Description: Buffer overflow in zawhttpd 0.8.23, and possibly previous versions, allows remote attackers to cause a denial of service (daemon crash) via a request for a URI composed of several "\" (backslash) characters.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-2309
    - Vulnerability Description: The HTTP service in EServ/3 3.25 allows remote attackers to obtain sensitive information via crafted HTTP requests containing dot, space, and slash characters, which reveals the source code of script files.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-2489
    - Vulnerability Description: Integer overflow in CGI scripts in Nagios 1.x before 1.4.1 and 2.x before 2.3.1 allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via a content length (Content-Length) HTTP header.  NOTE: this is a different vulnerability than CVE-2006-2162.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-2587
    - Vulnerability Description: Buffer overflow in the WebTool HTTP server component in (1) PunkBuster before 1.229, as used by multiple products including (2) America's Army 1.228 and earlier, (3) Battlefield 1942 1.158 and earlier, (4) Battlefield 2 1.184 and earlier, (5) Battlefield Vietnam 1.150 and earlier, (6) Call of Duty 1.173 and earlier, (7) Call of Duty 2 1.108 and earlier, (8) DOOM 3 1.159 and earlier, (9) Enemy Territory 1.167 and earlier, (10) Far Cry 1.150 and earlier, (11) F.E.A.R. 1.093 and earlier, (12) Joint Operations 1.187 and earlier, (13) Quake III Arena 1.150 and earlier, (14) Quake 4 1.181 and earlier, (15) Rainbow Six 3: Raven Shield 1.169 and earlier, (16) Rainbow Six 4: Lockdown 1.093 and earlier, (17) Return to Castle Wolfenstein 1.175 and earlier, and (18) Soldier of Fortune II 1.183 and earlier allows remote attackers to cause a denial of service (application crash) via a long webkey parameter.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-2802
    - Vulnerability Description: Buffer overflow in the HTTP Plugin (xineplug_inp_http.so) for xine-lib 1.1.1 allows remote attackers to cause a denial of service (application crash) via a long reply from an HTTP server, as demonstrated using gxine 0.5.6.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-2830
    - Vulnerability Description: Buffer overflow in TIBCO Rendezvous before 7.5.1, TIBCO Runtime Agent (TRA) before 5.4, and Hawk before 4.6.1 allows remote attackers to cause a denial of service and possibly execute arbitrary code via the HTTP administrative interface.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-2926
    - Vulnerability Description: Stack-based buffer overflow in the WWW Proxy Server of Qbik WinGate 6.1.1.1077 allows remote attackers to cause a denial of service and possibly execute arbitrary code via a long URL HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-3124
    - Vulnerability Description: Buffer overflow in the HTTP header parsing in Streamripper before 1.61.26 allows remote attackers to cause a denial of service and possibly execute arbitrary code via crafted HTTP headers.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-3276
    - Vulnerability Description: Heap-based buffer overflow in RealNetworks Helix DNA Server 10.0 and 11.0 allows remote attackers to execute arbitrary code via (1) a long User-Agent HTTP header in the RTSP service and (2) unspecified vectors involving the "parsing of HTTP URL schemes".
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-3379
    - Vulnerability Description: Algorithmic complexity vulnerability in Hiki Wiki 0.6.0 through 0.6.5 and 0.8.0 through 0.8.5 allows remote attackers to cause a denial of service (CPU consumption) by performing a diff between large, crafted pages that trigger the worst case.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-3380
    - Vulnerability Description: Algorithmic complexity vulnerability in FreeStyle Wiki before 3.6.2 allows remote attackers to cause a denial of service (CPU consumption) by performing a diff between large, crafted pages that trigger the worst case.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-3511
    - Vulnerability Description: Internet Explorer 6 on Windows XP SP2 allows remote attackers to cause a denial of service (crash) by setting the fonts property of the HtmlDlgSafeHelper object, which triggers a null dereference.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-3546
    - Vulnerability Description: Patrice Freydiere ImgSvr (aka ADA Image Server) allows remote attackers to cause a denial of service (daemon crash) via a long HTTP POST request.  NOTE: this might be the same issue as CVE-2004-2463.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-3548
    - Vulnerability Description: Multiple cross-site scripting (XSS) vulnerabilities in Horde Application Framework 3.0.0 through 3.0.10 and 3.1.0 through 3.1.1 allow remote attackers to inject arbitrary web script or HTML via a (1) javascript URI or an external (2) http, (3) https, or (4) ftp URI in the url parameter in services/go.php (aka the dereferrer), (5) a javascript URI in the module parameter in services/help (aka the help viewer), and (6) the name parameter in services/problem.php (aka the problem reporting screen).
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-3549
    - Vulnerability Description: services/go.php in Horde Application Framework 3.0.0 through 3.0.10 and 3.1.0 through 3.1.1 does not properly restrict its image proxy capability, which allows remote attackers to perform "Web tunneling" attacks and use the server as a proxy via (1) http, (2) https, and (3) ftp URL in the url parameter, which is requested from the server.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-3731
    - Vulnerability Description: Mozilla Firefox 1.5.0.4 and earlier allows remote user-assisted attackers to cause a denial of service (crash) via a form with a multipart/form-data encoding and a user-uploaded file.  NOTE: a third party has claimed that this issue might be related to the LiveHTTPHeaders extension.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-3869
    - Vulnerability Description: Heap-based buffer overflow in URLMON.DLL in Microsoft Internet Explorer 6 SP1 on Windows 2000 and XP SP1, with versions the MS06-042 patch before 20060824, allows remote attackers to cause a denial of service (crash) or execute arbitrary code via a long URL on a website that uses HTTP 1.1 compression.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-3873
    - Vulnerability Description: Heap-based buffer overflow in URLMON.DLL in Microsoft Internet Explorer 6 SP1 on Windows 2000 and XP SP1, with versions the MS06-042 patch before 20060912, allows remote attackers to cause a denial of service (crash) or execute arbitrary code via a long URL in a GZIP-encoded website that was the target of an HTTP redirect, due to an incomplete fix for CVE-2006-3869.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-3945
    - Vulnerability Description: The CSS functionality in Opera 9 on Windows XP SP2 allows remote attackers to cause a denial of service (crash) by setting the background property of a DHTML element to a long http or https URL, which triggers memory corruption.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-4089
    - Vulnerability Description: Multiple buffer overflows in Andy Lo-A-Foe AlsaPlayer 0.99.76 and earlier allow remote attackers to cause a denial of service (application crash), or have other unknown impact, via (1) a long Location field sent by a web server, which triggers an overflow in the reconnect function in reader/http/http.c
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-4133
    - Vulnerability Description: Heap-based buffer overflow in SAP Internet Graphics Service (IGS) 6.40 and earlier, and 7.00 and earlier, allows remote attackers to cause a denial of service (crash) or execute arbitrary code via an HTTP request with an ADM:GETLOGFILE command and a long portwatcher argument, which triggers the overflow during error message construction when the _snprintf function returns a negative value that is used in a memcpy operation.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-4134
    - Vulnerability Description: Unspecified vulnerability related to a "design flaw" in SAP Internet Graphics Service (IGS) 6.40 and earlier and 7.00 and earlier allows remote attackers to cause a denial of service (service shutdown) via certain HTTP requests.  NOTE: This information is based upon a vague initial disclosure. Details will be updated after the grace period has ended.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-4197
    - Vulnerability Description: Multiple buffer overflows in libmusicbrainz (aka mb_client or MusicBrainz Client Library) 2.1.2 and earlier, and SVN 8406 and earlier, allow remote attackers to cause a denial of service (crash) or execute arbitrary code via (1) a long Location header by the HTTP server, which triggers an overflow in the MBHttp::Download function in lib/http.cpp
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-4409
    - Vulnerability Description: The Online Certificate Status Protocol (OCSP) service in the Security Framework in Apple Mac OS X 10.4 through 10.4.8 retrieve certificate revocation lists (CRL) when an HTTP proxy is in use, which could cause the system to accept certificates that have been revoked.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-4511
    - Vulnerability Description: Messenger Agents (nmma.exe) in Novell GroupWise 2.0.2 and 1.0.6 allows remote attackers to cause a denial of service (crash) via a crafted HTTP POST request to TCP port 8300 with a modified val parameter, which triggers a null dereference related to "zero-size strings in blowfish routines."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-4517
    - Vulnerability Description: Novell iManager 2.5 and 2.0.2 allows remote attackers to cause a denial of service (crash) in the Tomcat server via a long TREE parameter in an HTTP POST, which triggers a NULL pointer dereference.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-4685
    - Vulnerability Description: The XMLHTTP ActiveX control in Microsoft XML Parser 2.6 and XML Core Services 3.0 through 6.0 does not properly handle HTTP server-side redirects, which allows remote user-assisted attackers to access content from other domains.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-5196
    - Vulnerability Description: The HTTP interface in the Motorola SURFboard SB4200 Cable Modem allows remote attackers to cause a denial of service (device crash) via a request with MfcISAPICommand set to SecretProc and a long string in the Secret parameter.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-5233
    - Vulnerability Description: Polycom SoundPoint IP 301 VoIP Desktop Phone, firmware version 1.4.1.0040, allows remote attackers to cause a denial of service (reboot) via (1) a long URL sent to the HTTP daemon and (2) unspecified manipulations as demonstrated by the Nessus http_fingerprinting_hmap.nasl script.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-5467
    - Vulnerability Description: The cgi.rb CGI library for Ruby 1.8 allows remote attackers to cause a denial of service (infinite loop and CPU consumption) via an HTTP request with a multipart MIME body that contains an invalid boundary specifier, as demonstrated using a specifier that begins with a "-" instead of "--" and contains an inconsistent ID.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-5468
    - Vulnerability Description: Unspecified vulnerability in the HTTP dissector in Wireshark (formerly Ethereal) 0.99.3 allows remote attackers to cause a denial of service (crash) via unspecified vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-5596
    - Vulnerability Description: Directory traversal vulnerability in the SSL server in AEP Smartgate 4.3b allows remote attackers to download arbitrary files via ..\ (dot dot backslash) sequences in an HTTP GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-5725
    - Vulnerability Description: The SSL server in AEP Smartgate 4.3b allows remote attackers to determine existence of directories via a direct request for a directory URI, which returns different HTTP status codes for existing and non-existing directories.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-5745
    - Vulnerability Description: Unspecified vulnerability in the setRequestHeader method in the XMLHTTP (XML HTTP) ActiveX Control 4.0 in Microsoft XML Core Services 4.0 on Windows, when accessed by Internet Explorer, allows remote attackers to execute arbitrary code via crafted arguments that lead to memory corruption, a different vulnerability than CVE-2006-4685.  NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-5801
    - Vulnerability Description: The owserver module in owfs and owhttpd 2.5p5 and earlier does not properly check the path type, which allows attackers to cause a denial of service (application crash) related to use of the path in owshell.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-5876
    - Vulnerability Description: The soup_headers_parse function in soup-headers.c for libsoup HTTP library before 2.2.99 allows remote attackers to cause a denial of service (crash) via malformed HTTP headers, probably involving missing fields or values.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-6303
    - Vulnerability Description: The read_multipart function in cgi.rb in Ruby before 1.8.5-p2 does not properly detect boundaries in MIME multipart content, which allows remote attackers to cause a denial of service (infinite loop) via crafted HTTP requests, a different issue than CVE-2006-5467.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-6345
    - Vulnerability Description: Directory traversal vulnerability in SAP Internet Graphics Service (IGS) 6.40 Patchlevel 16 and earlier, and 7.00 Patchlevel 6 and earlier, allows remote attackers to delete arbitrary files via directory traversal sequences in an HTTP request.  NOTE: This information is based upon an initial disclosure. Details will be updated after the grace period has ended. This issue is different from CVE-2006-4133 and CVE-2006-4134.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-6361
    - Vulnerability Description: Heap-based buffer overflow in the uploadprogress_php_rfc1867_file function in uploadprogress.c in Bitflux Upload Progress Meter before 8276 allows remote attackers to cause a denial of service (crash) or execute arbitrary code via crafted HTTP POST fileupload requests.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-6430
    - Vulnerability Description: Web services in Xerox WorkCentre and WorkCentre Pro before 12.060.17.000, 13.x before 13.060.17.000, and 14.x before 14.060.17.000 do not require HTTPS, which allows remote attackers to obtain sensitive information by sniffing the unencrypted HTTP traffic.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-6674
    - Vulnerability Description: Ozeki HTTP-SMS Gateway 1.0, and possibly earlier, stores usernames and passwords in plaintext in the HKLM\Software\Ozeki\SMSServer\CurrentVersion\Plugins\httpsmsgate registry key, which allows local users to obtain sensitive information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-6684
    - Vulnerability Description: Heap-based buffer overflow in Pedro Lineu Orso chetcpasswd before 2.4 allows remote attackers to cause a denial of service (application crash) and possibly execute arbitrary code via a long X-Forwarded-For HTTP header.  NOTE: The provenance of this information is unknown
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-6855
    - Vulnerability Description: AIDeX Mini-WebServer 1.1 early release 3 allows remote attackers to cause a denial of service (daemon crash) via a flood of HTTP GET requests, possibly related to display of HTTP log data by the GUI. NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-6931
    - Vulnerability Description: Algorithmic complexity vulnerability in Snort before 2.6.1, during predicate evaluation in rule matching for certain rules, allows remote attackers to cause a denial of service (CPU consumption and detection outage) via crafted network traffic, aka a "backtracking attack."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-7121
    - Vulnerability Description: The HTTP server in Linksys SPA-921 VoIP Desktop Phone allows remote attackers to cause a denial of service (reboot) via (1) a long URL, or a long (2) username or (3) password during Basic Authentication.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-7160
    - Vulnerability Description: The Sandbox.sys driver in Outpost Firewall PRO 4.0, and possibly earlier versions, does not validate arguments to hooked SSDT functions, which allows local users to cause a denial of service (crash) via invalid arguments to the (1) NtAssignProcessToJobObject,, (2) NtCreateKey, (3) NtCreateThread, (4) NtDeleteFile, (5) NtLoadDriver, (6) NtOpenProcess, (7) NtProtectVirtualMemory, (8) NtReplaceKey, (9) NtTerminateProcess, (10) NtTerminateThread, (11) NtUnloadDriver, and (12) NtWriteVirtualMemory functions.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2006-7239
    - Vulnerability Description: The _gnutls_x509_oid2mac_algorithm function in lib/gnutls_algorithms.c in GnuTLS before 1.4.2 allows remote attackers to cause a denial of service (crash) via a crafted X.509 certificate that uses a hash algorithm that is not supported by GnuTLS, which triggers a NULL pointer dereference.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-0019
    - Vulnerability Description: Multiple heap-based buffer overflows in rumpusd in Rumpus 5.1 and earlier (1) allow remote authenticated users to execute arbitrary code via a long LIST command and other unspecified requests to the FTP service, and (2) allow remote attackers to execute arbitrary code via unspecified requests to the HTTP service.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-0086
    - Vulnerability Description: ** DISPUTED **  The Apache HTTP Server, when accessed through a TCP connection with a large window size, allows remote attackers to cause a denial of service (network bandwidth consumption) via a Range header that specifies multiple copies of the same fragment.  NOTE: the severity of this issue has been disputed by third parties, who state that the large window size required by the attack is not normally supported or configured by the server, or that a DDoS-style attack would accomplish the same goal.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-0105
    - Vulnerability Description: Stack-based buffer overflow in the CSAdmin service in Cisco Secure Access Control Server (ACS) for Windows before 4.1 and ACS Solution Engine before 4.1 allows remote attackers to execute arbitrary code via a crafted HTTP GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-0120
    - Vulnerability Description: Acunetix Web Vulnerability Scanner (WVS) 4.0 Build 20060717 and earlier allows remote attackers to cause a denial of service (application crash) via multiple HTTP requests containing invalid Content-Length values.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-0124
    - Vulnerability Description: Unspecified vulnerability in Drupal before 4.6.11, and 4.7 before 4.7.5, when MySQL is used, allows remote authenticated users to cause a denial of service by poisoning the page cache via unspecified vectors, which triggers erroneous 404 HTTP errors for pages that exist.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-0356
    - Vulnerability Description: The Common Controls Replacement Project (CCRP) FolderTreeview (FTV) ActiveX control (ccrpftv6.ocx) allows remote attackers to cause a denial of service (Internet Explorer 7 crash) via a long CCRP.RootFolder property value.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-0419
    - Vulnerability Description: The BEA WebLogic Server proxy plug-in before June 2006 for the Apache HTTP Server does not properly handle protocol errors, which allows remote attackers to cause a denial of service (server outage).
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-0458
    - Vulnerability Description: Unspecified vulnerability in the HTTP dissector in Wireshark (formerly Ethereal) 0.99.3 and 0.99.4 allows remote attackers to cause a denial of service (application crash) via unspecified vectors, a different issue than CVE-2006-5468.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-0459
    - Vulnerability Description: packet-tcp.c in the TCP dissector in Wireshark (formerly Ethereal) 0.99.2 through 0.99.4 allows remote attackers to cause a denial of service (application crash or hang) via fragmented HTTP packets.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-0464
    - Vulnerability Description: The _CFNetConnectionWillEnqueueRequests function in CFNetwork 129.19 on Apple Mac OS X 10.4 through 10.4.10 allows remote attackers to cause a denial of service (application crash) via a crafted HTTP 301 response, which results in a NULL pointer dereference.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-0524
    - Vulnerability Description: The LG Chocolate KG800 phone allows remote attackers to cause a denial of service (continual modal dialogs and UI unavailability) by repeatedly trying to OBEX push a file over Bluetooth, as demonstrated by ussp-push.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-0533
    - Vulnerability Description: The AToZed IntraWeb component 8.0 and earlier for Borland Delphi and Kylix, and IntraWeb 9.0 before build (9.0.12), allows remote attackers to cause a denial of service (thread hang or CPU consumption) via a crafted HTTP request, related to the OnBeforeDispatch function in the TIWServerController object.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-0548
    - Vulnerability Description: KarjaSoft Sami HTTP Server 2.0.1 allows remote attackers to cause a denial of service (daemon hang) via a large number of requests for nonexistent objects.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-0578
    - Vulnerability Description: The http_open function in httpget.c in mpg123 before 0.64 allows remote attackers to cause a denial of service (infinite loop) by closing the HTTP connection early.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-0672
    - Vulnerability Description: LGSERVER.EXE in BrightStor Mobile Backup 4.0 allows remote attackers to cause a denial of service (disk consumption and daemon hang) via a value of 0xFFFFFF7F at a certain point in an authentication negotiation packet, which writes a large amount of data to a .USX file in CA_BABLDdata\Server\data\transfer\.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-0673
    - Vulnerability Description: LGSERVER.EXE in BrightStor ARCserve Backup for Laptops & Desktops r11.1 allows remote attackers to cause a denial of service (daemon crash) via a value of 0xFFFFFFFF at a certain point in an authentication negotiation packet, which results in an out-of-bounds read.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-0674
    - Vulnerability Description: Pictures and Videos on Windows Mobile 5.0 and Windows Mobile 2003 and 2003SE for Smartphones and PocketPC allows user-assisted remote attackers to cause a denial of service (device hang) via a malformed JPEG file.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-0685
    - Vulnerability Description: Internet Explorer on Windows Mobile 5.0 and Windows Mobile 2003 and 2003SE for Smartphones and PocketPC allows attackers to cause a denial of service (application crash and device instability) via unspecified vectors, possibly related to a buffer overflow.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-0709
    - Vulnerability Description: cmdmon.sys in Comodo Firewall Pro (formerly Comodo Personal Firewall) 2.4.16.174 and earlier does not validate arguments that originate in user mode for the (1) NtCreateSection, (2) NtOpenProcess, (3) NtOpenSection, (4) NtOpenThread, and (5) NtSetValueKey hooked SSDT functions, which allows local users to cause a denial of service (system crash) and possibly gain privileges via invalid arguments.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-0756
    - Vulnerability Description: Chicken of the VNC (cotv) 2.0 allows remote attackers to cause a denial of service (application crash) via a large computer-name size value in a ServerInit packet, which triggers a failed malloc and a resulting NULL dereference.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-0796
    - Vulnerability Description: Blue Coat Systems WinProxy 6.1a and 6.0 r1c, and possibly earlier, allows remote attackers to cause a denial of service (daemon crash) or possibly execute arbitrary code via a long HTTP CONNECT request, which triggers heap corruption.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-0962
    - Vulnerability Description: Cisco PIX 500 and ASA 5500 Series Security Appliances 7.0 before 7.0(4.14) and 7.1 before 7.1(2.1), and the FWSM 2.x before 2.3(4.12) and 3.x before 3.1(3.24), when "inspect http" is enabled, allows remote attackers to cause a denial of service (device reboot) via malformed HTTP traffic.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-0964
    - Vulnerability Description: Cisco FWSM 3.x before 3.1(3.18), when authentication is configured to use "aaa authentication match" or "aaa authentication include", allows remote attackers to cause a denial of service (device reboot) via a malformed HTTPS request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-0965
    - Vulnerability Description: Cisco FWSM 3.x before 3.1(3.2), when authentication is configured to use "aaa authentication match" or "aaa authentication include", allows remote attackers to cause a denial of service (device reboot) via a long HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-0966
    - Vulnerability Description: Cisco Firewall Services Module (FWSM) 3.x before 3.1(3.11), when the HTTPS server is enabled, allows remote attackers to cause a denial of service (device reboot) via certain HTTPS traffic.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-0977
    - Vulnerability Description: IBM Lotus Domino R5 and R6 WebMail, with "Generate HTML for all fields" enabled, stores HTTPPassword hashes from names.nsf in a manner accessible through Readviewentries and OpenDocument requests to the defaultview view, a different vector than CVE-2005-2428.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-1204
    - Vulnerability Description: Stack-based buffer overflow in the Universal Plug and Play (UPnP) service in Microsoft Windows XP SP2 allows remote attackers on the same subnet to execute arbitrary code via crafted HTTP headers in request or notification messages, which trigger memory corruption.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-1327
    - Vulnerability Description: The SILC_SERVER_CMD_FUNC function in apps/silcd/command.c in silc-server 1.0.2 allows remote attackers to cause a denial of service (NULL dereference and daemon crash) via a request without a cipher algorithm and an invalid HMAC algorithm.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-1501
    - Vulnerability Description: Stack-based buffer overflow in Avant Browser 11.0 build 26 allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via a long Content-Type HTTP header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-1504
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in the Servlet Service in Fujitsu Interstage Application Server (IJServer) 8.0.2 and earlier allows remote attackers to inject arbitrary web script or HTML via unspecified vectors, possibly involving web.xml and HTTP 404 and 500 status codes.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-1685
    - Vulnerability Description: Buffer overflow in k9filter.exe in BlueCoat K9 Web Protection 3.2.36, and probably other versions before 3.2.44, allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via a long HTTP GET request to port 2372.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-1863
    - Vulnerability Description: cache_util.c in the mod_cache module in Apache HTTP Server (httpd), when caching is enabled and a threaded Multi-Processing Module (MPM) is used, allows remote attackers to cause a denial of service (child processing handler crash) via a request with the (1) s-maxage, (2) max-age, (3) min-fresh, or (4) max-stale Cache-Control headers without a value.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-1868
    - Vulnerability Description: The management service in IBM Tivoli Provisioning Manager for OS Deployment before 5.1 Fix Pack 2 does not properly handle multipart/form-data in HTTP POST requests, which allows remote attackers to execute arbitrary code or cause a denial of service (daemon crash) via crafted POST requests to port 8080/tcp or 443/tcp.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-1869
    - Vulnerability Description: lighttpd 1.4.12 and 1.4.13 allows remote attackers to cause a denial of service (cpu and resource consumption) by disconnecting while lighttpd is parsing CRLF sequences, which triggers an infinite loop and file descriptor consumption.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-1870
    - Vulnerability Description: lighttpd before 1.4.14 allows attackers to cause a denial of service (crash) via a request to a file whose mtime is 0, which results in a NULL pointer dereference.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-1987
    - Vulnerability Description: ** DISPUTED **  Multiple PHP remote file inclusion vulnerabilities in PHPEcho CMS 2.0 allow remote attackers to execute arbitrary PHP code via a URL in the (1) _plugin_file parameter to smarty/internals/core.load_pulgins.php or the (2) root_path parameter to index.php.  NOTE: CVE disputes (1) because the inclusion occurs within a function that is not called during a direct request. CVE disputes (2) because root_path is defined in config.php before use.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-2031
    - Vulnerability Description: Buffer overflow in the HTTP proxy service for 3proxy 0.5 to 0.5.3g, and 0.6b-devel before 20070413, might allow remote attackers to execute arbitrary code via crafted transparent requests.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-2279
    - Vulnerability Description: The Scheduler Service (VxSchedService.exe) in Symantec Storage Foundation for Windows 5.0 allows remote attackers to bypass authentication and execute arbitrary code via certain requests to the service socket that create (1) PreScript or (2) PostScript registry values under Veritas\VxSvc\CurrentVersion\Schedules specifying future command execution.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-2336
    - Vulnerability Description: Unspecified vulnerability in InterVations NaviCOPA Web Server 2.01 20070323 allows remote attackers to cause a denial of service (daemon crash) via crafted HTTP requests, as demonstrated by long requests containing '\A' characters, probably a different issue than CVE-2006-5112 and CVE-2007-1733.  NOTE: the provenance of this information is unknown
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-2367
    - Vulnerability Description: Buffer overflow in wserve_console.exe in Wserve HTTP Server (whttp) 4.6 allows remote attackers to cause a denial of service (forced application exit) via a long directory name in the URI.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-2494
    - Vulnerability Description: Multiple stack-based buffer overflows in the PowerPointOCX ActiveX control in PowerPointViewer.ocx 3.1.0.3 allow remote attackers to cause a denial of service (Internet Explorer 7 crash) via a long (1) DoOleCommand, (2) FTPDownloadFile, (3) FTPUploadFile, (4) HttpUploadFile, (5) Save, (6) SaveWebFile, (7) HttpDownloadFile, (8) Open, or (9) OpenWebFile property value.  NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-2495
    - Vulnerability Description: Multiple stack-based buffer overflows in the ExcelOCX ActiveX control in ExcelViewer.ocx 3.1.0.6 allow remote attackers to cause a denial of service (Internet Explorer 7 crash) via a long (1) DoOleCommand, (2) FTPDownloadFile, (3) FTPUploadFile, (4) HttpUploadFile, (5) Save, (6) SaveWebFile, (7) HttpDownloadFile, (8) Open, or (9) OpenWebFile property value.  NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-2496
    - Vulnerability Description: The WordOCX ActiveX control in WordViewer.ocx 3.2.0.5 allows remote attackers to cause a denial of service (Internet Explorer 7 crash) via a long (1) DoOleCommand, (2) FTPDownloadFile, (3) FTPUploadFile, (4) HttpUploadFile, (5) GotoPage, (6) Save, (7) SaveWebFile, (8) HttpDownloadFile, (9) Open, (10) OpenWebFile, (11) SaveAs, or (12) ShowWordStandardDialog property value.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-2588
    - Vulnerability Description: Multiple buffer overflows in the Office Viewer OCX ActiveX control (oa.ocx) 3.2 allow remote attackers to cause a denial of service (crash) or possibly execute arbitrary code via a long argument to the (1) HttpDownloadFile, (2) Open, (3) OpenWebFile, (4) DoOleCommand, (5) FTPDownloadFile, (6) FTPUploadFile, (7) HttpUploadFile, (8) Save, or (9) SaveWebFile function.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-2635
    - Vulnerability Description: Unspecified vulnerability in Interchange before 5.4.2 allows remote attackers to cause an unspecified denial of service (possibly server hang) via crafted HTTP requests.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-2952
    - Vulnerability Description: Multiple stack-based buffer overflows in the filter service (aka k9filter.exe) in Blue Coat K9 Web Protection 3.2.44 with Filter 3.2.32 allow (1) remote attackers to execute arbitrary code via a long HTTP Referer header to the K9 Web Protection Administration interface and (2) man-in-the-middle attackers to execute arbitrary code via an HTTP response with a long HTTP version field.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-3009
    - Vulnerability Description: Format string vulnerability in the MprLogToFile::logEvent function in Mbedthis AppWeb 2.0.5-4, when the build supports logging but the configuration disables logging, allows remote attackers to cause a denial of service (daemon crash) via format string specifiers in the HTTP scheme, as demonstrated by a "GET %n://localhost:80/" request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-3159
    - Vulnerability Description: http.c in MiniWeb Http Server 0.8.x allows remote attackers to cause a denial of service (application crash) via a negative value in the Content-Length HTTP header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-3169
    - Vulnerability Description: Buffer overflow in a certain ActiveX control in the EDraw Office Viewer Component (edrawofficeviewer.ocx) 4.0.5.20, and other versions before 5.0, allows remote attackers to cause a denial of service (Internet Explorer 7 crash) or execute arbitrary code via a long first argument to the HttpDownloadFile method.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-3216
    - Vulnerability Description: Multiple buffer overflows in the LGServer component of CA (Computer Associates) BrightStor ARCserve Backup for Laptops and Desktops r11.1 allow remote attackers to execute arbitrary code via crafted arguments to the (1) rxsAddNewUser, (2) rxsSetUserInfo, (3) rxsRenameUser, (4) rxsSetMessageLogSettings, (5) rxsExportData, (6) rxsSetServerOptions, (7) rxsRenameFile, (8) rxsACIManageSend, (9) rxsExportUser, (10) rxsImportUser, (11) rxsMoveUserData, (12) rxsUseLicenseIni, (13) rxsLicGetSiteId, (14) rxsGetLogFileNames, (15) rxsGetBackupLog, (16) rxsBackupComplete, (17) rxsSetDataProtectionSecurityData, (18) rxsSetDefaultConfigName, (19) rxsGetMessageLogSettings, (20) rxsHWDiskGetTotal, (21) rxsHWDiskGetFree, (22) rxsGetSubDirs, (23) rxsGetServerDBPathName, (24) rxsSetServerOptions, (25) rxsDeleteFile, (26) rxsACIManageSend, (27) rxcReadBackupSetList, (28) rxcWriteConfigInfo, (29) rxcSetAssetManagement, (30) rxcWriteFileListForRestore, (31) rxcReadSaveSetProfile, (32) rxcInitSaveSetProfile, (33) rxcAddSaveSetNextAppList, (34) rxcAddSaveSetNextFilesPathList, (35) rxcAddNextBackupSetIncWildCard, (36) rxcGetRevisions, (37) rxrAddMovedUser, (38) rxrSetClientVersion, or (39) rxsSetDataGrowthScheduleAndFilter commands.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-3303
    - Vulnerability Description: Apache httpd 2.0.59 and 2.2.4, with the Prefork MPM module, allows local users to cause a denial of service via certain code sequences executed in a worker process that (1) stop request processing by killing all worker processes and preventing creation of replacements or (2) hang the system by forcing the master process to fork an arbitrarily large number of worker processes.  NOTE: This might be an inherent design limitation of Apache with respect to worker processes in hosted environments.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-3304
    - Vulnerability Description: Apache httpd 1.3.37, 2.0.59, and 2.2.4 with the Prefork MPM module, allows local users to cause a denial of service by modifying the worker_score and process_score arrays to reference an arbitrary process ID, which is sent a SIGUSR1 signal from the master process, aka "SIGUSR1 killer."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-3340
    - Vulnerability Description: BugHunter HTTP SERVER (httpsv.exe) 1.6.2 allows remote attackers to cause a denial of service (application crash) via a large number of requests for nonexistent pages.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-3368
    - Vulnerability Description: Buffer overflow in the HTTP server on the Polycom SoundPoint IP 601 SIP phone with BootROM 3.0.x+ allows remote attackers to cause a denial of service (device reboot) via a malformed CGI parameter.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-3389
    - Vulnerability Description: Wireshark before 0.99.6 allows remote attackers to cause a denial of service (crash) via a crafted chunked encoding in an HTTP response, possibly related to a zero-length payload.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-3496
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in SAP Web Dynpro Java (BC-WD-JAV) in SAP NetWeaver Nw04 SP15 through SP19 and Nw04s SP7 through SP11, aka SAP Java Technology Services 640 before SP20 and SAP Web Dynpro Runtime Core Components 700 before SP12, allows remote attackers to inject arbitrary web script or HTML via the User-Agent HTTP header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-3804
    - Vulnerability Description: The AntiVirus engine in the HTTP-ALG in Clavister CorePlus before 8.81.00 and 8.80.03 might allow remote attackers to bypass scanning via small files.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-3911
    - Vulnerability Description: Multiple heap-based buffer overflows in (1) clsscheduler.exe (aka scheduler client) and (2) srvscheduler.exe (aka scheduler server) in BakBone NetVault Reporter 3.5 before Update4 allow remote attackers to execute arbitrary code via long filename arguments in HTTP requests.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-3946
    - Vulnerability Description: mod_auth (http_auth.c) in lighttpd before 1.4.16 allows remote attackers to cause a denial of service (daemon crash) via unspecified vectors involving (1) a memory leak, (2) use of md5-sess without a cnonce, (3) base64 encoded strings, and (4) trailing whitespace in the Auth-Digest header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-3947
    - Vulnerability Description: request.c in lighttpd 1.4.15 allows remote attackers to cause a denial of service (daemon crash) by sending an HTTP request with duplicate headers, as demonstrated by a request containing two Location header lines, which results in a segmentation fault.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-3948
    - Vulnerability Description: connections.c in lighttpd before 1.4.16 might accept more connections than the configured maximum, which allows remote attackers to cause a denial of service (failed assertion) via a large number of connection attempts.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-3950
    - Vulnerability Description: lighttpd 1.4.15, when run on 32 bit platforms, allows remote attackers to cause a denial of service (daemon crash) via unspecified vectors involving the use of incompatible format specifiers in certain debugging messages in the (1) mod_scgi, (2) mod_fastcgi, and (3) mod_webdav modules.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-4213
    - Vulnerability Description: Palm OS on Treo 650, 680, 700p, and 755p Smart phones allows remote attackers to cause a denial of service (device reset or hang) via a flood of large ICMP echo requests.  NOTE: this is probably a different vulnerability than CVE-2003-0293.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-4348
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in the CAD service in IBM Tivoli Storage Manager (TSM) Client 5.3.5.3 and 5.4.1.2 for Windows allows remote attackers to inject arbitrary web script or HTML via HTTP requests to port 1581, which generate log entries in a dsmerror.log file that is accessible through a certain web interface.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-4477
    - Vulnerability Description: The administration interface in the Planet VC-200M VDSL2 router allows remote attackers to cause a denial of service (administration interface outage) via an HTTP request without a Host header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-4570
    - Vulnerability Description: Algorithmic complexity vulnerability in the MCS translation daemon in mcstrans 0.2.3 allows local users to cause a denial of service (temporary daemon outage) via a large range of compartments in sensitivity labels.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-4580
    - Vulnerability Description: Buffer underflow in redlight.sys in BufferZone 2.1 and 2.5 allows local users to cause a denial of service (crash) and possibly execute arbitrary code by sending a small buffer size value to the FsSetVolumeInformation IOCTL handler code with a FsSetDirectoryInformation subcode containing a large buffer.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-4591
    - Vulnerability Description: vstor-ws60.sys in VMWare Workstation 6.0 allows local users to cause a denial of service (host operating system crash) and possibly gain privileges by sending a small file buffer size value to the FsSetVolumeInformation IOCTL handler with an FsSetFileInformation subcode.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-4618
    - Vulnerability Description: Unspecified vulnerability in BEA WebLogic Server 6.1 Gold through SP7 and 7.0 Gold through SP7 allows remote attackers to cause a denial of service (disk consumption) via certain malformed HTTP headers.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-4625
    - Vulnerability Description: Polipo before 1.0.2 allows remote HTTP servers to cause a denial of service (daemon crash) by aborting the response to a POST request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-4967
    - Vulnerability Description: Online Armor Personal Firewall 2.0.1.215 does not properly validate certain parameters to System Service Descriptor Table (SSDT) function handlers, which allows local users to cause a denial of service (crash) and possibly gain privileges via unspecified kernel SSDT hooks for Windows Native API functions including (1) NtAllocateVirtualMemory, (2) NtConnectPort, (3) NtCreateFile, (4) NtCreateKey, (5) NtCreatePort, (6) NtDeleteFile, (7) NtDeleteValueKey, (8) NtLoadKey, (9) NtOpenFile, (10) NtOpenProcess, (11) NtOpenThread, (12) NtResumeThread, (13) NtSetContextThread, (14) NtSetValueKey, (15) NtSuspendProcess, (16) NtSuspendThread, and (17) NtTerminateThread.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-4969
    - Vulnerability Description: Process Monitor 1.22 does not properly validate certain parameters to System Service Descriptor Table (SSDT) function handlers, which allows local users to cause a denial of service (crash) and possibly gain privileges via unspecified kernel SSDT hooks for Windows Native API functions including (1) NtCreateKey, (2) NtDeleteValueKey, (3) NtLoadKey, (4) NtOpenKey, (5) NtQueryValueKey, (6) NtSetValueKey, and (7) NtUnloadKey.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-4970
    - Vulnerability Description: ProcessGuard 3.410 does not properly validate certain parameters to System Service Descriptor Table (SSDT) function handlers, which allows local users to cause a denial of service (crash) and possibly gain privileges via kernel SSDT hooks for Windows Native API functions including (1) NtCreateFile, (2) NtCreateKey, (3) NtDeleteValueKey, (4) NtOpenFile, (5) NtOpenKey, and (6) NtSetValueKey.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-4980
    - Vulnerability Description: The readRequest method in org/gcaldaemon/core/http/HTTPListener.java in GCALDaemon 1.0-beta13 allows remote attackers to cause a denial of service via a large integer value in the Content-Length HTTP header, which triggers a fatal Java OutOfMemoryError.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-5036
    - Vulnerability Description: Multiple buffer overflows in the AirDefense Airsensor M520 with firmware 4.3.1.1 and 4.4.1.4 allow remote authenticated users to cause a denial of service (HTTPS service outage) via a crafted query string in an HTTPS request to (1) adLog.cgi, (2) post.cgi, or (3) ad.cgi, related to the "files filter."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-5039
    - Vulnerability Description: Ghost Security Suite beta 1.110 does not properly validate certain parameters to System Service Descriptor Table (SSDT) function handlers, which allows local users to cause a denial of service (crash) and possibly gain privileges via the (1) NtCreateKey, (2) NtDeleteValueKey, (3) NtQueryValueKey, (4) NtSetSystemInformation, and (5) NtSetValueKey kernel SSDT hooks.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-5040
    - Vulnerability Description: Ghost Security Suite alpha 1.200 does not properly validate certain parameters to System Service Descriptor Table (SSDT) function handlers, which allows local users to cause a denial of service (crash) and possibly gain privileges via the (1) NtCreateKey, (2) NtCreateThread, (3) NtDeleteValueKey, (4) NtQueryValueKey, (5) NtSetSystemInformation, and (6) NtSetValueKey kernel SSDT hooks.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-5546
    - Vulnerability Description: Multiple stack-based buffer overflows in TIBCO SmartPGM FX allow remote attackers to execute arbitrary code or cause a denial of service (service stop and file-transfer outage) via unspecified vectors.  NOTE: as of 20071016, the only disclosure is a vague pre-advisory with no actionable information. However, since it is from a well-known researcher, it is being assigned a CVE identifier for tracking purposes.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-5558
    - Vulnerability Description: Integer overflow in the LG Mobile handset allows remote attackers to cause a denial of service (reboot) via a crafted HTTP packet.  NOTE: as of 20071016, the only disclosure is a vague pre-advisory with no actionable information. However, since it is from a well-known researcher, it is being assigned a CVE identifier for tracking purposes.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-5559
    - Vulnerability Description: Heap-based buffer overflow in the IBM ThinkVantage TPM Service allows remote attackers to execute arbitrary code via a crafted HTTP packet. NOTE: as of 20071016, the only disclosure is a vague pre-advisory with no actionable information. However, since it is from a well-known researcher, it is being assigned a CVE identifier for tracking purposes.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-5560
    - Vulnerability Description: Heap-based buffer overflow in the Juniper HTTP Service allows remote attackers to execute arbitrary code via a crafted HTTP packet.  NOTE: as of 20071016, the only disclosure is a vague pre-advisory with no actionable information. However, since it is from a well-known researcher, it is being assigned a CVE identifier for tracking purposes.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-5570
    - Vulnerability Description: Cisco Firewall Services Module (FWSM) 3.2(1), and 3.1(5) and earlier, allows remote attackers to cause a denial of service (device reload) via a crafted HTTPS request, aka CSCsi77844.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-5655
    - Vulnerability Description: TIBCO SmartSockets RTserver 6.8.0 and earlier, RTworks before 4.0.4, and Enterprise Message Service (EMS) 4.0.0 through 4.4.1 allows remote attackers to execute arbitrary code via crafted requests containing values that are used as pointers.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-5656
    - Vulnerability Description: TIBCO SmartSockets RTserver 6.8.0 and earlier, RTworks before 4.0.4, and Enterprise Message Service (EMS) 4.0.0 through 4.4.1 allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via crafted requests that control loop operations related to memory.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-5657
    - Vulnerability Description: TIBCO SmartSockets RTserver 6.8.0 and earlier, RTworks before 4.0.4, and Enterprise Message Service (EMS) 4.0.0 through 4.4.1 allows remote attackers to execute arbitrary code via crafted requests containing values that are used as pointer offsets.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-5658
    - Vulnerability Description: Heap-based buffer overflow in TIBCO SmartSockets RTserver 6.8.0 and earlier, RTworks before 4.0.4, and Enterprise Message Service (EMS) 4.0.0 through 4.4.1 allows remote attackers to execute arbitrary code via crafted requests containing size and copy-length values that trigger the overflow.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-5712
    - Vulnerability Description: The internationalization (i18n) framework in Django 0.91, 0.95, 0.95.1, and 0.96, and as used in other products such as PyLucid, when the USE_I18N option and the i18n component are enabled, allows remote attackers to cause a denial of service (memory consumption) via many HTTP requests with large Accept-Language headers.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-5893
    - Vulnerability Description: HTTPSocket.cpp in the C++ Sockets Library before 2.2.5 allows remote attackers to cause a denial of service (crash) via an HTTP request with a missing protocol version number, which triggers an exception. NOTE: some of these details were obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-6000
    - Vulnerability Description: KDE Konqueror 3.5.6 and earlier allows remote attackers to cause a denial of service (crash) via large HTTP cookie parameters.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-6067
    - Vulnerability Description: Algorithmic complexity vulnerability in the regular expression parser in TCL before 8.4.17, as used in PostgreSQL 8.2 before 8.2.6, 8.1 before 8.1.11, 8.0 before 8.0.15, and 7.4 before 7.4.19, allows remote authenticated users to cause a denial of service (memory consumption) via a crafted "complex" regular expression with doubly-nested states.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-6117
    - Vulnerability Description: Unspecified vulnerability in the HTTP dissector for Wireshark (formerly Ethereal) 0.10.14 to 0.99.6 allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via crafted chunked messages.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-6239
    - Vulnerability Description: The "cache update reply processing" functionality in Squid 2.x before 2.6.STABLE17 and Squid 3.0 allows remote attackers to cause a denial of service (crash) via unknown vectors related to HTTP headers and an Array memory leak during requests for cached objects.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-6315
    - Vulnerability Description: Group Chat in BarracudaDrive Web Server before 3.8 allows remote authenticated users to cause a denial of service (crash) via a HTTP request to /eh/chat.ehintf/C. that does not contain a Connection ID, which results in a NULL pointer dereference.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-6326
    - Vulnerability Description: Sergey Lyubka Simple HTTPD (shttpd) 1.3 on Windows allows remote attackers to cause a denial of service via a request that includes an MS-DOS device name, as demonstrated by the /aux URI.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-6349
    - Vulnerability Description: P4Webs.exe in Perforce P4Web 2006.2 and earlier, when running on Windows, allows remote attackers to cause a denial of service (CPU consumption) via an HTTP request with an empty body and a Content-Length greater than 0.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-6360
    - Vulnerability Description: Unspecified vulnerability in the Sun eXtended System Control Facility (XSCF) Control Package (XCP) firmware before 1050 on SPARC Enterprise M4000, M5000, M8000, and M9000 servers allows remote attackers to cause a denial of service (reboot) via (1) telnet, (2) ssh, or (3) http network traffic that triggers memory exhaustion.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-6422
    - Vulnerability Description: The balancer_handler function in mod_proxy_balancer in the Apache HTTP Server 2.2.0 through 2.2.6, when a threaded Multi-Processing Module is used, allows remote authenticated users to cause a denial of service (child process crash) via an invalid bb variable.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-6454
    - Vulnerability Description: Heap-based buffer overflow in the handshakeHTTP function in servhs.cpp in PeerCast 0.1217 and earlier, and SVN 344 and earlier, allows remote attackers to cause a denial of service and possibly execute arbitrary code via a long SOURCE request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-6523
    - Vulnerability Description: Algorithmic complexity vulnerability in Opera 9.50 beta and 9.x before 9.25 allows remote attackers to cause a denial of service (CPU consumption) via a crafted bitmap (BMP) file that triggers a large number of calculations and checks.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-6640
    - Vulnerability Description: Creammonkey 0.9 through 1.1 and GreaseKit 1.2 through 1.3 does not properly prevent access to dangerous functions, which allows remote attackers to read the configuration, modify the configuration, or send an HTTP request via the (1) GM_addStyle, (2) GM_log, (3) GM_openInTab, (4) GM_setValue, (5) GM_getValue, or (6) GM_xmlhttpRequest function within a web page on which a userscript is configured.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2007-6750
    - Vulnerability Description: The Apache HTTP Server 1.x and 2.x allows remote attackers to cause a denial of service (daemon outage) via partial HTTP requests, as demonstrated by Slowloris, related to the lack of the mod_reqtimeout module in versions before 2.2.15.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-0017
    - Vulnerability Description: The http-index-format MIME type parser (nsDirIndexParser) in Firefox 3.x before 3.0.4, Firefox 2.x before 2.0.0.18, and SeaMonkey 1.x before 1.1.13 does not check for an allocation failure, which allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via an HTTP index response with a crafted 200 header, which triggers memory corruption and a buffer overflow.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-0071
    - Vulnerability Description: The Web UI interface in (1) BitTorrent before 6.0.3 build 8642 and (2) uTorrent before 1.8beta build 10524 allows remote attackers to cause a denial of service (application crash) via an HTTP request with a malformed Range header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-0179
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in service/impl/UserLocalServiceImpl.java in Liferay Portal 4.3.6 allows remote attackers to inject arbitrary web script or HTML via the User-Agent HTTP header, which is used when composing Forgot Password e-mail messages in HTML format.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-0311
    - Vulnerability Description: Stack-based buffer overflow in the PGMWebHandler::parse_request function in the StarTeam Multicast Service component (STMulticastService) 6.4 in Borland CaliberRM 2006 allows remote attackers to execute arbitrary code via a large HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-0401
    - Vulnerability Description: Buffer overflow in the logging functionality of the HTTP server in IBM Tivoli Provisioning Manager for OS Deployment (TPMfOSD) before 5.1.0.3 Interim Fix 3 allows remote attackers to cause a denial of service (daemon crash) or possibly execute arbitrary code via an HTTP request with a long method string to port 443/tcp.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-0406
    - Vulnerability Description: HTTP File Server (HFS) before 2.2c, when account names are used as log filenames, allows remote attackers to cause a denial of service (daemon crash) via a long account name.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-0527
    - Vulnerability Description: The HTTP server in Cisco Unified IP Phone 7935 and 7936 running SCCP firmware allows remote attackers to cause a denial of service (reboot) via a crafted HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-0548
    - Vulnerability Description: Steamcast 0.9.75 and earlier allows remote attackers to cause a denial of service (daemon crash) via a large integer in the Content-Length HTTP header, which triggers a NULL dereference when malloc fails.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-0550
    - Vulnerability Description: Off-by-one error in Steamcast 0.9.75 and earlier allows remote attackers to cause a denial of service (daemon crash) or execute arbitrary code via a certain HTTP request that leads to a buffer overflow, as demonstrated by a long User-Agent header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-0563
    - Vulnerability Description: Cross-site request forgery (CSRF) vulnerability in service/impl/UserLocalServiceImpl.java in Liferay Portal 4.3.6 allows remote attackers to perform unspecified actions as unspecified authenticated users via the User-Agent HTTP header, which is used when composing Forgot Password e-mail messages in HTML format.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-0871
    - Vulnerability Description: Multiple stack-based buffer overflows in Now SMS/MMS Gateway 2007.06.27 and earlier allow remote attackers to execute arbitrary code via a (1) long password in an Authorization header to the HTTP service or a (2) large packet to the SMPP service.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-0927
    - Vulnerability Description: dhost.exe in Novell eDirectory 8.7.3 before sp10 and 8.8.2 allows remote attackers to cause a denial of service (CPU consumption) via an HTTP request with (1) multiple Connection headers or (2) a Connection header with multiple comma-separated values.  NOTE: this might be similar to CVE-2008-1777.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-0983
    - Vulnerability Description: lighttpd 1.4.18, and possibly other versions before 1.5.0, does not properly calculate the size of a file descriptor array, which allows remote attackers to cause a denial of service (crash) via a large number of connections, which triggers an out-of-bounds access.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-1052
    - Vulnerability Description: The administration web interface in NetWin SurgeFTP 2.3a2 and earlier allows remote attackers to cause a denial of service (daemon crash) via a large integer in the Content-Length HTTP header, which triggers a NULL pointer dereference when memory allocation fails.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-1054
    - Vulnerability Description: Stack-based buffer overflow in the _lib_spawn_user_getpid function in (1) swatch.exe and (2) surgemail.exe in NetWin SurgeMail 38k4 and earlier, and beta 39a, allows remote attackers to cause a denial of service (daemon crash) and possibly execute arbitrary code via an HTTP request with multiple long headers to webmail.exe and unspecified other CGI executables, which triggers an overflow when assigning values to environment variables.  NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-1207
    - Vulnerability Description: Multiple unspecified vulnerabilities in Fujitsu Interstage Smart Repository, as used in multiple Fujitsu Interstage products, allow remote attackers to cause a denial of service (daemon crash) via (1) an invalid request or (2) a large amount of data sent to the registered attribute value.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-1245
    - Vulnerability Description: cgi-bin/setup_virtualserver.exe on the Belkin F5D7230-4 router with firmware 9.01.10 allows remote attackers to cause a denial of service (control center outage) via an HTTP request with invalid POST data and a "Connection: Keep-Alive" header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-1266
    - Vulnerability Description: Multiple buffer overflows in the web interface on the D-Link DI-524 router allow remote attackers to cause a denial of service (device crash) or possibly have unspecified other impact via (1) a long username or (2) an HTTP header with a large name and an empty value.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-1267
    - Vulnerability Description: The Siemens SpeedStream 6520 router allows remote attackers to cause a denial of service (web interface crash) via an HTTP request to basehelp_English.htm with a large integer in the Content-Length field.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-1328
    - Vulnerability Description: Buffer overflow in the LGServer service in CA ARCserve Backup for Laptops and Desktops r11.0 through r11.5, and Suite 11.1 and 11.2, allows remote attackers to execute arbitrary code via unspecified "command arguments."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-1366
    - Vulnerability Description: Trend Micro OfficeScan Corporate Edition 8.0 Patch 2 build 1189 and earlier, and 7.3 Patch 3 build 1314 and earlier, allows remote attackers to cause a denial of service (process consumption) via (1) an HTTP request without a Content-Length header or (2) invalid characters in unspecified CGI arguments, which triggers a NULL pointer dereference.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-1423
    - Vulnerability Description: Integer overflow in a certain quantvals and quantlist calculation in Xiph.org libvorbis 1.2.0 and earlier allows remote attackers to cause a denial of service (crash) or execute arbitrary code via a crafted OGG file with a large virtual space for its codebook, which triggers a heap overflow.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-1446
    - Vulnerability Description: Integer overflow in the Internet Printing Protocol (IPP) ISAPI extension in Microsoft Internet Information Services (IIS) 5.0 through 7.0 on Windows 2000 SP4, XP SP2 and SP3, Server 2003 SP1 and SP2, and Server 2008 allows remote authenticated users to execute arbitrary code via an HTTP POST request that triggers an outbound IPP connection from a web server to a machine operated by the attacker, aka "Integer Overflow in IPP Service Vulnerability."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-1531
    - Vulnerability Description: The connection_state_machine function (connections.c) in lighttpd 1.4.19 and earlier, and 1.5.x before 1.5.0, allows remote attackers to cause a denial of service (active SSL connection loss) by triggering an SSL error, such as disconnecting before a download has finished, which causes all active SSL connections to be lost.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-1678
    - Vulnerability Description: Memory leak in the zlib_stateful_init function in crypto/comp/c_zlib.c in libssl in OpenSSL 0.9.8f through 0.9.8h allows remote attackers to cause a denial of service (memory consumption) via multiple calls, as demonstrated by initial SSL client handshakes to the Apache HTTP Server mod_ssl that specify a compression algorithm.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-1689
    - Vulnerability Description: Stack consumption vulnerability in WebContainer.exe 1.0.0.336 and earlier in SLMail Pro 6.3.1.0 and earlier allows remote attackers to cause a denial of service (daemon crash) via a long request header in an HTTP request to TCP port 801.  NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-1690
    - Vulnerability Description: WebContainer.exe 1.0.0.336 and earlier in SLMail Pro 6.3.1.0 and earlier allows remote attackers to cause a denial of service (memory corruption and daemon crash) or possibly execute arbitrary code via a long URI in HTTP requests to TCP port 801.  NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-1734
    - Vulnerability Description: Interpretation conflict in PHP Toolkit before 1.0.1 on Gentoo Linux might allow local users to cause a denial of service (PHP outage) and read contents of PHP scripts by creating a file with a one-letter lowercase alphabetic name, which triggers interpretation of a certain unquoted [a-z] argument as a matching shell glob for this name, rather than interpretation as the literal [a-z] regular-expression string, and consequently blocks the launch of the PHP interpreter within the Apache HTTP Server.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-1771
    - Vulnerability Description: Integer overflow in the ws_getpostvars function in Firefly Media Server (formerly mt-daapd) 0.2.4.1 (0.9~r1696-1.2 on Debian) allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via an HTTP POST request with a large Content-Length.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-1777
    - Vulnerability Description: The eDirectory Host Environment service (dhost.exe) in Novell eDirectory 8.8.2 allows remote attackers to cause a denial of service (CPU consumption) via a long HTTP HEAD request to TCP port 8028.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-1854
    - Vulnerability Description: Unspecified vulnerability in SmarterMail Web Server (SMWebSvr.exe) in SmarterMail 5.0.2999 allows remote attackers to cause a denial of service (service termination) via a long HTTP (1) GET, (2) HEAD, (3) PUT, (4) POST, or (5) TRACE request.  NOTE: the provenance of this information is unknown
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-1905
    - Vulnerability Description: NMMediaServer.exe in Nero MediaHome 3.3.3.0 and earlier, as used in Nero 8.3.2.1 and earlier, allows remote attackers to cause a denial of service (NULL pointer dereference and application crash) via a long HTTP request to TCP port 54444, a different vector than CVE-2007-2322.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-2040
    - Vulnerability Description: Stack-based buffer overflow in the HTTP::getAuthUserPass function (core/common/http.cpp) in Peercast 0.1218 and gnome-peercast allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via a Basic Authentication string with a long (1) username or (2) password.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-2240
    - Vulnerability Description: Stack-based buffer overflow in the Web Server service in IBM Lotus Domino before 7.0.3 FP1, and 8.x before 8.0.1, allows remote attackers to cause a denial of service (daemon crash) or possibly execute arbitrary code via a long Accept-Language HTTP header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-2364
    - Vulnerability Description: The ap_proxy_http_process_response function in mod_proxy_http.c in the mod_proxy module in the Apache HTTP Server 2.0.63 and 2.2.8 does not limit the number of forwarded interim responses, which allows remote HTTP servers to cause a denial of service (memory consumption) via a large number of interim responses.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-2423
    - Vulnerability Description: Unspecified vulnerability in Interchange before 5.6.0 and before 5.5.2 allows remote attackers to cause a denial of service via crafted HTTP requests.  NOTE: this might overlap CVE-2007-2635.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-2439
    - Vulnerability Description: Directory traversal vulnerability in the UpdateAgent function in TmListen.exe in the OfficeScanNT Listener service in the client in Trend Micro OfficeScan 7.3 Patch 4 build 1367 and other builds before 1372, OfficeScan 8.0 SP1 before build 1222, OfficeScan 8.0 SP1 Patch 1 before build 3087, and Worry-Free Business Security 5.0 before build 1220 allows remote attackers to read arbitrary files via directory traversal sequences in an HTTP request.  NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-2541
    - Vulnerability Description: Multiple stack-based buffer overflows in the HTTP Gateway Service (icihttp.exe) in CA eTrust Secure Content Manager 8.0 allow remote attackers to execute arbitrary code or cause a denial of service via long FTP responses, related to (1) the file month field in a LIST command
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-2631
    - Vulnerability Description: The WordClient interface in Alt-N Technologies MDaemon 9.6.5 allows remote attackers to cause a denial of service (NULL pointer dereference and application crash) via a crafted HTTP POST request. NOTE: the provenance of this information is unknown
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-2636
    - Vulnerability Description: The HTTP service on the Cisco Linksys WRH54G with firmware 1.01.03 allows remote attackers to cause a denial of service (management interface outage) or possibly execute arbitrary code via a URI that begins with a "/./" sequence, contains many instances of a "front_page" sequence, and ends with a ".asp" sequence.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-2734
    - Vulnerability Description: Memory leak in the crypto functionality in Cisco Adaptive Security Appliance (ASA) 5500 devices 7.2 before 7.2(4)2, 8.0 before 8.0(3)14, and 8.1 before 8.1(1)4, when configured as a clientless SSL VPN endpoint, allows remote attackers to cause a denial of service (memory consumption and VPN hang) via a crafted SSL or HTTP packet, aka Bug ID CSCso66472.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-2735
    - Vulnerability Description: The HTTP server in Cisco Adaptive Security Appliance (ASA) 5500 devices 8.0 before 8.0(3)15 and 8.1 before 8.1(1)5, when configured as a clientless SSL VPN endpoint, does not properly process URIs, which allows remote attackers to cause a denial of service (device reload) via a URI in a crafted SSL or HTTP packet, aka Bug ID CSCsq19369.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-2749
    - Vulnerability Description: Unspecified vulnerability in cshttpd in Sun Java System Calendar Server 6 and 6.3, and Sun ONE Calendar Server 6.0, when access logging (aka service.http.commandlog.all) is enabled, allows remote attackers to cause a denial of service (daemon crash) via unspecified vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-2928
    - Vulnerability Description: Multiple buffer overflows in the adminutil library in CGI applications in Red Hat Directory Server 7.1 before SP7 allow remote attackers to cause a denial of service (daemon crash) or possibly execute arbitrary code via a crafted Accept-Language HTTP header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-2932
    - Vulnerability Description: Heap-based buffer overflow in Red Hat adminutil 1.1.6 allows remote attackers to cause a denial of service (daemon crash) or possibly execute arbitrary code via % (percent) encoded HTTP input to unspecified CGI scripts in Fedora Directory Server.  NOTE: this vulnerability exists because of an incorrect fix for CVE-2008-2929.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-3134
    - Vulnerability Description: Multiple unspecified vulnerabilities in GraphicsMagick before 1.2.4 allow remote attackers to cause a denial of service (crash, infinite loop, or memory consumption) via (a) unspecified vectors in the (1) AVI, (2) AVS, (3) DCM, (4) EPT, (5) FITS, (6) MTV, (7) PALM, (8) RLA, and (9) TGA decoder readers
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-3172
    - Vulnerability Description: Opera allows web sites to set cookies for country-specific top-level domains that have DNS A records, such as co.tv, which could allow remote attackers to perform a session fixation attack and hijack a user's HTTP session, aka "Cross-Site Cooking."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-3175
    - Vulnerability Description: Integer underflow in rxRPC.dll in the LGServer service in the server in CA ARCserve Backup for Laptops and Desktops 11.0 through 11.5 allows remote attackers to execute arbitrary code or cause a denial of service via a crafted message that triggers a buffer overflow.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-3349
    - Vulnerability Description: Multiple unspecified vulnerabilities in NetApp Data ONTAP, as used on NetApp and IBM eServer platforms, allow remote attackers to execute arbitrary commands, cause a denial of service (system crash), or obtain sensitive information, probably related to insufficient access control for HTTP requests.  NOTE: this may overlap CVE-2008-3160.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-3529
    - Vulnerability Description: Heap-based buffer overflow in the xmlParseAttValueComplex function in parser.c in libxml2 before 2.7.0 allows context-dependent attackers to cause a denial of service (crash) or execute arbitrary code via a long XML entity name.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-3624
    - Vulnerability Description: Heap-based buffer overflow in Apple QuickTime before 7.5.5 allows remote attackers to execute arbitrary code or cause a denial of service (application crash) via a QuickTime Virtual Reality (QTVR) movie file with crafted panorama atoms.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-3625
    - Vulnerability Description: Stack-based buffer overflow in Apple QuickTime before 7.5.5 allows remote attackers to execute arbitrary code or cause a denial of service (application crash) via a QuickTime Virtual Reality (QTVR) movie file with crafted (1) maxTilt, (2) minFieldOfView, and (3) maxFieldOfView elements in panorama track PDAT atoms.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-3656
    - Vulnerability Description: Algorithmic complexity vulnerability in the WEBrick::HTTPUtils.split_header_value function in WEBrick::HTTP::DefaultFileHandler in WEBrick in Ruby 1.8.5 and earlier, 1.8.6 through 1.8.6-p286, 1.8.7 through 1.8.7-p71, and 1.9 through r18423 allows context-dependent attackers to cause a denial of service (CPU consumption) via a crafted HTTP request that is processed by a backtracking regular expression.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-3688
    - Vulnerability Description: sockethandler.cpp in HTTP Antivirus Proxy (HAVP) 0.88 allows remote attackers to cause a denial of service (hang) by connecting to a non-responsive server, which triggers an infinite loop due to an uninitialized variable.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-3812
    - Vulnerability Description: Cisco IOS 12.4, when IOS firewall Application Inspection Control (AIC) with HTTP Deep Packet Inspection is enabled, allows remote attackers to cause a denial of service (device reload) via a malformed HTTP transit packet.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-3933
    - Vulnerability Description: Wireshark (formerly Ethereal) 0.10.14 through 1.0.2 allows attackers to cause a denial of service (crash) via a packet with crafted zlib-compressed data that triggers an invalid read in the tvb_uncompress function.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-4033
    - Vulnerability Description: Cross-domain vulnerability in Microsoft XML Core Services 3.0 through 6.0, as used in Microsoft Expression Web, Office, Internet Explorer, and other products, allows remote attackers to obtain sensitive information from another domain and corrupt the session state via HTTP request header fields, as demonstrated by the Transfer-Encoding field, aka "MSXML Header Request Vulnerability."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-4077
    - Vulnerability Description: The CGI scripts in (1) LedgerSMB (LSMB) before 1.2.15 and (2) SQL-Ledger 2.8.17 and earlier allow remote attackers to cause a denial of service (resource exhaustion) via an HTTP POST request with a large Content-Length.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-4128
    - Vulnerability Description: Multiple cross-site request forgery (CSRF) vulnerabilities in the HTTP Administration component in Cisco IOS 12.4 on the 871 Integrated Services Router allow remote attackers to execute arbitrary commands via (1) a certain "show privilege" command to the /level/15/exec/- URI, and (2) a certain "alias exec" command to the /level/15/exec/-/configure/http URI.  NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-4298
    - Vulnerability Description: Memory leak in the http_request_parse function in request.c in lighttpd before 1.4.20 allows remote attackers to cause a denial of service (memory consumption) via a large number of requests with duplicate request headers.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-4310
    - Vulnerability Description: httputils.rb in WEBrick in Ruby 1.8.1 and 1.8.5, as used in Red Hat Enterprise Linux 4 and 5, allows remote attackers to cause a denial of service (CPU consumption) via a crafted HTTP request.  NOTE: this issue exists because of an incomplete fix for CVE-2008-3656.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-4380
    - Vulnerability Description: The web interface in Samsung DVR SHR2040 allows remote attackers to cause a denial of service (crash) via a malformed HTTP request, related to the filter for configuration properties and "/x" characters.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-4403
    - Vulnerability Description: The CGI modules in the server in Trend Micro OfficeScan 8.0 SP1 before build 2439 and 8.0 SP1 Patch 1 before build 3087 allow remote attackers to cause a denial of service (NULL pointer dereference and child process crash) via crafted HTTP headers, related to the "error handling mechanism."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-4546
    - Vulnerability Description: Adobe Flash Player before 9.0.277.0 and 10.x before 10.1.53.64, and Adobe AIR before 2.0.2.12610, allows remote web servers to cause a denial of service (NULL pointer dereference and browser crash) by returning a different response when an HTTP request is sent a second time, as demonstrated by two responses that provide SWF files with different SWF version numbers.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-4678
    - Vulnerability Description: The HTTP_Request_Parser method in the HTTP Transport component in IBM WebSphere Application Server (WAS) 6.0.2 before 6.0.2.31 allows remote attackers to cause a denial of service (controller 0C4 abend and application hang) via a long HTTP Host header, related to "storage overlay" on the stack and a "parse failure."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-4683
    - Vulnerability Description: The dissect_btacl function in packet-bthci_acl.c in the Bluetooth ACL dissector in Wireshark 0.99.2 through 1.0.3 allows remote attackers to cause a denial of service (application crash or abort) via a packet with an invalid length, related to an erroneous tvb_memcpy call.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-5033
    - Vulnerability Description: The chip_command function in drivers/media/video/tvaudio.c in the Linux kernel 2.6.25.x before 2.6.25.19, 2.6.26.x before 2.6.26.7, and 2.6.27.x before 2.6.27.3 allows attackers to cause a denial of service (NULL function pointer dereference and OOPS) via unknown vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-5160
    - Vulnerability Description: Unspecified vulnerability in MyServer 0.8.11 allows remote attackers to cause a denial of service (daemon crash) via multiple invalid requests with the HTTP GET, DELETE, OPTIONS, and possibly other methods, related to a "204 No Content error."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-5239
    - Vulnerability Description: xine-lib 1.1.12, and other 1.1.15 and earlier versions, does not properly handle (a) negative and (b) zero values during unspecified read function calls in input_file.c, input_net.c, input_smb.c, and input_http.c, which allows remote attackers to cause a denial of service (crash) or possibly execute arbitrary code via vectors such as (1) a file or (2) an HTTP response, which triggers consequences such as out-of-bounds reads and heap-based buffer overflows.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-5257
    - Vulnerability Description: webseald in WebSEAL 6.0.0.17 in IBM Tivoli Access Manager for e-business allows remote attackers to cause a denial of service (crash or hang) via HTTP requests, as demonstrated by a McAfee vulnerability scan.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-5284
    - Vulnerability Description: The web server in IEA Software RadiusNT and RadiusX 5.1.38 and other versions before 5.1.44, Emerald 5.0.49 and other versions before 5.0.52, Air Marshal 2.0.4 and other versions before 2.0.8, and Radius test client (aka Radlogin) 4.0.20 and earlier, allows remote attackers to cause a denial of service (crash) via an HTTP Content-Length header with a negative value, which triggers a single byte overwrite of memory using a NULL terminator.  NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-5409
    - Vulnerability Description: Unspecified vulnerability in the pdf.xmd module in (1) BitDefender Free Edition 10 and Antivirus Standard 10, (2) BullGuard Internet Security 8.5, and (3) Software602 Groupware Server 6.0.08.1118 allows remote attackers to cause a denial of service (application crash) or possibly execute arbitrary code via a crafted PDF file, possibly related to included compressed streams that were processed with the ASCIIHexDecode filter.  NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-5421
    - Vulnerability Description: The SSL web administration service in NetWin SmsGate 1.1n and earlier allows remote attackers to cause a denial of service (hang) via (1) a large integer in the Content-Length HTTP header
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-5564
    - Vulnerability Description: Unspecified vulnerability in the media server in Orb Networks Orb before 2.01.0025 allows remote attackers to cause a denial of service (daemon crash) via a malformed HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-5674
    - Vulnerability Description: Multiple array index errors in the HTTP server in Darkwet Network webcamXP 3.72.440.0 and earlier and beta 4.05.280 and earlier allow remote attackers to cause a denial of service (device crash) and read portions of memory via (1) an invalid camnum parameter to the pocketpc component and (2) an invalid id parameter to the show_gallery_pic component.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-5676
    - Vulnerability Description: Multiple unspecified vulnerabilities in the ModSecurity (aka mod_security) module 2.5.0 through 2.5.5 for the Apache HTTP Server, when SecCacheTransformations is enabled, allow remote attackers to cause a denial of service (daemon crash) or bypass the product's functionality via unknown vectors related to "transformation caching."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-5825
    - Vulnerability Description: The SmartPoster implementation on the Nokia 6131 Near Field Communication (NFC) phone with 05.12 firmware does not properly display the URI record when the Title record contains a certain combination of space, CR (aka \r), and . (dot) characters, which allows remote attackers to trick a user into loading an arbitrary URI via a crafted NDEF tag, as demonstrated by (1) an http: URI for a malicious web site, (2) a tel: URI for a premium-rate telephone number, and (3) an sms: URI that triggers purchase of a ringtone.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-6395
    - Vulnerability Description: The web management interface in 3Com Wireless 8760 Dual Radio 11a/b/g PoE Access Point allows remote attackers to cause a denial of service (device crash) via a malformed HTTP POST request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-6497
    - Vulnerability Description: The Neostrada Livebox ADSL Router allows remote attackers to cause a denial of service (network outage) via multiple HTTP requests for the /- URI.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-6712
    - Vulnerability Description: The HTTP/XML-RPC service in Crysis 1.21 (game version 1.1.1.6156) and earlier allows remote attackers to cause a denial of service (crash) via a long HTTP request, which triggers a NULL pointer dereference.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-6898
    - Vulnerability Description: Buffer overflow in the XHTTP Module 4.1.0.0 in the ActiveX control for SaschArt SasCam Webcam Server 2.6.5 allows remote attackers to cause a denial of service (crash) or execute arbitrary code via a long argument to the Get method and other unspecified methods.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-7014
    - Vulnerability Description: fhttpd 0.4.2 allows remote attackers to cause a denial of service (crash) via an Authorization HTTP header with an invalid character after the Basic value.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-7025
    - Vulnerability Description: TrueVector in Check Point ZoneAlarm 8.0.020.000, with vsmon.exe running, allows remote HTTP proxies to cause a denial of service (crash) and disable the HIDS module via a crafted response.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-7078
    - Vulnerability Description: Multiple buffer overflows in Rumpus before 6.0.1 allow remote attackers to (1) cause a denial of service (segmentation fault) via a long HTTP verb in the HTTP component
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-7107
    - Vulnerability Description: easdrv.sys in ESET Smart Security 3.0.667.0 allows local users to cause a denial of service (crash) via a crafted IOCTL 0x222003 request to the \\.\easdrv device interface.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-7126
    - Vulnerability Description: Integer overflow in osagent.exe in Borland VisiBroker Smart Agent 08.00.00.C1.03 and earlier allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via a crafted packet with a large string length value to UDP port 14000, which triggers a heap-based buffer overflow.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-7127
    - Vulnerability Description: osagent.exe in Borland VisiBroker Smart Agent 08.00.00.C1.03 and earlier allows remote attackers to cause a denial of service (crash) via a crafted packet with a large string length value to UDP port 14000, which triggers a memory allocation failure that is not properly handled.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-7194
    - Vulnerability Description: Unspecified vulnerability in Fujitsu Interstage HTTP Server, as used in Interstage Application Server 5.0, 7.0, 7.0.1, and 8.0.0 for Windows, allows attackers to cause a denial of service via a crafted request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-7195
    - Vulnerability Description: Unspecified vulnerability in Fujitsu Interstage HTTP Server, as used in Interstage Application Server Enterprise Edition 7.0.1 for Solaris, allows attackers to cause a denial of service via unknown vectors related to SSL.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2008-7312
    - Vulnerability Description: The Filtering Service in Websense Enterprise 5.2 through 6.3 does not consider the IP address during URL categorization, which makes it easier for remote attackers to bypass filtering via an HTTP request, as demonstrated by a request to a compromised server associated with a specific IP address.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-0002
    - Vulnerability Description: Heap-based buffer overflow in Apple QuickTime before 7.6 allows remote attackers to cause a denial of service (application termination) and possibly execute arbitrary code via a QTVR movie file with crafted THKD atoms.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-0023
    - Vulnerability Description: The apr_strmatch_precompile function in strmatch/apr_strmatch.c in Apache APR-util before 1.3.5 allows remote attackers to cause a denial of service (daemon crash) via crafted input involving (1) a .htaccess file used with the Apache HTTP Server, (2) the SVNMasterURI directive in the mod_dav_svn module in the Apache HTTP Server, (3) the mod_apreq2 module for the Apache HTTP Server, or (4) an application that uses the libapreq2 library, which triggers a heap-based buffer underflow.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-0033
    - Vulnerability Description: Apache Tomcat 4.1.0 through 4.1.39, 5.5.0 through 5.5.27, and 6.0.0 through 6.0.18, when the Java AJP connector and mod_jk load balancing are used, allows remote attackers to cause a denial of service (application outage) via a crafted request with invalid headers, related to temporary blocking of connectors that have encountered errors, as demonstrated by an error involving a malformed HTTP Host header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-0086
    - Vulnerability Description: Integer underflow in Windows HTTP Services (aka WinHTTP) in Microsoft Windows 2000 SP4, XP SP2 and SP3, Server 2003 SP1 and SP2, Vista Gold and SP1, and Server 2008 allows remote HTTP servers to execute arbitrary code via crafted parameter values in a response, related to error handling, aka "Windows HTTP Services Integer Underflow Vulnerability."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-0089
    - Vulnerability Description: Windows HTTP Services (aka WinHTTP) in Microsoft Windows 2000 SP4, XP SP2 and SP3, Server 2003 SP1 and SP2, and Vista Gold allows remote web servers to impersonate arbitrary https web sites by using DNS spoofing to "forward a connection" to a different https web site that has a valid certificate matching its own domain name, but not a certificate matching the domain name of the host requested by the user, aka "Windows HTTP Services Certificate Name Mismatch Vulnerability."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-0157
    - Vulnerability Description: Heap-based buffer overflow in CFNetwork in Apple Mac OS X 10.5 before 10.5.7 allows remote web servers to execute arbitrary code or cause a denial of service (application crash) via long HTTP headers.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-0321
    - Vulnerability Description: Apple Safari 3.2.1 (aka AppVer 3.525.27.1) on Windows allows remote attackers to cause a denial of service (infinite loop or access violation) via a link to an http URI in which the authority (aka hostname) portion is either a (1) . (dot) or (2) .. (dot dot) sequence.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-0388
    - Vulnerability Description: Multiple integer signedness errors in (1) UltraVNC 1.0.2 and 1.0.5 and (2) TightVnc 1.3.9 allow remote VNC servers to cause a denial of service (heap corruption and application crash) or possibly execute arbitrary code via a large length value in a message, related to the (a) ClientConnection::CheckBufferSize and (b) ClientConnection::CheckFileZipBufferSize functions in ClientConnection.cpp.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-0419
    - Vulnerability Description: Microsoft XML Core Services, as used in Microsoft Expression Web, Office, Internet Explorer 6 and 7, and other products, does not properly restrict access from web pages to Set-Cookie2 HTTP response headers, which allows remote attackers to obtain sensitive information from cookies via XMLHttpRequest calls, related to the HTTPOnly protection mechanism.  NOTE: this issue reportedly exists because of an incomplete fix for CVE-2008-4033.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-0433
    - Vulnerability Description: Unspecified vulnerability in IBM WebSphere Application Server (WAS) 5.1.x before 5.1.1.19, 6.0.x before 6.0.2.29, and 6.1.x before 6.1.0.19, when Web Server plug-in content buffering is enabled, allows attackers to cause a denial of service (daemon crash) via unknown vectors, related to a mishandling of client read failures in which clients receive many 500 HTTP error responses and backend servers are incorrectly labeled as down.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-0478
    - Vulnerability Description: Squid 2.7 to 2.7.STABLE5, 3.0 to 3.0.STABLE12, and 3.1 to 3.1.0.4 allows remote attackers to cause a denial of service via an HTTP request with an invalid version number, which triggers a reachable assertion in (1) HttpMsg.c and (2) HttpStatusLine.c.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-0550
    - Vulnerability Description: Windows HTTP Services (aka WinHTTP) in Microsoft Windows 2000 SP4, XP SP2 and SP3, Server 2003 SP1 and SP2, Vista Gold and SP1, and Server 2008
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-0626
    - Vulnerability Description: The SSLVPN feature in Cisco IOS 12.3 through 12.4 allows remote attackers to cause a denial of service (device reload or hang) via a crafted HTTPS packet.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-0803
    - Vulnerability Description: SmoothWall SmoothGuardian, as used in SmoothWall Firewall, NetworkGuardian, and SchoolGuardian 2008, when transparent interception mode is enabled, uses the HTTP Host header to determine the remote endpoint, which allows remote attackers to bypass access controls for Flash, Java, Silverlight, and probably other technologies, and possibly communicate with restricted intranet sites, via a crafted web page that causes a client to send HTTP requests with a modified Host header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-0809
    - Vulnerability Description: The Web Editor in Dassault Systemes ENOVIA SmarTeam V5 before Release 18 Service Pack 8, and possibly CATIA and other products, allows remote authenticated users to read the profile card of an object in the document class via a link that is sent from the owner of the document object.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-0819
    - Vulnerability Description: sql/item_xmlfunc.cc in MySQL 5.1 before 5.1.32 and 6.0 before 6.0.10 allows remote authenticated users to cause a denial of service (crash) via "an XPath expression employing a scalar expression as a FilterExpr with ExtractValue() or UpdateXML()," which triggers an assertion failure.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-1101
    - Vulnerability Description: Unspecified vulnerability in the lightweight HTTP server implementation in Java SE Development Kit (JDK) and Java Runtime Environment (JRE) 6 Update 12 and earlier allows remote attackers to cause a denial of service (probably resource consumption) for a JAX-WS service endpoint via a connection without any data, which triggers a file descriptor "leak."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-1122
    - Vulnerability Description: The WebDAV extension in Microsoft Internet Information Services (IIS) 5.0 on Windows 2000 SP4 does not properly decode URLs, which allows remote attackers to bypass authentication, and possibly read or create files, via a crafted HTTP request, aka "IIS 5.0 WebDAV Authentication Bypass Vulnerability," a different vulnerability than CVE-2009-1535.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-1156
    - Vulnerability Description: Unspecified vulnerability on Cisco Adaptive Security Appliances (ASA) 5500 Series devices 8.0 before 8.0(4)25 and 8.1 before 8.1(2)15, when an SSL VPN or ASDM access is configured, allows remote attackers to cause a denial of service (device reload) via a crafted (1) SSL or (2) HTTP packet.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-1164
    - Vulnerability Description: The administrative web interface on the Cisco Wireless LAN Controller (WLC) platform 4.2 before 4.2.205.0 and 5.x before 5.2.178.0, as used in Cisco 1500 Series, 2000 Series, 2100 Series, 4100 Series, 4200 Series, and 4400 Series Wireless Services Modules (WiSM), WLC Modules for Integrated Services Routers, and Catalyst 3750G Integrated Wireless LAN Controllers, allows remote attackers to cause a denial of service (device reload) via a malformed response to a (1) HTTP or (2) HTTPS authentication request, aka Bug ID CSCsx03715.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-1166
    - Vulnerability Description: The administrative web interface on the Cisco Wireless LAN Controller (WLC) platform 4.x before 4.2.205.0 and 5.x before 5.2.191.0, as used in Cisco 1500 Series, 2000 Series, 2100 Series, 4100 Series, 4200 Series, and 4400 Series Wireless Services Modules (WiSM), WLC Modules for Integrated Services Routers, and Catalyst 3750G Integrated Wireless LAN Controllers, allows remote attackers to cause a denial of service (device reload) via a crafted (1) HTTP or (2) HTTPS request, aka Bug ID CSCsy27708.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-1167
    - Vulnerability Description: Unspecified vulnerability on the Cisco Wireless LAN Controller (WLC) platform 4.x before 4.2.205.0 and 5.x before 5.2.191.0, as used in Cisco 1500 Series, 2000 Series, 2100 Series, 4100 Series, 4200 Series, and 4400 Series Wireless Services Modules (WiSM), WLC Modules for Integrated Services Routers, and Catalyst 3750G Integrated Wireless LAN Controllers, allows remote attackers to modify the configuration via a crafted (1) HTTP or (2) HTTPS request, aka Bug ID CSCsy44672.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-1190
    - Vulnerability Description: Algorithmic complexity vulnerability in the java.util.regex.Pattern.compile method in Sun Java Development Kit (JDK) before 1.6, when used with spring.jar in SpringSource Spring Framework 1.1.0 through 2.5.6 and 3.0.0.M1 through 3.0.0.M2 and dm Server 1.0.0 through 1.0.2, allows remote attackers to cause a denial of service (CPU consumption) via serializable data with a long regex string containing multiple optional groups, a related issue to CVE-2004-2540.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-1227
    - Vulnerability Description: ** DISPUTED **  NOTE: this issue has been disputed by the vendor.  Buffer overflow in the PKI Web Service in Check Point Firewall-1 PKI Web Service allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via a long (1) Authorization or (2) Referer HTTP header to TCP port 18624.  NOTE: the vendor has disputed this issue, stating "Check Point Security Alert Team has analyzed this report. We've tried to reproduce the attack on all VPN-1 versions from NG FP2 and above with and without HFAs. The issue was not reproduced. We have conducted a thorough analysis of the relevant code and verified that we are secure against this attack. We consider this attack to pose no risk to Check Point customers."  In addition, the original researcher, whose reliability is unknown as of 20090407, also states that the issue "was discovered during a pen-test where the client would not allow further analysis."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-1291
    - Vulnerability Description: Stack-based buffer overflow in TIBCO SmartSockets before 6.8.2, SmartSockets Product Family (aka RTworks) before 4.0.5, and Enterprise Message Service (EMS) 4.0.0 through 5.1.1, as used in SmartSockets Server and RTworks Server (aka RTserver), SmartSockets client libraries and add-on products, RTworks libraries and components, EMS Server (aka tibemsd), SmartMQ, iProcess Engine, ActiveMatrix products, and CA Enterprise Communicator, allows remote attackers to execute arbitrary code via "inbound data," as demonstrated by requests to the UDP interface of the RTserver component, and data injection into the TCP stream to tibemsd.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-1353
    - Vulnerability Description: Buffer overflow in the http_parse_hex function in libz/misc.c in Zervit Webserver 0.02 allows remote attackers to cause a denial of service (daemon crash) via a long URI, related to http.c.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-1370
    - Vulnerability Description: Stack-based buffer overflow in ape_plugin.plg in Xilisoft Video Converter 3.1.53.0704n and 5.1.23.0402 allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via a long string in a .cue file.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-1425
    - Vulnerability Description: Unspecified vulnerability in HP ProCurve Threat Management Services zl Module (J9155A) ST.1.0.090213 and earlier allows remote attackers to cause a denial of service by triggering a stop or crash in httpd, aka PR_18770, a different vulnerability than CVE-2009-1423 and CVE-2009-1424.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-1536
    - Vulnerability Description: ASP.NET in Microsoft .NET Framework 2.0 SP1 and SP2 and 3.5 Gold and SP1, when ASP 2.0 is used in integrated mode on IIS 7.0, does not properly manage request scheduling, which allows remote attackers to cause a denial of service (daemon outage) via a series of crafted HTTP requests, aka "Remote Unauthenticated Denial of Service in ASP.NET Vulnerability."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-1890
    - Vulnerability Description: The stream_reqbody_cl function in mod_proxy_http.c in the mod_proxy module in the Apache HTTP Server before 2.3.3, when a reverse proxy is configured, does not properly handle an amount of streamed data that exceeds the Content-Length value, which allows remote attackers to cause a denial of service (CPU consumption) via crafted requests.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-1891
    - Vulnerability Description: The mod_deflate module in Apache httpd 2.2.11 and earlier compresses large files until completion even after the associated network connection is closed, which allows remote attackers to cause a denial of service (CPU consumption).
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-1903
    - Vulnerability Description: The PDF XSS protection feature in ModSecurity before 2.5.8 allows remote attackers to cause a denial of service (Apache httpd crash) via a request for a PDF file that does not use the GET method.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-1955
    - Vulnerability Description: The expat XML parser in the apr_xml_* interface in xml/apr_xml.c in Apache APR-util before 1.3.7, as used in the mod_dav and mod_dav_svn modules in the Apache HTTP Server, allows remote attackers to cause a denial of service (memory consumption) via a crafted XML document containing a large number of nested entity references, as demonstrated by a PROPFIND request, a similar issue to CVE-2003-1564.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-2121
    - Vulnerability Description: Buffer overflow in the browser kernel in Google Chrome before 2.0.172.33 allows remote HTTP servers to cause a denial of service (application crash) or possibly execute arbitrary code via a crafted response.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-2173
    - Vulnerability Description: The LAN game feature in Carom3D 5.06 allows remote authenticated users to cause a denial of service (application hang) via a crafted HTTP request to TCP port 28012.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-2256
    - Vulnerability Description: The administrative web interface on the Netgear DG632 with firmware 3.4.0_ap allows remote attackers to cause a denial of service (web outage) via an HTTP POST request to cgi-bin/firmwarecfg.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-2299
    - Vulnerability Description: The Artofdefence Hyperguard Web Application Firewall (WAF) module before 2.5.5-11635, 3.0 before 3.0.3-11636, and 3.1 before 3.1.1-11637, a module for the Apache HTTP Server, allows remote attackers to cause a denial of service (memory consumption) via an HTTP request with a large Content-Length value but no POST data.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-2509
    - Vulnerability Description: Active Directory Federation Services (ADFS) in Microsoft Windows Server 2003 SP2 and Server 2008 Gold and SP2 does not properly validate headers in HTTP requests, which allows remote authenticated users to execute arbitrary code via a crafted request to an IIS web server, aka "Remote Code Execution in ADFS Vulnerability."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-2621
    - Vulnerability Description: Squid 3.0 through 3.0.STABLE16 and 3.1 through 3.1.0.11 does not properly enforce "buffer limits and related bound checks," which allows remote attackers to cause a denial of service via (1) an incomplete request or (2) a request with a large header size, related to (a) HttpMsg.cc and (b) client_side.cc.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-2622
    - Vulnerability Description: Squid 3.0 through 3.0.STABLE16 and 3.1 through 3.1.0.11 allows remote attackers to cause a denial of service via malformed requests including (1) "missing or mismatched protocol identifier," (2) missing or negative status value," (3) "missing version," or (4) "missing or invalid status number," related to (a) HttpMsg.cc and (b) HttpReply.cc.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-2699
    - Vulnerability Description: The Solaris pollset feature in the Event Port backend in poll/unix/port.c in the Apache Portable Runtime (APR) library before 1.3.9, as used in the Apache HTTP Server before 2.2.14 and other products, does not properly handle errors, which allows remote attackers to cause a denial of service (daemon hang) via unspecified HTTP requests, related to the prefork and event MPMs.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-2732
    - Vulnerability Description: The checkHTTPpassword function in http.c in ntop 3.3.10 and earlier allows remote attackers to cause a denial of service (NULL pointer dereference and daemon crash) via an Authorization HTTP header that lacks a : (colon) character in the base64-decoded string.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-2855
    - Vulnerability Description: The strListGetItem function in src/HttpHeaderTools.c in Squid 2.7 allows remote attackers to cause a denial of service via a crafted auth header with certain comma delimiters that trigger an infinite loop of calls to the strcspn function.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-2865
    - Vulnerability Description: Buffer overflow in the login implementation in the Extension Mobility feature in the Unified Communications Manager Express (CME) component in Cisco IOS 12.4XW, 12.4XY, 12.4XZ, and 12.4YA allows remote attackers to execute arbitrary code or cause a denial of service via crafted HTTP requests, aka Bug ID CSCsq58779.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-2950
    - Vulnerability Description: Heap-based buffer overflow in the GIFLZWDecompressor::GIFLZWDecompressor function in filter.vcl/lgif/decode.cxx in OpenOffice.org (OOo) before 3.2 allows remote attackers to cause a denial of service (application crash) or possibly execute arbitrary code via a crafted GIF file, related to LZW decompression.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-2966
    - Vulnerability Description: avp.exe in Kaspersky Internet Security 9.0.0.459 and Anti-Virus 9.0.0.463 allows remote attackers to cause a denial of service (CPU consumption and network connectivity loss) via an HTTP URL request that contains a large number of dot "." characters.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-2973
    - Vulnerability Description: Google Chrome before 2.0.172.43 does not prevent SSL connections to a site with an X.509 certificate signed with the (1) MD2 or (2) MD4 algorithm, which makes it easier for man-in-the-middle attackers to spoof arbitrary HTTPS servers via a crafted certificate, a related issue to CVE-2009-2409.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-3000
    - Vulnerability Description: The sockfs module in the kernel in Sun Solaris 10 and OpenSolaris snv_41 through snv_122, when Network Cache Accelerator (NCA) logging is enabled, allows remote attackers to cause a denial of service (panic) via unspecified web-server traffic that triggers a NULL pointer dereference in the nl7c_http_log function, related to "improper http response handling."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-3094
    - Vulnerability Description: The ap_proxy_ftp_handler function in modules/proxy/proxy_ftp.c in the mod_proxy_ftp module in the Apache HTTP Server 2.0.63 and 2.2.13 allows remote FTP servers to cause a denial of service (NULL pointer dereference and child process crash) via a malformed reply to an EPSV command.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-3305
    - Vulnerability Description: Polipo 1.0.4, and possibly other versions, allows remote attackers to cause a denial of service (crash) via a request with a Cache-Control header that lacks a value for the max-age field, which triggers a segmentation fault in the httpParseHeaders function in http_parse.c, and possibly other unspecified vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-3448
    - Vulnerability Description: npvmgr.exe in BakBone NetVault Backup 8.22 Build 29 allows remote attackers to cause a denial of service (daemon crash) via a packet to (1) TCP or (2) UDP port 20031 with a large value in an unspecified size field, which is not properly handled in a malloc operation.  NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-3555
    - Vulnerability Description: The TLS protocol, and the SSL protocol 3.0 and possibly earlier, as used in Microsoft Internet Information Services (IIS) 7.0, mod_ssl in the Apache HTTP Server 2.2.14 and earlier, OpenSSL before 0.9.8l, GnuTLS 2.8.5 and earlier, Mozilla Network Security Services (NSS) 3.12.4 and earlier, multiple Cisco products, and other products, does not properly associate renegotiation handshakes with an existing connection, which allows man-in-the-middle attackers to insert data into HTTPS sessions, and possibly other types of sessions protected by TLS or SSL, by sending an unauthenticated request that is processed retroactively by a server in a post-renegotiation context, related to a "plaintext injection" attack, aka the "Project Mogul" issue.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-3586
    - Vulnerability Description: Off-by-one error in src/http.c in CoreHTTP 0.5.3.1 and earlier allows remote attackers to cause a denial of service or possibly execute arbitrary code via an HTTP request with a long first line that triggers a buffer overflow.  NOTE: this vulnerability reportedly exists because of an incorrect fix for CVE-2007-4060.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-3622
    - Vulnerability Description: Algorithmic complexity vulnerability in wp-trackback.php in WordPress before 2.8.5 allows remote attackers to cause a denial of service (CPU consumption and server hang) via a long title parameter in conjunction with a charset parameter composed of many comma-separated "UTF-8" substrings, related to the mb_convert_encoding function in PHP.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-3663
    - Vulnerability Description: Format string vulnerability in the h_readrequest function in http.c in httpdx Web Server 1.4 allows remote attackers to cause a denial of service (crash) or execute arbitrary code via format string specifiers in the Host header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-3695
    - Vulnerability Description: Algorithmic complexity vulnerability in the forms library in Django 1.0 before 1.0.4 and 1.1 before 1.1.1 allows remote attackers to cause a denial of service (CPU consumption) via a crafted (1) EmailField (email address) or (2) URLField (URL) that triggers a large amount of backtracking in a regular expression.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-3711
    - Vulnerability Description: Stack-based buffer overflow in the h_handlepeer function in http.cpp in httpdx 1.4, and possibly 1.4.3, allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via a long HTTP GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-3749
    - Vulnerability Description: The Web Administrator service (STEMWADM.EXE) in Websense Personal Email Manager 7.1 before Hotfix 4 and Email Security 7.1 before Hotfix 4 allows remote attackers to cause a denial of service (crash) by sending a HTTP GET request to TCP port 8181 and closing the socket before the service can send a response.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-3877
    - Vulnerability Description: Unspecified vulnerability in Sun Java SE in JDK and JRE 5.0 before Update 22, JDK and JRE 6 before Update 17, SDK and JRE 1.3.x before 1.3.1_27, and SDK and JRE 1.4.x before 1.4.2_24 allows remote attackers to cause a denial of service (memory consumption) via crafted HTTP headers, which are not properly parsed by the ASN.1 DER input stream parser, aka Bug Id 6864911.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-3896
    - Vulnerability Description: src/http/ngx_http_parse.c in nginx (aka Engine X) 0.1.0 through 0.4.14, 0.5.x before 0.5.38, 0.6.x before 0.6.39, 0.7.x before 0.7.62, and 0.8.x before 0.8.14 allows remote attackers to cause a denial of service (NULL pointer dereference and worker process crash) via a long URI.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-3923
    - Vulnerability Description: The VirtualBox 2.0.8 and 2.0.10 web service in Sun Virtual Desktop Infrastructure (VDI) 3.0 does not require authentication, which allows remote attackers to obtain unspecified access via vectors involving requests to an Apache HTTP Server.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-4355
    - Vulnerability Description: Memory leak in the zlib_stateful_finish function in crypto/comp/c_zlib.c in OpenSSL 0.9.8l and earlier and 1.0.0 Beta through Beta 4 allows remote attackers to cause a denial of service (memory consumption) via vectors that trigger incorrect calls to the CRYPTO_cleanup_all_ex_data function, as demonstrated by use of SSLv3 and PHP with the Apache HTTP Server, a related issue to CVE-2008-1678.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-4413
    - Vulnerability Description: The httpClientDiscardBody function in client.c in Polipo 0.9.8, 0.9.12, 1.0.4, and possibly other versions, allows remote attackers to cause a denial of service (crash) via a request with a large Content-Length value, which triggers an integer overflow, a signed-to-unsigned conversion error with a negative value, and a segmentation fault.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-4775
    - Vulnerability Description: Format string vulnerability in Ipswitch WS_FTP Professional 12 before 12.2 allows remote attackers to cause a denial of service (crash) via format string specifiers in the status code portion of an HTTP response.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-4873
    - Vulnerability Description: Stack-based buffer overflow in the HTTP server in Rhino Software Serv-U Web Client 9.0.0.5 allows remote attackers to cause a denial of service (server crash) or execute arbitrary code via a long Session cookie.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-4901
    - Vulnerability Description: The MSGFunctionDemarshall function in winscard_svc.c in the PC/SC Smart Card daemon (aka PCSCD) in MUSCLE PCSC-Lite before 1.5.4 might allow local users to cause a denial of service (daemon crash) via crafted SCARD_SET_ATTRIB message data, which is improperly demarshalled and triggers a buffer over-read, a related issue to CVE-2010-0407.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-5110
    - Vulnerability Description: dhttpd allows remote attackers to cause a denial of service (daemon outage) via partial HTTP requests, as demonstrated by Slowloris.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2009-5111
    - Vulnerability Description: GoAhead WebServer allows remote attackers to cause a denial of service (daemon outage) via partial HTTP requests, as demonstrated by Slowloris.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-0010
    - Vulnerability Description: Integer overflow in the ap_proxy_send_fb function in proxy/proxy_util.c in mod_proxy in the Apache HTTP Server before 1.3.42 on 64-bit platforms allows remote origin servers to cause a denial of service (daemon crash) or possibly execute arbitrary code via a large chunk size that triggers a heap-based buffer overflow.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-0101
    - Vulnerability Description: The embedded HTTP server in multiple Lexmark laser and inkjet printers and MarkNet devices, including X94x, W840, T656, N4000, E462, C935dn, 25xxN, and other models, allows remote attackers to cause a denial of service (operating system halt) via a malformed HTTP Authorization header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-0295
    - Vulnerability Description: lighttpd before 1.4.26, and 1.5.x, allocates a buffer for each read operation that occurs for a request, which allows remote attackers to cause a denial of service (memory consumption) by breaking a request into small pieces that are sent at a slow rate.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-0361
    - Vulnerability Description: Stack-based buffer overflow in the WebDAV implementation in webservd in Sun Java System Web Server (aka SJWS) 7.0 Update 7 allows remote attackers to cause a denial of service (daemon crash) and possibly have unspecified other impact via a long URI in an HTTP OPTIONS request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-0387
    - Vulnerability Description: Multiple heap-based buffer overflows in (1) webservd and (2) the admin server in Sun Java System Web Server 7.0 Update 7 allow remote attackers to cause a denial of service (daemon crash) and possibly have unspecified other impact via a long string in an "Authorization: Digest" HTTP header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-0389
    - Vulnerability Description: The admin server in Sun Java System Web Server 7.0 Update 6 allows remote attackers to cause a denial of service (NULL pointer dereference and daemon crash) via an HTTP request that lacks a method token.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-0408
    - Vulnerability Description: The ap_proxy_ajp_request function in mod_proxy_ajp.c in mod_proxy_ajp in the Apache HTTP Server 2.2.x before 2.2.15 does not properly handle certain situations in which a client sends no request body, which allows remote attackers to cause a denial of service (backend server outage) via a crafted request, related to use of a 500 error code instead of the appropriate 400 error code.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-0534
    - Vulnerability Description: Wiki Server in Apple Mac OS X 10.6 before 10.6.3 does not enforce the service access control list (SACL) for weblogs during weblog creation, which allows remote authenticated users to publish content via HTTP requests.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-0597
    - Vulnerability Description: Unspecified vulnerability in Cisco Mediator Framework 1.5.1 before 1.5.1.build.14-eng, 2.2 before 2.2.1.dev.1, and 3.0 before 3.0.9.release.1 on the Cisco Network Building Mediator NBM-2400 and NBM-4800 and the Richards-Zeta Mediator 2500 allows remote authenticated users to read or modify the device configuration, and gain privileges or cause a denial of service (device reload), via a (1) XML RPC or (2) XML RPC over HTTPS request, aka Bug ID CSCtb83618.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-1226
    - Vulnerability Description: The HTTP client functionality in Apple iPhone OS 3.1 on the iPhone 2G and 3.1.3 on the iPhone 3GS allows remote attackers to cause a denial of service (Safari, Mail, or Springboard crash) via a crafted innerHTML property of a DIV element, related to a "malformed character" issue.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-1452
    - Vulnerability Description: The (1) mod_cache and (2) mod_dav modules in the Apache HTTP Server 2.2.x before 2.2.16 allow remote attackers to cause a denial of service (process crash) via a request that lacks a path.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-1544
    - Vulnerability Description: micro_httpd on the RCA DCM425 cable modem allows remote attackers to cause a denial of service (device reboot) via a long string to TCP port 80.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-1576
    - Vulnerability Description: The Cisco Content Services Switch (CSS) 11500 with software before 8.20.4.02 and the Application Control Engine (ACE) 4710 with software before A2(3.0) do not properly handle use of LF, CR, and LFCR as alternatives to the standard CRLF sequence between HTTP headers, which allows remote attackers to bypass intended header insertions or conduct HTTP request smuggling attacks via crafted header data, as demonstrated by LF characters preceding ClientCert-Subject and ClientCert-Subject-CN headers, aka Bug ID CSCta04885.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-1623
    - Vulnerability Description: Memory leak in the apr_brigade_split_line function in buckets/apr_brigade.c in the Apache Portable Runtime Utility library (aka APR-util) before 1.3.10, as used in the mod_reqtimeout module in the Apache HTTP Server and other software, allows remote attackers to cause a denial of service (memory consumption) via unspecified vectors related to the destruction of an APR bucket.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-1632
    - Vulnerability Description: Apache Axis2 before 1.5.2, as used in IBM WebSphere Application Server (WAS) 7.0 through 7.0.0.12, IBM Feature Pack for Web Services 6.1.0.9 through 6.1.0.32, IBM Feature Pack for Web 2.0 1.0.1.0, Apache Synapse, Apache ODE, Apache Tuscany, Apache Geronimo, and other products, does not properly reject DTDs in SOAP messages, which allows remote attackers to read arbitrary files, send HTTP requests to intranet servers, or cause a denial of service (CPU and memory consumption) via a crafted DTD, as demonstrated by an entity declaration in a request to the Synapse SimpleStockQuoteService.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-1866
    - Vulnerability Description: The dechunk filter in PHP 5.3 through 5.3.2, when decoding an HTTP chunked encoding stream, allows context-dependent attackers to cause a denial of service (crash) and possibly trigger memory corruption via a negative chunk size, which bypasses a signed comparison, related to an integer overflow in the chunk size decoder.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-2054
    - Vulnerability Description: Integer overflow in httpAdapter.c in httpAdapter in SBLIM SFCB 1.3.4 through 1.3.7, when the configuration sets httpMaxContentLength to a zero value, allows remote attackers to cause a denial of service (heap memory corruption) or possibly execute arbitrary code via a large integer in the Content-Length HTTP header, aka bug #3001915.  NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-2076
    - Vulnerability Description: Apache CXF 2.0.x before 2.0.13, 2.1.x before 2.1.10, and 2.2.x before 2.2.9, as used in Apache ServiceMix, Apache Camel, Apache Chemistry, Apache jUDDI, Apache Geronimo, and other products, does not properly reject DTDs in SOAP messages, which allows remote attackers to read arbitrary files, send HTTP requests to intranet servers, or cause a denial of service (CPU and memory consumption) via a crafted DTD, as demonstrated by an entity declaration in a request to samples/wsdl_first_pure_xml, a similar issue to CVE-2010-1632.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-2195
    - Vulnerability Description: bozotic HTTP server (aka bozohttpd) 20090522 through 20100512 allows attackers to cause a denial of service via vectors related to a "wrong code generation interaction with GCC."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-2327
    - Vulnerability Description: mod_ibm_ssl in IBM HTTP Server 6.0 before 6.0.2.43, 6.1 before 6.1.0.33, and 7.0 before 7.0.0.11, as used in IBM WebSphere Application Server (WAS) on z/OS, does not properly handle a large HTTP request body in uploading over SSL, which might allow remote attackers to cause a denial of service (daemon fail) via an upload.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-2328
    - Vulnerability Description: The HTTP Channel in IBM WebSphere Application Server (WAS) 7.0 before 7.0.0.11 allows remote attackers to cause a denial of service (NullPointerException) via a large amount of chunked data that uses gzip compression.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-2432
    - Vulnerability Description: The cupsDoAuthentication function in auth.c in the client in CUPS before 1.4.4, when HAVE_GSSAPI is omitted, does not properly handle a demand for authorization, which allows remote CUPS servers to cause a denial of service (infinite loop) via HTTP_UNAUTHORIZED responses.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-2435
    - Vulnerability Description: Weborf HTTP Server 0.12.1 and earlier allows remote attackers to cause a denial of service (crash) via Unicode characters in a Connection HTTP header, and possibly other headers.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-2493
    - Vulnerability Description: The default configuration of the deployment descriptor (aka web.xml) in picketlink-sts.war in (1) the security_saml quickstart, (2) the webservice_proxy_security quickstart, (3) the web-console application, (4) the http-invoker application, (5) the gpd-deployer application, (6) the jbpm-console application, (7) the contract application, and (8) the uddi-console application in JBoss Enterprise SOA Platform before 5.0.2 contains GET and POST http-method elements, which allows remote attackers to bypass intended access restrictions via a crafted HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-2498
    - Vulnerability Description: The psh_glyph_find_strong_points function in pshinter/pshalgo.c in FreeType before 2.4.0 does not properly implement hinting masks, which allows remote attackers to cause a denial of service (heap memory corruption and application crash) or possibly execute arbitrary code via a crafted font file that triggers an invalid free operation.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-2561
    - Vulnerability Description: Microsoft XML Core Services (aka MSXML) 3.0 does not properly handle HTTP responses, which allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption) via a crafted response, aka "Msxml2.XMLHTTP.3.0 Response Handling Memory Corruption Vulnerability."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-2629
    - Vulnerability Description: The Cisco Content Services Switch (CSS) 11500 with software 8.20.4.02 and the Application Control Engine (ACE) 4710 with software A2(3.0) do not properly handle LF header terminators in situations where the GET line is terminated by CRLF, which allows remote attackers to conduct HTTP request smuggling attacks and possibly bypass intended header insertions via crafted header data, as demonstrated by an LF character between the ClientCert-Subject and ClientCert-Subject-CN headers. NOTE: this vulnerability exists because of an incomplete fix for CVE-2010-1576.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-2648
    - Vulnerability Description: The implementation of the Unicode Bidirectional Algorithm (aka Bidi algorithm or UBA) in Google Chrome before 5.0.375.99 allows remote attackers to cause a denial of service (memory corruption) or possibly have unspecified other impact via unknown vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-2823
    - Vulnerability Description: Unspecified vulnerability in the deep packet inspection feature on the Cisco Application Control Engine (ACE) 4710 appliance with software before A3(2.6) allows remote attackers to cause a denial of service (device reload) via crafted HTTP packets, related to HTTP, RTSP, and SIP inspection, aka Bug ID CSCtb54493.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-2836
    - Vulnerability Description: Memory leak in the SSL VPN feature in Cisco IOS 12.4, 15.0, and 15.1, when HTTP port redirection is enabled, allows remote attackers to cause a denial of service (memory consumption) by improperly disconnecting SSL sessions, leading to connections that remain in the CLOSE-WAIT state, aka Bug ID CSCtg21685.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-2883
    - Vulnerability Description: Stack-based buffer overflow in CoolType.dll in Adobe Reader and Acrobat 9.x before 9.4, and 8.x before 8.2.5 on Windows and Mac OS X, allows remote attackers to execute arbitrary code or cause a denial of service (application crash) via a PDF document with a long field in a Smart INdependent Glyphlets (SING) table in a TTF font, as exploited in the wild in September 2010. NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-3260
    - Vulnerability Description: oxf/xml/xerces/XercesSAXParserFactoryImpl.java in the xforms-server component in the XForms service in Orbeon Forms before 3.9 does not properly restrict DTDs in Ajax requests, which allows remote attackers to read arbitrary files or send HTTP requests to intranet servers via an entity declaration in conjunction with an entity reference, related to an "XML injection" issue.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-3281
    - Vulnerability Description: Stack-based buffer overflow in the HTTP proxy service in Alcatel-Lucent OmniVista 4760 server before R5.1.06.03.c_Patch3 allows remote attackers to execute arbitrary code or cause a denial of service (service crash) via a long request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-3614
    - Vulnerability Description: named in ISC BIND 9.x before 9.6.2-P3, 9.7.x before 9.7.2-P3, 9.4-ESV before 9.4-ESV-R4, and 9.6-ESV before 9.6-ESV-R3 does not properly determine the security status of an NS RRset during a DNSKEY algorithm rollover, which might allow remote attackers to cause a denial of service (DNSSEC validation error) by triggering a rollover.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-3679
    - Vulnerability Description: Oracle MySQL 5.1 before 5.1.49 allows remote authenticated users to cause a denial of service (mysqld daemon crash) via certain arguments to the BINLOG command, which triggers an access of uninitialized memory, as demonstrated by valgrind.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-3802
    - Vulnerability Description: Integer signedness error in Apple QuickTime before 7.6.9 allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption and application crash) via a crafted panorama atom in a QuickTime Virtual Reality (QTVR) movie file.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-3903
    - Vulnerability Description: Unspecified vulnerability in OpenConnect before 2.23 allows remote AnyConnect SSL VPN servers to cause a denial of service (application crash) via a 404 HTTP status code.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-4302
    - Vulnerability Description: /opt/rv/Versions/CurrentVersion/Mcu/Config/Mcu.val in Cisco Unified Videoconferencing (UVC) System 5110 and 5115, when the Linux operating system is used, uses a weak hashing algorithm for the (1) administrator and (2) operator passwords, which makes it easier for local users to obtain sensitive information by recovering the cleartext values, aka Bug ID CSCti54010.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-4488
    - Vulnerability Description: Google Chrome before 8.0.552.215 does not properly handle HTTP proxy authentication, which allows remote attackers to cause a denial of service (application crash) via unspecified vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-4531
    - Vulnerability Description: Stack-based buffer overflow in the ATRDecodeAtr function in the Answer-to-Reset (ATR) Handler (atrhandler.c) for pcscd in PCSC-Lite 1.5.3, and possibly other 1.5.x and 1.6.x versions, allows physically proximate attackers to cause a denial of service (crash) and possibly execute arbitrary code via a smart card with an ATR message containing a long attribute value.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-4539
    - Vulnerability Description: The walk function in repos.c in the mod_dav_svn module for the Apache HTTP Server, as distributed in Apache Subversion before 1.6.15, allows remote authenticated users to cause a denial of service (NULL pointer dereference and daemon crash) via vectors that trigger the walking of SVNParentPath collections.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-4590
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in HTTP Access Services (HTTP-AS) in the Connection Manager in IBM Lotus Mobile Connect (LMC) before 6.1.4 allows remote attackers to inject arbitrary web script or HTML via unspecified vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-4591
    - Vulnerability Description: The Connection Manager in IBM Lotus Mobile Connect (LMC) before 6.1.4, when HTTP Access Services (HTTP-AS) is enabled, does not delete LTPA tokens in response to use of the iNotes Logoff button, which might allow physically proximate attackers to obtain access via an unattended client, related to a cookie domain mismatch.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-4592
    - Vulnerability Description: The Mobile Network Connections functionality in the Connection Manager in IBM Lotus Mobile Connect before 6.1.4, when HTTP Access Services (HTTP-AS) is enabled, does not properly handle failed attempts at establishing HTTP-TCP sessions, which allows remote attackers to cause a denial of service (memory consumption and daemon crash) by making many TCP connection attempts.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-4594
    - Vulnerability Description: The Connection Manager in IBM Lotus Mobile Connect before 6.1.4, when HTTP Access Services (HTTP-AS) is enabled, does not properly process TCP connection requests, which allows remote attackers to cause a denial of service (memory consumption and HTTP-AS hang) by making many connection requests that trigger "queue size delta errors," related to a "timing hole" issue.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-4595
    - Vulnerability Description: The Connection Manager in IBM Lotus Mobile Connect before 6.1.4 disables the http.device.stanza blacklisting functionality for HTTP Access Services (HTTP-AS), which allows remote attackers to bypass intended access restrictions via an HTTP request that contains a disallowed User-Agent header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2010-4690
    - Vulnerability Description: The Mobile User Security (MUS) service on Cisco Adaptive Security Appliances (ASA) 5500 series devices with software before 8.3(2) does not properly authenticate HTTP requests from a Web Security appliance (WSA), which might allow remote attackers to obtain sensitive information via a HEAD request, aka Bug ID CSCte53635.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-0043
    - Vulnerability Description: Kerberos in Microsoft Windows XP SP2 and SP3 and Server 2003 SP2 supports weak hashing algorithms, which allows local users to gain privileges by operating a service that sends crafted service tickets, as demonstrated by the CRC32 algorithm, aka "Kerberos Unkeyed Checksum Vulnerability."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-0162
    - Vulnerability Description: Wi-Fi in Apple iOS before 4.3 and Apple TV before 4.2 does not properly perform bounds checking for Wi-Fi frames, which allows remote attackers to cause a denial of service (device reset) via unspecified traffic on the local wireless network.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-0212
    - Vulnerability Description: servermgrd in Apple Mac OS X before 10.6.8 allows remote attackers to read arbitrary files, and possibly send HTTP requests to intranet servers or cause a denial of service (CPU and memory consumption), via an XML-RPC request containing an entity declaration in conjunction with an entity reference, related to an XML External Entity (aka XXE) issue.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-0348
    - Vulnerability Description: Cisco IOS 12.4(11)MD, 12.4(15)MD, 12.4(22)MD, 12.4(24)MD before 12.4(24)MD3, 12.4(22)MDA before 12.4(22)MDA5, and 12.4(24)MDA before 12.4(24)MDA3 on the Cisco Content Services Gateway Second Generation (aka CSG2) allows remote attackers to bypass intended access restrictions and intended billing restrictions by sending HTTP traffic to a restricted destination after sending HTTP traffic to an unrestricted destination, aka Bug ID CSCtk35917.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-0419
    - Vulnerability Description: Stack consumption vulnerability in the fnmatch implementation in apr_fnmatch.c in the Apache Portable Runtime (APR) library before 1.4.3 and the Apache HTTP Server before 2.2.18, and in fnmatch.c in libc in NetBSD 5.1, OpenBSD 4.8, FreeBSD, Apple Mac OS X 10.6, Oracle Solaris 10, and Android, allows context-dependent attackers to cause a denial of service (CPU and memory consumption) via *? sequences in the first argument, as demonstrated by attacks against mod_autoindex in httpd.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-0534
    - Vulnerability Description: Apache Tomcat 7.0.0 through 7.0.6 and 6.0.0 through 6.0.30 does not enforce the maxHttpHeaderSize limit for requests involving the NIO HTTP connector, which allows remote attackers to cause a denial of service (OutOfMemoryError) via a crafted request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-0715
    - Vulnerability Description: The mod_dav_svn module for the Apache HTTP Server, as distributed in Apache Subversion before 1.6.16, allows remote attackers to cause a denial of service (NULL pointer dereference and daemon crash) via a request that contains a lock token.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-1180
    - Vulnerability Description: Multiple stack-based buffer overflows in the iriap_getvaluebyclass_indication function in net/irda/iriap.c in the Linux kernel before 2.6.39 allow remote attackers to cause a denial of service (memory corruption) or possibly have unspecified other impact by leveraging connectivity to an IrDA infrared network and sending a large integer value for a (1) name length or (2) attribute length.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-1209
    - Vulnerability Description: IBM WebSphere Application Server (WAS) 6.1 before 6.1.0.39 and 7.0 before 7.0.0.17 uses a weak WS-Security XML encryption algorithm, which makes it easier for remote attackers to obtain plaintext data from a (1) JAX-RPC or (2) JAX-WS Web Services request via unspecified vectors related to a "decryption attack."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-1316
    - Vulnerability Description: The Session Initiation Protocol (SIP) Proxy in the HTTP Transport component in IBM WebSphere Application Server (WAS) before 7.0.0.15 allows remote attackers to cause a denial of service (worker thread exhaustion and UDP messaging outage) by sending many UDP messages.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-1323
    - Vulnerability Description: Yamaha RTX, RT, SRT, RTV, RTW, and RTA series routers with firmware 6.x through 10.x, and NEC IP38X series routers with firmware 6.x through 10.x, do not properly handle IP header options, which allows remote attackers to cause a denial of service (device reboot) via a crafted option that triggers access to an invalid memory location.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-1357
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in agentDetect.jsp in the web UI in IBM WebSphere Service Registry and Repository (WSRR) 6.3 before 6.3.0.5, 7.0 before 7.0.0.5, and 7.5 before 7.5.0.1 allows remote attackers to inject arbitrary web script or HTML via the User-Agent HTTP header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-1465
    - Vulnerability Description: The SPDY implementation in net/http/http_network_transaction.cc in Google Chrome before 11.0.696.14 drains the bodies from SPDY responses, which might allow remote SPDY servers to cause a denial of service (application exit) by canceling a stream.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-1469
    - Vulnerability Description: Unspecified vulnerability in the Streams component in PHP before 5.3.6 allows context-dependent attackers to cause a denial of service (application crash) by accessing an ftp:// URL during use of an HTTP proxy with the FTP wrapper.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-1710
    - Vulnerability Description: Multiple integer overflows in the HTTP server in the Novell XTier framework 3.1.8 allow remote attackers to cause a denial of service (service crash) or possibly execute arbitrary code via crafted header length variables.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-1752
    - Vulnerability Description: The mod_dav_svn module for the Apache HTTP Server, as distributed in Apache Subversion before 1.6.17, allows remote attackers to cause a denial of service (NULL pointer dereference and daemon crash) via a request for a baselined WebDAV resource, as exploited in the wild in May 2011.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-1783
    - Vulnerability Description: The mod_dav_svn module for the Apache HTTP Server, as distributed in Apache Subversion 1.5.x and 1.6.x before 1.6.17, when the SVNPathAuthz short_circuit option is enabled, allows remote attackers to cause a denial of service (infinite loop and memory consumption) in opportunistic circumstances by requesting data.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-1860
    - Vulnerability Description: Unspecified vulnerability in HP Service Manager 7.02, 7.11, 9.20, and 9.21 and Service Center 6.2.8 allows remote attackers to capture HTTP session credentials via unknown vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-1928
    - Vulnerability Description: The fnmatch implementation in apr_fnmatch.c in the Apache Portable Runtime (APR) library 1.4.3 and 1.4.4, and the Apache HTTP Server 2.2.18, allows remote attackers to cause a denial of service (infinite loop) via a URI that does not match unspecified types of wildcard patterns, as demonstrated by attacks against mod_autoindex in httpd when a /*/WEB-INF/ configuration pattern is used.  NOTE: this issue exists because of an incorrect fix for CVE-2011-0419.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-2149
    - Vulnerability Description: Multiple SQL injection vulnerabilities in the SmarterTools SmarterStats 6.0 web server allow remote attackers to execute arbitrary SQL commands via certain parameters to (1) Admin/frmSite.aspx, (2) Default.aspx, (3) Services/SiteAdmin.asmx, or (4) Client/frmViewReports.aspx
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-2150
    - Vulnerability Description: The SmarterTools SmarterStats 6.0 web server does not properly validate string data that is intended for storage in an XML document, which allows remote attackers to cause a denial of service (parsing error and daemon pause) via vectors involving (1) certain cookies in a SiteInfoLookup action to Admin/frmSites.aspx, or certain (2) cookies or (3) parameters to (a) Client/frmViewOverviewReport.aspx, (b) Client/frmViewReports.aspx, or (c) Services/SiteAdmin.asmx, as demonstrated by a ]]>> string, related to an "XML injection" issue.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-2154
    - Vulnerability Description: login.aspx in the SmarterTools SmarterStats 6.0 web server does not include the HTTPOnly flag in a Set-Cookie header for the loginsettings cookie, which makes it easier for remote attackers to obtain potentially sensitive information via script access to this cookie.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-2156
    - Vulnerability Description: The SmarterTools SmarterStats 6.0 web server allows remote attackers to obtain directory listings via a direct request for the (1) Admin/, (2) Admin/Defaults/, (3) Admin/GettingStarted/, (4) Admin/Popups/, (5) App_Themes/, (6) Client/, (7) Client/Popups/, (8) Services/, (9) Temp/, (10) UserControls/, (11) UserControls/PanelBarTemplates/, (12) UserControls/Popups/, (13) aspnet_client/, or (14) aspnet_client/system_web/ directory name, or (15) certain directory names under App_Themes/Default/.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-2159
    - Vulnerability Description: The SmarterTools SmarterStats 6.0 web server omits the Content-Type header for certain resources, which might allow remote attackers to have an unspecified impact by leveraging an interpretation conflict involving (1) Admin/Defaults/frmDefaultSiteSettings.aspx, (2) Admin/Defaults/frmServerDefaults.aspx, (3) Admin/frmReportSettings.aspx, (4) Admin/frmSite.aspx, (5) App_Themes/Default/ButtonBarIcons.xml, (6) App_Themes/Default/Skin.xml, (7) Client/frmImportSettings.aspx, (8) Client/frmSeoSettings.aspx, (9) Services/Web.config, (10) aspnet_client/system_web/4_0_30319/, (11) clientaccesspolicy.xml, (12) cloudscan.exe, (13) crossdomain.xml, or (14) sitemap.xml.  NOTE: it is possible that only clients, not the SmarterStats product, could be affected by this issue.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-2174
    - Vulnerability Description: Double free vulnerability in the tvb_uncompress function in epan/tvbuff.c in Wireshark 1.2.x before 1.2.17 and 1.4.x before 1.4.7 allows remote attackers to cause a denial of service (application crash) via a packet with malformed data that uses zlib compression.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-2206
    - Vulnerability Description: XMLParser.pm in DJabberd before 0.85 allows remote authenticated users to read arbitrary files, and possibly send HTTP requests to intranet servers or cause a denial of service (CPU and memory consumption), via an XML external entity declaration in conjunction with an entity reference, a different vulnerability than CVE-2011-1757.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-2475
    - Vulnerability Description: Format string vulnerability in ECTrace.dll in the iMailGateway service in the Internet Mail Gateway in OneBridge Server and DMZ Proxy in Sybase OneBridge Mobile Data Suite 5.5 and 5.6 allows remote attackers to execute arbitrary code via format string specifiers in unspecified string fields, related to authentication logging.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-2511
    - Vulnerability Description: Integer overflow in libvirt before 0.9.3 allows remote authenticated users to cause a denial of service (libvirtd crash) and possibly execute arbitrary code via a crafted VirDomainGetVcpus RPC call that triggers memory corruption.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-2526
    - Vulnerability Description: Apache Tomcat 5.5.x before 5.5.34, 6.x before 6.0.33, and 7.x before 7.0.19, when sendfile is enabled for the HTTP APR or HTTP NIO connector, does not validate certain request attributes, which allows local users to bypass intended file access restrictions or cause a denial of service (infinite loop or JVM crash) by leveraging an untrusted web application.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-2586
    - Vulnerability Description: The HTTP client in Cisco IOS 12.4 and 15.0 allows user-assisted remote attackers to cause a denial of service (device crash) via a malformed HTTP response to a request for service installation, aka Bug ID CSCts12249.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-2667
    - Vulnerability Description: Icihttp.exe in CA Gateway Security for HTTP, as used in CA Gateway Security 8.1 before 8.1.0.69 and CA Total Defense r12, does not properly parse URLs, which allows remote attackers to execute arbitrary code or cause a denial of service (heap memory corruption and daemon crash) via a malformed request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-2960
    - Vulnerability Description: Heap-based buffer overflow in httpsvr.exe 6.0.5.3 in Sunway ForceControl 6.1 SP1, SP2, and SP3 allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via a crafted URL.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-3184
    - Vulnerability Description: The msn_httpconn_parse_data function in httpconn.c in the MSN protocol plugin in libpurple in Pidgin before 2.10.0 does not properly handle HTTP 100 responses, which allows remote attackers to cause a denial of service (incorrect memory access and application crash) via vectors involving a crafted server message.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-3188
    - Vulnerability Description: The (1) IPv4 and (2) IPv6 implementations in the Linux kernel before 3.1 use a modified MD4 algorithm to generate sequence numbers and Fragment Identification values, which makes it easier for remote attackers to cause a denial of service (disrupted networking) or hijack network sessions by predicting these values and sending crafted packets.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-3192
    - Vulnerability Description: The byterange filter in the Apache HTTP Server 1.3.x, 2.0.x through 2.0.64, and 2.2.x through 2.2.19 allows remote attackers to cause a denial of service (memory and CPU consumption) via a Range header that expresses multiple overlapping ranges, as exploited in the wild in August 2011, a different vulnerability than CVE-2007-0086.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-3259
    - Vulnerability Description: The kernel in Apple iOS before 5 and Apple TV before 4.4 does not properly recover memory allocated for incomplete TCP connections, which allows remote attackers to cause a denial of service (resource consumption) by making many connection attempts.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-3271
    - Vulnerability Description: Unspecified vulnerability in the Smart Install functionality in Cisco IOS 12.2 and 15.1 allows remote attackers to execute arbitrary code or cause a denial of service (device crash) via crafted TCP packets to port 4786, aka Bug ID CSCto10165.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-3281
    - Vulnerability Description: Unspecified vulnerability in Cisco IOS 15.0 through 15.1, in certain HTTP Layer 7 Application Control and Inspection configurations, allows remote attackers to cause a denial of service (device reload or hang) via a crafted HTTP packet, aka Bug ID CSCto68554.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-3340
    - Vulnerability Description: SQL injection vulnerability in ATCOM Netvolution 2.5.8 ASP allows remote attackers to execute arbitrary SQL commands via the Referer HTTP header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-3348
    - Vulnerability Description: The mod_proxy_ajp module in the Apache HTTP Server before 2.2.21, when used with mod_proxy_balancer in certain configurations, allows remote attackers to cause a denial of service (temporary "error state" in the backend server) via a malformed HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-3427
    - Vulnerability Description: The Data Security component in Apple iOS before 5 and Apple TV before 4.4 does not properly restrict use of the MD5 hash algorithm within X.509 certificates, which makes it easier for man-in-the-middle attackers to spoof servers or obtain sensitive information via a crafted certificate.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-3483
    - Vulnerability Description: Wireshark 1.6.x before 1.6.2 allows remote attackers to cause a denial of service (application crash) via a malformed capture file that leads to an invalid root tvbuff, related to a "buffer exception handling vulnerability."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-3487
    - Vulnerability Description: Directory traversal vulnerability in CarelDataServer.exe in Carel PlantVisor 2.4.4 and earlier allows remote attackers to read arbitrary files via a .. (dot dot) in an HTTP GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-3579
    - Vulnerability Description: server/webmail.php in IceWarp WebMail in IceWarp Mail Server before 10.3.3 allows remote attackers to read arbitrary files, and possibly send HTTP requests to intranet servers or cause a denial of service (CPU and memory consumption), via an XML external entity declaration in conjunction with an entity reference.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-4045
    - Vulnerability Description: Buffer overflow in an unspecified ActiveX control in aipgctl.ocx in ARC Informatique PcVue 6.0 through 10.0, FrontVue, and PlantVue allows remote attackers to cause a denial of service via a crafted HTML document.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-4081
    - Vulnerability Description: crypto/ghash-generic.c in the Linux kernel before 3.1 allows local users to cause a denial of service (NULL pointer dereference and OOPS) or possibly have unspecified other impact by triggering a failed or missing ghash_setkey function call, followed by a (1) ghash_update function call or (2) ghash_final function call, as demonstrated by a write operation on an AF_ALG socket.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-4237
    - Vulnerability Description: CRLF injection vulnerability in autologin.jsp in Cisco CiscoWorks Common Services 4.0, as used in Cisco Prime LAN Management Solution and other products, allows remote attackers to inject arbitrary HTTP headers and conduct HTTP response splitting attacks via the URL parameter, aka Bug ID CSCtu18693.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-4362
    - Vulnerability Description: Integer signedness error in the base64_decode function in the HTTP authentication functionality (http_auth.c) in lighttpd 1.4 before 1.4.30 and 1.5 before SVN revision 2806 allows remote attackers to cause a denial of service (segmentation fault) via crafted base64 input that triggers an out-of-bounds read with a negative index.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-4415
    - Vulnerability Description: The ap_pregsub function in server/util.c in the Apache HTTP Server 2.0.x through 2.0.64 and 2.2.x through 2.2.21, when the mod_setenvif module is enabled, does not restrict the size of values of environment variables, which allows local users to cause a denial of service (memory consumption or NULL pointer dereference) via a .htaccess file with a crafted SetEnvIf directive, in conjunction with a crafted HTTP request header, related to (1) the "len +=" statement and (2) the apr_pcalloc function call, a different vulnerability than CVE-2011-3607.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-4873
    - Vulnerability Description: Unspecified vulnerability in the server in Certec EDV atvise before 2.1 allows remote attackers to cause a denial of service (daemon crash) via crafted requests to TCP port 4840.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-4880
    - Vulnerability Description: Directory traversal vulnerability in the web server in Certec atvise webMI2ADS (aka webMI) before 2.0.2 allows remote attackers to read arbitrary files via a crafted HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-4881
    - Vulnerability Description: The web server in Certec atvise webMI2ADS (aka webMI) before 2.0.2 does not properly check return values from functions, which allows remote attackers to cause a denial of service (NULL pointer dereference) via a crafted HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-4882
    - Vulnerability Description: The web server in Certec atvise webMI2ADS (aka webMI) before 2.0.2 allows remote attackers to cause a denial of service (application exit) via an unspecified command in an HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-4883
    - Vulnerability Description: The web server in Certec atvise webMI2ADS (aka webMI) before 2.0.2 does not properly validate values in HTTP requests, which allows remote attackers to cause a denial of service (resource consumption) via a crafted request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-4899
    - Vulnerability Description: ** DISPUTED ** wp-admin/setup-config.php in the installation component in WordPress 3.3.1 and earlier does not ensure that the specified MySQL database service is appropriate, which allows remote attackers to configure an arbitrary database via the dbhost and dbname parameters, and subsequently conduct static code injection and cross-site scripting (XSS) attacks via (1) an HTTP request or (2) a MySQL query.  NOTE: the vendor disputes the significance of this issue
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-5009
    - Vulnerability Description: The CmpWebServer.dll module in the Control service in 3S CoDeSys 3.4 SP4 Patch 2 allows remote attackers to cause a denial of service (NULL pointer dereference) via (1) a crafted Content-Length in an HTTP POST or (2) an invalid HTTP request method.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-5058
    - Vulnerability Description: The CmbWebserver.dll module of the Control service in 3S CoDeSys 3.4 SP4 Patch 2 allows remote attackers to create arbitrary directories under the web root by specifying a non-existent directory using \ (backslash) characters in an HTTP GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2011-5086
    - Vulnerability Description: https50.ocx in IP*Works! SSL in the server in Unitronics UniOPC before 2.0.0 does not properly implement an unspecified function, which allows remote attackers to cause a denial of service (application crash) or possibly execute arbitrary code via a crafted web site.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-0021
    - Vulnerability Description: The log_cookie function in mod_log_config.c in the mod_log_config module in the Apache HTTP Server 2.2.17 through 2.2.21, when a threaded MPM is used, does not properly handle a %{}C format string, which allows remote attackers to cause a denial of service (daemon crash) via a cookie that lacks both a name and a value.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-0031
    - Vulnerability Description: scoreboard.c in the Apache HTTP Server 2.2.21 and earlier might allow local users to cause a denial of service (daemon crash during shutdown) or possibly have unspecified other impact by modifying a certain type field within a scoreboard shared memory segment, leading to an invalid call to the free function.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-0256
    - Vulnerability Description: Apache Traffic Server 2.0.x and 3.0.x before 3.0.4 and 3.1.x before 3.1.3 does not properly allocate heap memory, which allows remote attackers to cause a denial of service (daemon crash) via a long HTTP Host header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-0368
    - Vulnerability Description: The administrative management interface on Cisco Wireless LAN Controller (WLC) devices with software 4.x, 5.x, 6.0, and 7.0 before 7.0.220.0, 7.1 before 7.1.91.0, and 7.2 before 7.2.103.0 allows remote attackers to cause a denial of service (device crash) via a malformed URL in an HTTP request, aka Bug ID CSCts81997.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-0370
    - Vulnerability Description: Cisco Wireless LAN Controller (WLC) devices with software 4.x, 5.x, 6.0, and 7.0 before 7.0.220.0 and 7.1 before 7.1.91.0, when WebAuth is enabled, allow remote attackers to cause a denial of service (device reload) via a sequence of (1) HTTP or (2) HTTPS packets, aka Bug ID CSCtt47435.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-0378
    - Vulnerability Description: Cisco Adaptive Security Appliances (ASA) 5500 series devices with software 8.0 through 8.4 allow remote attackers to cause a denial of service (connection limit exceeded) by triggering a large number of stale connections that result in an incorrect value for an MPF connection count, aka Bug ID CSCtv19854.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-0385
    - Vulnerability Description: The Smart Install feature in Cisco IOS 12.2, 15.0, 15.1, and 15.2 allows remote attackers to cause a denial of service (device reload) by sending a malformed Smart Install message over TCP, aka Bug ID CSCtt16051.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-0387
    - Vulnerability Description: Memory leak in the HTTP Inspection Engine feature in the Zone-Based Firewall in Cisco IOS 12.4, 15.0, 15.1, and 15.2 allows remote attackers to cause a denial of service (memory consumption or device reload) via crafted transit HTTP traffic, aka Bug ID CSCtq36153.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-0429
    - Vulnerability Description: dhost in NetIQ eDirectory 8.8.6.x before 8.8.6.7 and 8.8.7.x before 8.8.7.2 on Windows allows remote authenticated users to cause a denial of service (daemon crash) via crafted characters in an HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-0667
    - Vulnerability Description: Integer signedness error in Apple QuickTime before 7.7.2 on Windows allows remote attackers to execute arbitrary code or cause a denial of service (application crash) via a crafted QTVR movie file.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-0714
    - Vulnerability Description: Cross-site request forgery (CSRF) vulnerability in IBM Maximo Asset Management 6.2 through 7.5, as used in SmartCloud Control Desk, Tivoli Asset Management for IT, Tivoli Service Request Manager, Maximo Service Desk, and Change and Configuration Management Database (CCMDB), allows remote attackers to hijack the authentication of unspecified victims via unknown vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-0727
    - Vulnerability Description: SQL injection vulnerability in IBM Maximo Asset Management 7.5, as used in SmartCloud Control Desk, Tivoli Asset Management for IT, Tivoli Service Request Manager, Maximo Service Desk, and Change and Configuration Management Database (CCMDB), allows remote authenticated users to execute arbitrary SQL commands via unspecified vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-0728
    - Vulnerability Description: SQL injection vulnerability in IBM Maximo Asset Management 7.1 through 7.5, as used in SmartCloud Control Desk, Tivoli Asset Management for IT, Tivoli Service Request Manager, Maximo Service Desk, and Change and Configuration Management Database (CCMDB), allows remote authenticated users to execute arbitrary SQL commands via unspecified vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-0746
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in IBM Maximo Asset Management 7.5, as used in SmartCloud Control Desk, Tivoli Asset Management for IT, Tivoli Service Request Manager, Maximo Service Desk, and Change and Configuration Management Database (CCMDB), allows remote authenticated users to inject arbitrary web script or HTML via unspecified vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-0747
    - Vulnerability Description: SQL injection vulnerability in IBM Maximo Asset Management 6.2 through 7.5, as used in SmartCloud Control Desk, Tivoli Asset Management for IT, Tivoli Service Request Manager, Maximo Service Desk, and Change and Configuration Management Database (CCMDB), allows remote authenticated users to execute arbitrary SQL commands via unspecified vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-0788
    - Vulnerability Description: The PDORow implementation in PHP before 5.3.9 does not properly interact with the session feature, which allows remote attackers to cause a denial of service (application crash) via a crafted application that uses a PDO driver for a fetch and then calls the session_start function, as demonstrated by a crash of the Apache HTTP Server.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-0804
    - Vulnerability Description: Heap-based buffer overflow in the proxy_connect function in src/client.c in CVS 1.11 and 1.12 allows remote HTTP proxy servers to cause a denial of service (crash) and possibly execute arbitrary code via a crafted HTTP response.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-0929
    - Vulnerability Description: Multiple buffer overflows in Schneider Electric Modicon Quantum PLC allow remote attackers to cause a denial of service via malformed requests to the (1) FTP server or (2) HTTP server.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-1148
    - Vulnerability Description: Memory leak in the poolGrow function in expat/lib/xmlparse.c in expat before 2.1.0 allows context-dependent attackers to cause a denial of service (memory consumption) via a large number of crafted XML files that cause improperly-handled reallocation failures when expanding entities.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-1181
    - Vulnerability Description: fcgid_spawn_ctl.c in the mod_fcgid module 2.3.6 for the Apache HTTP Server does not recognize the FcgidMaxProcessesPerClass directive for a virtual host, which makes it easier for remote attackers to cause a denial of service (memory consumption) via a series of HTTP requests that triggers a process count higher than the intended limit.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-1184
    - Vulnerability Description: Stack-based buffer overflow in the ast_parse_digest function in main/utils.c in Asterisk 1.8.x before 1.8.10.1 and 10.x before 10.2.1 allows remote attackers to cause a denial of service (crash) or possibly execute arbitrary code via a long string in an HTTP Digest Authentication header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-1465
    - Vulnerability Description: Stack-based buffer overflow in the HTTP Server in NetMechanica NetDecision before 4.6.1 allows remote attackers to cause a denial of service (application crash) via a long URL in an HTTP request.  NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-1588
    - Vulnerability Description: Algorithmic complexity vulnerability in the _filter_url function in the text filtering system (modules/filter/filter.module) in Drupal 7.x before 7.14 allows remote authenticated users with certain roles to cause a denial of service (CPU consumption) via a long email address.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-1783
    - Vulnerability Description: Tiny Server 1.1.9 and earlier allows remote attackers to cause a denial of service (crash) via a long string in a GET request without an HTTP version number.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-1804
    - Vulnerability Description: The OPC server in Progea Movicon before 11.3 allows remote attackers to cause a denial of service (out-of-bounds read and memory corruption) via a crafted HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-2017
    - Vulnerability Description: Unspecified vulnerability on HP Photosmart Wireless e-All-in-One B110, e-All-in-One D110, Plus e-All-in-One B210, eStation All-in-One C510, Ink Advantage e-All-in-One K510, and Premium Fax e-All-in-One C410 printers allows remote attackers to cause a denial of service via unknown vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-2089
    - Vulnerability Description: Buffer overflow in ngx_http_mp4_module.c in the ngx_http_mp4_module module in nginx 1.0.7 through 1.0.14 and 1.1.3 through 1.1.18, when the mp4 directive is used, allows remote attackers to cause a denial of service (memory overwrite) or possibly execute arbitrary code via a crafted MP4 file.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-2091
    - Vulnerability Description: Multiple buffer overflows in FlightGear 2.6 and earlier and SimGear 2.6 and earlier allow user-assisted remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via a (1) long string in a rotor tag of an aircraft xml model to the Rotor::getValueforFGSet function in src/FDM/YASim/Rotor.cpp or (2) a crafted UDP packet to the SGSocketUDP::read function in simgear/simgear/simgear/io/sg_socket_udp.cxx.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-2098
    - Vulnerability Description: Algorithmic complexity vulnerability in the sorting algorithms in bzip2 compressing stream (BZip2CompressorOutputStream) in Apache Commons Compress before 1.4.1 allows remote attackers to cause a denial of service (CPU consumption) via a file with many repeating inputs.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-2138
    - Vulnerability Description: The @CopyFrom operation in the POST servlet in the org.apache.sling.servlets.post bundle before 2.1.2 in Apache Sling does not prevent attempts to copy an ancestor node to a descendant node, which allows remote attackers to cause a denial of service (infinite loop) via a crafted HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-2183
    - Vulnerability Description: Session fixation vulnerability in IBM Maximo Asset Management 6.2 through 7.5, as used in SmartCloud Control Desk, Tivoli Asset Management for IT, Tivoli Service Request Manager, Maximo Service Desk, and Change and Configuration Management Database (CCMDB), allows remote attackers to hijack web sessions via unspecified vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-2184
    - Vulnerability Description: Session fixation vulnerability in IBM Maximo Asset Management 7.1 through 7.5, as used in SmartCloud Control Desk, Tivoli Asset Management for IT, Tivoli Service Request Manager, Maximo Service Desk, and Change and Configuration Management Database (CCMDB), allows remote attackers to hijack web sessions via unspecified vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-2185
    - Vulnerability Description: IBM Maximo Asset Management 6.2 through 7.5, as used in SmartCloud Control Desk, Tivoli Asset Management for IT, Tivoli Service Request Manager, Maximo Service Desk, and Change and Configuration Management Database (CCMDB), allows remote authenticated users to obtain sensitive information via unspecified vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-2190
    - Vulnerability Description: IBM Global Security Kit (aka GSKit), as used in IBM HTTP Server in IBM WebSphere Application Server (WAS) 6.1.x before 6.1.0.45, 7.0.x before 7.0.0.25, 8.0.x before 8.0.0.4, and 8.5.x before 8.5.0.1, allows remote attackers to cause a denial of service (daemon crash) via a crafted ClientHello message in the TLS Handshake Protocol.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-2210
    - Vulnerability Description: The Sony Bravia TV KDL-32CX525 allows remote attackers to cause a denial of service (configuration outage or device crash) via a flood of TCP SYN packets, as demonstrated by hping, a related issue to CVE-1999-0116.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-2329
    - Vulnerability Description: Buffer overflow in the apache_request_headers function in sapi/cgi/cgi_main.c in PHP 5.4.x before 5.4.3 allows remote attackers to cause a denial of service (application crash) via a long string in the header of an HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-2357
    - Vulnerability Description: The Multi-Authentication feature in the Central Authentication Service (CAS) functionality in auth/cas/cas_form.html in Moodle 2.1.x before 2.1.6 and 2.2.x before 2.2.3 does not use HTTPS, which allows remote attackers to obtain credentials by sniffing the network.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-2438
    - Vulnerability Description: ar web content manager (AWCM) 2.2 does not restrict the number of comment records that can be submitted through HTTP requests, which allows remote attackers to cause a denial of service (disk consumption) via the coment parameter to (1) show_video.php or (2) topic.php.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-2585
    - Vulnerability Description: Multiple cross-site scripting (XSS) vulnerabilities in ManageEngine ServiceDesk Plus 8.1 allow remote attackers to inject arbitrary web script or HTML via an e-mail message body with (1) a SCRIPT element, (2) a crafted Cascading Style Sheets (CSS) expression property, (3) a CSS expression property in the STYLE attribute of an arbitrary element, or (4) a crafted SRC attribute of an IFRAME element, or an e-mail message subject with (5) a SCRIPT element, (6) a CSS expression property in the STYLE attribute of an arbitrary element, (7) a crafted SRC attribute of an IFRAME element, (8) a crafted CONTENT attribute of an HTTP-EQUIV="refresh" META element, or (9) a data: URL in the CONTENT attribute of an HTTP-EQUIV="refresh" META element.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-2619
    - Vulnerability Description: The Broadcom BCM4325 and BCM4329 Wi-Fi chips, as used in certain Acer, Apple, Asus, Ford, HTC, Kyocera, LG, Malata, Motorola, Nokia, Pantech, Samsung, and Sony products, allow remote attackers to cause a denial of service (out-of-bounds read and Wi-Fi outage) via an RSN 802.11i information element.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-2733
    - Vulnerability Description: java/org/apache/coyote/http11/InternalNioInputBuffer.java in the HTTP NIO connector in Apache Tomcat 6.x before 6.0.36 and 7.x before 7.0.28 does not properly restrict the request-header size, which allows remote attackers to cause a denial of service (memory consumption) via a large amount of header data.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-2868
    - Vulnerability Description: Race condition in Google Chrome before 21.0.1180.89 allows remote attackers to cause a denial of service or possibly have unspecified other impact via vectors involving improper interaction between worker processes and an XMLHttpRequest (aka XHR) object.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-3006
    - Vulnerability Description: The Innominate mGuard Smart HW before HW-101130 and BD before BD-101030, mGuard industrial RS, mGuard delta HW before HW-103060 and BD before BD-211010, mGuard PCI, mGuard blade, and EAGLE mGuard appliances with software before 7.5.0 do not use a sufficient source of entropy for private keys, which makes it easier for man-in-the-middle attackers to spoof (1) HTTPS or (2) SSH servers by predicting a key value.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-3017
    - Vulnerability Description: Siemens SIMATIC S7-400 PN CPU devices with firmware 5.x allow remote attackers to cause a denial of service (defect-mode transition and service outage) via (1) malformed HTTP traffic or (2) malformed IP packets.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-3297
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in the embedded HTTP server in the Service Console in IBM Tivoli Monitoring 6.2.2 before 6.2.2-TIV-ITM-FP0009 and 6.3.2 before 6.2.3-TIV-ITM-FP0001 allows remote attackers to inject arbitrary web script or HTML via a crafted URI.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-3313
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in IBM Maximo Asset Management 6.2 through 7.5, as used in SmartCloud Control Desk, Tivoli Asset Management for IT, Tivoli Service Request Manager, Maximo Service Desk, and Change and Configuration Management Database (CCMDB), allows remote attackers to inject arbitrary web script or HTML via unspecified vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-3316
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in the Tivoli Process Automation Engine (TPAE) in IBM Maximo Asset Management 6.2 through 7.5, Maximo Asset Management Essentials 6.2 through 7.5, Tivoli Asset Management for IT 6.2 through 7.2, Tivoli Service Request Manager 7.1 and 7.2, Maximo Service Desk 6.2, Change and Configuration Management Database (CCMDB) 7.1 and 7.2, and SmartCloud Control Desk 7.5 allows remote authenticated users to inject arbitrary web script or HTML via unspecified vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-3322
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in IBM Maximo Asset Management 6.2 through 7.5, Maximo Asset Management Essentials 6.2 through 7.5, Tivoli Asset Management for IT 6.2 through 7.2, Tivoli Service Request Manager 7.1 and 7.2, Maximo Service Desk 6.2, Change and Configuration Management Database (CCMDB) 7.1 and 7.2, and SmartCloud Control Desk 7.5 allows remote authenticated users to inject arbitrary web script or HTML via vectors related to a display name.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-3326
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in IBM Maximo Asset Management 7.5, as used in SmartCloud Control Desk, Tivoli Asset Management for IT, Tivoli Service Request Manager, Maximo Service Desk, and Change and Configuration Management Database (CCMDB), allows remote attackers to inject arbitrary web script or HTML via unspecified vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-3327
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in IBM Maximo Asset Management 6.2 through 7.5, Maximo Asset Management Essentials 6.2 through 7.5, Tivoli Asset Management for IT 6.2 through 7.2, Tivoli Service Request Manager 7.1 and 7.2, Maximo Service Desk 6.2, Change and Configuration Management Database (CCMDB) 7.1 and 7.2, and SmartCloud Control Desk 7.5 allows remote attackers to inject arbitrary web script or HTML via vectors related to a login action.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-3398
    - Vulnerability Description: Algorithmic complexity vulnerability in Moodle 1.9.x before 1.9.19, 2.0.x before 2.0.10, 2.1.x before 2.1.7, and 2.2.x before 2.2.4 allows remote authenticated users to cause a denial of service (CPU consumption) by using the advanced-search feature on a database activity that has many records.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-3424
    - Vulnerability Description: The decode_credentials method in actionpack/lib/action_controller/metal/http_authentication.rb in Ruby on Rails 3.x before 3.0.16, 3.1.x before 3.1.7, and 3.2.x before 3.2.7 converts Digest Authentication strings to symbols, which allows remote attackers to cause a denial of service by leveraging access to an application that uses a with_http_digest helper method, as demonstrated by the authenticate_or_request_with_http_digest method.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-3526
    - Vulnerability Description: The reverse proxy add forward module (mod_rpaf) 0.5 and 0.6 for the Apache HTTP Server allows remote attackers to cause a denial of service (server or application crash) via multiple X-Forwarded-For headers in a request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-3973
    - Vulnerability Description: The debugger in the developer-tools subsystem in Mozilla Firefox before 15.0, when remote debugging is disabled, does not properly restrict access to the remote-debugging service, which allows remote attackers to execute arbitrary code by leveraging the presence of the HTTPMonitor extension and connecting to that service through the HTTPMonitor port.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-4329
    - Vulnerability Description: The Samsung D6000 TV and possibly other products allow remote attackers to cause a denial of service (continuous restart) via a crafted controller name.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-4330
    - Vulnerability Description: The Samsung D6000 TV and possibly other products allows remote attackers to cause a denial of service (crash) via a long string in certain fields, as demonstrated by the MAC address field, possibly a buffer overflow.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-4534
    - Vulnerability Description: org/apache/tomcat/util/net/NioEndpoint.java in Apache Tomcat 6.x before 6.0.36 and 7.x before 7.0.28, when the NIO connector is used in conjunction with sendfile and HTTPS, allows remote attackers to cause a denial of service (infinite loop) by terminating the connection during the reading of a response.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-4555
    - Vulnerability Description: The token processing system (pki-tps) in Red Hat Certificate System (RHCS) before 8.1.3 does not properly handle interruptions of token format operations, which allows remote attackers to cause a denial of service (NULL pointer dereference and Apache httpd web server child process crash) via unspecified vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-4556
    - Vulnerability Description: The token processing system (pki-tps) in Red Hat Certificate System (RHCS) before 8.1.3 allows remote attackers to cause a denial of service (Apache httpd web server child process restart) via certain unspecified empty search fields in a user certificate search query.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-4557
    - Vulnerability Description: The mod_proxy_ajp module in the Apache HTTP Server 2.2.12 through 2.2.21 places a worker node into an error state upon detection of a long request-processing time, which allows remote attackers to cause a denial of service (worker consumption) via an expensive request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-4618
    - Vulnerability Description: The SIP ALG feature in the NAT implementation in Cisco IOS 12.2, 12.4, and 15.0 through 15.2 allows remote attackers to cause a denial of service (device reload) via transit IP packets, aka Bug ID CSCtn76183.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-4689
    - Vulnerability Description: Integer overflow in CimWebServer.exe in GE Intelligent Platforms Proficy HMI/SCADA - CIMPLICITY 4.01 through 8.0, and Proficy Process Systems with CIMPLICITY, allows remote attackers to cause a denial of service (daemon crash) via a malformed HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-4710
    - Vulnerability Description: Invensys Wonderware Win-XML Exporter 1522.148.0.0 allows remote attackers to read arbitrary files, send HTTP requests to intranet servers, or cause a denial of service (CPU and memory consumption) via an XML external entity declaration in conjunction with an entity reference.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-4876
    - Vulnerability Description: Stack-based buffer overflow in the UltraMJCam ActiveX Control in TRENDnet SecurView TV-IP121WN Wireless Internet Camera allows remote attackers to execute arbitrary code via a long string to the OpenFileDlg method.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-4999
    - Vulnerability Description: Mercury MR804 Router 8.0 3.8.1 Build 101220 Rel.53006nB allows remote attackers to cause a denial of service (service hang) via a crafted string in HTTP header fields such as (1) If-Modified-Since, (2) If-None-Match, or (3) If-Unmodified-Since.  NOTE: some of these details are obtained from third party information.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-5134
    - Vulnerability Description: Heap-based buffer underflow in the xmlParseAttValueComplex function in parser.c in libxml2 2.9.0 and earlier, as used in Google Chrome before 23.0.1271.91 and other products, allows remote attackers to cause a denial of service or possibly execute arbitrary code via crafted entities in an XML document.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-5332
    - Vulnerability Description: at32 Reverse Proxy 1.060.310 allows remote attackers to cause a denial of service (NULL pointer dereference and application crash) via a long string in an HTTP header field, as demonstrated using the If-Unmodified-Since field.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-5370
    - Vulnerability Description: JRuby computes hash values without properly restricting the ability to trigger hash collisions predictably, which allows context-dependent attackers to cause a denial of service (CPU consumption) via crafted input to an application that maintains a hash table, as demonstrated by a universal multicollision attack against the MurmurHash2 algorithm, a different vulnerability than CVE-2011-4838.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-5371
    - Vulnerability Description: Ruby (aka CRuby) 1.9 before 1.9.3-p327 and 2.0 before r37575 computes hash values without properly restricting the ability to trigger hash collisions predictably, which allows context-dependent attackers to cause a denial of service (CPU consumption) via crafted input to an application that maintains a hash table, as demonstrated by a universal multicollision attack against a variant of the MurmurHash2 algorithm, a different vulnerability than CVE-2011-4815.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-5372
    - Vulnerability Description: Rubinius computes hash values without properly restricting the ability to trigger hash collisions predictably, which allows context-dependent attackers to cause a denial of service (CPU consumption) via crafted input to an application that maintains a hash table, as demonstrated by a universal multicollision attack against the MurmurHash3 algorithm.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-5373
    - Vulnerability Description: Oracle Java SE 7 and earlier, and OpenJDK 7 and earlier, computes hash values without properly restricting the ability to trigger hash collisions predictably, which allows context-dependent attackers to cause a denial of service (CPU consumption) via crafted input to an application that maintains a hash table, as demonstrated by a universal multicollision attack against the MurmurHash3 algorithm, a different vulnerability than CVE-2012-2739.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-5533
    - Vulnerability Description: The http_request_split_value function in request.c in lighttpd before 1.4.32 allows remote attackers to cause a denial of service (infinite loop) via a request with a header containing an empty token, as demonstrated using the "Connection: TE,,Keep-Alive" header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-5568
    - Vulnerability Description: Apache Tomcat through 7.0.x allows remote attackers to cause a denial of service (daemon outage) via partial HTTP requests, as demonstrated by Slowloris.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-5633
    - Vulnerability Description: The URIMappingInterceptor in Apache CXF before 2.5.8, 2.6.x before 2.6.5, and 2.7.x before 2.7.2, when using the WSS4JInInterceptor, bypasses WS-Security processing, which allows remote attackers to obtain access to SOAP services via an HTTP GET request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-5657
    - Vulnerability Description: The (1) Zend_Feed_Rss and (2) Zend_Feed_Atom classes in Zend_Feed in Zend Framework 1.11.x before 1.11.15 and 1.12.x before 1.12.1 allow remote attackers to read arbitrary files, send HTTP requests to intranet servers, and possibly cause a denial of service (CPU and memory consumption) via an XML External Entity (XXE) attack.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-5769
    - Vulnerability Description: IBM SPSS Modeler 14.0, 14.1, 14.2 through FP3, and 15.0 before FP2 allows remote attackers to read arbitrary files, and possibly send HTTP requests to intranet servers or cause a denial of service (CPU and memory consumption), via an XML external entity declaration in conjunction with an entity reference.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-5783
    - Vulnerability Description: Apache Commons HttpClient 3.x, as used in Amazon Flexible Payments Service (FPS) merchant Java SDK and other products, does not verify that the server hostname matches a domain name in the subject's Common Name (CN) or subjectAltName field of the X.509 certificate, which allows man-in-the-middle attackers to spoof SSL servers via an arbitrary valid certificate.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-5875
    - Vulnerability Description: Firefly Media Server 1.0.0.1359 allows remote attackers to cause a denial of service (NULL pointer dereference) via a (1) crafted Connection HTTP header
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-5951
    - Vulnerability Description: Unspecified vulnerability in IBM Tivoli NetView 1.4, 5.1 through 5.4, and 6.1 on z/OS allows local users to gain privileges by leveraging access to the normal Unix System Services (USS) security level.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-5953
    - Vulnerability Description: IBM WebSphere Message Broker 6.1 before 6.1.0.12, 7.0 before 7.0.0.6, and 8.0 before 8.0.0.2, when the Parse Query Strings option is enabled on an HTTPInput node, allows remote attackers to cause a denial of service (infinite loop) via a crafted query string.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-5970
    - Vulnerability Description: The Huawei E585 device allows remote attackers to cause a denial of service (NULL pointer dereference and device outage) via crafted HTTP requests, as demonstrated by unspecified vulnerability-scanning software.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-6026
    - Vulnerability Description: The HTTP Profiler on the Cisco Aironet Access Point with software 15.2 and earlier does not properly manage buffers, which allows remote attackers to cause a denial of service (device reload) via crafted HTTP requests, aka Bug ID CSCuc62460.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-6128
    - Vulnerability Description: Multiple stack-based buffer overflows in http.c in OpenConnect before 4.08 allow remote VPN gateways to cause a denial of service (application crash) via a long (1) hostname, (2) path, or (3) cookie list in a response.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-6355
    - Vulnerability Description: IBM Maximo Asset Management 6.2 through 7.5, Maximo Asset Management Essentials 6.2 through 7.5, Tivoli Asset Management for IT 6.2 through 7.2, Tivoli Service Request Manager 7.1 and 7.2, Maximo Service Desk 6.2, Change and Configuration Management Database (CCMDB) 7.1 and 7.2, and SmartCloud Control Desk 7.5 allow remote authenticated users to gain privileges via vectors related to a work order.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-6461
    - Vulnerability Description: The X.509 certificate-validation functionality in the https implementation in Opera before 12.10 allows remote attackers to trigger a false indication of successful revocation-status checking by causing a failure of a single checking service.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-6468
    - Vulnerability Description: Heap-based buffer overflow in Opera before 12.11 allows remote attackers to execute arbitrary code or cause a denial of service (memory corruption) via a long HTTP response.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2012-6551
    - Vulnerability Description: The default configuration of Apache ActiveMQ before 5.8.0 enables a sample web application, which allows remote attackers to cause a denial of service (broker resource consumption) via HTTP requests.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-0005
    - Vulnerability Description: The WCF Replace function in the Open Data (aka OData) protocol implementation in Microsoft .NET Framework 3.5, 3.5 SP1, 3.5.1, and 4, and the Management OData IIS Extension on Windows Server 2012, allows remote attackers to cause a denial of service (resource consumption and daemon restart) via crafted values in HTTP requests, aka "Replace Denial of Service Vulnerability."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-0176
    - Vulnerability Description: The publickey_from_privatekey function in libssh before 0.5.4, when no algorithm is matched during negotiations, allows remote attackers to cause a denial of service (NULL pointer dereference and crash) via a "Client: Diffie-Hellman Key Exchange Init" packet.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-0183
    - Vulnerability Description: multipart/parser.rb in Rack 1.3.x before 1.3.8 and 1.4.x before 1.4.3 allows remote attackers to cause a denial of service (memory consumption and out-of-memory error) via a long string in a Multipart HTTP packet.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-0230
    - Vulnerability Description: Stack-based buffer overflow in the ExecuteSoapAction function in the SOAPAction handler in the HTTP service in MiniUPnP MiniUPnPd 1.0 allows remote attackers to execute arbitrary code via a long quoted method.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-0270
    - Vulnerability Description: OpenStack Keystone Grizzly before 2013.1, Folsom, and possibly earlier allows remote attackers to cause a denial of service (CPU and memory consumption) via a large HTTP request, as demonstrated by a long tenant_name when requesting a token.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-0486
    - Vulnerability Description: Memory leak in the HTTP server in IBM Domino 8.5.x allows remote attackers to cause a denial of service (memory consumption and daemon crash) via GET requests, aka SPR KLYH92NKZY.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-0494
    - Vulnerability Description: IBM Sterling B2B Integrator 5.0 and 5.1 allows remote attackers to cause a denial of service (memory and CPU consumption) via a crafted HTTP (1) Range or (2) Request-Range header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-0532
    - Vulnerability Description: Cross-site request forgery (CSRF) vulnerability in IBM Security AppScan Enterprise 5.6 and 8.x before 8.7 and IBM Rational Policy Tester 5.6 and 8.x before 8.5.0.4 allows remote attackers to hijack the authentication of arbitrary users for requests that cause a denial of service via malformed HTTP data.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-0548
    - Vulnerability Description: Multiple cross-site scripting (XSS) vulnerabilities in the Basic Services component in IBM Tivoli Monitoring (ITM) 6.2.0 through FP3, 6.2.1 through FP4, 6.2.2 through FP9, and 6.2.3 before FP3, as used in IBM Application Manager for Smart Business (formerly Tivoli Foundations Application Manager) 1.2.1 before 1.2.1.0-TIV-IAMSB-FP0004 and other products, allow remote attackers to inject arbitrary web script or HTML via unspecified vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-0551
    - Vulnerability Description: The Basic Services component in IBM Tivoli Monitoring (ITM) 6.2.0 through FP3, 6.2.1 through FP4, 6.2.2 through FP9, and 6.2.3 before FP3, as used in IBM Application Manager for Smart Business (formerly Tivoli Foundations Application Manager) 1.2.1 before 1.2.1.0-TIV-IAMSB-FP0004 and other products, allows remote attackers to cause a denial of service (abend) via a crafted URL.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-0658
    - Vulnerability Description: Heap-based buffer overflow in RFManagerService.exe in Schneider Electric Accutech Manager 2.00.1 and earlier allows remote attackers to execute arbitrary code via a crafted HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-0664
    - Vulnerability Description: The FactoryCast service on the Schneider Electric Quantum 140NOE77111 and 140NWM10000, M340 BMXNOE0110x, and Premium TSXETY5103 PLC modules allows remote authenticated users to send Modbus messages, and consequently execute arbitrary code, by embedding these messages in SOAP HTTP POST requests.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-0669
    - Vulnerability Description: The HMI web application in Siemens WinCC (TIA Portal) 11 allows remote authenticated users to cause a denial of service (daemon crash) via a crafted HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-0680
    - Vulnerability Description: Stack-based buffer overflow in the web server in Cogent Real-Time Systems Cogent DataHub before 7.3.0, OPC DataHub before 6.4.22, Cascade DataHub before 6.4.22 on Windows, and DataHub QuickTrend before 7.3.0 allows remote attackers to cause a denial of service (daemon crash) or possibly execute arbitrary code via a long HTTP header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-0686
    - Vulnerability Description: Invensys Wonderware Information Server (WIS) 4.0 SP1SP1, 4.5- Portal, and 5.0- Portal allows remote attackers to read arbitrary files, send HTTP requests to intranet servers, or cause a denial of service (CPU and memory consumption) via an XML document containing an external entity declaration in conjunction with an entity reference, related to an XML External Entity (XXE) issue.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-0936
    - Vulnerability Description: Cross-site scripting (XSS) vulnerability in EMC Smarts IP Manager, Smarts Service Assurance Manager, Smarts Server Manager, Smarts VoIP Availability Manager, Smarts Network Protocol Manager, and Smarts MPLS Manager before 9.2 allows remote attackers to inject arbitrary web script or HTML via a crafted URL.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-1100
    - Vulnerability Description: The HTTP server in Cisco IOS on Catalyst switches does not properly handle TCP socket events, which allows remote attackers to cause a denial of service (device crash) via crafted packets on TCP port (1) 80 or (2) 443, aka Bug ID CSCuc53853.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-1122
    - Vulnerability Description: Cisco NX-OS on the Nexus 7000, when a certain Overlay Transport Virtualization (OTV) configuration is used, allows remote attackers to cause a denial of service (M1-Series module reload) via crafted packets, aka Bug ID CSCud15673.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-1146
    - Vulnerability Description: The Smart Install client functionality in Cisco IOS 12.2 and 15.0 through 15.3 on Catalyst switches allows remote attackers to cause a denial of service (device reload) via crafted image list parameters in Smart Install packets, aka Bug ID CSCub55790.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-1154
    - Vulnerability Description: The Cisco Small Business 200 Series Smart Switch 1.2.7.76 and earlier, Small Business 300 Series Managed Switch 1.2.7.76 and earlier, and Small Business 500 Series Stackable Managed Switch 1.2.7.76 and earlier allow remote attackers to cause a denial of service (SSL/TLS layer outage) via malformed (1) SSH or (2) SSL packets, aka Bug ID CSCua30246.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-1166
    - Vulnerability Description: Cisco IOS XE 3.2 through 3.4 before 3.4.5S, and 3.5 through 3.7 before 3.7.1S, on 1000 series Aggregation Services Routers (ASR), when VRF-aware NAT and SIP ALG are enabled, allows remote attackers to cause a denial of service (card reload) by sending many SIP packets, aka Bug ID CSCuc65609.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-1305
    - Vulnerability Description: HTTP.sys in Microsoft Windows 8, Windows Server 2012, and Windows RT allows remote attackers to cause a denial of service (infinite loop) via a crafted HTTP header, aka "HTTP.sys Denial of Service Vulnerability."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-1461
    - Vulnerability Description: The ExecuteSoapAction function in the SOAPAction handler in the HTTP service in MiniUPnP MiniUPnPd 1.0 allows remote attackers to cause a denial of service (NULL pointer dereference and service crash) via a SOAPAction header that lacks a # (pound sign) character, a different vulnerability than CVE-2013-0230.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-1462
    - Vulnerability Description: Integer signedness error in the ExecuteSoapAction function in the SOAPAction handler in the HTTP service in MiniUPnP MiniUPnPd 1.0 allows remote attackers to cause a denial of service (incorrect memory copy) via a SOAPAction header that lacks a " (double quote) character, a different vulnerability than CVE-2013-0230.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-1585
    - Vulnerability Description: epan/tvbuff.c in Wireshark 1.6.x before 1.6.13 and 1.8.x before 1.8.5 does not properly validate certain length values for the MS-MMC dissector, which allows remote attackers to cause a denial of service (application crash) via a malformed packet.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-1801
    - Vulnerability Description: The httparty gem 0.9.0 and earlier for Ruby does not properly restrict casts of string values, which might allow remote attackers to conduct object-injection attacks and execute arbitrary code, or cause a denial of service (memory and CPU consumption) by leveraging Action Pack support for YAML type conversion, a similar vulnerability to CVE-2013-0156.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-1845
    - Vulnerability Description: The mod_dav_svn Apache HTTPD server module in Subversion 1.6.x before 1.6.21 and 1.7.0 through 1.7.8 allows remote authenticated users to cause a denial of service (memory consumption) by (1) setting or (2) deleting a large number of properties for a file or directory.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-1846
    - Vulnerability Description: The mod_dav_svn Apache HTTPD server module in Subversion 1.6.x before 1.6.21 and 1.7.0 through 1.7.8 allows remote authenticated users to cause a denial of service (NULL pointer dereference and crash) via a LOCK on an activity URL.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-1847
    - Vulnerability Description: The mod_dav_svn Apache HTTPD server module in Subversion 1.6.0 through 1.6.20 and 1.7.0 through 1.7.8 allows remote attackers to cause a denial of service (NULL pointer dereference and crash) via an anonymous LOCK for a URL that does not exist.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-1849
    - Vulnerability Description: The mod_dav_svn Apache HTTPD server module in Subversion 1.6.x through 1.6.20 and 1.7.0 through 1.7.8 allows remote attackers to cause a denial of service (NULL pointer dereference and crash) via a PROPFIND request for an activity URL.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-1884
    - Vulnerability Description: The mod_dav_svn Apache HTTPD server module in Subversion 1.7.0 through 1.7.8 allows remote attackers to cause a denial of service (segmentation fault and crash) via a log REPORT request with an invalid limit, which triggers an access of an uninitialized variable.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-1896
    - Vulnerability Description: mod_dav.c in the Apache HTTP Server before 2.2.25 does not properly determine whether DAV is enabled for a URI, which allows remote attackers to cause a denial of service (segmentation fault) via a MERGE request in which the URI is configured for handling by the mod_dav_svn module, but a certain href attribute in XML data refers to a non-DAV URI.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-1912
    - Vulnerability Description: Buffer overflow in HAProxy 1.4 through 1.4.22 and 1.5-dev through 1.5-dev17, when HTTP keep-alive is enabled, using HTTP keywords in TCP inspection rules, and running with rewrite rules that appends to requests, allows remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via crafted pipelined HTTP requests that prevent request realignment from occurring.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-1915
    - Vulnerability Description: ModSecurity before 2.7.3 allows remote attackers to read arbitrary files, send HTTP requests to intranet servers, or cause a denial of service (CPU and memory consumption) via an XML external entity declaration in conjunction with an entity reference, aka an XML External Entity (XXE) vulnerability.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-2028
    - Vulnerability Description: The ngx_http_parse_chunked function in http/ngx_http_parse.c in nginx 1.3.9 through 1.4.0 allows remote attackers to cause a denial of service (crash) and execute arbitrary code via a chunked Transfer-Encoding request with a large chunk size, which triggers an integer signedness error and a stack-based buffer overflow.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-2070
    - Vulnerability Description: http/modules/ngx_http_proxy_module.c in nginx 1.1.4 through 1.2.8 and 1.3.0 through 1.4.0, when proxy_pass is used with untrusted HTTP servers, allows remote attackers to cause a denial of service (crash) and obtain sensitive information from worker process memory via a crafted proxy response, a similar vulnerability to CVE-2013-2028.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-2339
    - Vulnerability Description: HP Smart Zero Core 4.3 and 4.3.1 on the t410 All-in-One Smart Zero Client, t410 Smart Zero Client, t510 Flexible Thin Client, t5565z Smart Client, t610 Flexible Thin Client, and t610 PLUS Flexible Thin Client allows local users to obtain sensitive information, modify data, or cause a denial of service via unknown vectors.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-2371
    - Vulnerability Description: The Web API in the Statistics Server in TIBCO Spotfire Statistics Services 3.3.x before 3.3.1, 4.5.x before 4.5.1, and 5.0.x before 5.0.1 allows remote attackers to obtain sensitive information via an unspecified HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-2503
    - Vulnerability Description: Privoxy before 3.0.21 does not properly handle Proxy-Authenticate and Proxy-Authorization headers in the client-server data stream, which makes it easier for remote HTTP servers to spoof the intended proxy service via a 407 (aka Proxy Authentication Required) HTTP status code.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-2765
    - Vulnerability Description: The ModSecurity module before 2.7.4 for the Apache HTTP Server allows remote attackers to cause a denial of service (NULL pointer dereference, process crash, and disk consumption) via a POST request with a large body and a crafted Content-Type header.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-2784
    - Vulnerability Description: Triangle Research International (aka Tri) Nano-10 PLC devices with firmware before r81 use an incorrect algorithm for bounds checking of data in Modbus/TCP packets, which allows remote attackers to cause a denial of service (networking outage) via a crafted packet to TCP port 502.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-2796
    - Vulnerability Description: Schneider Electric Vijeo Citect 7.20 and earlier, CitectSCADA 7.20 and earlier, and PowerLogic SCADA 7.20 and earlier allow remote attackers to read arbitrary files, send HTTP requests to intranet servers, or cause a denial of service (CPU and memory consumption) via an XML document containing an external entity declaration in conjunction with an entity reference, related to an XML External Entity (XXE) issue.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-2873
    - Vulnerability Description: Use-after-free vulnerability in Google Chrome before 28.0.1500.71 allows remote attackers to cause a denial of service or possibly have unspecified other impact via vectors involving a 404 HTTP status code during the loading of resources.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-2960
    - Vulnerability Description: Buffer overflow in KDSMAIN in the Basic Services component in IBM Tivoli Monitoring (ITM) 6.2.0 through FP3, 6.2.1 through FP4, 6.2.2 through FP9, and 6.2.3 before FP3, as used in IBM Application Manager for Smart Business (formerly Tivoli Foundations Application Manager) 1.2.1 before 1.2.1.0-TIV-IAMSB-FP0004 and other products, allows remote attackers to cause a denial of service (segmentation fault) via a crafted http URL.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-2961
    - Vulnerability Description: The internal web server in the Basic Services component in IBM Tivoli Monitoring (ITM) 6.2.0 through FP3, 6.2.1 through FP4, 6.2.2 through FP9, and 6.2.3 before FP3, as used in IBM Application Manager for Smart Business (formerly Tivoli Foundations Application Manager) 1.2.1 before 1.2.1.0-TIV-IAMSB-FP0004 and other products, allows remote attackers to perform unspecified redirection of HTTP requests, and bypass the proxy-server configuration, via crafted HTTP traffic.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-3060
    - Vulnerability Description: The web console in Apache ActiveMQ before 5.8.0 does not require authentication, which allows remote attackers to obtain sensitive information or cause a denial of service via HTTP requests.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-3562
    - Vulnerability Description: Multiple integer signedness errors in the tvb_unmasked function in epan/dissectors/packet-websocket.c in the Websocket dissector in Wireshark 1.8.x before 1.8.7 allow remote attackers to cause a denial of service (application crash) via a malformed packet.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-3672
    - Vulnerability Description: The mm_decode_inter function in mmvideo.c in libavcodec in FFmpeg before 1.2.1 does not validate the relationship between a horizontal coordinate and a width value, which allows remote attackers to cause a denial of service (out-of-bounds array access and application crash) via crafted American Laser Games (ALG) MM Video data.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-3724
    - Vulnerability Description: The mk_request_header_process function in mk_request.c in Monkey 1.1.1 allows remote attackers to cause a denial of service (thread crash and service outage) via a '\0' character in an HTTP request.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-3735
    - Vulnerability Description: ** DISPUTED ** The Zend Engine in PHP before 5.4.16 RC1, and 5.5.0 before RC2, does not properly determine whether a parser error occurred, which allows context-dependent attackers to cause a denial of service (memory consumption and application crash) via a crafted function definition, as demonstrated by an attack within a shared web-hosting environment.  NOTE: the vendor's http://php.net/security-note.php page says "for critical security situations you should be using OS-level security by running multiple web servers each as their own user id."
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-3925
    - Vulnerability Description: Atlassian Crowd 2.5.x before 2.5.4, 2.6.x before 2.6.3, 2.3.8, and 2.4.9 allows remote attackers to read arbitrary files and send HTTP requests to intranet servers via a request to (1) /services/2 or (2) services/latest with a DTD containing an XML external entity declaration in conjunction with an entity reference.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-4081
    - Vulnerability Description: The http_payload_subdissector function in epan/dissectors/packet-http.c in the HTTP dissector in Wireshark 1.6.x before 1.6.16 and 1.8.x before 1.8.8 does not properly determine when to use a recursive approach, which allows remote attackers to cause a denial of service (stack consumption) via a crafted packet.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-4131
    - Vulnerability Description: The mod_dav_svn Apache HTTPD server module in Subversion 1.7.0 through 1.7.10 and 1.8.x before 1.8.1 allows remote authenticated users to cause a denial of service (assertion failure or out-of-bounds read) via a certain (1) COPY, (2) DELETE, or (3) MOVE request against a revision root.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-4687
    - Vulnerability Description: flowd in Juniper Junos 10.4 before 10.4S14, 11.2 and 11.4 before 11.4R6-S2, and 12.1 before 12.1R6 on SRX devices, when certain Application Layer Gateways (ALGs) are enabled, allows remote attackers to cause a denial of service (daemon crash) via crafted TCP packets, aka PRs 727980, 806269, and 835593.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-4688
    - Vulnerability Description: flowd in Juniper Junos 10.4 before 10.4R11 on SRX devices, when the MSRPC Application Layer Gateway (ALG) is enabled, allows remote attackers to cause a denial of service (daemon crash) via crafted MSRPC requests, aka PR 772834.
  </vulnerability>

  
  <vulnerability>
    - Associated with the following service ID: 
    - Vulnerability from the following database: MITRE CVE
    - Vulnerability ID: CVE-2013-4890
    - Vulnerability Description: The DMCRUIS/0.1 web server on the Samsung PS50C7700 TV allows remote attackers to cause a denial of service (daemon crash) via a long URI to TCP port 5600.
  </vulnerability>

  
</vulnerabilities>
