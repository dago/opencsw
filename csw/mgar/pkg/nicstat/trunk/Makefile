NAME = nicstat
VERSION = 1.90
CATEGORIES = net
GARTYPE = v2
WORKSRC = $(WORKDIR)/$(NAME)-src-$(VERSION)

DESCRIPTION = Network monitoring tool
define BLURB
  Network monitoring tool
endef

MASTER_SITES = $(SF_MIRRORS)
SF_PROJ = $(NAME)
DISTFILES  = $(NAME)-src-$(VERSION).tar.gz

VENDOR_URL = http://blogs.sun.com/timc/entry/nicstat_the_solaris_and_linux

# Harmless build example not relevant to usage
CHECKPKG_OVERRIDES_CSWnicstat += file-with-bad-content|/usr/local|root/opt/csw/share/doc/nicstat/README.txt

CONFIGURE_ARGS = $(DIRPATHS)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

ifeq ($(shell uname -p), sparc)
  MYARCH = -xarch=v8
else
  MYARCH =
endif

include gar/category.mk

build-custom:
	@echo " ==> Build $(NAME) (custom)"
	@( cd $(WORKSRC) ; \
	  sed "s/CFLAGS =/CFLAGS = $(MYARCH) /" Makefile.Solaris > Makefile ; \
	  gmake )
	@$(MAKECOOKIE)

install-custom:
	@echo " ==> Install $(NAME) (custom)"
	@ginstall -d -m 755 $(DESTDIR)$(bindir)
	@ginstall -m 755 $(WORKSRC)/.nicstat* $(DESTDIR)$(bindir)/nicstat
	@ginstall -d -m 755 $(DESTDIR)$(mandir)/man1
	@ginstall -m 444 $(WORKSRC)/nicstat.1 $(DESTDIR)$(mandir)/man1
	@ginstall -d -m 755 $(DESTDIR)$(docdir)/$(NAME)
	@ginstall -m 444 $(WORKSRC)/README.txt $(WORKSRC)/ChangeLog.txt $(DESTDIR)$(docdir)/$(NAME)
	@ginstall -m 444 $(WORKSRC)/LICENSE.txt $(DESTDIR)$(docdir)/$(NAME)/license
	@$(MAKECOOKIE)
