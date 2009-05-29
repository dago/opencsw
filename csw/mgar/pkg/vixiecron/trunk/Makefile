# Copyright 2009 Google Inc.
# Distributed under the terms of the GNU General Public License v2
# $Header: $

GARNAME = vixiecron
GARVERSION = 3.0pl1
CATEGORIES = server

DESCRIPTION = Paul Vixie cron
define BLURB
  vixiecron is one of the most widely used cron implementations.

  This build includes patches from Debian.  It supports /etc/cron.d directory,
  which can be used to conveniently set up cron jobs by placing files. It also
  supports a slash notation: */5 denotes "Every five minutes".
endef

# TODO:
#  - Improve man page locations. The original manpage install script
#    looks retarded.

MASTER_SITES  = http://ftp.de.debian.org/debian/pool/main/c/cron/
DISTFILES  = cron_$(GARVERSION).orig.tar.gz
DISTFILES += cron_$(GARVERSION)-105.diff.gz
DISTFILES += CSWvixiecron.preinstall
DISTFILES += CSWvixiecron.postinstall
DISTFILES += CSWvixiecron.postremove
DISTFILES += csw$(GARNAME)
DISTFILES += crontab.CSW
DISTFILES += run-crons-0.3.2

WORKSRC = $(WORKDIR)/cron-$(GARVERSION).orig

SPKG_CLASSES = none cswcpsampleconf cswinitsmf
REQUIRED_PKGS = CSWcswclassutils

PROTOTYPE_FILTER  = awk ' \
    $$$$3 ~ /\/init.d\/cswvixiecron$$$$/ { $$$$2 = "cswinitsmf" } \
    $$$$3 ~ /\/crontab\.CSW$$$$/ { $$$$2 = "cswcpsampleconf" } \
    $$$$3 ~ /\/opt\/csw\/bin\/crontab$$$$/ { $$$$4 = "1755" } \
    { print }'

PATCHFILES = cron_$(GARVERSION)-105.diff.gz \
             gar-$(GARNAME)_$(GARVERSION).patch

TEST_SCRIPTS =
CONFIGURE_SCRIPTS =
EXTRA_CFLAGS = -DDEBUGGING=0 -DPOSIX -DDEBIAN

pre-install-modulated:
	ginstall -d $(DESTDIR)/opt/csw
	ginstall -d $(DESTDIR)/opt/csw/bin
	ginstall -d $(DESTDIR)/opt/csw/sbin
	ginstall -d $(DESTDIR)/opt/csw/share/man/cat5
	ginstall -d $(DESTDIR)/opt/csw/share/man/cat8
	@$(MAKECOOKIE)

post-install-modulated:
	ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall $(FILEDIR)/csw$(GARNAME) \
		$(DESTDIR)/etc/opt/csw/init.d/csw$(GARNAME)
	ginstall -d $(DESTDIR)/etc
	ginstall -m 750 $(FILEDIR)/crontab.CSW \
		$(DESTDIR)/etc/crontab.CSW
	ginstall -m 755 $(FILEDIR)/run-crons-0.3.2 \
		$(DESTDIR)/opt/csw/sbin/run-crons
	for base in hourly daily weekly monthly; do \
		ginstall -d $(DESTDIR)/etc/cron.$$base; \
	done
	@$(MAKECOOKIE)

include gar/category.mk
