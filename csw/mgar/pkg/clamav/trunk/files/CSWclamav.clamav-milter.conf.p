--- /etc/clamav-milter.conf  Mon Feb  7 19:09:08 2011
+++ /etc/clamav-milter.conf  Mon Feb  7 19:10:42 2011
@@ -3,7 +3,7 @@
 ##
 
 # Comment or remove the line below.
-Example
+#Example
 
 
 ##
@@ -201,7 +201,7 @@
 # Note #3: clamav-milter will wait for the process to exit. Be quick or fork to
 # avoid unnecessary delays in email delievery
 # Default: disabled
-#VirusAction /usr/local/bin/my_infected_message_handler
+#VirusAction /opt/csw/bin/my_infected_message_handler
 
 ##
 ## Logging options
