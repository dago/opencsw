###############################################################################
#
# FILE:		Makefile
#
# DESCRIPTION:	Control file for the XTIDEH src directory.
#		These are the harmonics data files used by the XTIDE package.
#
# PACKAGE:      CSWxtideh
#
# REVISION:     02-05-08
#
# NOTES:	* Set the HARVER variable to the current harmonics file date.
#
#		* Am using CJSA custom install(1M) utility in ${HOME}/bin.
#
#		* INSTALL_ROOT controls the location of the installation.
#
#		* Files at:  http://www.flaterco.com/xtide/files.html
#
#		* Version 1 harmonics used with xtide <= 2.7
#		  Version 2 harmonics used with xtide >= 2.8
#
# REQMTS:       * The CJSA custom install(1M) utility in ${HOME}/bin
#               * The CJSA custom   unpak(1M) utility in ${HOME}/bin
#
###############################################################################

BOILER	= harmonics_boilerplate.txt

HARVER	= 20071228

HARMON1	= harmonics-dwf-$(HARVER)-free.tcd
HARMON2	= harmonics-dwf-$(HARVER)-nonfree.tcd

HAR1	= harmonics-free.tcd
HAR2	= harmonics-nonfree.tcd

HARTAR	= xtideh-$(HARVER).tar

HARCH	= $(HARTAR).gz

LIBDIR	= $(INSTALL_ROOT)/opt/csw/share/xtide

help:
	@echo "---------------------------------------------------------------"
	@echo "Harmonics Ver:  $(HARVER)"
	@echo "---------------------------------------------------------------"
	@echo "make get        download the harmonics.tcd & boilerplate files"
	@echo ""
	@echo "make install    install the harmonics.tcd file"
	@echo ""
	@echo "make pack       tar up and gzip the harmonics source code"
	@echo ""
	@echo "make unpack     extract source code from gzipped tarball"
	@echo ""
	@echo "make clean      remove previous copies of files and cswstage"
	@echo ""
	@echo "make realclean  clean + rm harmonics.tcd & boilerplate files"
	@echo "---------------------------------------------------------------"


get:  get_bp get_hf

get_bp:
	@rm -rf boilerplate.txt.PREV harmonics.*.PREV
	@if [ -f boilerplate.txt ] ; then \
	    mv boilerplate.txt boilerplate.txt.PREV ; \
	fi
	wget http://www.flaterco.com/xtide/$(BOILER)
	mv $(BOILER) boilerplate.txt

get_hf:
	@if [ -f harmonics.tcd ] ; then \
	    mv harmonics.tcd harmonics.tcd.PREV ; \
	fi
	wget ftp://ftp.flaterco.com/xtide/$(HARMON1).bz2
	bunzip2 $(HARMON1).bz2
	wget ftp://ftp.flaterco.com/xtide/$(HARMON2).bz2
	bunzip2 $(HARMON2).bz2


install: boilerplate.txt $(HARMON1) $(HARMON2)
	install -d -o root -g bin -m 755 $(LIBDIR)
	install -c -o root -g bin -m 644 boilerplate.txt $(LIBDIR)
	install -c -o root -g bin -m 644 $(HARMON1)      $(LIBDIR)/$(HAR1)
	install -c -o root -g bin -m 644 $(HARMON2)      $(LIBDIR)/$(HAR2)

pack pak tar: boilerplate.txt $(HARMON1) $(HARMON2)
	@if [ -f $(HARTAR) ] ; then \
	    echo "Cannot pack: $(HARTAR) exists." ; \
	elif [ -f $(HARCH) ] ; then \
	    echo "Cannot pack: $(HARCH) exists." ; \
	else \
	    tar cvf $(HARTAR) boilerplate.txt $(HARMON1) $(HARMON2) ; \
	    gzip $(HARTAR) ; \
	fi

unpack unpak: $(HARCH)
	unpak $(HARCH)

clean:
	rm -rf *.PREV cswstage

realclean: clean $(HARCH)
	rm -rf boilerplate.txt $(HARMON1) $(HARMON2)
