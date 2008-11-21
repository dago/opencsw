GARNAME = figlet
GARVERSION = 2.2.2
RELEASE = 222
CATEGORIES = apps

DESCRIPTION = FIGlet is a program for making large letters out of ordinary text
define BLURB
   _____ ___ ____ _      _   
  |  ___|_ _/ ___| | ___| |_ 
  | |_   | | |  _| |/ _ \ __|
  |  _|  | | |_| | |  __/ |_ 
  |_|   |___\____|_|\___|\__|
endef

MASTER_SITES = ftp://ftp.figlet.org/pub/figlet/program/unix/
DISTFILES  = $(GARNAME)$(RELEASE).tar.gz
MASTER_SITES += ftp://ftp.figlet.org/pub/figlet/fonts/
# ours.tar.gz is already in the figlet distribution
DISTFILES += contributed.tar.gz international.tar.gz ms-dos.tar.gz
DISTFILES += $(call admfiles,CSWfiglet)

DISTNAME = $(GARNAME)$(RELEASE)

# We don't have this modern autoconfig-doodle-crap
CONFIGURE_SCRIPTS =

APPDIR = $(sharedstatedir)/$(GARNAME)
DEFAULTFONTDIR = $(APPDIR)/fonts

BUILD_OVERRIDE_DIRS = CC DEFAULTFONTDIR

# FIGlet doesn't have tests
TEST_SCRIPTS =

INSTALL_SCRIPTS = custom

include ../category.mk

# The install part from the Makefile is completely unrelocatable :-(
install-custom:
	@echo " ==> Installing $(GARNAME)"
	@ginstall -d $(DESTDIR)$(bindir)
	@ginstall $(WORKSRC)/figlet $(WORKSRC)/chkfont $(WORKSRC)/figlist $(WORKSRC)/showfigfonts \
		$(DESTDIR)$(bindir)
	@ginstall -d $(DESTDIR)$(mandir)/man6
	@ginstall $(WORKSRC)/figlet.6 $(DESTDIR)$(mandir)/man6/figlet.6
	@ginstall -d $(DESTDIR)$(DEFAULTFONTDIR)
	@ginstall $(WORKSRC)/fonts/*.fl[cf] $(DESTDIR)$(DEFAULTFONTDIR)
	@ginstall $(WORKDIR)/contributed/*.fl[cf] $(DESTDIR)$(DEFAULTFONTDIR)
	@# We don't include fonts for Chinese-Japanese-Korean by default, as they are quite big
	@# These may go into an addon-package
	@ginstall $(WORKDIR)/international/*.fl[cf] $(DESTDIR)$(DEFAULTFONTDIR)
	@ginstall $(WORKDIR)/international/febrew $(DESTDIR)$(APPDIR)
	@$(MAKECOOKIE)
