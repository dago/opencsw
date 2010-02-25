--- pidgin-2.6.6.orig/libpurple/plugin.c	2010-02-16 10:34:06.000000000 +0100
+++ pidgin-2.6.6/libpurple/plugin.c	2010-02-25 12:01:40.545624295 +0100
@@ -876,7 +876,7 @@
 		 * it keeps all the plugins open, meaning that valgrind is able to
 		 * resolve symbol names in leak traces from plugins.
 		 */
-		if (!g_getenv("PURPLE_LEAKCHECK_HELP") && !RUNNING_ON_VALGRIND)
+		if (!g_getenv("PURPLE_LEAKCHECK_HELP"))
 		{
 			if (plugin->handle != NULL)
 				g_module_close(plugin->handle);
