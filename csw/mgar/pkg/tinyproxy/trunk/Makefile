# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = tinyproxy
VERSION = 1.8.3
GARTYPE = v2

DESCRIPTION = Tinyproxy is a light-weight HTTP/HTTPS proxy daemon for POSIX operating systems
define BLURB
Tinyproxy is a light-weight HTTP/HTTPS proxy daemon for POSIX operating systems. Designed from the ground up to be fast and yet small, it is an ideal solution for use cases such as embedded deployments where a full featured HTTP proxy is required, but the system resources for a larger proxy are unavailable.
endef

MASTER_SITES = https://files.banu.com/tinyproxy/1.8/
DISTFILES  = $(DISTNAME).tar.bz2

GARCOMPILER = GNU

CONFIGURE_ARGS = $(DIRPATHS) --disable-silent-rules --disable-regexcheck
CHECKPKG_OVERRIDES_CSWtinyproxy += file-with-bad-content|/usr/local|root/etc/opt/csw/tinyproxy.conf
CHECKPKG_OVERRIDES_CSWtinyproxy += file-with-bad-content|/usr/share|root/etc/opt/csw/tinyproxy.conf

include gar/category.mk

