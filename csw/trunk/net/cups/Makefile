GARNAME = cups
GARVERSION = 1.2.2
CATEGORIES = net

#DESCRIPTION = The Common UNIX Printing System
define BLURB
  CUPS provides a portable printing layer for UNIX(R)-based operating
  systems.  It is developed and maintained by Easy Software Products to
  promote a standard printing solution and is the standard printing system
  in MacOS(R) X and most Linux(R) distributions.
endef

MASTER_SITES = http://ftp.easysw.com/pub/cups/1.2.2/
DISTFILES  = cups-$(GARVERSION)-source.tar.bz2
DISTFILES += $(call admfiles,CSWlibcups,depend prototype)
DISTFILES += $(call admfiles,CSWcupsd,depend prototype postinstall preremove \
	postremove)
DISTFILES += $(call admfiles,CSWcupsclient,depend prototype)
DISTFILES += $(call admfiles,CSWcupsdoc,depend prototype)
DISTFILES += $(call admfiles,CSWcupsdev,depend prototype)
DISTFILES += $(call admfiles,CSWcups,depend prototype)

DISTFILES += i.smfyes i.smfno space checkinstall

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

#WORKSRC ?= $(WORKDIR)/cups-$(GARVERSION)

# Don't run tests (at least for now); there are some LD_LIBRARY_PATH issues
TEST_TARGET = 

include ../category.mk

post-install:
#	(cd $(DESTDIR)$(prefix)/sbin; \
#	mv exim-$(GARVERSION) exim; \
#	/usr/ccs/bin/strip $(BINS); \
#	/usr/ccs/bin/mcs -d $(BINS))
	(cd $(DESTDIR)$(prefix)/share; \
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
	fi \
	)
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
