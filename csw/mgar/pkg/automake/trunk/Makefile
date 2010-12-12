NAME = automake
VERSION = 1.11.1
CATEGORIES = devel

EXTRA_MODULATORS = VERSION
MODULATIONS_VERSION = 1.6.3 1.7.9 1.8.5 1.9.6 1.10.3 1.11.1

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
SOURCEFILES = $(foreach VERSION,$(MODULATIONS_VERSION),$(NAME)-$(VERSION).tar.gz)
DISTFILES = $(SOURCEFILES)
POSTMSG = $(docdir)/automake/CSWautomake.postmsg
DISTFILES += $(notdir $(POSTMSG))
NOCHECKSUM = $(notdir $(POSTMSG))
NOEXTRACT = $(filter-out $(NAME)-$(VERSION).tar.gz, $(SOURCEFILES))

SPKG_SOURCEURL = http://www.gnu.org/software/automake/

RUNTIME_DEP_PKGS = CSWperl

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

# Lots of test fail on Solaris, but they are safe to ignore for now:
#   <http://lists.gnu.org/archive/html/bug-automake/2009-07/msg00001.html>
SKIPTEST ?= 1

ARCHALL = 1

$(foreach VERSION,$(MODULATIONS_VERSION),$(eval MERGE_SCRIPTS_isa-$(ISA)-garversion-$(VERSION) = copy-all))

# These are hardlinks to the versioned versions and will confuse the merging
EXTRA_MERGE_EXCLUDE_FILES_isa-sparcv8-garversion-1.6.3 = $(bindir)/automake $(bindir)/aclocal $(infodir)/.*
EXTRA_MERGE_EXCLUDE_FILES_isa-sparcv8-garversion-1.7.9 = $(bindir)/automake $(bindir)/aclocal $(infodir)/.*
EXTRA_MERGE_EXCLUDE_FILES_isa-sparcv8-garversion-1.8.5 = $(bindir)/automake $(bindir)/aclocal $(infodir)/.*
EXTRA_MERGE_EXCLUDE_FILES_isa-sparcv8-garversion-1.9.6 = $(bindir)/automake $(bindir)/aclocal $(infodir)/.*
EXTRA_MERGE_EXCLUDE_FILES_isa-sparcv8-garversion-1.10.3 = $(bindir)/automake $(bindir)/aclocal $(infodir)/.*

#     alternatives [options] --install link name path priority  [-
#     -slave link name path]...  [--initscript service]

ALTERNATIVES = 1.6 1.7 1.8 1.9 1.10 1.11
ALTERNATIVE_1.6 = $(bindir)/automake automake $(bindir)/automake-1.6 60
ALTERNATIVE_1.6 += $(bindir)/aclocal aclocal $(bindir)/aclocal-1.6
ALTERNATIVE_1.7 = $(bindir)/automake automake $(bindir)/automake-1.7 70
ALTERNATIVE_1.7 += $(bindir)/aclocal aclocal $(bindir)/aclocal-1.7
ALTERNATIVE_1.8 = $(bindir)/automake automake $(bindir)/automake-1.8 80
ALTERNATIVE_1.8 += $(bindir)/aclocal aclocal $(bindir)/aclocal-1.8
ALTERNATIVE_1.9 = $(bindir)/automake automake $(bindir)/automake-1.9 90
ALTERNATIVE_1.9 += $(bindir)/aclocal aclocal $(bindir)/aclocal-1.9
ALTERNATIVE_1.10 = $(bindir)/automake automake $(bindir)/automake-1.10 100
ALTERNATIVE_1.10 += $(bindir)/aclocal aclocal $(bindir)/aclocal-1.10
ALTERNATIVE_1.11 = $(bindir)/automake automake $(bindir)/automake-1.11 110
ALTERNATIVE_1.11 += $(bindir)/aclocal aclocal $(bindir)/aclocal-1.11

include gar/category.mk

$(DOWNLOADDIR)/$(notdir $(POSTMSG)):
	@echo " ==> Generating $(notdir $(POSTMSG))"
	@(exec >$@;								\
		echo "There are multiple versions of automake on the system installed:"; \
		echo; \
	  	for VERSION in $(MODULATIONS_VERSION); do \
		  echo "  * automake-$$VERSION"; \
		done; \
		echo; \
		echo "You can easily select between the versions with the alternatives(8)"; \
		echo "system by executing"; \
		echo; \
		echo "  /opt/csw/sbin/alternatives --config automake"; \
		echo; \
		echo "See http://www.opencsw.org/packages/alternatives for details."; \
	)
	@$(MAKECOOKIE)

post-merge:
	rm -f $(PKGROOT)$(bindir)/aclocal
	rm -f $(PKGROOT)$(bindir)/automake
	ginstall -d $(PKGROOT)$(dir $(POSTMSG))
	ginstall $(WORKDIR)/$(notdir $(POSTMSG)) $(PKGROOT)$(POSTMSG)
	@$(MAKECOOKIE)
