NAME = zsh
VERSION = 4.3.12
CATEGORIES = devel

DESCRIPTION = Powerful UNIX shell
define BLURB
  Zsh is a shell designed for interactive use, although it is also a
  powerful scripting language. Many of the useful features of bash,
  ksh, and tcsh were incorporated into zsh; many original features were added.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTFILES += _pkgutil _mgar

PACKAGES = CSWzsh
CATALOGNAME_CSWzsh = zsh

LICENSE = LICENCE

RUNTIME_DEP_PKGS = CSWiconv CSWlibncursesw5 CSWlibpcre0 CSWlibgdbm3 CSWcas-etcshells
BUILD_DEP_PKGS = CSWpcre

SPKG_SOURCEURL = http://www.zsh.org
UPSTREAM_MASTER_SITES = http://www.zsh.org/pub/

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-maildir-support
CONFIGURE_ARGS += --enable-fndir=$(sharedstatedir)/$(NAME)/functions
CONFIGURE_ARGS += --enable-pcre

CHECKPKG_OVERRIDES_CSWzsh += file-with-bad-content|/usr/share|root/opt/csw/share/zsh/functions/_units
CHECKPKG_OVERRIDES_CSWzsh += file-with-bad-content|/usr/share|root/opt/csw/share/zsh/functions/_hg
CHECKPKG_OVERRIDES_CSWzsh += file-with-bad-content|/usr/share|root/opt/csw/share/zsh/functions/_loadkeys
CHECKPKG_OVERRIDES_CSWzsh += file-with-bad-content|/usr/share|root/opt/csw/share/zsh/functions/_ecasound
CHECKPKG_OVERRIDES_CSWzsh += file-with-bad-content|/usr/share|root/opt/csw/share/zsh/functions/_path_commands
CHECKPKG_OVERRIDES_CSWzsh += file-with-bad-content|/usr/share|root/opt/csw/share/zsh/functions/_lintian
CHECKPKG_OVERRIDES_CSWzsh += file-with-bad-content|/usr/share|root/opt/csw/share/zsh/functions/_lsusb
CHECKPKG_OVERRIDES_CSWzsh += file-with-bad-content|/usr/share|root/opt/csw/share/zsh/functions/run-help
CHECKPKG_OVERRIDES_CSWzsh += file-with-bad-content|/usr/share|root/opt/csw/share/zsh/functions/_cdrdao
CHECKPKG_OVERRIDES_CSWzsh += file-with-bad-content|/usr/share|root/opt/csw/share/zsh/functions/_setxkbmap
CHECKPKG_OVERRIDES_CSWzsh += file-with-bad-content|/usr/local|root/opt/csw/share/zsh/functions/_units
CHECKPKG_OVERRIDES_CSWzsh += file-with-bad-content|/usr/local|root/opt/csw/bin/zsh-4.3.12
CHECKPKG_OVERRIDES_CSWzsh += file-with-bad-content|/usr/share|root/opt/csw/share/man/man1/zshcontrib.1
CHECKPKG_OVERRIDES_CSWzsh += file-with-bad-content|/usr/local|root/opt/csw/share/zsh/functions/_gcc
CHECKPKG_OVERRIDES_CSWzsh += file-with-bad-content|/usr/local|root/opt/csw/share/zsh/functions/_urls
CHECKPKG_OVERRIDES_CSWzsh += file-with-bad-content|/usr/local|root/opt/csw/share/zsh/functions/_path_files
CHECKPKG_OVERRIDES_CSWzsh += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/zshmisc.1
CHECKPKG_OVERRIDES_CSWzsh += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/zshmodules.1
CHECKPKG_OVERRIDES_CSWzsh += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/zshoptions.1
CHECKPKG_OVERRIDES_CSWzsh += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/zshcontrib.1
CHECKPKG_OVERRIDES_CSWzsh += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/zshparam.1
CHECKPKG_OVERRIDES_CSWzsh += file-with-bad-content|/usr/local|root/opt/csw/share/zsh/functions/_complete_tag
CHECKPKG_OVERRIDES_CSWzsh += file-with-bad-content|/usr/local|root/opt/csw/share/zsh/functions/_twisted
CHECKPKG_OVERRIDES_CSWzsh += file-with-bad-content|/usr/local|root/opt/csw/share/zsh/functions/compaudit
CHECKPKG_OVERRIDES_CSWzsh += file-with-bad-content|/usr/share|root/opt/csw/share/zsh/functions/mere

SPKG_CLASSES = none cswetcshells
ETCSHELLS = /opt/csw/bin/zsh

include gar/category.mk

# Use term.h from ncurses or we get compile errors
#   http://www.zsh.org/mla/workers/2007/msg01236.html
CPPFLAGS := -I$(includedir)/ncursesw $(CPPFLAGS)

post-install:
	cp -p $(WORKDIR)/_pkgutil $(WORKDIR)/_mgar $(DESTDIR)$(sharedstatedir)/$(NAME)/functions
