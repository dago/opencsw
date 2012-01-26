# $Id$
NAME = bitlbee
VERSION = 1.2.8
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = An IRC to other chat networks gateway
define BLURB
  BitlBee brings IM (instant messaging) to IRC clients. It's a great solution for people who have an
  IRC client running all the time and don't want to run an additional MSN/AIM/whatever client.
  BitlBee currently supports the following IM networks/protocols: XMPP/Jabber (including Google Talk),
  MSN Messenger, Yahoo! Messenger, AIM and ICQ.
endef

MASTER_SITES = http://get.bitlbee.org/src/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# Use these patches until this is fixed:
#   http://bugs.bitlbee.org/bitlbee/ticket/667
PATCHFILES  = 0001-Do-not-use-gcc-specific-Wall.patch
PATCHFILES += 0002-Use-putenv-instead-of-setenv.patch
PATCHFILES += 0003-Remove-more-GCC-specific-Wall.patch
PATCHFILES += 0004-Use-inttypes.h-instead-of-stdint.h.patch
PATCHFILES += 0005-Do-not-return-values-in-void-functions-and-make-seco.patch
PATCHFILES += 0006-Remove-definition-on-Solaris-confusing-includes.patch

# This must be patched in at this place as the includes of the local dirs must come before
# the one we set for OpenCSW
PATCHFILES += 0007-Honour-CPPFLAGS.patch

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

BUILD_DEP_PKGS = CSWossldevel CSWlibevent-devel CSWggettext CSWglib2devel
RUNTIME_DEP_PKGS = CSWosslrt CSWlibevent CSWggettextrt CSWglib2

sysconfdir = /etc/opt/csw
localstatedir = /var/opt/csw

CONFIGURE_SCRIPTS = custom
CONFIGURE_ARGS  = --prefix=$(prefix)
CONFIGURE_ARGS += --etcdir=$(sysconfdir)
CONFIGURE_ARGS += --pidfile=/var/run/bitlbee.pid
CONFIGURE_ARGS += --config=$(localstatedir)/bitlbee/
CONFIGURE_ARGS += --ipcsocket=/var/run/bitlbee.sock
CONFIGURE_ARGS += --ssl=openssl --events=libevent

# Critical check.h is missing on Solaris
SKIPTEST ?= 1
PRESERVECONF = $(sysconfdir)/bitlbee.conf

include gar/category.mk

configure-custom:
	@echo " ==> Running configure in $*"
	cd $(WORKSRC) && $(CONFIGURE_ENV) bash ./configure $(CONFIGURE_ARGS)
	@$(MAKECOOKIE)

# Make sure the right install is in place
install-%/Makefile: PATH:=/usr/ucb:$(PATH)

post-install-modulated:
	ginstall -d $(DESTDIR)$(sysconfdir)
	ginstall $(WORKSRC)/bitlbee.conf $(DESTDIR)$(sysconfdir)/bitlbee.conf.CSW
	@$(MAKECOOKIE)
