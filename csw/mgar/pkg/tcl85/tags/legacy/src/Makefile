###############################################################################
#
# FILE:		Makefile
#
# DESCRIPTION:	Control file for the TCL src directory.  This is used to
#		retrieve current source code for the specified package(s).
#
# REVISION:	04-27-08
#
# NOTES:	* Set TVER to the current version of the software.
#
###############################################################################

TVER=8.5.2


help:
	@echo "---------------------------------------------------------------"
	@echo "TCL Version:  $(TVER)"
	@echo "---------------------------------------------------------------"
	@echo "make get      download the current TCL source code"
	@echo ""
	@echo "make rename   rename downloaded source code file"
	@echo ""
	@echo "make unpack   unpack the TCL source code"
	@echo ""
	@echo "make clean    remove source working directory
	@echo "---------------------------------------------------------------"


# target get does not work until we can locate an unambiguous download site
# for the TCL source

get tcl TCL:
	 wget \
	 http://downloads.sourceforge.net/tcl/tcl$(TVER)-src.tar.gz

rename:
	mv tcl$(TVER)-src.tar.gz TCL.$(TVER)-src.tar.gz
	clear ; ls

unpack unpak:	TCL.$(TVER)-src.tar.gz
	unpak TCL.$(TVER)-src.tar.gz

clean:
	rm -rf tcl${TVER}
