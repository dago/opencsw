###############################################################################
#
# FILE:		Makefile
#
# DESCRIPTION:	Control file for the XTIDE src directory
#
# PACKAGE:      CSWxtide
#
# REVISION:     02-05-08
#
# NOTES:	* Set the XVER variable to the current xtide v ersion number
#		* Set the LVER variable to the current libtcd version number
#
#		* INSTALL_ROOT controls the location of the installation
#
# REQMTS:	* The CJSA custom install(1M) utility in ${HOME}/bin
#		* The CJSA custom   unpak(1M) utility in ${HOME}/bin
#
###############################################################################

XVER	= 2.10
LVER	= 2.2.3

XSOURCE	= xtide-$(XVER).tar.bz2
LSOURCE	= libtcd-$(LVER).tar.bz2

XSAVE	= $(XSOURCE)X
LSAVE	= $(LSOURCE)X

XDIR	= xtide-$(XVER)
LDIR	= libtcd-$(LVER)

XTAR	= xtide-$(XVER).tar

XARCH	= $(XTAR).gz

help:
	@echo "---------------------------------------------------------------"
	@echo "xtide ver: $(XVER)       libtcd ver: $(LVER)"
	@echo "---------------------------------------------------------------"
	@echo "make get        download xtide and libtcd source code"
	@echo ""
	@echo "make extract    extract source code from downloaded archives"
	@echo ""
	@echo "make links      create symbolic links to libtcd directory"
	@echo ""
	@echo "make pack       tar up and gzip the source code directory"
	@echo ""
	@echo "make unpack     extract source code from gzipped tarball"
	@echo ""
	@echo ""
	@echo "make clean      remove the source code directory"
	@echo "---------------------------------------------------------------"


get: getx getl

getx:
	wget ftp://ftp.flaterco.com/xtide/$(XSOURCE)

getl:
	wget ftp://ftp.flaterco.com/xtide/$(LSOURCE)


extract: extractx extractl

extractx: $(XSOURCE)
	unpak $(XSOURCE)
	mv $(XSOURCE) $(XSAVE)

extractl: $(LSOURCE)
	unpak $(LSOURCE)
	mv $(LSOURCE) $(LSAVE)


pack pak tar: $(LDIR) $(XDIR)
	@if [ -f $(XTAR) ] ; then \
	    echo "Cannot pack: $(XTAR) exists." ; \
	elif [ -f $(XARCH) ] ; then \
	    echo "Cannot pack: $(XARCH) exists." ; \
	else \
	    tar cvf $(XTAR) $(LDIR) $(XDIR) ; \
	    gzip $(XTAR) ; \
	fi

unpack unpak: $(XARCH)
	unpak $(XARCH)

links link:
	@rm -f xtide*[0-9]/libtcd xtide*[0-9]/tcd.h
	(cd xtide*[0-9] ; \
	ln -s ../libtcd*[0-9]/.libs libtcd)
	(cd xtide*[0-9] ; \
	ln -s ../libtcd*[0-9]/tcd.h tcd.h)

clean:
	@if [ ! -f $(XARCH) ] ; then \
	    echo "You must first archive the source with:  make pack" ; \
	else \
	    rm -rf $(XDIR) $(XSOURCE) $(XSAVE) $(LDIR) $(LSOURCE) $(LSAVE) ; \
	fi
