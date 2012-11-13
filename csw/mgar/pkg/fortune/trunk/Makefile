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
DISTFILES += COPYING

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

INSTALL_ENV_PATH = $(prefix)/gnu:$(PATH)

REINPLACE_MATCH = /usr/local/share/games
REINPLACE_WITH = /opt/csw/share
REINPLACE_FILES += Notes

include gar/category.mk

post-merge:
	[ -f "$(PKGROOT)/$(bindir)/fortune" ] || \
	      mv "$(PKGROOT)/$(sharedstatedir)/fortunes/fortune" "$(PKGROOT)/$(bindir)"/
                
post-install:
	ginstall -d $(DESTDIR)/$(docdir)/$(NAME)
	cd $(DOWNLOADDIR)/ && ginstall -m 0644 changelog.CSW $(DESTDIR)/$(docdir)/$(NAME)/
	cd $(WORKSRC)/ && ginstall -m 0644 $(DOCFILES) $(DESTDIR)/$(docdir)/$(NAME)/


