# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = cowsay
VERSION = 3.03
GARTYPE = v2

DESCRIPTION = Generates ASCII pictures of a cow with a message

MASTER_SITES = ftp://ftp.netbsd.org/pub/pkgsrc/distfiles/
DISTFILES  = $(DISTNAME).tar.gz

VENDOR_URL = http://www.nog.net/~tony/wareza

PACKAGES += CSWcowsay
SPKG_DESC_CSWcowsay = Generates ASCII pictures of a cow with a message
# PKGFILES is catchall
ARCHALL_CSWcowsay = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	ginstall -d -m 0755 $(DESTDIR)$(bindir)
	cat $(WORKSRC)/cowsay | \
		sed -e 's,%BANGPERL%,!/usr/bin/perl,' -e 's,%PREFIX%/share,$(sharedstatedir),' \
		> $(DESTDIR)$(bindir)/cowsay
	chmod 755 $(DESTDIR)$(bindir)/cowsay
	ln -s cowsay $(DESTDIR)$(bindir)/cowthink
	ginstall -d -m 0755 $(DESTDIR)$(mandir)/man1
	cat $(WORKSRC)/cowsay.1 | \
		sed -e 's,%BANGPERL%,!/usr/bin/perl,' -e 's,%PREFIX%/share,$(sharedtatedir),' \
		> $(DESTDIR)$(mandir)/man1/cowsay.1
	ln -s cowsay.1 $(DESTDIR)$(mandir)/man1/cowthink.1
	ginstall -d -m 0755 $(DESTDIR)$(sharedstatedir)/cows
	ginstall -m 0644 $(WORKSRC)/cows/* $(DESTDIR)$(sharedstatedir)/cows
	@$(MAKECOOKIE)
