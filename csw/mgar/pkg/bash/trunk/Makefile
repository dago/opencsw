GARNAME = bash
GARVERSION = 3.2
PATCHLEVEL = 48
CATEGORIES = devel

DESCRIPTION = A sh-compatible command language interpreter
define BLURB
  GNU Bash is an sh-compatible command language interpreter that executes commands read from the standard input or from a file. Bash also incorporates useful features from the Korn and C shells (ksh and csh). Bash is intended to be a conforming implementation of the IEEE POSIX Shell and Tools specification (IEEE Working Group 1003.2).
endef

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = bash-(\d+\.\d+).tar.gz $(PATCHFILE_PREFIX)-(\d+)

# Patches download location
MASTER_SITES = $(GNU_MIRROR)/bash-$(GARVERSION)-patches/
# Main archive location
MASTER_SITES += $(GNU_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWbash,prototype postinstall postremove depend)
DISTFILES += changelog.CSW

PATCHFILE_PREFIX = bash$(subst .,,$(GARVERSION))
PATCHDIRLEVEL = 0
# we generate the list of patches from the PATCHLEVEL
PATCHFILES = $(shell LEVEL=1; \
	        PREFIX_0="00"; \
	     	while [ $$LEVEL -le $(PATCHLEVEL)  ]; do \
			echo $(PATCHFILE_PREFIX)-$$PREFIX_0$$LEVEL; \
			LEVEL=`expr $$LEVEL + 1`; \
			if [ $$LEVEL -ge 10 ]; then \
				PREFIX_0="0"; \
			fi; \
		done )

PATCHFILES += use_system_bashrc_and_logout.patch


CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

# We touch these file to avoid aclocal/autoconf
# configure to be run again
pre-configure:
	touch $(WORKSRC)/aclocal.m4
	touch $(WORKSRC)/configure
	touch $(WORKSRC)/config.status


post-install:
	@( for FILE in README RBASH NEWS NOTES POSIX AUTHORS doc/FAQ doc/INTRO; do \
		 ginstall -D $(WORKSRC)/$$FILE $(DESTDIR)$(docdir)/$(GARNAME)/`basename $$FILE`; \
	done )

