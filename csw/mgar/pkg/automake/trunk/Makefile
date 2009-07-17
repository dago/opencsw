GARNAME = automake
GARVERSION = 1.11
CATEGORIES = devel

EXTRA_MODULATORS = GARVERSION
# Version 1.1.2 is the last to contain libflac.so.7 where most of the binaries depend on
MODULATIONS_GARVERSION = 1.6.3 1.7.9 1.8.5 1.9.6 1.10.2 1.11

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

MASTER_SITES = $(GNU_MIRROR)
SOURCEFILES = $(foreach VERSION,$(MODULATIONS_GARVERSION),$(GARNAME)-$(VERSION).tar.gz)
DISTFILES = $(SOURCEFILES)
DISTFILES += README.CSW
NOCHECKSUM = README.CSW
NOEXTRACT = $(filter-out $(GARNAME)-$(GARVERSION).tar.gz, $(SOURCEFILES))

REQUIRED_PKGS = CSWperl

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

# Lots of test fail on Solaris, but they are safe to ignore for now:
#   <http://lists.gnu.org/archive/html/bug-automake/2009-07/msg00001.html>
SKIPTEST = 1

ARCHALL = 1

$(foreach VERSION,$(MODULATIONS_GARVERSION),$(eval MERGE_SCRIPTS_isa-$(ISA)-garversion-$(VERSION) = copy-all))

#CLEAN_SCRIPTS = custom

include gar/category.mk

$(DOWNLOADDIR)/README.CSW:
	@echo " ==> Generating README.CSW"
	@(exec >$@;								\
	  echo "This package contains the following automake versions:";	\
	  for VERSION in $(MODULATIONS_GARVERSION); do					\
	    echo "  automake-$$VERSION";					\
	  done)

post-merge:
	@rm -f $(PKGROOT)$(bindir)/aclocal
	@gln -s aclocal-1.11 $(PKGROOT)$(bindir)/aclocal
	@rm -f $(PKGROOT)$(bindir)/automake
	@gln -s automake-1.11 $(PKGROOT)$(bindir)/automake
	@ginstall $(WORKDIR)/README.CSW $(PKGROOT)$(docdir)/$(GARNAME)/
	@$(MAKECOOKIE)
