GARNAME = libtool
GARVERSION = 1.5.24
CATEGORIES = devel

DESCRIPTION = A generic library support tool.
define BLURB
  GNU libtool is a generic library support script. Libtool hides the complexity
  of using shared and static libraries behind a consistent, portable interface.
  Libtool supports building static libraries on all platforms.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWlibtool,depend prototype)
DISTFILES += $(call admfiles,CSWlibtool_rt,prototype)
DISTFILES += $(foreach ARCH,i386 sparc,$(ARCH)-gcc2.conf $(ARCH)-gcc2.tags $(ARCH)-gcc3.conf $(ARCH)-gcc3.tags)

TEST_TARGET = check

include ../category.mk

post-install:
	@echo " ==> Fixing install anomalies"
	@rm -f $(DESTDIR)$(infodir)/dir
	@(for f in gcc2.conf gcc2.tags gcc3.conf gcc3.tags; do				\
		ginstall $(WORKDIR)/$(GARCH)-$$f $(DESTDIR)$(datadir)/$(GARNAME)/$$f;	\
	done)
	@$(MAKECOOKIE)

