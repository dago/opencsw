--- /shared/optparser.c	Mon Feb  7 19:06:36 2011
+++ /shared/optparser.c	Mon Feb  7 19:00:11 2011
@@ -439,7 +439,7 @@
 
     { "ReportHostname", NULL, 0, TYPE_STRING, NULL, -1, NULL, 0, OPT_MILTER, "When AddHeader is in use, this option allows to arbitrary set the reported\nhostname. This may be desirable in order to avoid leaking internal names.\nIf unset the real machine name is used.", "my.mail.server.name" },
 
-    { "VirusAction", NULL, 0, TYPE_STRING, NULL, -1, NULL, 0, OPT_MILTER, "Execute a command when an infected message is processed.\nThe following parameters are passed to the invoked program in this order:\nvirus name, queue id, sender, destination, subject, message id, message date.\nNote #1: this requires MTA macroes to be available (see LogInfected below)\nNote #2: the process is invoked in the context of clamav-milter\nNote #3: clamav-milter will wait for the process to exit. Be quick or fork to\navoid unnecessary delays in email delievery", "/usr/local/bin/my_infected_message_handler" },
+    { "VirusAction", NULL, 0, TYPE_STRING, NULL, -1, NULL, 0, OPT_MILTER, "Execute a command when an infected message is processed.\nThe following parameters are passed to the invoked program in this order:\nvirus name, queue id, sender, destination, subject, message id, message date.\nNote #1: this requires MTA macroes to be available (see LogInfected below)\nNote #2: the process is invoked in the context of clamav-milter\nNote #3: clamav-milter will wait for the process to exit. Be quick or fork to\navoid unnecessary delays in email delievery", "/opt/csw/bin/my_infected_message_handler" },
 
     { "Chroot", NULL, 0, TYPE_STRING, NULL, -1, NULL, 0, OPT_MILTER, "Chroot to the specified directory.\nChrooting is performed just after reading the config file and before\ndropping privileges.", "/newroot" },

