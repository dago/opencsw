*** Pound-1.10.orig/config.c	Wed Feb  1 12:22:03 2006
--- Pound-1.10/config.c	Tue Jun 30 14:36:24 2009
***************
*** 230,239 ****
  
  static CODE facilitynames[] = {
      { "auth", LOG_AUTH },
-     { "authpriv", LOG_AUTHPRIV },
      { "cron", LOG_CRON },
      { "daemon", LOG_DAEMON },
-     { "ftp", LOG_FTP },
      { "kern", LOG_KERN },
      { "lpr", LOG_LPR },
      { "mail", LOG_MAIL },
--- 230,237 ----
