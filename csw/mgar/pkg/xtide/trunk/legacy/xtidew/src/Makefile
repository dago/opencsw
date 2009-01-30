###############################################################################
#
# FILE:		Makefile
#
# DESCRIPTION:	Control file for the XTIDE_WVS src directory.
#		This is the world vector shoreline data file used by the XTIDE
#		package.  Installing this large database allows the shoreline
#		to be drawn on the world map used to locate harmonic tide data
#		locations.
#
# PACKAGE:      CSWxtidew
#
# REVISION:     02-05-08
#
# NOTES:	* Set the WVS variable to the current world vector shoreline
#		  data file name.
#
#		* INSTALL_ROOT controls the location of the installation.
#
#		* Files at:  ftp://www.flaterco.com/xtide/
#
# REQMTS:       * The CJSA custom install(1M) utility in ${HOME}/bin
#               * The CJSA custom   unpak(1M) utility in ${HOME}/bin
#
###############################################################################

WVSVER	= 1.0

WVSDATA = wvs.tar.bz2

WVS	= xtidew-$(WVSVER).tar.bz2

LIBDIR	= $(INSTALL_ROOT)/opt/csw/share/xtide/wvs

help:
	@echo "---------------------------------------------------------------"
	@echo "World Vector Shorline Data Ver:  $(WVSVER)"
	@echo "---------------------------------------------------------------"
	@echo "make get        download the $(WVSDATA) file"
	@echo ""
	@echo "make unpack     extract all files from $(WVS)"
	@echo ""
	@echo "make install    install the world vector shoreline files"
	@echo ""
	@echo "make clean      remove previous copies of files and cswstage"
	@echo "---------------------------------------------------------------"


get:
	@rm -rf $(WVSDATA).PREV
	@if [ -f $(WVSDATA) ] ; then \
	    mv $(WVSDATA) $(WVSDATA).PREV ; \
	fi
	wget ftp://ftp.flaterco.com/xtide/$(WVSDATA)
	mv $(WVSDATA) $(WVS)

unpack unpak: $(WVS)
	unpak $(WVS)

install: $(WVS)
	install -d -o root -g bin -m 755 $(LIBDIR)
	unpak $(WVS)
	install -o root -g bin -m 644 wvs*.dat $(LIBDIR)
	rm -f wvs*.dat

clean:
	rm -rf *.PREV wvs*.dat cswstage
