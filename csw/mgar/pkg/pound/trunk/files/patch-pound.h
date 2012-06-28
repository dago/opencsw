*** Pound-2.4.5.orig/pound.h	Mon Jun 29 17:53:58 2009
--- Pound-2.4.5/pound.h	Tue Jun 30 13:47:08 2009
***************
*** 271,281 ****
  #define MAXHEADERS  128
  
  #ifndef F_CONF
! #define F_CONF  "/usr/local/etc/pound.cfg"
  #endif
  
  #ifndef F_PID
! #define F_PID  "/var/run/pound.pid"
  #endif
  
  /* matcher chain */
--- 271,281 ----
  #define MAXHEADERS  128
  
  #ifndef F_CONF
! #define F_CONF  "/usr/local/etc/pound2/pound2.cfg"
  #endif
  
  #ifndef F_PID
! #define F_PID  "/var/opt/csw/run/pound2.pid"
  #endif
  
  /* matcher chain */
