--- ./ltmain.sh~	2006-04-24 11:47:24.000000000 -0400
+++ ./ltmain.sh	2006-05-01 18:58:23.996798000 -0400
@@ -388,7 +388,7 @@
 #####################################
 
 # Darwin sucks
-eval std_shrext=\"$shrext_cmds\"
+eval std_shrext=\"$shrext\"
 
 disable_libs=no
 
@@ -1413,7 +1413,7 @@
 	  continue
 	  ;;
 	shrext)
-  	  shrext_cmds="$arg"
+  	  shrext="$arg"
 	  prev=
 	  continue
 	  ;;
@@ -3095,7 +3095,7 @@
       case $outputname in
       lib*)
 	name=`$echo "X$outputname" | $Xsed -e 's/\.la$//' -e 's/^lib//'`
-	eval shared_ext=\"$shrext_cmds\"
+	eval shared_ext=\"$shrext\"
 	eval libname=\"$libname_spec\"
 	;;
       *)
@@ -3107,7 +3107,7 @@
 	if test "$need_lib_prefix" != no; then
 	  # Add the "lib" prefix for modules if required
 	  name=`$echo "X$outputname" | $Xsed -e 's/\.la$//'`
-	  eval shared_ext=\"$shrext_cmds\"
+	  eval shared_ext=\"$shrext\"
 	  eval libname=\"$libname_spec\"
 	else
 	  libname=`$echo "X$outputname" | $Xsed -e 's/\.la$//'`
@@ -3903,7 +3903,7 @@
 	fi
 
 	# Get the real and link names of the library.
-	eval shared_ext=\"$shrext_cmds\"
+	eval shared_ext=\"$shrext\"
 	eval library_names=\"$library_names_spec\"
 	set dummy $library_names
 	realname="$2"
