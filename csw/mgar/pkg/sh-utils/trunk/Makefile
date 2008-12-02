GARNAME = sh-utils
GARVERSION = 2.0
CATEGORIES = utils

DESCRIPTION = sh utilities
define BLURB
  A set of command utilities.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz 

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# Chinese translation has errors
PATCHFILES = zh.diff

INSTALL_SCRIPTS = $(WORKSRC)/Makefile $(WORKSRC)/Makefile-root
CONFIGURE_ARGS  = $(DIRPATHS)

TEST_TARGET = check

# Some tests require a controlling terminal
TEST_SCRIPTS =

include gar/category.mk

install-%/Makefile-root:
	@echo " ==> Running make install in $*"
	$(INSTALL_ENV) $(MAKE) DESTDIR=$(DESTDIR) $(foreach TTT,$(INSTALL_OVERRIDE_DIRS),$(TTT)="$(DESTDIR)$($(TTT))") -C $* $(INSTALL_ARGS) install-root
	@$(MAKECOOKIE)

# We should use Solaris utils here instead
post-install:
	@rm -f $(DESTDIR)$(bindir)/su $(DESTDIR)$(bindir)/hostname
