PKGVERSION = 1.10.1
GARNAME = automake
GARVERSION ?= $(PKGVERSION)
CATEGORIES = devel

DESCRIPTION = A tool for automatically generating Makefiles.
define BLURB
    Automake is a tool for automatically generating Makefiles compliant with the
    GNU Coding Standards. It was inspired by the 4.4BSD make and include files, but
    aims to be portable and to conform to the GNU standards for Makefile variables
    and targets. Automake is a Perl script. The input files are called Makefile.am.
    The output files are called Makefile.in; They are intended for use with
    Autoconf. Automake requires certain things to be done in your configure.in.
    This package also includes the "aclocal" program. aclocal is a program to
    generate an 'aclocal.m4' based on the contents of 'configure.in'. It is useful
    as an extensible, maintainable mechanism for augmenting autoconf.
endef

OLD_VERSIONS = 1.6.3 1.7.9 1.8.5 1.9.6
ALL_VERSIONS = $(OLD_VERSIONS) $(PKGVERSION)

MASTER_SITES = $(GNU_MIRROR)
SOURCEFILES  = $(foreach VERSION, $(ALL_VERSIONS), $(GARNAME)-$(VERSION).tar.gz)
DISTFILES    = $(SOURCEFILES)
DISTFILES   += $(call admfiles,CSWautomake,depend)
DISTFILES   += README.CSW
NOEXTRACT    = $(filter-out $(GARNAME)-$(GARVERSION).tar.gz, $(SOURCEFILES))

COOKIEROOTDIR = cookies-$(GARVERSION)

# Move old documentation away
ifneq ($(GARVERSION), $(PKGVERSION))
  infodir = /ignore
endif

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

CLEAN_SCRIPTS = custom

include gar/category.mk

$(DOWNLOADDIR)/README.CSW:
	@echo " ==> Generating README.CSW"
	@(exec >$@;								\
	  echo "This package contains the following automake versions:";	\
	  for VERSION in $(ALL_VERSIONS); do					\
	    echo "  automake-$$VERSION";					\
	  done)

post-install:
	@rm -f $(DESTDIR)$(prefix)/share/info/dir
	@rm -f $(DESTDIR)$(bindir)/aclocal
	@gln -s aclocal-1.10 $(DESTDIR)$(bindir)/aclocal
	@rm -f $(DESTDIR)$(bindir)/automake
	@gln -s automake-1.10 $(DESTDIR)$(bindir)/automake
	@ginstall $(WORKDIR)/README.CSW $(DESTDIR)$(docdir)/$(GARNAME)/
	@$(MAKECOOKIE)

pre-package:
	@(for VERSION in $(OLD_VERSIONS); do gmake GARVERSION=$$VERSION install; done)
	@$(MAKECOOKIE)
	
clean-custom: clean-all
	@(for VERSION in $(OLD_VERSIONS); do gmake GARVERSION=$$VERSION clean-all; done)
