# Known issues
# - watch only handles characters on a byte-by-byte basis, as such it
#   doesn't cope with wide characters like the ones encoded via UTF-8.
#   LATIN SMALL LETTER A WITH DIAERESIS (U+00E4) encoded in UTF-8
#   for example is simply skipped in the output. For the current 
#   implementation of watch it depends on the result of isprint() 
#   whether a one byte component of a character is printed.

# watch doesn't follow the procps versioning. It has a hardcoded
# version in watch.c which is emitted when calling watch -v
NAME = watch
VERSION = 0.2.0
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Watch a program output change over time
define BLURB
  "watch" from the procps package.
endef

# Usually we would use $(SF_MIRROR), but the procps folks didn't upload
# procps the usual way
SF_PROJ        = procps
SF_PROJ_VER    = 3.2.8
MASTER_SITES   = http://$(SF_PROJ).sourceforge.net/
DISTFILES      = $(SF_PROJ)-$(SF_PROJ_VER).tar.gz
DISTNAME       = $(SF_PROJ)-$(SF_PROJ_VER)
UFILES_REGEX   = $(SF_PROJ)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS = CSWncurses

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

pre-build-modulated:
	rm $(WORKSRC)/ps/module.mk $(WORKSRC)/proc/module.mk
	cp $(FILEDIR)/snprintf* $(WORKSRC)
	cp $(FILEDIR)/getopt* $(WORKSRC)
	cp $(FILEDIR)/gettext.h* $(WORKSRC)
	@$(MAKECOOKIE)

# Feature flags for snprintf.c. Don't tell it that you have v?snprintf,
# output will be garbled.
CFLAGS := $(CFLAGS) -DHAVE_STDARG_H -DHAVE_STDLIB_H -DHAVE_STDDEF
CFLAGS := $(CFLAGS) -DHAVE_INTTYPES_H -DHAVE_LOCALE_H -DHAVE_LOCALECONV
CFLAGS := $(CFLAGS) -DHAVE_LOCALECONV -DHAVE_UINTMAX_T -DHAVE_VA_COPY

# BUILD_ARGS with ALL_?FLAGS req. for $(WORKSRC)/Makefile
build-custom: BUILD_ARGS:=ALL_CFLAGS="$(CFLAGS)" ALL_LDFLAGS="$(LDFLAGS)"
build-custom:
	$(BUILD_ENV) gmake -C $(WORKSRC) $(BUILD_ARGS) snprintf.o
	$(BUILD_ENV) gmake -C $(WORKSRC) $(BUILD_ARGS) getopt.o
	$(BUILD_ENV) gmake -C $(WORKSRC) $(BUILD_ARGS) getopt1.o
	$(BUILD_ENV) gmake -C $(WORKSRC) \
		ALL_CFLAGS="$(CPPFLAGS) $(CFLAGS) snprintf.o getopt.o getopt1.o" \
	        ALL_LDFLAGS="$(LDFLAGS)" watch
	@$(MAKECOOKIE)

install-custom: DOCDEST=$(DESTDIR)$(docdir)/$(NAME)
install-custom:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(mandir)/man1
	ginstall -d $(DOCDEST)
	ginstall -m 755 $(WORKSRC)/watch $(DESTDIR)$(bindir)
	cp $(WORKSRC)/watch.1 $(DESTDIR)$(mandir)/man1
	cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	printf "This watch version (%s) was taken from procps %s, %s\n" \
		$(VERSION) $(SF_PROJ_VER) $(subst sourceforge,sf,$(MASTER_SITES)) \
		>> $(DOCDEST)/README.CSW
	@$(MAKECOOKIE)
