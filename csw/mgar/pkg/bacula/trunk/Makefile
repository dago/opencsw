# $Id$
NAME = bacula
VERSION = 5.0.3
CATEGORIES = apps

DESCRIPTION = The Open Source Network Backup Solution
define BLURB
Bacula is a set of Open Source, enterprise ready, computer programs that permit you (or the system administrator) to manage backup, recovery, and verification of computer data across a network of computers of different kinds. Bacula is relatively easy to use and efficient, while offering many advanced storage management features that make it easy to find and recover lost or damaged files. In technical terms, it is an Open Source, enterprise ready, network based backup program. 
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(DISTNAME).tar.gz
PATCHFILES += 0001-Update-AC_INIT-use-to-make-configure-handle-docdir.patch

BUILD_DEP_PKGS  = CSWmysql5devel CSWiconv CSWtcpwrap CSWossldevel
BUILD_DEP_PKGS += CSWreadline CSWggettext-dev

RUNTIME_DEP_PKGS += CSWmtx
RUNTIME_DEP_PKGS += CSWtcpwrap
RUNTIME_DEP_PKGS += CSWfconfig
RUNTIME_DEP_PKGS += CSWlibatk
RUNTIME_DEP_PKGS += CSWlibintl8
RUNTIME_DEP_PKGS += CSWlibcairo
RUNTIME_DEP_PKGS += CSWzlib
RUNTIME_DEP_PKGS += CSWncurses
RUNTIME_DEP_PKGS += CSWreadline
RUNTIME_DEP_PKGS += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS += CSWpango
RUNTIME_DEP_PKGS += CSWperl
RUNTIME_DEP_PKGS += CSWosslrt
RUNTIME_DEP_PKGS += CSWftype2
RUNTIME_DEP_PKGS += CSWgtk2
RUNTIME_DEP_PKGS += CSWglib2

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-working-dir=$(localstatedir)/$(NAME)/working
CONFIGURE_ARGS += --with-libiconv-prefix=$(prefix)
CONFIGURE_ARGS += --with-libintl-prefix=$(prefix)
CONFIGURE_ARGS += --disable-conio
CONFIGURE_ARGS += --enable-readline
CONFIGURE_ARGS += --with-readline=$(prefix)
CONFIGURE_ARGS += --with-python=$(prefix)
CONFIGURE_ARGS += --with-tcp-wrappers=$(prefix)
CONFIGURE_ARGS += --with-openssl=$(prefix)
CONFIGURE_ARGS += --with-mysql=$(prefix)/mysql5
CONFIGURE_ARGS += --with-scriptdir=$(libexecdir_install)/$(NAME)
CONFIGURE_ARGS += --with-logdir=$(localstatedir)/log/$(NAME)
CONFIGURE_ARGS += --with-pid-dir=$(localstatedir)/run
CONFIGURE_ARGS += --with-subsys-dir=$(localstatedir)/run/subsys
CONFIGURE_ARGS += --enable-tray-monitor

EXTRA_INC += $(includedir)/ncursesw
EXTRA_LIB += $(libdir)/ncursesw

# no tests supplied.
TEST_SCRIPTS =

include gar/category.mk

pre-configure-modulated:
	@echo Re-generating configure so docdir works properly...
	@(cd $(WORKSRC); \
		autoconf --prepend-include=$(abspath $(WORKSRC))/autoconf \
			autoconf/configure.in > configure; \
        chmod 755 configure)
	@$(MAKECOOKIE)

post-merge:
	@(cd $(PKGROOT); rmdir tmp)
	@$(MAKECOOKIE)
