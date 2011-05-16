# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = hyperion
VERSION = 1.0.2
GARTYPE = v2
CATEGORIES = apps

SPKG_SOURCEURL = http://www.stack.nl/~jilles/irc/
DESCRIPTION = Brief description
define BLURB
endef

MASTER_SITES = http://www.stack.nl/~jilles/irc/
DISTFILES  = $(DISTNAME).tar.gz
DISTFILES  += gpl-1.0.txt

LICENSE = gpl-1.0.txt

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-pedantic
CONFIGURE_ARGS += --disable-debug-syms

RUNTIME_DEP_PKGS_CSWhyperion += CSWzlib
PATCHFILES += 0001-Using-localstatedir-instead-of-prefix-var.patch
PATCHFILES += 0002-Use-OpenCSW-paths.patch

CHECKPKG_OVERRIDES_CSWhyperion += file-with-bad-content|/usr/local|root/etc/opt/csw/dancer-ircd/example.conf

include gar/category.mk
