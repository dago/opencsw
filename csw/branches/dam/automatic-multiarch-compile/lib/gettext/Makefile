GARNAME = gettext
GARVERSION = 0.17
CATEGORIES = lib

DESCRIPTION = GNU gettext
define BLURB
endef

MASTER_SITES = $(GNU_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWggettext)

EXTRA_BUILD_ISAS_sparc = sparcv9
EXTRA_BUILD_ISAS_i386  = amd64

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --program-transform-name='s/^/g&/'

TEST_TARGET = check

include ../category.mk

LIBS = -lsec
export LIBS

post-install:
	@# Only CSWiconv should have lib/charset.alias in it
	@rm -f $(DESTDIR)$(libdir)/charset.alias
	@# Only CSWcommon should have share/locale/locale.alias in it
	@rm -f $(DESTDIR)$(sharedstatedir)/locale/locale.alias

