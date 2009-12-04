GARNAME = lastx
GARVERSION = 1.1
CATEGORIES = utils

DESCRIPTION = An extension of the last utility shipped with Solaris
define BLURB
  lastx is an extension of the last utility shipped with Solaris. It
  prints all 32-characters of the users utmpx entry, and provides
  facilities to display last data over a period of days. It also
  allows the user to print unique logins, and the total # of attempted
  logins. 
endef

MASTER_SITES = http://prefetch.net/code/
DISTFILES = lastx.c
DISTFILES += COPYING

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://prefetch.net/code/lastx.c.html

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

build-custom:
	cd $(WORKDIR) && $(CC) -o lastx $(CPPFLAGS) $(CFLAGS) $(LDFLAGS) lastx.c
	@$(MAKECOOKIE)

install-custom:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall $(WORKDIR)/lastx $(DESTDIR)$(bindir)/lastx
