###############################################################################
#
# FILE:		Makefile
#
# DESCRIPTION:	Control file for the UNClUTTER src directory.
#
# PACKAGE:      CSWunclutter
#
# REVISION:     02-05-07
#
# NOTES:	* Set the UVER variable to the current par version number.
#
#		* INSTALL_ROOT controls the location of the installation.
#
#		* Source is located at:    sourceforge.net
#
# REQMTS:	* The CJSA custom install(1M) utility in ${HOME}/bin
#		* The CJSA custom   unpak(1M) utility in ${HOME}/bin
#
###############################################################################

UVERS	= 1.09

UDIR	= unclutter-$(UVERS)

UTAR	= unclutter-$(UVERS).tar

UARCH	= $(UTAR).gz

help:
	@echo "---------------------------------------------------------------"
	@echo "Unclutter Ver:      $(UVERS)"
	@echo "---------------------------------------------------------------"
	@echo "make unpack     extract source code from gzipped tarball"
	@echo ""
	@echo ""
	@echo "make clean      remove the source code directory"
	@echo "---------------------------------------------------------------"


unpack unpak:	$(UARCH)
	unpak $(UARCH)

clean:
	@if [ ! -f $(UARCH) ] ; then \
	    echo "You must first archive the source" ; \
	else \
	    rm -rf $(UDIR) ; \
	fi
