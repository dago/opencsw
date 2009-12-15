GARNAME = Trac
GARVERSION = 0.11.6
CATEGORIES = apps

DESCRIPTION = Integrated SCM and Project Management
define BLURB
	Trac is an enhanced wiki and issue tracking system for software development
	projects. Trac uses a minimalistic approach to web-based software project
	management. Our mission; to help developers write great software while
	staying out of the way. Trac should impose as little as possible on a team's
	established development process and policies.
endef

MASTER_SITES = http://ftp.edgewall.com/pub/trac/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PACKAGES = CSWtrac
REQUIRED_PKGS_CSWtrac = CSWpysetuptools CSWpysvn CSWgenshi
REQUIRED_PKGS_CSWtrac += CSWpython CSWpython-devel

CATALOGNAME_CSWtrac = trac
SPKG_DESC_CSWtrac = Integrated SCM and Project Management

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://trac.edgewall.org/wiki/TracDownload

EXTRA_MERGE_EXCLUDE_FILES = .*\.pyo .*\.pyc
PROTOTYPE_FILTER = awk '$$$$3 ~ /.*\.py$$$$/ { $$$$2 = "cswpycompile" } { print }'
SPKG_CLASSES = none cswpycompile
REQUIRED_PKGS += CSWcswclassutils

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py
TEST_SCRIPTS =
INSTALL_SCRIPTS = $(WORKSRC)/setup.py
INSTALL_ARGS = --root=$(DESTDIR)

include gar/category.mk

post-install-modulated: copy-docs
	$(DONADA)

copy-docs:
	@install -d $(DESTDIR)$(docdir)/trac
	@cp -R $(WORKSRC)/contrib $(DESTDIR)$(docdir)/trac
	@for f in COPYING ChangeLog INSTALL README README.tracd UPGRADE ; do \
		ginstall -m 0644 $(WORKSRC)/$$f $(DESTDIR)$(docdir)/trac ; \
	done
	$(DONADA)

