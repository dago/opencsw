# $Id$
NAME = lighttpd
VERSION = 1.4.28
CATEGORIES = devel

DESCRIPTION = lighttpd - Security, speed, compliance, and flexibility http server
define BLURB
  Security, speed, compliance, and flexibility -- all of these describe lighttpd
  (pron. lighty) which is rapidly redefining efficiency of a webserver; as it is
  designed and optimized for high performance environments. With a small memory
  footprint compared to other web-servers, effective management of the cpu-load,
  and advanced feature set (FastCGI, SCGI, Auth, Output-Compression,
  URL-Rewriting and many more) lighttpd is the perfect solution for every server
  that is suffering load problems. And best of all it's Open Source licensed
  under the revised BSD license. 
endef

MASTER_SITES = http://download.lighttpd.net/lighttpd/releases-1.4.x/
DISTFILES    = $(NAME)-$(VERSION).tar.gz
EXTRA_LIB = $(prefix)/lib
EXTRA_LDFLAGS += -lsendfile

# To fix undefined symbol 'dlopen' on Solaris 9
EXTRA_LDFLAGS_5.9 += -ldl
EXTRA_LDFLAGS += $(EXTRA_LDFLAGS_$(GAROSREL))

PATCHFILES += 0001-Work-around-linking-problem-buffer.c.patch

# The module compilation ignores LDFLAGS by default, let's force them to
# inject the right -R flag.
PATCHFILES += 0002-Force-LDFLAGS-on-mod_compress.patch

# There's a thread started on lighttpd forums about the issue:
# http://redmine.lighttpd.net/boards/2/topics/4163

# lighttpd puts its modules under libdir, so we pass libdir as a subdirectory,
# because modules are not supposed to be in /opt/csw/lib.
libdir = $(prefix)/lib/lighttpd

CONFIGURE_ARGS  = $(DIRPATHS)
# Solaris 9 does not have IPV6_V6ONLY.
# IPv6 support only works on Solaris 10.
CONFIGURE_ARGS_5.9 = --disable-ipv6
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GAROSREL))

PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386                                                                          
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

# One test is still failing.
TEST_TARGET = check

include gar/category.mk
