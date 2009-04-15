GARNAME = watch
GARVERSION = 0.2.0
CATEGORIES = utils

DESCRIPTION = Watch a program output change over time
define BLURB
  "watch" from the procps package.
endef

# Usually we would use $(SF_MIRROR), but the procps folks didn't upload
# procps the usual way
SF_PROJ 	= procps
SF_PROJ_VER	= 3.2.7
MASTER_SITES 	= http://$(SF_PROJ).sourceforge.net/
DISTFILES  	= $(SF_PROJ)-$(SF_PROJ_VER).tar.gz
DISTNAME   	= $(SF_PROJ)-$(SF_PROJ_VER)

REQUIRED_PKGS = CSWncurses

TEST_SCRIPTS =
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
INSTALL_SCRIPTS = custom

# Include additional libraries (see pre-build-modulated below)
PATCHFILES = patch-extralibs.diff

# Avoid "Broken pipe" error message on pclose() for cmds with longish output
PATCHFILES += patch-sigpipe.diff

CONFIGURE_ARGS = $(DIRPATHS)

EXTRA_INC = /opt/csw/include/ncurses

include gar/category.mk

# procps is heavily GNU tailored, so we need to make some adjustments
#
# 1) Remove unnecessary build instructions that would cause errors otherwise
# 2) Bring in GNU getopt for getopt_long()
# 3) Bring in snprintf.c for a portable version of asprintf()
#
# GNU getopt taken from 
#   http://svn.cherokee-project.com/browser/cherokee/trunk/cherokee/getopt
# snprintf.c taken from http://www.jhweiss.de/software/snprintf.html
#

# Don't tell snprintf.c that you have v?snprintf, output will be garbled 
CFLAGS := $(CFLAGS) -DHAVE_STDARG_H -DHAVE_STDLIB_H -DHAVE_STDDEF
CFLAGS := $(CFLAGS) -DHAVE_INTTYPES_H -DHAVE_LOCALE_H -DHAVE_LOCALECONV
CFLAGS := $(CFLAGS) -DHAVE_LOCALECONV -DHAVE_UINTMAX_T -DHAVE_VA_COPY

pre-build-modulated:
	@rm $(WORKSRC)/ps/module.mk $(WORKSRC)/proc/module.mk
	@cp $(FILEDIR)/snprintf* $(WORKSRC)
	@cp $(FILEDIR)/getopt* $(WORKSRC)
	@cp $(FILEDIR)/gettext.h* $(WORKSRC)
	$(MAKECOOKIE)

build-custom: BUILD_ARGS:=ALL_CFLAGS="$(CFLAGS)" ALL_LDFLAGS="$(LDFLAGS)"
build-custom:
	@$(BUILD_ENV) gmake -C $(WORKSRC) $(BUILD_ARGS) snprintf.o
	@$(BUILD_ENV) gmake -C $(WORKSRC) $(BUILD_ARGS) getopt.o
	@$(BUILD_ENV) gmake -C $(WORKSRC) $(BUILD_ARGS) getopt1.o
	@$(BUILD_ENV) gmake -C $(WORKSRC) \
		ALL_CFLAGS="$(CFLAGS) snprintf.o getopt.o getopt1.o" \
	        ALL_LDFLAGS="$(LDFLAGS)" watch
	$(MAKECOOKIE)

install-custom:
	@ginstall -d $(DESTDIR)$(bindir)
	@ginstall -d $(DESTDIR)$(mandir)/man1
	@ginstall -m 755 $(WORKSRC)/watch $(DESTDIR)$(bindir)
	@ginstall -m 644 $(WORKSRC)/watch.1 $(DESTDIR)$(mandir)/man1
	$(MAKECOOKIE)
