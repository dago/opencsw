NAME = zsh
VERSION = 5.0.8
CATEGORIES = devel
GARTYPE = v2

DESCRIPTION = Powerful UNIX shell
define BLURB
  Zsh is a shell designed for interactive use, although it is also a
  powerful scripting language. Many of the useful features of bash,
  ksh, and tcsh were incorporated into zsh; many original features were added.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTFILE _alternativesS += _pkgutil _mgar

PACKAGES = CSWzsh
CATALOGNAME_CSWzsh = zsh

LICENSE = LICENCE

RUNTIME_DEP_PKGS = CSWlibiconv2 CSWlibncursesw5 CSWlibpcre1 CSWlibgdbm4
BUILD_DEP_PKGS = CSWlibpcre-dev

SPKG_SOURCEURL = http://www.zsh.org
UPSTREAM_MASTER_SITES = http://www.zsh.org/pub/

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-maildir-support
CONFIGURE_ARGS += --enable-fndir=$(sharedstatedir)/$(NAME)/functions
CONFIGURE_ARGCONFIGURE_ARGS += --enable-etcdir=$(sysconfdir)
/CHECKPKG_OVERRIDES_CSWzsh += file-with-bad-content|/usr/local|root/opt/csw/bin/zsh
EXTRA_MERGE_EXCLUDE_FILES = /opt/csw/bin/zsh-$(VERSION)/sh/functions/mere

ETCSHELLS = /opt/csw/bin/zsh

include gar/category.mk

# Use term.h from ncurses or we get compile errors
#   http://www.zsh.org/mla/workers/2007/msg01236.html
CPPFLAGS := -I$(includedir)/ncursesw $(CPPFLAGS)

post-install-modulated:
	cp -p $(WORKDIR)/_pkgutil WORKDIR)/_alternatives $(DESTDIR)$(sharedstatedir)/$(NAME)/functions
	@$(MAKECOOKIE)
