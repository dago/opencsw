GARNAME = irssi
GARVERSION = 0.8.14
CATEGORIES = apps

DESCRIPTION = IRC client with IPv6, proxy, bot, socks and Perl support
define BLURB
	Irssi is a modular IRC client that currently has only text mode user
	interface, but 80-90% of the code isn't text mode specific, so other UIs
	could be created pretty easily. Also, Irssi isn't really even IRC
	specific anymore, there's already a working SILC module available.
	Support for other protocols like ICQ could be created some day too.
endef

MASTER_SITES = http://www.irssi.org/files/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_CLASSES = none cswcpsampleconf
PROTOTYPE_FILTER = awk '$$$$3 ~ /\/irssi.conf.CSW$$$$/ { $$$$2 = "cswcpsampleconf" } { print }'

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-ipv6
CONFIGURE_ARGS += --with-socks
CONFIGURE_ARGS += --with-bot
CONFIGURE_ARGS += --with-proxy
CONFIGURE_ARGS += --with-perl=module
CONFIGURE_ARGS += --with-perl-lib=vendor

EXTRA_MERGE_EXCLUDE_FILES = .*~ .*perllocal\.pod

REQUIRED_PKGS = CSWglib2
REQUIRED_PKGS += CSWiconv
REQUIRED_PKGS += CSWosslrt
REQUIRED_PKGS += CSWperl
REQUIRED_PKGS += CSWsunmath
REQUIRED_PKGS += CSWggettextrt
REQUIRED_PKGS += CSWcswclassutils

TEST_TARGET = check

# moving configuration file
post-install-modulated:
	(cd $(DESTDIR)$(prefix)/etc; \
	for i in irssi.conf; do \
		if [ -r "$$i" ]; then \
			echo "$$i -> $$i.CSW"; \
			mv "$$i" "$$i.CSW";     \
		fi \
	done)

include gar/category.mk
PATH := /opt/csw/gnu:$(PATH)
