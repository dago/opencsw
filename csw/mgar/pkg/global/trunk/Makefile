# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = global
VERSION = 6.1
GARTYPE = v2
CATEGORIES = devel

DESCRIPTION = GNU GLOBAL source code tag system
define BLURB
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --with-exuberant-ctags=$(bindir)/ectags

# checkpkg can not detect this
CHECKPKG_OVERRIDES_CSWglobal += surplus-dependency|CSWectags

RUNTIME_DEP_PKGS_CSWglobal += CSWperl
RUNTIME_DEP_PKGS_CSWglobal += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWglobal += CSWectags

# Just because it ships an emacs mode doesn't mean to depend on it
CHECKPKG_OVERRIDES_CSWglobal += missing-dependency|CSWemacscommon

# These are docs only, overwrite for now
CHECKPKG_OVERRIDES_CSWglobal += file-with-bad-content|/usr/local|root/opt/csw/share/info/global.info
CHECKPKG_OVERRIDES_CSWglobal += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/htags.1
CHECKPKG_OVERRIDES_CSWglobal += file-with-bad-content|/usr/local|root/opt/csw/share/gtags/INSTALL
CHECKPKG_OVERRIDES_CSWglobal += file-with-bad-content|/usr/local|root/opt/csw/share/gtags/ChangeLog
CHECKPKG_OVERRIDES_CSWglobal += file-with-bad-content|/usr/local|root/opt/csw/share/gtags/NEWS
CHECKPKG_OVERRIDES_CSWglobal += file-with-bad-content|/usr/local|root/opt/csw/share/gtags/script/README
CHECKPKG_OVERRIDES_CSWglobal += file-with-bad-content|/usr/share|root/opt/csw/share/gtags/ChangeLog

include gar/category.mk

post-extract-modulated:
	-perl -pi -e 's,/usr/local/apache/conf/http.conf,$(prefix)/apache2/etc/httpd.conf,' \
		$(WORKSRC)/htags/htags.c
	@$(MAKECOOKIE)
