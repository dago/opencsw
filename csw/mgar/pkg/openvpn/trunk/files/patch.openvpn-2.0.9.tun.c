--- openvpn-2.0.9/tun.c	Wed Apr  5 15:29:24 2006
+++ 207/openvpn/tun.c	Wed May 20 23:10:36 2009
@@ -30,6 +30,12 @@
  * from VTun by Maxim Krasnyansky <max_mk@yahoo.com>.
  */
 
+/*
+ *  Modified by: Kazuyoshi <admin2@whiteboard.ne.jp>
+ *  Modified for supporting tap device for Solaris 
+ *  $Date: 2009/05/20 14:10:36 $, $Revision: 1.10.2.1 $
+ */
+
 #ifdef WIN32
 #include "config-win32.h"
 #else
@@ -49,6 +55,7 @@
 
 #ifdef TARGET_SOLARIS
 static void solaris_error_close (struct tuntap *tt, const struct env_set *es, const char *actual);
+#include <stropts.h>
 #endif
 
 bool
@@ -629,7 +636,12 @@
 			    );
 	}
       else
-	no_tap_ifconfig ();
+          openvpn_snprintf (command_line, sizeof (command_line),
+                            IFCONFIG_PATH " %s %s netmask %s broadcast + up",
+                            actual, 
+                            ifconfig_local,
+                            ifconfig_remote_netmask 
+                            );          
 
       msg (M_INFO, "%s", command_line);
       if (!system_check (command_line, es, 0, "Solaris ifconfig phase-2 failed"))
