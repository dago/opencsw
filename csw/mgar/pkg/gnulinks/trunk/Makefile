NAME = gnulinks
VERSION = 1.4
CATEGORIES = xtra
GARTYPE = v2

VENDOR_URL = ht#GLINKPKGS =  CSWbinutils CSWggetopt CSWgwhois
#ggetopt CSWgwhois
BUILD_DEP_PKGS = $(GLINKPKGS) CSWpkgutil CSWbash

DESCRIPTION = Creates native symlinks for GNU tools in /opt/csw/gnu
define BLURB
  Installs links for GNU utilities with a 'g' prefix into
  /opt/csw/gnu.
endef

MASTER_SITES = http/
DISTFILES += COPYING

PACKAGES += CSWgnulinks
CATALOGNAME_CSWgnulinks = gnulinks_stub
SPKG_DESC_CSWgnulinks = Transitional package. Content moved to individual packages.
# Thats the purpose
CHECKPKG_OVERRIDES_CSWgnulinks += catalogname-does-not-match-pkgnameST#where can we build?
PACKAGING_PLATFORMS += solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386
             STFILES += COPYING

CONFIGURE_SCRIPTS = 
BUILD_SCRIPTS = 
INSTALL_SCRIPTS = custom
TEST_SCRIPTS =

ARCHALL = 1

SHELL = /opt/csw/bin/bash

# We point to these packages, but do not depend on them on purpose.
CHECKPKG_OVERRIDES_CSWgnulinks += $(foreach P,$(GLINKPKGS),missing-dependency|$P)

include ../COPYING .; )

install-custom:
	@mkdir -p $(DESTDIR)
	( cd $(DESTDIR); pwd; mkdir -p opt/csw/gnu; cd opt/csw/gnu; pwd; \
		for p in $(GLINKPKGS); do \
			echo Creating links for $$p; \
			for f in $$(pkgutil -L $$p | grep /opt/csw/bin/g); do \
				base=$$(basename $$f); \
				basenog=$${base/g/}; \
				gln -sf ../bin/$$base $$basenog; \
			done; \
		done; \
		rm -f descriptions* catalog* )
	@$(MAKECOOKIE)

# this shouldn't be used now, but is helpful if you ever want to
# generate a manual prototype file for this package
newproto:
	@echo Generating new prototype...
	@( { echo /opt/csw/gnu;  \
	     for p in $(GLINKPKGS); do \
		pkgutil -L $$p | grep /opt/csw/bin/g; \
	     done } | \
		pkgproto | \
		perl -plne 's,f none /opt/csw/bin/g([\w\d-\+\.]+) (45|07)55 root bin,s none /opt/csw/gnu/$$1=../bin/g$$1,' | \
		grep -v "^l " | sort > $(FILEDIR)/CSWgnulinks.prototype.new )
	@echo Installing new prototype.
	@mv $(FILEDIR)/CSWgnulinks.prototype.new \
		 $(FILEDIR)/CSWgnulinks.prototype
	