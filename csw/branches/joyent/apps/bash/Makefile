GARNAME = bash
GARVERSION = 3.1
CATEGORIES = apps

DESCRIPTION = A sh-compatible command language interpreter
define BLURB
  LONG DESCRIPTION
  GNU Bash is an sh-compatible command language interpreter that executes commands read from the standard input or from a file. Bash also incorporates useful features from the Korn and C shells (ksh and csh). Bash is intended to be a conforming implementation of the IEEE POSIX Shell and Tools specification (IEEE Working Group 1003.2).
endef

MASTER_SITES = ftp://ftp.cwru.edu/pub/bash/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWbash,prototype postinstall postremove depend)
DISTFILES += changelog.CSW

PATCHDIRLEVEL = 2
PATCHFILES = $(shell cd files; for FILE in bash31-???.patch; do echo $$FILE; done)

CONFIGURE_ARGS = $(DIRPATHS)

include ../category.mk

# We touch these file to avoid aclocal/autoconf
# configure to be run again
pre-configure:
	touch $(WORKSRC)/aclocal.m4
	touch $(WORKSRC)/configure
	touch $(WORKSRC)/config.status

post-install:
	@ginstall -D $(WORKDIR)/changelog.CSW $(DESTDIR)$(docdir)/$(GARNAME)/changelog.CSW
	@ginstall -D $(WORKSRC)/README $(DESTDIR)$(docdir)/$(GARNAME)/README
	@ginstall -D $(WORKSRC)/doc/FAQ $(DESTDIR)$(docdir)/$(GARNAME)/FAQ