@@ -1186,14 +1198,17 @@
 void
 open_tun (const char *dev, const char *dev_type, const char *dev_node, bool ipv6, struct tuntap *tt)
 {
-  int if_fd, muxid, ppa = -1;
-  struct ifreq ifr;
+  int if_fd, ip_muxid, arp_muxid, arp_fd, ppa = -1;
+  struct lifreq ifr;
   const char *ptr;
-  const char *ip_node;
+  const char *ip_node, *arp_node;
   const char *dev_tuntap_type;
   int link_type;
   bool is_tun;
+  struct strioctl  strioc_if, strioc_ppa;
 
+  memset(&ifr, 0x0, sizeof(ifr));
+
   ipv6_support (ipv6, false, tt);
 
   if (tt->type == DEV_TYPE_NULL)
@@ -1213,9 +1228,10 @@
     }
   else if (tt->type == DEV_TYPE_TAP)
     {
-      ip_node = "/dev/ip";
+      ip_node = "/dev/udp";
       if (!dev_node)
 	dev_node = "/dev/tap";
+      arp_node = dev_node;
       dev_tuntap_type = "tap";
       link_type = I_PLINK; /* was: I_LINK */
       is_tun = false;
@@ -1242,7 +1258,11 @@
     msg (M_ERR, "Can't open %s", dev_node);
 
   /* Assign a new PPA and get its unit number. */
-  if ((ppa = ioctl (tt->fd, TUNNEWPPA, ppa)) < 0)
+  strioc_ppa.ic_cmd = TUNNEWPPA;
+  strioc_ppa.ic_timout = 0;
+  strioc_ppa.ic_len = sizeof(ppa);
+  strioc_ppa.ic_dp = (char *)&ppa;
+  if ((ppa = ioctl (tt->fd, I_STR, &strioc_ppa)) < 0)
     msg (M_ERR, "Can't assign new interface");
 
   if ((if_fd = open (dev_node, O_RDWR, 0)) < 0)
@@ -1251,27 +1271,85 @@
   if (ioctl (if_fd, I_PUSH, "ip") < 0)
     msg (M_ERR, "Can't push IP module");
 
-  /* Assign ppa according to the unit number returned by tun device */
-  if (ioctl (if_fd, IF_UNITSEL, (char *) &ppa) < 0)
-    msg (M_ERR, "Can't set PPA %d", ppa);
+  if (tt->type == DEV_TYPE_TUN) 
+    {
+	  /* Assign ppa according to the unit number returned by tun device */
+	  if (ioctl (if_fd, IF_UNITSEL, (char *) &ppa) < 0)
+	    msg (M_ERR, "Can't set PPA %d", ppa);
+    }
 
-  if ((muxid = ioctl (tt->ip_fd, link_type, if_fd)) < 0)
-    msg (M_ERR, "Can't link %s device to IP", dev_tuntap_type);
-
-  close (if_fd);
-
   tt->actual_name = (char *) malloc (32);
   check_malloc_return (tt->actual_name);
 
   openvpn_snprintf (tt->actual_name, 32, "%s%d", dev_tuntap_type, ppa);
 
+  if (tt->type == DEV_TYPE_TAP) 
+    {
+	  if (ioctl(if_fd, SIOCGLIFFLAGS, &ifr) < 0)
+	    msg (M_ERR, "Can't get flags\n");
+          strncpynt (ifr.lifr_name, tt->actual_name, sizeof (ifr.lifr_name));          
+	  ifr.lifr_ppa = ppa;
+	  /* Assign ppa according to the unit number returned by tun device */          
+	  if (ioctl (if_fd, SIOCSLIFNAME, &ifr) < 0)
+	    msg (M_ERR, "Can't set PPA %d", ppa);              
+	  if (ioctl(if_fd, SIOCGLIFFLAGS, &ifr) <0)
+	    msg (M_ERR, "Can't get flags\n");
+          /* Push arp module to if_fd */
+          if (ioctl (if_fd, I_PUSH, "arp") < 0)
+	    msg (M_ERR, "Can't push ARP module");
+
+          /* Pop any modules on the stream */
+          while (true)
+            {
+                 if (ioctl (tt->ip_fd, I_POP, NULL) < 0)
+                     break;
+            }
+          /* Push arp module to ip_fd */
+	  if (ioctl (tt->ip_fd, I_PUSH, "arp") < 0) 
+	    msg (M_ERR, "Can't push ARP module\n");
+
+	  /* Open arp_fd */
+	  if ((arp_fd = open (arp_node, O_RDWR, 0)) < 0)
+	    msg (M_ERR, "Can't open %s\n", arp_node);
+          /* Push arp module to arp_fd */          
+	  if (ioctl (arp_fd, I_PUSH, "arp") < 0)
+	    msg (M_ERR, "Can't push ARP module\n");
+
+          /* Set ifname to arp */
+	  strioc_if.ic_cmd = SIOCSLIFNAME;
+	  strioc_if.ic_timout = 0;
+	  strioc_if.ic_len = sizeof(ifr);
+	  strioc_if.ic_dp = (char *)&ifr;
+	  if (ioctl(arp_fd, I_STR, &strioc_if) < 0){
+	      msg (M_ERR, "Can't set ifname to arp\n");
+	  }
+   }
+
+  if ((ip_muxid = ioctl (tt->ip_fd, link_type, if_fd)) < 0)
+    msg (M_ERR, "Can't link %s device to IP", dev_tuntap_type);
+
+  if (tt->type == DEV_TYPE_TAP) {
+	  if ((arp_muxid = ioctl (tt->ip_fd, link_type, arp_fd)) < 0)
+	    msg (M_ERR, "Can't link %s device to ARP", dev_tuntap_type);
+	  close (arp_fd);
+  }
+
+  close (if_fd);
+
   CLEAR (ifr);
-  strncpynt (ifr.ifr_name, tt->actual_name, sizeof (ifr.ifr_name));
-  ifr.ifr_ip_muxid = muxid;
+  strncpynt (ifr.lifr_name, tt->actual_name, sizeof (ifr.lifr_name));
+  ifr.lifr_ip_muxid  = ip_muxid;
+  if (tt->type == DEV_TYPE_TAP) {
+	  ifr.lifr_arp_muxid = arp_muxid;
+  }
 
-  if (ioctl (tt->ip_fd, SIOCSIFMUXID, &ifr) < 0)
+  if (ioctl (tt->ip_fd, SIOCSLIFMUXID, &ifr) < 0)
     {
-      ioctl (tt->ip_fd, I_PUNLINK, muxid);
+      if (tt->type == DEV_TYPE_TAP) 
+        {
+	      ioctl (tt->ip_fd, I_PUNLINK , arp_muxid);
+        }
+      ioctl (tt->ip_fd, I_PUNLINK, ip_muxid);
       msg (M_ERR, "Can't set multiplexor id");
     }
 
@@ -1289,19 +1367,25 @@
     {
       if (tt->ip_fd >= 0)
 	{
-	  struct ifreq ifr;
+	  struct lifreq ifr;
 	  CLEAR (ifr);
-	  strncpynt (ifr.ifr_name, tt->actual_name, sizeof (ifr.ifr_name));
+	  strncpynt (ifr.lifr_name, tt->actual_name, sizeof (ifr.lifr_name));
 
-	  if (ioctl (tt->ip_fd, SIOCGIFFLAGS, &ifr) < 0)
+	  if (ioctl (tt->ip_fd, SIOCGLIFFLAGS, &ifr) < 0)
 	    msg (M_WARN | M_ERRNO, "Can't get iface flags");
 
-	  if (ioctl (tt->ip_fd, SIOCGIFMUXID, &ifr) < 0)
+	  if (ioctl (tt->ip_fd, SIOCGLIFMUXID, &ifr) < 0)
 	    msg (M_WARN | M_ERRNO, "Can't get multiplexor id");
 
-	  if (ioctl (tt->ip_fd, I_PUNLINK, ifr.ifr_ip_muxid) < 0)
-	    msg (M_WARN | M_ERRNO, "Can't unlink interface");
+	  if (tt->type == DEV_TYPE_TAP)
+            {
+		  if (ioctl (tt->ip_fd, I_PUNLINK, ifr.lifr_arp_muxid) < 0)
+		    msg (M_WARN | M_ERRNO, "Can't unlink interface(arp)");
+	    }
 
+	  if (ioctl (tt->ip_fd, I_PUNLINK, ifr.lifr_ip_muxid) < 0)
+	    msg (M_WARN | M_ERRNO, "Can't unlink interface(ip)");
+
 	  close (tt->ip_fd);
 	  tt->ip_fd = -1;
 	}
