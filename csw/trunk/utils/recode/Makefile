GARNAME = recode
GARVERSION = 3.6
CATEGORIES = utils

DESCRIPTION = GNU recode character set conversion
define BLURB
  The program recognizes or produces approx. 150 character
  sets and can convert almost any character set to almost
  any other. When exact translations are not possible, the
  program may get rid of offending characters or use approximations.
  Particular attention has been paid to the proper representation
  of French language diacritics.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz 
DISTFILES += $(call admfiles,CSWrecode,)

CONFIGURE_ARGS = $(DIRPATHS) \
	--enable-static=no

#TEST_TARGET = check
TEST_TARGET =

post-install:
	@echo " ==> Removing charset.alias"
	@rm -f $(DESTDIR)$(libdir)/charset.alias
	@echo " ==> Removing info/dir"
	@rm -f $(DESTDIR)$(infodir)/dir
	@$(MAKECOOKIE)

include ../category.mk

LDFLAGS += -lintl
