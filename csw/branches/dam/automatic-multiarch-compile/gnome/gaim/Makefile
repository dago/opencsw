GARNAME = gaim
GARVERSION = 2.0.0beta3
CATEGORIES = gnome

DESCRIPTION = A GTK2-based instant messaging client.
define BLURB
	Gaim is a GTK2-based instant messenger application. It supports multiple
	protocols via modules, including AIM, ICQ, Yahoo!, MSN, Jabber, IRC,
	Napster, Gadu-Gadu and Zephyr. It has many common features found in other
	clients, as well as many unique features. Gaim is not endorsed by or
	affiliated with AOL TimeWarner, Microsoft, or Yahoo.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.bz2

ifneq ($(BUILD_XDEPS),0)
LIBDEPS = lib/libao
endif

CONFIGURE_ARGS = $(DIRPATHS)

include ../category.mk
