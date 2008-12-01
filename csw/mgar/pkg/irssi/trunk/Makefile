GARNAME = irssi
GARVERSION = 0.8.12
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
DISTFILES += $(call admfiles,CSWirssi, postinstall depend)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-ipv6
CONFIGURE_ARGS += --with-socks
CONFIGURE_ARGS += --with-bot
CONFIGURE_ARGS += --with-proxy
CONFIGURE_ARGS += --with-perl=module
CONFIGURE_ARGS += --with-perl-lib=vendor

GARCOMPILER = SUN
TEST_TARGET = check

# moving configuration file
post-install:
	(cd $(DESTDIR)$(prefix)/etc; \
	for i in irssi.conf; do \
		if [ -r "$$i" ]; then \
			echo "$$i -> $$i.CSW"; \
			mv "$$i" "$$i.CSW";     \
		fi \
	done)


include gar/category.mk
