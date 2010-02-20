#!/bin/ksh -p
# 
# $Id$

# pkgtrans leaves a directory in /var/tmp/aaXXXXXXX even after clean quit.
# Emulating pkgtrans behaviour, for "pkgtrans src destdir pkgname".  Except
# that the pkgname arg is ignored, and only the first pkg is processed.

custom_pkgtrans(){
	if [[ ! -d $2 ]] ; then
		print ERROR: $2 is not a directory >/dev/fd/2
		return 1
	fi
	hdrblks=`(dd if=$1 skip=1 2>/dev/null| cpio -i -t  >/dev/null) 2>&1 |
		nawk '{print $1; exit;}'`

	## print initial hdrblks=$hdrblks

	hdrblks=$(($hdrblks + 1))
	mkdir $2/$3 || return 1

	dd if=$1 skip=$hdrblks 2>/dev/null | (cd $2/$3 ; cpio -ivdm)
	# on fail, SOMETIMES cpio returns 1, but sometimes it returns 0!!
	if [[ ! -d $2/$3/install ]] ; then
		print retrying extract with different archive offset...
		# no, I can't tell in advance why/when the prev fails
		hdrblks=$(($hdrblks + 1))
		dd if=$1 skip=$hdrblks 2>/dev/null| (cd $2/$3 ; cpio -ivdm)
	fi
}
