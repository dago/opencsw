NAME = m4
VERSION = 1.4.17
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = GNU m4 Unix macro processor
define BLURB
  GNU M4 is an implementation of the traditional Unix macro processor.
  It is mostly SVR4 compatible although it has some extensions (for example,
  handling more than 9 positional parameters to macros). GNU m4 also has
  built-in functions for including files, running shell commands, doing arithmetic, etc.
endef

MASTER_SITES = $(GNU+= $(DISTNAME).tar.xz

VENDOR_URL = http://www.gnu.org/software/m4/

GARCOMPILER = SOS12U3
PACKAGING_PLATFORMS += solaris11-sparc solaris11-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

# Having a .git in $WORKSRC turns on developer mode and enabled gcc flags.
# Disable until this is fixed:
#   http://lists.gnu.org/archive/html/bug-m4/2013-09/msg00009.html
NOGITPATCH = 1

PACKAGES = CSWgm4

BUILD64 = 1
ISAEXEC = 1+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --program-prefix=g

# This must only be shipped by libiconv
EXTRA_MER.*E_FILES = $(libdir)/charset.alias

include gar/category.mk

post-install-modulated:
	@# Every package carries his own links in /opt/csw/gnu
	ginstall -d $(DESTDIR)$(prefix)/gnu
	$(foreach G,$(notdir $(wildcard $(DESTDIR)$(bindir)/*)),ln -s ../bin/$G $(DESTDIR)$(prefix)/gnu/$(patsubst g%,%,$G);