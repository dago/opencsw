# Todo
# * asprintf() from portable snprintf.c isn't working yet
#   Header line on watch output always reads "Every fs: "
#
GARNAME = watch
GARVERSION = 3.2.7
CATEGORIES = utils

DESCRIPTION = Watch a program output change over time
define BLURB
endef

# Usually we would use $(SF_MIRROR), but the procps folks didn't upload
# procps the usual way
SF_PROJ 	= procps
MASTER_SITES 	= http://$(SF_PROJ).sourceforge.net/
DISTFILES  	= $(SF_PROJ)-$(GARVERSION).tar.gz
PATCHFILES	= patch-extralibs.diff
DISTNAME   	= $(SF_PROJ)-$(GARVERSION)

REQUIRED_PKGS = CSWncurses

CONFIGURE_ARGS = $(DIRPATHS)

EXTRA_INC = /opt/csw/include/ncurses

TEST_SCRIPTS =
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
INSTALL_SCRIPTS = custom

include gar/category.mk

# procps is heavily GNU tailored, so we need to make some adjustments
#
# 1) Remove unnecessary build instructions that would cause errors otherwise
# 2) Bring in GNU getopt for getopt_long()
# 3) Bring in asprintf()
#
# GNU getopt from http://cherokee-project.com
# asprintf from http://www.ijs.si/software/snprintf/
#

# Tell snprintf.c that we have snprintf and need asprintf()
CFLAGS := $(CFLAGS) -DHAVE_SNPRINTF -DNEED_ASPRINTF

pre-build-modulated:
	@rm $(WORKSRC)/ps/module.mk $(WORKSRC)/proc/module.mk
	@cp $(FILEDIR)/snprintf* $(WORKSRC)
	@cp $(FILEDIR)/getopt* $(WORKSRC)
	@cp $(FILEDIR)/gettext.h* $(WORKSRC)
	$(MAKECOOKIE)

build-custom:
	@(cd $(WORKSRC); \
	    gmake ALL_CFLAGS="$(CFLAGS)" ALL_LDFLAGS="$(LDFLAGS)" snprintf.o; \
	    gmake ALL_CFLAGS="$(CFLAGS)" ALL_LDFLAGS="$(LDFLAGS)" getopt.o; \
	    gmake ALL_CFLAGS="$(CFLAGS)" ALL_LDFLAGS="$(LDFLAGS)" getopt1.o; \
	    gmake ALL_CFLAGS="$(CFLAGS) snprintf.o getopt.o getopt1.o" \
	        ALL_LDFLAGS="$(LDFLAGS)" watch)
	$(MAKECOOKIE)

install-custom:
	@ginstall -d $(DESTDIR)$(bindir)
	@ginstall -d $(DESTDIR)$(mandir)/man1
	@ginstall -m 755 $(WORKSRC)/watch $(DESTDIR)$(bindir)
	@ginstall -m 644 $(WORKSRC)/watch.1 $(DESTDIR)$(mandir)/man1
	$(MAKECOOKIE)
