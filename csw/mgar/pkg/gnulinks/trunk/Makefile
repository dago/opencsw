GARNAME = gnulinks
GARVERSION = 1.2
CATEGORIES = xtra

GLINKPKGS = CSWdiffutils CSWggettext CSWggettextrt CSWbison CSWbinutils
GLINKPKGS += CSWggrep CSWgawk CSWgsed CSWggetopt CSWfindutils
PREREQUISITE_PKGS = $(GLINKPKGS) CSWpkgutil

SPKG_SOURCEURL = No Source

DESCRIPTION = Creates native symlinks for GNU tools in /opt/csw/gnu
define BLURB
  Installs links for GNU utilities with a 'g' prefix into
  /opt/csw/gnu.
endef

MASTER_SITES = 
DISTFILES = CSWgnulinks.gspec CSWgnulinks.prototype

CONFIGURE_SCRIPTS = 
BUILD_SCRIPTS = 
INSTALL_SCRIPTS = 
TEST_SCRIPTS =

include gar/category.mk



newproto:
	@echo Generating new prototype...
	@( { echo /opt/csw/gnu;  \
	     for p in $(GLINKPKGS); do \
		pkgutil -L $$p | grep /opt/csw/bin/g; \
	     done } | \
		pkgproto | \
		perl -plne 's,f none /opt/csw/bin/g([\w\d-\+\.]+) 0755 root bin,s none /opt/csw/gnu/$$1=../bin/g$$1,' | \
		grep -v "^l " | sort > $(FILEDIR)/CSWgnulinks.prototype.new )
	@echo Installing new prototype.
	@mv $(FILEDIR)/CSWgnulinks.prototype.new \
		 $(FILEDIR)/CSWgnulinks.prototype
	@$(MAKE) makesums
