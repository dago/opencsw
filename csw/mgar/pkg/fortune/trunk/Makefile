#####################################################################
# OpenCSW build recipe for fortune
#
# Author: Yann Rouillard <yann@pleiades.fr.eu.org>
#
# Redistribution and/or use, with or without modification, is
# permitted.  This software is without warranty of any kind.  The
# author(s) shall not be liable in the event that use of the
# software causes damage.
#####################################################################

###### Package information #######

NAME = fortune
VERSION = 9708
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Provides fortune cookies on demand
define BLURB
  Provides fortune cookies on demand
endef

MASTER_SITES = http://www.ibiblio.org/pub/Linux/games/amusements/fortune/
UPSTREAM_MASTER = ftp://ftp.ibiblio.org/pub/linux/games/amusements/fortune/

PACKAGES = CSWfortune

###### Upstream and opencsw files information #######

DISTNAME   = fortune-mod-$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz
DISTFILES += changelog.CSW 
DISTFILES += license

PATCHFILES = 0001-use-ginstall.patch
#PATCHFILES += 0002-Honor-DESTDIR.patch

DOCFILES = INSTALL Notes Offensive README TODO


##### Build and installation information #####


GARCOMPILER = SUN

CONFIGURE_ARGS = $(DIRPATHS)

CONFIGURE_SCRIPTS =
TEST_SCRIPTS =

BUILD_OVERRIDE_VARS = COOKIEDIR
BUILD_OVERRIDE_VAR_COOKIEDIR = $(sharedstatedir)/fortunes

INSTALL_OVERRIDE_VARS = FORTDIR BINDIR FORTMANDIR BINMANDIR COOKIEDIR
INSTALL_OVERRIDE_VAR_FORTDIR = $(DESTDIR)/$(sharedstatedir)/fortunes
INSTALL_OVERRIDE_VAR_FORTMANDIR = $(DESTDIR)/$(mandir)/man6
INSTALL_OVERRIDE_VAR_BINDIR = $(DESTDIR)/$(bindir)/
INSTALL_OVERRIDE_VAR_BINMANDIR = $(DESTDIR)/$(mandir)/man1
INSTALL_OVERRIDE_VAR_COOKIEDIR = $(DESTDIR)/$(sharedstatedir)/fortunes

REINPLACE_MATCH = /usr/local/share/games
REINPLACE_WITH = /opt/csw/share
REINPLACE_FILES += Notes

include gar/category.mk

mv-fortune:
	[ -f "$(PKGROOT)/$(bindir)/fortune" ] || \
	      mv "$(PKGROOT)/$(sharedstatedir)/fortunes/fortune" "$(PKGROOT)/$(bindir)"/
                
merge-doc:
	ginstall -d $(PKGROOT)/$(docdir)/$(NAME)
	cd $(DOWNLOADDIR)/ && ginstall -m 0644 license changelog.CSW $(PKGROOT)/$(docdir)/$(NAME)/
	cd $(WORKSRC_FIRSTMOD)/ && ginstall -m 0644 $(DOCFILES) $(PKGROOT)/$(docdir)/$(NAME)/
	@$(MAKECOOKIE)

post-merge: mv-fortune merge-doc


