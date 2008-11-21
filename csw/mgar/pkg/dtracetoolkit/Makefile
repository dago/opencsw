GARNAME = DTraceToolkit
GARVERSION = 0.99
CATEGORIES = utils

DESCRIPTION = A collection of dtrace scripts developed by the DTrace community
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

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include ../category.mk

SPKG_SOURCEURL = http://www.brendangregg.com/dtrace.html

USEFUL_SCRIPTS = dexplorer dtruss dvmstat errinfo execsnoop hotkernel hotuser \
	iopattern iosnoop iotop opensnoop procsystime rwsnoop rwtop statsnoop

dtracedir = $(datadir)/dtracetoolkit

install-custom:
	@echo " ==> Installing $(GARNAME)"
	@ginstall -d $(DESTDIR)$(dtracedir)
	@rm -rf $(DESTDIR)$(dtracedir)
	@cp -r $(WORKSRC) $(DESTDIR)$(dtracedir)
	@rm -f $(DESTDIR)$(dtracedir)/install
	@ginstall -d $(DESTDIR)$(prefix)/bin
	@rm -f $(foreach SCRIPT, $(USEFUL_SCRIPTS), $(DESTDIR)$(prefix)/bin/$(SCRIPT))
	@gln -s $(foreach SCRIPT, $(USEFUL_SCRIPTS), ../share/dtracetoolkit/$(SCRIPT)) \
		$(DESTDIR)$(prefix)/bin
	@$(MAKECOOKIE)
