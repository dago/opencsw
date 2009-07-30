--- sendmail-8.14.3.orig/devtools/M4/depend/CC-M.m4	1999-05-28 00:03:28.000000000 +0200
+++ sendmail-8.14.3/devtools/M4/depend/CC-M.m4	2009-07-30 17:49:02.234202786 +0200
@@ -3,6 +3,6 @@
 	@mv Makefile Makefile.old
 	@sed -e '/^# Do not edit or remove this line or anything below it.$$/,$$d' < Makefile.old > Makefile
 	@echo "# Do not edit or remove this line or anything below it." >> Makefile
-	${CC} -M ${COPTS} ${SRCS} >> Makefile
+	${CC} -xM ${COPTS} ${SRCS} >> Makefile
 
 #	End of $RCSfile: CC-M.m4,v $
