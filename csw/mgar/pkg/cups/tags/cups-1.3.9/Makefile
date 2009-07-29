GARNAME = cups
GARVERSION = 1.3.9
CATEGORIES = net

define BLURB
  CUPS provides a portable printing layer for UNIX(R)-based operating
  systems.  It is developed and maintained by Easy Software Products to
  promote a standard printing solution and is the standard printing system
  in MacOS(R) X and most Linux(R) distributions.
endef

# These are the source mirrors published on the CUPS home-page.
CUPS_MIRRORS = http://ftp.easysw.com/pub
CUPS_MIRRORS += ftp://ftp2.easysw.com/pub
CUPS_MIRRORS += ftp://ftp3.easysw.com/pub
CUPS_MIRRORS += http://www.nu6.org/_/mirror/ftp.easysw.com/pub
CUPS_MIRRORS += http://ftp.funet.fi/pub/mirrors/ftp.easysw.com/pub
CUPS_MIRRORS += ftp://ftp.funet.fi/pub/mirrors/ftp.easysw.com/pub
CUPS_MIRRORS += http://ftp.rz.tu-bs.de/pub/mirror/ftp.easysw.com/ftp/pub
# Complete the mirror paths by adding /cups/x.y.z/ at the end.
FULL_MIRRORS = $(foreach S,$(CUPS_MIRRORS),$(S)/$(GARNAME)/$(GARVERSION)/)
MASTER_SITES += $(FULL_MIRRORS)

DISTFILES  = cups-$(GARVERSION)-source.tar.bz2
DISTFILES += $(call admfiles,CSWlibcups,depend prototype)
DISTFILES += $(call admfiles,CSWcupsd,depend prototype postinstall preremove \
	postremove)
DISTFILES += $(call admfiles,CSWcupsclient,depend prototype)
DISTFILES += $(call admfiles,CSWcupsdoc,depend prototype)
DISTFILES += $(call admfiles,CSWcupsdev,depend prototype)
DISTFILES += $(call admfiles,CSWcups,depend prototype)

DISTFILES += i.smfyes i.smfno space checkinstall

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = cups-(\d+(?:\.\d+)*)-source.tar.bz2

LD_OPTIONS = -R/opt/csw/lib/\$$ISALIST -R/opt/csw/lib

CONFIGURE_ARGS = $(DIRPATHS)

# This is a hack that's needed, because configure (Makedefs) will otherwise
# plase -ltiff, etc. first and -L/opt/csw/lib afterwards, thus being unable
# to find any of the image libraries.
# Fortunately, configure honors values already in $DSOFLAGS, so we can use
# that to make sure -L/opt/csw/lib is the first argument passed to ld.
DSOFLAGS = -L/opt/csw/lib
export DSOFLAGS

# For some reason, the CUPS guys have decided to use DSTROOT for what
# everybody else calls DESTDIR.
DSTROOT = $(DESTDIR)
export DSTROOT

# Don't run tests (at least for now); there are some LD_LIBRARY_PATH issues
TEST_TARGET = 

SPKG_SOURCEURL = http://www.cups.org/

include gar/category.mk

PRIVATE_CUPS_INC = $(DESTDIR)$(includedir)/cups

post-configure:
	(test -d $(PRIVATE_CUPS_INC) || mkdir -p $(PRIVATE_CUPS_INC); \
	cd $(WORKSRC)/cups; \
	cp -p adminutil.h array.h cups.h dir.h file.h http.h i18n.h ipp.h \
		language.h md5.h ppd.h transcode.h $(PRIVATE_CUPS_INC); \
	cd ../filter; \
	cp -p image.h raster.h $(PRIVATE_CUPS_INC))

post-install:
	(test -d $(DESTDIR)$(prefix)/share || \
	mkdir $(DESTDIR)$(prefix)/share; \
	cd $(DESTDIR)$(prefix)/share; \
	if [ ! -d locale ]; then \
		test -d ../lib/locale && mv ../lib/locale .; \
		cd locale; \
		for i in *; do \
			echo "Processing $$i..."; \
			cd $$i; \
			mkdir LC_MESSAGES; \
			mv cups*.po LC_MESSAGES; \
			cd ..; \
		done \
	fi)
	(cd $(DESTDIR); \
	if [ -d usr/share ]; then \
		mv usr/share/* ./$(prefix)/share; \
		rmdir -p usr/share; \
	fi)
	(cd $(DESTDIR)$(prefix)/etc/cups; \
	for i in cupsd.conf; do \
		if [ -r "$$i" ]; then \
			echo "$$i -> $$i.CSW"; \
			mv "$$i" "$$i.CSW";	\
		fi \
	done)
	files/create_rc.d.sh $(DESTDIR)
	mkdir -p $(DESTDIR)$(prefix)/var/svc/manifest/application/print
	cp -p files/cups.xml  $(DESTDIR)$(prefix)/var/svc/manifest/application/print
	mkdir -p $(DESTDIR)$(prefix)/lib/svc/method
	cp -p files/cswcups \
		$(DESTDIR)$(prefix)/lib/svc/method/svc-cups
