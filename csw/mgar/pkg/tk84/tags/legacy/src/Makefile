###############################################################################
#
# FILE:		Makefile
#
# DESCRIPTION:	Control file for the TK src directory.  This is used to
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
	@echo "TK Version:  $(TVER)"
	@echo "---------------------------------------------------------------"
	@echo "make get      download the current TK source code"
	@echo ""
	@echo "make rename   rename downloaded source code file"
	@echo ""
	@echo "make unpack   unpack the TK source code"
	@echo ""
	@echo "make links     create symbolic links to current TCL source"
	@echo ""
	@echo "make clean    remove source working directory
	@echo "---------------------------------------------------------------"


# target get does not work until we can locate an unambiguous download site
# for the TK source

get tk TK:
	 wget \
	 http://prdownloads.sourceforge.net/tcl/tk$(TVER)-src.tar.gz

rename:
	mv tk$(TVER)-src.tar.gz TK.$(TVER)-src.tar.gz
	clear ; ls

unpack:	TK.$(TVER)-src.tar.gz
	unpak TK.$(TVER)-src.tar.gz

links link tcl tcl-link:
	rm -rf tcl*[0-9] tcl.h
	ln -s ../../tcl/src/tcl*[0-9] .
	ln -s ../../tcl/src/tcl*[0-9]/generic/tcl.h .

clean:
	rm -rf tk${TVER} tcl*
