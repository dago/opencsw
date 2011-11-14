# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = inetutils
VERSION = 1.8.150-c548
GARTYPE = v2
CATEGORIES = net

DESCRIPTION = Inetutils is a collection of common network programs
define BLURB
Inetutils is a collection of common network programs. It includes:
An ftp client and server.
A telnet client and server.
An rsh client and server.
An rlogin client and server.
A tftp client and server.
And much more...
Most of them are improved versions of programs originally from BSD. Some others are original versions, written from scratch.
endef

MASTER_SITES = http://daily.josefsson.org/$(NAME)/
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0001-Handle-missing-sethostname-prototype-on-Solaris.patch

BUILD_DEPS += CSWlibncurses-dev
BUILD_DEPS += CSWlibkrb5-dev

CONFIGURE_ARGS = $(DIRPATHS)
# CONFIGURE_ARGS += --enable-encryption
# CONFIGURE_ARGS += --enable-authentication
# CONFIGURE_ARGS += --with-krb5
CONFIGURE_ARGS += --with-wrap=/opt/csw
CONFIGURE_ARGS += --with-pam
CONFIGURE_ARGS += --with-ncurses-include-dir=/opt/csw/include/ncursesw

include gar/category.mk

