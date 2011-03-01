# $Id$
NAME = lighttpd
VERSION = 1.4.28
CATEGORIES = devel

DESCRIPTION = HTTP server built for security, speed, compliance, and flexibility
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

PATCHFILES += 0001-Work-around-linking-problem-buffer.c.patch

# When mkdir is issued on an automounted directory like /home/<someuser> errno is
# set to ENOSYS halting recursive directory generation. This patches handles
# ENOSYS similar to EEXIST and just continues with the creation which then may
# or may not work later on.
#
# There's a thread started on lighttpd forums about the issue:
#   http://redmine.lighttpd.net/boards/2/topics/4163
PATCHFILES += 0003-Ignore-ENOSYS-on-mkdir-which-happens-on-automounted-.patch

PACKAGES += CSWlighttpd
CATALOGNAME_CSWlighttpd = lighttpd
SPKG_DESC_CSWlighttpd = HTTP server built for security, speed, compliance, and flexibility
RUNTIME_DEP_PKGS_CSWlighttpd += CSWlibpcre0
RUNTIME_DEP_PKGS_CSWlighttpd += CSWbzip2
RUNTIME_DEP_PKGS_CSWlighttpd += CSWzlib

EXTRA_LINKER_FLAGS += -lsendfile

# To fix undefined symbol 'dlopen' on Solaris 9
EXTRA_LINKER_FLAGS_5.9 += -ldl
EXTRA_LINKER_FLAGS += $(EXTRA_LINKER_FLAGS_$(GAROSREL))

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
