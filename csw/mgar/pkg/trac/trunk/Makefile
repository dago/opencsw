# $Id$

NAME = Trac
VERSION = 0.12.1
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = Integrated SCM and Project Management
define BLURB
	Trac is an enhanced wiki and issue tracking system for software development
	projects. Trac uses a minimalistic approach to web-based software project
	management. Our mission; to help developers write great software while
	staying out of the way. Trac should impose as little as possible on a team's
	established development process and policies.
endef

MASTER_SITES           = http://ftp.edgewall.com/pub/trac/
SPKG_SOURCEURL         = http://trac.edgewall.org/wiki/TracDownload
DISTFILES              = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX           = (\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWtrac
RUNTIME_DEP_PKGS_CSWtrac  = CSWpysetuptools CSWpythonsvn CSWgenshi
ARCHALL_CSWtrac = 1

CATALOGNAME_CSWtrac    = trac
SPKG_DESC_CSWtrac      = Integrated SCM and Project Management

CHECKPKG_OVERRIDES_CSWtrac += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWtrac += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWtrac += surplus-dependency|CSWpysetuptools
CHECKPKG_OVERRIDES_CSWtrac += surplus-dependency|CSWgenshi
CHECKPKG_OVERRIDES_CSWtrac += surplus-dependency|CSWpythonsvn


TEST_SCRIPTS           =

include gar/category.mk

post-install-modulated: copy-docs
	@$(DONADA)

copy-docs:
	@install -d $(DESTDIR)$(docdir)/trac
	@cp -R $(WORKSRC)/contrib $(DESTDIR)$(docdir)/trac
	@for f in COPYING ChangeLog INSTALL README README.tracd UPGRADE ; do \
		ginstall -m 0644 $(WORKSRC)/$$f $(DESTDIR)$(docdir)/trac ; \
	done
	@$(DONADA)

