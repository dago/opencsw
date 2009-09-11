# TODO/Issues
# - Man pages don't display right now
# - Set sudosh.conf ownership to root:root?
# - Compiled in default for logdir /var/adm/..., if not existant sudosh2
#   totally hangs (^C doesn't work). Change default and include the dir in the
#   package?
# - Submit DESTDIR patch upstream
GARNAME = sudosh2
GARVERSION = 1.0.2
CATEGORIES = apps

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tgz

CONFIGURE_ARGS = $(DIRPATHS)

# No tests available
TEST_SCRIPTS = 

# Installation for sudosh.conf doesn't honor DESTDIR
PATCHFILES = 001-installsudosh.conf-destdir.patch

include gar/category.mk

pre-configure-modulated:
	perl -pi -e 's|-Werror|-errwarn|g' $(WORKSRC)/Makefile.in $(WORKSRC)/src/Makefile.in
	@$(MAKECOOKIE)
