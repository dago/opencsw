# Copyright 2009 Google Inc.
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = vixiecron
VERSION = 3.0pl1
CATEGORIES = server
GARTYPE = v2

DESCRIPTION = Paul Vixie cron
define BLURB
  vixiecron is one of the most widely used cron implementations.

  This build includes patches from Debian.  It supports /etc/cron.d directory,
  which can be used to conveniently set up cron jobs by placing files. It also
  supports slash notation: */5 denotes "Every five minutes".
endef

# TODO:
#  - Improve man page locations. The original manpage install script
#    looks retarded.

MASTER_SITES  = http://ftp.de.debian.org/debian/pool/main/c/cron/
DISTFILES  = cron_$(VERSION).orig.tar.gz
DISTFILES += cron_$(VERSION)-111.diff.gz
DISTFILES += CSWvixiecron.preinstall
DISTFILES += CSWvixiecron.postinstall
DISTFILES += CSWvixiecron.postremove
DISTFILES += csw$(NAME)
DISTFILES += crontab.CSW
DISTFILES += run-crons-0.3.2

DISTNAME = cron-$(VERSION).orig
# WORKSRC = $(WORKDIR)/cron-$(VERSION).orig

LICENSE = README

#    $$$$3 ~ /\/init.d\/cswvixiecron$$$$/ { $$$$2 = "cswinitsmf" }
#    $$$$3 ~ /\/crontab\.CSW$$$$/ { $$$$2 = "cswcpsampleconf" }
PROTOTYPE_FILTER  = awk ' \
    $$$$3 ~ /\/opt\/csw\/bin\/crontab$$$$/ { $$$$4 = "1755" } \
    { print }'

INITSMF = /etc/opt/csw/init.d/cswvixiecron
PRESERVECONF = /etc/crontab

PATCHFILES += cron_$(VERSION)-111.diff.gz
PATCHFILES += 0001-Use-bash-for-putman.sh.patch
PATCHFILES += 0002-Makefile-adjustments.patch
PATCHFILES += 0003-mkdtemp-support.patch
PATCHFILES += 0004-Sun-Studio-detection.patch
PATCHFILES += 0005-bitstring.h-a-local-header-file.patch
PATCHFILES += 0006-signal-handlers-and-setenv.patch
PATCHFILES += 0007-Solaris-9-doesn-t-have-O_NOFOLLOW.patch
PATCHFILES += 0008-consts-needed-in-externs.h.patch
PATCHFILES += 0009-lockf-instead-of-flock.patch
PATCHFILES += 0010-A-workaround-for-O_NOFOLLOW.patch

TEST_SCRIPTS =
CONFIGURE_SCRIPTS =
EXTRA_CFLAGS = -DDEBUGGING=0 -DPOSIX -DDEBIAN

include gar/category.mk

pre-install-modulated:
	ginstall -d $(DESTDIR)/opt/csw
	ginstall -d $(DESTDIR)/opt/csw/bin
	ginstall -d $(DESTDIR)/opt/csw/sbin
	ginstall -d $(DESTDIR)/opt/csw/share/man/cat5
	ginstall -d $(DESTDIR)/opt/csw/share/man/cat8
	@$(MAKECOOKIE)

post-install-modulated:
	ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall $(FILEDIR)/csw$(NAME) \
		$(DESTDIR)/etc/opt/csw/init.d/csw$(NAME)
	ginstall -d $(DESTDIR)/etc
	ginstall -m 750 $(FILEDIR)/crontab.CSW \
		$(DESTDIR)/etc/crontab.CSW
	ginstall -m 755 $(FILEDIR)/run-crons-0.3.2 \
		$(DESTDIR)/opt/csw/sbin/run-crons
	for base in hourly daily weekly monthly; do \
		ginstall -d $(DESTDIR)/etc/cron.$$base; \
	done
	@$(MAKECOOKIE)
