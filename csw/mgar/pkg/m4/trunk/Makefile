NAME = m4
VERSION = 1.4.16
CATEGORIES = utils

DESCRIPTION = GNU m4 Unix macro processor
define BLURB
  GNU M4 is an implementation of the traditional Unix macro processor.
  It is mostly SVR4 compatible although it has some extensions (for example,
  handling more than 9 positional parameters to macros). GNU m4 also has
  built-in functions for including files, running shell commands, doing arithmetic, etc.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.xz

PACKAGES = CSWgm4

SPKG_SOURCEURL = http://www.gnu.org/software/m4/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --program-prefix=g

# This must only be shipped by libiconv
EXTRA_MERGE_EXCLUDE_FILES = $(libdir)/charset.alias

include gar/category.mk

post-install-modulated:
	@# Every package carries his own links in /opt/csw/gnu
	ginstall -d $(DESTDIR)$(prefix)/gnu
	$(foreach G,$(notdir $(wildcard $(DESTDIR)$(bindir)/*)),ln -s ../bin/$G $(DESTDIR)$(prefix)/gnu/$(patsubst g%,%,$G);)
	@$(MAKECOOKIE)

