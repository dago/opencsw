NAME = make
VERSION = 3.82
CATEGORIES = devel

DESCRIPTION = Controls generation of executables and other compile-related tasks
define BLURB
  GNU Make examines the timestamps on a set of interdependent files, and, if
  necessary, issues commands to bring them up-to-date. The user creates a
  makefile describing the files, their relationships, and the commands to run.
  Most often make is used to rebuild libraries and programs when their sources
  are changed, but it can be used for any situation where one set of files needs
  to be generated from another set.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(NAME)-$(VERSION).tar.bz2

VENDOR_URL = http://www.gnu.org/software/make/

PACKAGES = CSWgmake
SPKG_DESC_CSWgmake = GNU Make controls generation of executables and other compile-related tasks
RUNTIME_DEP_PKGS_CSWgmake += CSWlibintl8

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --program-prefix=g

# These are hardcoded fallback pathes for include (see read.c):
#   "/usr/gnu/include", "/usr/local/include", "/usr/include"
CHECKPKG_OVERRIDES_CSWgmake += file-with-bad-content|/usr/local|root/opt/csw/bin/gmake

# These are just examples
CHECKPKG_OVERRIDES_CSWgmake += file-with-bad-content|/usr/local|root/opt/csw/share/info/make.info-1
CHECKPKG_OVERRIDES_CSWgmake += file-with-bad-content|/usr/local|root/opt/csw/share/info/make.info-2

include gar/category.mk

post-install-modulated:
	ginstall -d $(DESTDIR)$(prefix)/gnu
	$(foreach G,$(notdir $(wildcard $(DESTDIR)$(bindir)/*)),ln -s ../bin/$G $(DESTDIR)$(prefix)/gnu/$(patsubst g%,%,$G);)
	@$(MAKECOOKIE)

