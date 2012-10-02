# $Id$
NAME = nmh
VERSION = 1.5
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Powerful electronic mail handling system
define BLURB
 This is the nmh mail user agent, a command-line based mail reader that
 is powerful and extensible. Unlike most mail user agents, nmh is not a
 single program, rather it is a set of programs that are run from the
 shell. This allows the user to utilize the full power of the Unix
 shell in conjunction with nmh.
endef

MASTER_SITES = http://download.savannah.gnu.org/releases/$(NAME)/
DISTFILES  = nmh-$(VERSION).tar.gz
SPKG_SOURCEURL = http://www.nongnu.org/nmh/
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS += CSWlibreadline6 CSWlibiconv2
LICENSE = COPYRIGHT
PRESERVECONF = /etc/opt/csw/nmh/mts.conf

CONFIGURE_ARGS = --enable-pop --enable-masquerade='' --with-mts=sendmail \
  --prefix=$(prefix) --mandir=$(mandir) --datadir=$(datadir)/nmh \
  --libdir=$(libdir)/nmh --sysconfdir=$(sysconfdir)/nmh 
TEST_SCRIPTS =

EXTRA_MERGE_EXCLUDE_FILES = $(datadir)/doc/nmh/(contrib.*|INSTALL|COPYRIGHT|README.developers|README.manpages)

CHECKPKG_OVERRIDES_CSWnmh += file-with-bad-content|/usr/local|root/opt/csw/share/doc/nmh/FAQ
CHECKPKG_OVERRIDES_CSWnmh += file-with-bad-content|/usr/local|root/opt/csw/share/doc/nmh/MAIL.FILTERING
CHECKPKG_OVERRIDES_CSWnmh += file-with-bad-content|/export/home|root/opt/csw/share/doc/nmh/README-ATTACHMENTS


include gar/category.mk
