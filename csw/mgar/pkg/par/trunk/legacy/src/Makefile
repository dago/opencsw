###############################################################################
#
# FILE:		Makefile
#
# DESCRIPTION:	Control file for the PAR src directory.
#
# PACKAGE:      CSWpar
#
# REVISION:     10-28-04
#
# NOTES:	* Set the PVER variable to the current par version number.
#
#		* INSTALL_ROOT controls the location of the installation.
#
#		* Source is located at:    http://www.nicemice.net/par/
#
# REQMTS:	* The CJSA custom install(1M) utility in ${HOME}/bin
#		* The CJSA custom   unpak(1M) utility in ${HOME}/bin
#
###############################################################################

PVER	= 152
PVERS	= 1.52

PSOURCE	= Par$(PVER).tar.gz

PDIR	= par.$(PVERS)

PTAR	= par-$(PVERS).tar

PARCH	= $(PTAR).gz

help:
	@echo "---------------------------------------------------------------"
	@echo "Par Ver:      $(PVERS)"
	@echo "---------------------------------------------------------------"
	@echo "make get        download par source code"
	@echo ""
	@echo "make extract    extract source code from downloaded archive"
	@echo ""
	@echo ""
	@echo "make pack       tar up and gzip the source code directory"
	@echo ""
	@echo "make unpack     extract source code from gzipped tarball"
	@echo ""
	@echo ""
	@echo "make clean      remove the source code directory"
	@echo "---------------------------------------------------------------"


get:
	wget http://www.nicemice.net/par/$(PSOURCE)


extract: $(PSOURCE)
	unpak $(PSOURCE)
	mv Par*[0-9] $(PDIR)


pack pak tar: $(PDIR)
	@if [ -f $(PTAR) ] ; then \
	    echo "Cannot pack: $(PTAR) exists." ; \
	elif [ -f $(PARCH) ] ; then \
	    echo "Cannot pack: $(PARCH) exists." ; \
	else \
	    tar cvf $(PTAR) $(PDIR) ; \
	    gzip $(PTAR) ; \
	fi

unpack unpak:	$(PARCH)
	unpak $(PARCH)

clean:
	@if [ ! -f $(PARCH) ] ; then \
	    echo "You must first archive the source with:  make pack" ; \
	else \
	    rm -rf $(PSOURCE) $(PDIR) ; \
	fi
