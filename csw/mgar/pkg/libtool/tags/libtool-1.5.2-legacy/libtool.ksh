#!/bin/ksh

# Wrapper for libtool, so that it auto-adjusts to whether you
# are using gcc, or Sun CC.
# libtool itself SHOULD do this. except it doesnt :-/
#
# It tries to base its choice on what environment vars are set to.
# Otherwise, it defaults to Sun CC if installed, or falls back
# to gcc if all else fails.

case CC in 
	gcc)
		LIBTOOL=libtool.gcc
	;;
	cc)
		LIBTOOL=libtool.cc
	;;
esac

case CXX in 
	g++)
		LIBTOOL=libtool.gcc
	;;
	CC)
		LIBTOOL=libtool.cc
	;;
esac

if [[ "$LIBTOOL" = "" ]] ; then
	case "$*" in
	*" "gcc" "*)
	 	LIBTOOL=libtool.gcc
	;;
	esac
fi

# Hmm. No compiler specified. Try to guess which one to use.
# Although this shouldnt really get called
if [[ "$LIBTOOL" = "" ]] ; then
	if [[ -x /opt/SUNWspro/bin/cc ]] ; then
		LIBTOOL=libtool.cc
	else
		LIBTOOL=libtool.gcc
	fi
fi

exec /opt/csw/bin/$LIBTOOL "$@"
