GARNAME = nicstat
GARVERSION = 1.20
CATEGORIES = net

DESCRIPTION = Network monitoring tool
define BLURB
  Network monitoring tool
endef

MASTER_SITES = http://blogs.sun.com/roller/resources/timc/nicstat/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

SPKG_SOURCEURL = http://blogs.sun.com/timc/entry/nicstat_the_solaris_and_linux

LICENSE = LICENSE.txt

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

WORKSRC = $(WORKDIR)

ifeq ($(shell uname -p), sparc)
  MYARCH = -xarch=v8
else
  MYARCH =
endif

include gar/category.mk

build-custom:
	@echo " ==> Build $(GARNAME) (custom)"
	@( cd $(WORKSRC) ; \
	  sed "s/CFLAGS =/CFLAGS = $(MYARCH) /" Makefile.Solaris > Makefile ; \
	  gmake )
	@$(MAKECOOKIE)

install-custom:
	@echo " ==> Install $(GARNAME) (custom)"
	@ginstall -d $(DESTDIR)$(bindir)
	@cp $(WORKSRC)/nicstat $(DESTDIR)$(bindir)
	@ginstall -d $(DESTDIR)$(mandir)/man1
	@cp $(WORKSRC)/nicstat.1 $(DESTDIR)$(mandir)/man1
	@$(MAKECOOKIE)
