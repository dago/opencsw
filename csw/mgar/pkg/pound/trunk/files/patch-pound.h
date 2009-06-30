*** Pound-1.10.orig/pound.h	Wed Feb  1 12:22:03 2006
--- Pound-1.10/pound.h	Tue Jun 30 14:32:19 2009
***************
*** 278,288 ****
  #define GLOB_SESS   15
  
  #ifndef F_CONF
! #define F_CONF  "/usr/local/etc/pound.cfg"
  #endif
  
  #ifndef F_PID
! #define F_PID  "/var/run/pound.pid"
  #endif
  
  #define SERVER_TO   (server_to > 0? server_to: 5)
--- 278,288 ----
  #define GLOB_SESS   15
  
  #ifndef F_CONF
! #define F_CONF  "/opt/csw/etc/pound/pound.cfg"
  #endif
  
  #ifndef F_PID
! #define F_PID  "/var/opt/csw/run/pound.pid"
  #endif
  
  #define SERVER_TO   (server_to > 0? server_to: 5)
