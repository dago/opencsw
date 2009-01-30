###############################################################################
#
# FILE:		Makefile
#
# DESCRIPTION:	Control file for the SPIDER src directory.
#
# PACKAGE:      CSWspider
#
# REVISION:     10-24-04
#
# NOTES:	* Set the SVER variable to the current spider version number.
#
# REQMTS:	* The CJSA custom   unpak(1M) utility in ${HOME}/bin
#
###############################################################################

SVER	= 1.1.1

SDIR	= spider.$(SVER)

STAR	= spider-$(SVER).tar

SARCH	= $(STAR).gz

help:
	@echo "---------------------------------------------------------------"
	@echo "Spider Ver:      $(SVER)"
	@echo "---------------------------------------------------------------"
	@echo "make pack       tar up and gzip the source code directory"
	@echo ""
	@echo "make unpack     extract source code from gzipped tarball"
	@echo ""
	@echo ""
	@echo "make clean      remove the source code directory"
	@echo "---------------------------------------------------------------"


pack tar: $(SDIR)
	@if [ -f $(STAR) ] ;  then mv $(STAR)  $(STAR).OLD ;  fi
	@if [ -f $(SARCH) ] ; then mv $(SARCH) $(SARCH).OLD ; fi
	tar cvf $(STAR) $(SDIR)
	gzip $(STAR)
	rm -rf $(STAR).OLD $(SARCH).OLD

unpack unpak:	$(SARCH)
	unpak $(SARCH)

clean:
	@if [ ! -f $(SARCH) ] ; then \
	    echo "You must first archive the source with:  make pack" ; \
	else \
	    rm -rf $(SDIR) ; \
	fi
