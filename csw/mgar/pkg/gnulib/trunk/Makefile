# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gnulib
VERSION = X.Y
GARTYPE = v2
CATEGORIES = devel

DESCRIPTION = ISO C / POSIX substitutes part of gnulib
define BLURB
endef

GIT_REPOS = git://git.savannah.gnu.org/gnulib.git
GIT_USE_PROXY = 1

VENDOR_URL = http://www.gnu.org/software/gnulib/manual/html_node/POSIX-Substitutes-Library.html

PACKAGES += CSWlibgnu-dev
SPKG_DESC_CSWlibgnu-dev = ISO C / POSIX substitution library libgnu.a and headers
# PKGFILES is catchall

WORKSRC = $(WORKDIR)/posixlib

BUILD64 = 1

INSTALL_SCRIPTS = custom

# We explicitly want libgnu.a
MERGE_EXCLUDE_STATICLIBS =
CHECKPKG_OVERRIDES_CSWlibgnu-dev += discouraged-path-in-pkgmap|/opt/csw/lib/libgnu.a
CHECKPKG_OVERRIDES_CSWlibgnu-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv9/libgnu.a
CHECKPKG_OVERRIDES_CSWlibgnu-dev += discouraged-path-in-pkgmap|/opt/csw/lib/amd64/libgnu.a

include gar/category.mk

post-extract-modulated:
	-cd $(WORKDIR)/$(NAME)-$(VERSION) && ./gnulib-tool --create-testdir --source-base=lib \
                 --dir=$(abspath $(WORKSRC)) `./posix-modules`
	@$(MAKECOOKIE)

install-custom:
	ginstall -d $(DESTDIR)$(libdir)
	ginstall $(WORKSRC)/gllib/libgnu.a $(DESTDIR)$(libdir)/libgnu.a
	ginstall -d $(DESTDIR)$(includedir)/gnulib
	cd $(WORKDIR)/$(NAME)-$(VERSION)/lib && ginstall *.h $(DESTDIR)$(includedir)/gnulib
	@$(MAKECOOKIE)
