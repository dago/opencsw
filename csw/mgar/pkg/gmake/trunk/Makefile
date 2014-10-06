NAME = make
VERSION = 4.1
CATEGORIES = devel
GARTYPE = v2

DESCRIPTION = Controls generation of executables and other compile-related tasks
define BLURB
  GNU Make examines the timestamps on a set of interdependent files, and, if
  necessary, issues commands to bring them up-to-date. The user creates a
  makefile describing the files, their relationships, and the commands to run.
  Most often make is used to rebuild libraries and programs when their sources
  are changed, but it can be used for any situation where one set of files needs
  to be generated from another set.
endef

MASTER_SITMASTER_SITES += ftp://alpha.gnu.org/gnu/make/
DISTFILES = $(NAME)-$(VERSION).tar.bz2

VENDOR_URL = http://www.gnu.org/software/make/

EXTRA_MODULATORS += GUILE
MODULATIONS_GUILE = yes no.org/software/make/

PACKAGES = CSWgmake
SPKG_DESC_CSWgmake = GNU Make controls generation of executables and other compile-related tasks
RUNTIME_DEP_PKGS_CSWgma-program-prefix=g

# These are hardcoded fallback pathes for include (see read.c):
#   "/usr/gnu/include", "/usr/local/include", "/usr/include"
CHECKPKG_OVERRIDES_CSWgmake += file-with-bad-content|/usr/local|roo-noguilot/opt/csw/bin/gmake

# These are just examples
CHECKPKG_OVERRIDES_CSWgmake += file-with-bad-content|/usr/local|root/opt/csw/share/info/make.info-1
CHECKPKG_OVERRIDES_CSWgmake += file-with-bad-content|/usr/local|root/opt/csw/share# This is handled by alternatives
CHECKPKG_OVERRIDES_CSWgmake += file-needed-but-no-package-satisfies-it|/opt/csw/bin/gmake|CSWgmake|contains|symlink|/opt/csw/gnu/make|which|needs|the|target|file:|/opt/csw/bin/gmakerePACKAGES += CSWgmake-guile
SPKG_DESC_CSWgmake-guile = GNU Make with GUILE support
PKGFILES_CSWgmake-guile += $(bindir)/gmake-guile
RUNTIME_DEP_PKGS_CSWgmake-guile += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgmake-guile += CSWlibguile2-0-22
# Needed, but unknown to checkpkg
RUNTIME_DEP_PKGS_CSWgmake-guile += CSWgmake
CHECKPKG_OVERRIDES_CSWgmake-guile += surplus-dependency|CSWgmake

CHECKPKG_OVERRIDES_CSWgmake-guile += file-with-bad-content|/usr/local|root/opt/csw/bin/gmake-guile

# Guile was compiled with GCC, so make sure to use same here
GARCOMPILER = GNU

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --program-prefix=g

CONFIGURE_ARGS_guile-yes += --with-guile
CONFIGURE_ARGS_guile-no += --without-guile
CONFIGURE_ARGS += $(CONFIGURE_ARGS_guile-$(GUILE))

 MERGE_SCRIPTS_isa-default-guile-no = copy-all
MERGE_SCRIPTS_isa-default-guile-yes = copy-guile-only

EXTRA_PAX_ARGS_isa-default-guile-no += -s ",\($(bindir)/gmake\),\1-noguile,"

ALTERNATIVES_CSWgmake = noguile
ALTERNATIVES_CSWgmake-guile = guile
ALTERNATIVE_noguile = $(bindir)/gmake gmake $(bindir)/gmake-noguile 100
ALTERNATIVE_guile = $(bindir)/gmake gmake $(bindir)/gmake-guile 200

include gar/category.mk

post-installt-install-modulated:
	ginstall -d $(DESTDIR)$(prefix)/gnu
	$(foreach G,$(notdir $(wildcard $(DESTDIR)$(bindir)/*)),ln -s ../bin/$G $(DESTDIR)$(prefix)/gnu/$(patsubst g%,%,$G);merge-copy-guile-only:
	ginstall -d $(PKGROOT)$(bindir)
	ginstall $(INSTALLISADIR)$(bindir)/gmake $(PKGROOT)$(bindir)/gmake-guile
	@$(MAKECOOKIE)
