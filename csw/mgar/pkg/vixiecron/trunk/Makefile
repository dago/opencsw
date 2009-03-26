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
#  - Improve man page locations. The original manpage install script looks retarded.
#  - SMF support for non-global zones.

MASTER_SITES  = http://ftp.de.debian.org/debian/pool/main/c/cron/
DISTFILES  = cron_$(GARVERSION).orig.tar.gz
DISTFILES += cron_$(GARVERSION)-105.diff.gz
DISTFILES += $(call admfiles,CSWvixiecron,postinstall)
DISTFILES += csw$(GARNAME) csw$(GARNAME).xml svc-csw$(GARNAME)
DISTFILES += crontab.CSW run-crons-0.3.2

WORKSRC = $(WORKDIR)/cron-$(GARVERSION).orig

SPKG_CLASSES = none cswinitsmf

PATCHFILES = cron_$(GARVERSION)-105.diff.gz \
             gar-$(GARNAME)_$(GARVERSION).patch

TEST_SCRIPTS =
CONFIGURE_SCRIPTS =
EXTRA_CFLAGS = -DDEBUGGING=0 -DPOSIX -DDEBIAN

pre-install:
	ginstall -d $(DESTDIR)/opt/csw
	ginstall -d $(DESTDIR)/opt/csw/bin
	ginstall -d $(DESTDIR)/opt/csw/sbin
	ginstall -d $(DESTDIR)/opt/csw/share/man/cat5
	ginstall -d $(DESTDIR)/opt/csw/share/man/cat8

pre-install-isa-sparcv9: pre-install
pre-install-isa-sparcv8: pre-install
pre-install-isa-i386: pre-install
pre-install-isa-amd64: pre-install

post-install:
	ginstall -d $(DESTDIR)/etc
	ginstall -m 750 files/crontab.CSW $(DESTDIR)/etc/crontab.CSW
	ginstall -m 755 files/run-crons-0.3.2 $(DESTDIR)/opt/csw/sbin/run-crons
	for base in hourly daily weekly monthly; do \
		ginstall -d $(DESTDIR)/etc/cron.$$base; \
	done

post-install-isa-sparcv8: post-install
post-install-isa-sparcv9: post-install
post-install-isa-i386: post-install
post-install-isa-amd64: post-install


include gar/category.mk
