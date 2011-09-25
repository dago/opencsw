NAME       = dnstop
VERSION    = 20110502
CATEGORIES = net

DESCRIPTION = Displays various tables of DNS traffic
define BLURB
  Displays various tables of DNS traffic
endef

SPKG_SOURCEURL = http://dns.measurement-factory.com/tools/dnstop
MASTER_SITES   = http://dns.measurement-factory.com/tools/dnstop/src/
DISTFILES      = $(NAME)-$(VERSION).tar.gz
DISTFILES     += dnstop.8

LICENSE = LICENSE

RUNTIME_DEP_PKGS = CSWlibpcap1

TEST_SCRIPTS    =
INSTALL_SCRIPTS = custom

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

ifeq ($(shell uname -p), sparc)
  PATCHFILE = Makefile.sparc.p
else
  PATCHFILE = Makefile.i386.p
endif

pre-build-modulated:
	@echo " ==> Pre-build $(NAME) (custom)"
	@( cd $(WORKSRC) ; \
	   gpatch < ../../../../$(FILEDIR)/$(PATCHFILE) )
	@$(MAKECOOKIE)

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
	@ginstall -m 755 -d $(DESTDIR)$(bindir)
	@ginstall -m 755 $(WORKSRC)/dnstop $(DESTDIR)$(bindir)
	@ginstall -m 755 -d $(DESTDIR)$(mandir)/man8
	@ginstall -m 444 $(FILEDIR)/dnstop.8 $(DESTDIR)$(mandir)/man8
	@ginstall -m 755 -d $(DESTDIR)$(docdir)/$(NAME)
	@ginstall -m 444 $(WORKSRC)/CHANGES $(DESTDIR)$(docdir)/$(NAME)
	@$(MAKECOOKIE)
