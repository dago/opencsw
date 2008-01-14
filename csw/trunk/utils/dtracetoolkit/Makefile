GARNAME = DTraceToolkit
GARVERSION = 0.99
CATEGORIES = utils

DESCRIPTION = A collection of useful documented scripts developed by the OpenSolaris DTrace community
define BLURB
  The following are miscellaneous open source tools and examples
  that use the DTrace language provided in Solaris 10 and OpenSolaris.
  DTrace helps troubleshoot problems on servers by providing new detailed
  views of the system internals, to a level that was previously difficult
  to access. The language is similar to C and is event based.
endef

MASTER_SITES = http://www.brendangregg.com/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWdtracetoolkit)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include ../category.mk

install-custom:
	@echo " ==> Installing $(GARNAME)"
	@rm -rf $(DESTDIR)$(prefix)/DTT
	@ginstall -d $(DESTDIR)$(prefix)
	@cp -R $(WORKSRC) $(DESTDIR)$(prefix)/DTT
	@rm -f $(DESTDIR)$(prefix)/DTT/install
	@$(MAKECOOKIE)
