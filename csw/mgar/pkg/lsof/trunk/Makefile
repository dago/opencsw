GARNAME = lsof
GARVERSION = 4.77
CATEGORIES = utils

DESCRIPTION = List open files
define BLURB
  Lsof is a Unix-specific diagnostic tool. Its name stands for LiSt Open Files,
  and it does just that. It lists information about any files that are open by
  processes currently running on the system. It can also list communications
  open by each process.
endef

MASTER_SITES = ftp://lsof.itap.purdue.edu/pub/tools/unix/lsof/

TOPDIST   = $(GARNAME)_$(GARVERSION)
SRCDIST   = $(TOPDIST)_src
#DISTFILES = $(TOPDIST).tar.bz2
WORKSRC   = $(WORKDIR)/$(TOPDIST)/$(SRCDIST)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)_(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_SCRIPTS = custom
CONFIGURE_ARGS    = -n solariscc

TEST_SCRIPTS = custom
INSTALL_SCRIPTS = custom

include gar/category.mk

post-extract:
	@echo " ==> Extracting source distribution"
	@( cd $(WORKDIR)/$(TOPDIST) ; tar xf $(SRCDIST).tar )

configure-custom:
	@echo " ==> Configuring in $(WORKSRC)"
	@( cd $(WORKSRC) ; ./Configure $(CONFIGURE_ARGS) )

test-custom:
	@echo " ==> Testing in $(WORKSRC)/tests"
	@$(MAKE) -C $(WORKSRC)/tests

install-custom:
	@echo " ==> Installing $(GARNAME) $(GARVERSION)"
	@( cd $(WORKSRC) ; \
		install -m 2755 -g sys lsof $(DESTDIR)$(bindir) ; \
		install -d $(DESTDIR)$(mandir)/man8 ; \
		install -m 444 lsof.8 $(DESTDIR)$(mandir)/man8 )
