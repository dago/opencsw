# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = svr4pkg
VERSION = 0.5
GARTYPE = v2

DESCRIPTION = Basic perl implementation of solaris native svr4 packages tools
define BLURB
  Basic perl implementation of solaris native svr4 packages tools
endef

GITHUB_USER = yannrouillard
MASTER_SITES = https://github.com/${GITHUB_USER}/${NAME}/archive/
DISTFILES = v$(VERSION).tar.gz

# We disable inclusion of CSWcommon by default as
# this package could be installed before anything
COMMON_PKG_DEPENDS = 
# We disable the checkpkg alarms related
CHECKPKG_OVERRIDES_CSWsvr4pkg += missing-dependency|

# We provide some default class action script
# located in a place not standard so we disable 
# the checkpkg warning
CHECKPKG_OVERRIDES_CSWsvr4pkg += bad-location-of-file|

ARCHALL = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

NATIVE_TOOLS = pkgadd pkgrm pkginfo pkgchk pkgparam installf removef

CAS_LOCATION = /var/sadm/install/scripts

install-custom:
	@echo " ==> Installing $(NAME)"
	ginstall -d $(DESTDIR)$(bindir)
	ginstall $(WORKSRC)/svr4pkg $(DESTDIR)$(bindir)
	cd "$(DESTDIR)$(bindir)" && for TOOL in $(NATIVE_TOOLS); do \
	    gln -sf svr4pkg "$$TOOL"; \
	done
	ginstall -d $(DESTDIR)$(CAS_LOCATION)
	cd "$(FILEDIR)" && for CAS in *.sh; do \
	    ginstall $$CAS $(DESTDIR)$(CAS_LOCATION)/`echo ${CAS} | sed -e '/\.sh$$//'`; \
        done
	ginstall -d $(DESTDIR)$(docdir)$(NAME)
	ginstall $(WORKSRC)/README.md $(DESTDIR)$(docdir)$(NAME)

	@$(MAKECOOKIE)

