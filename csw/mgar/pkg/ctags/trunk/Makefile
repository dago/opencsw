# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = ctags
VERSION = 5.8
GARTYPE = v2

DESCRIPTION = Exuberant Ctags
define BLURB
  Exuberant Ctags is a multilanguage reimplementation of the Unix ctags utility. Ctags generates an index of source code definitions which is used by numerous editors and utilities to instantly locate the definitions.
endef

MASTER_SITES = $(SFMIRROS)
DISTFILES  = $(DISTNAME).tar.gz
VENDOR_URL = http://ctags.sourceforge.net/

INCOMPATIBLE_PKGS = CSWemacs-bin-common
INCOMPATIBLE_PKGS = CSWemacs-common

REINPLACE_MATCH = /usr/local/etc
REINPLACE_WITH = /etc/opt/csw
REINPLACE_FILES += options.c 
REINPLACE_FILES += ctags.1

CHECKPKG_OVERRIDES_CSWctags += file-collision|/opt/csw/bin/ctags|CSWctags|CSWemacs-bin-common
CHECKPKG_OVERRIDES_CSWctags += file-collision|/opt/csw/share/man/man1/ctags.1|CSWctags|CSWemacs-common

# no traget check
SKIPTEST = 1
# no DESTDIR support
INSTALL_SCRIPTS = custom

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

install-custom:
	@ginstall -d $(DESTDIR)$(bindir)
	@ginstall -d $(DESTDIR)$(mandir)/man1
	@gcp -fp $(WORKSRC)/ctags $(DESTDIR)$(bindir)
	@gcp -fp $(WORKSRC)/ctags.1 $(DESTDIR)$(mandir)/man1
	@$(MAKECOOKIE)
