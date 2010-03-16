--- /etc/clamd.conf	2010-03-12 16:32:28.977878541 +0100
+++ /etc/clamd.conf	2010-03-12 16:32:23.707431670 +0100
@@ -5,7 +5,7 @@
 
 
 # Comment or remove the line below.
-Example
+#Example
 
 # Uncomment this option to enable logging.
 # LogFile must be writable for the user running daemon.
@@ -73,7 +73,7 @@
 
 # Path to a local socket file the daemon will listen on.
 # Default: disabled (must be specified by a user)
-#LocalSocket /tmp/clamd.socket
+LocalSocket /tmp/clamd.socket
 
 # Sets the group ownership on the unix socket.
 # Default: disabled (the primary group of the user running clamd)
