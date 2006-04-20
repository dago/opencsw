GARNAME = gawk
GARVERSION = 3.1.3
CATEGORIES = utils

DESCRIPTION = A pattern scanning and processing language.
define BLURB
    The awk utility interprets a special-purpose programming language that makes it
    possible to handle simple data-reformatting jobs with just a few lines of code.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz 

CONFIGURE_ARGS = $(DIRPATHS)

INSTALL_ARGS = $(foreach VAR, bindir sbindir libexecdir datadir sysconfdir sharedstatedir localstatedir libdir infodir mandir includedir,$(VAR)=$($(VAR)))

include ../category.mk

post-install:
	(cd $(DESTDIR)$(bindir); ln -sf gawk awk)
	$(MAKECOOKIE)
