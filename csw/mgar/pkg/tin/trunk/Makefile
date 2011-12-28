NAME = tin
VERSION = 2.0.1
CATEGORIES = net

DESCRIPTION = Terminal-based news reader
define BLURB
  tin is an easy-to-use USENET news reader for the console using NNTP.
  It supports threading, scoring, different charsets, and many other
  useful things. It has also support for different languages.
endef

MASTER_SITES = ftp://ftp.tin.org/pub/news/clients/tin/stable/
DISTFILES = $(NAME)-$(VERSION).tar.bz2
DISTFILES += COPYING

BUILD_DEP_PKGS += CSWperl
BUILD_DEP_PKGS += CSWlibpcre-dev
BUILD_DEP_PKGS += CSWggettext-dev
BUILD_DEP_PKGS += CSWlibidn-dev
BUILD_DEP_PKGS += CSWlibicu-dev
BUILD_DEP_PKGS += CSWlibiconv-dev
BUILD_DEP_PKGS += CSWlibncurses-dev
BUILD_DEP_PKGS += CSWlibgsasl-dev

RUNTIME_DEP_PKGS_CSWtin += CSWperl
RUNTIME_DEP_PKGS_CSWtin += CSWlibpcre0
RUNTIME_DEP_PKGS_CSWtin += CSWlibintl8
RUNTIME_DEP_PKGS_CSWtin += CSWlibidn11
RUNTIME_DEP_PKGS_CSWtin += CSWlibicuuc48
RUNTIME_DEP_PKGS_CSWtin += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWtin += CSWlibncursesw5
RUNTIME_DEP_PKGS_CSWtin += CSWlibgsasl7

VENDOR_URL = http://www.tin.org/

# Old default is
#   #define TIN_DEFAULTS_BUILTIN "/etc/opt/tin","/etc/tin","/etc","/usr/local/lib/tin","/usr/local/lib","/usr/local/etc/tin","/usr/local/etc","/usr/lib/tin","/usr/lib",NULL
REINPLACEMENTS += tin_defaults_builtin
REINPLACE_MATCH_tin_defaults_builtin = (\#define\s+TIN_DEFAULTS_BUILTIN\s+).*
REINPLACE_WITH_tin_defaults_builtin = $$1 "/etc/opt/csw/tin","/opt/csw/etc/tin",NULL
REINPLACE_FILES_tin_defaults_builtin += include/tin.h

MAILCAP_PATH = ~/.mailcap:/etc/opt/csw/mailcap:/opt/csw/etc/mailcap
NEWS_PATH = /var/opt/csw/spool/news

# Old default is
#    ./src/rfc1524.c:#define DEFAULT_MAILCAPS "~/.mailcap:/etc/mailcap:/usr/etc/mailcap:/usr/local/etc/mailcap:/etc/mail/mailcap"
REINPLACEMENTS += default_mailcaps
REINPLACE_MATCH_default_mailcaps = (\#define\s+DEFAULT_MAILCAPS\s+).*
REINPLACE_WITH_default_mailcaps = $$1 "$(MAILCAP_PATH)"
REINPLACE_FILES_default_mailcaps += src/rfc1524.c

# These need to be adjusted:

# unstable9s% strings work/solaris9-sparc/pkgroot/opt/csw/share/man/man1/tin.1 | grep /usr/local
# 30 6 * * * /usr/local/bin/tin \-u
# .IR /usr/local/etc/mailcap
# .IR /usr/local/share/locale/${LC_MESSAGES}/LC_MESSAGES/tin.mo

# unstable9s% strings work/solaris9-sparc/pkgroot/opt/csw/share/man/man5/tin.5 | grep /usr/local
# .IR /usr/local/etc/mailcap
# \fI/usr/lib/news\fR, \fI/var/lib/news\fR, \fI/usr/local/lib/news\fR or
# .IR /usr/local/share/locale/$LC_MESSAGES/LC_MESSAGES/tin.mo

REINPLACEMENTS += tindir
REINPLACE_MATCH_tindir = /usr/local/bin/tin
REINPLACE_WITH_tindir = $(bindir)/tin
REINPLACE_FILES_tindir += doc/tin.1

REINPLACEMENTS += mailcap
REINPLACE_MATCH_mailcap = /usr/local/etc/mailcap
REINPLACE_WITH_mailcap = $(MAILCAP_PATH)
REINPLACE_FILES_mailcap += doc/tin.1
REINPLACE_FILES_mailcap += doc/tin.5

REINPLACEMENTS += locale
REINPLACE_MATCH_locale = /usr/local/share/locale
REINPLACE_WITH_locale = $(sharedstatedir)/locale
REINPLACE_FILES_locale += doc/tin.1
REINPLACE_FILES_locale += doc/tin.5

REINPLACEMENTS += news_path
REINPLACE_MATCH_news_path = \\fI/usr/lib/news.*news\\fR
REINPLACE_WITH_news_path = \\fI$(NEWS_PATH)\\fR
REINPLACE_FILES_news_path += doc/tin.5

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-coffee
CONFIGURE_ARGS += --enable-ipv6
CONFIGURE_ARGS += --with-screen=ncursesw --with-curses-dir=$(prefix)
CONFIGURE_ARGS += --with-pcre=$(prefix)
CONFIGURE_ARGS += --x-includes=/usr/openwin/include
CONFIGURE_ARGS += --x-libraries=/usr/openwin/lib 
CONFIGURE_ARGS += --with-x --with-Xaw3d
CONFIGURE_ARGS += --with-libdir=$(libdir)/news
CONFIGURE_ARGS += --with-spooldir=$(NEWS_PATH)

# tin requires to run 'make build'
BUILD_ARGS = build

# tin doesn't have a test target
TEST_SCRIPTS =

# These are provided by CSWmutt-base
EXTRA_MERGE_EXCLUDE_FILES += $(mandir)/man5/mmdf\.5
EXTRA_MERGE_EXCLUDE_FILES += $(mandir)/man5/mbox\.5

include gar/category.mk

post-extract-modulated:
	@# This is most certainly an upstream typo
	-cp po/Makefile.inn po/Makefile.in
