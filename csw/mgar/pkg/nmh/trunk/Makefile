# $Id$
NAME = nmh
VERSION = 1.4
CATEGORIES = apps

DESCRIPTION = Powerful electronic mail handling system
define BLURB
 This is the nmh mail user agent, a command-line based mail reader that
 is powerful and extensible. Unlike most mail user agents, nmh is not a
 single program, rather it is a set of programs that are run from the
 shell. This allows the user to utilize the full power of the Unix
 shell in conjunction with nmh.
endef

MASTER_SITES = http://download.savannah.gnu.org/releases/$(NAME)/
DISTFILES  = nmh-$(VERSION).tar.gz
SPKG_SOURCEURL = http://www.nongnu.org/nmh/
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS += CSWlibiconv2
PATCHFILES += 0000-skip-chgrp-of-inc.patch
LICENSE = COPYRIGHT
PRESERVECONF = /etc/opt/csw/nmh/mts.conf

CONFIGURE_ARGS = --enable-pop --enable-masquerade='' --with-mts=sendmail \
  --prefix=$(prefix) --mandir=$(mandir) --datadir=$(datadir)/nmh \
  --libdir=$(libdir)/nmh --sysconfdir=$(sysconfdir)/nmh 
TEST_SCRIPTS =

include gar/category.mk
