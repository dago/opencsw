NAME = xmlrpc-c
VERSION = 1.16.39
CATEGORIES = lib

DESCRIPTION = A lightweight RPC library based on XML and HTTP
define BLURB
	It's a spec and a set of implementations that allow software 
	running on disparate operating systems, running in different 
	environments to make procedure calls over the Internet.
	It's remote procedure calling using HTTP as the transport and 
	XML as the encoding. XML-RPC is designed to be as simple as possible, 
	while allowing complex data structures to be transmitted, 
	processed and returned.
endef

MASTER_SITES  = $(SF_MIRROR)
DISTFILES += $(DISTNAME).tgz
PATCHFILES += 0001-Remove-inclusion-of-curl-types.h.patch
PATCHFILES += 0002-Use-direct-unistd-for-close.patch

LICENSE = doc/COPYING
DOCFILES += CREDITS DEVELOPING HISTORY INSTALL SECURITY TESTING TODO

VENDOR_URL = http://xmlrpc-c.sourceforge.net

PACKAGES += CSWxmlrpc-c
SPKG_DESC_CSWxmlrpc-c = $(DESCRIPTION)

RUNTIME_DEP_PKGS_CSWxmlrpc-c  = CSWcurlrt CSWlibidn CSWoldaprt CSWosslrt CSWzlib

EXTRA_CPPFLAGS += -D__EXTENSIONS__

BUILD_OVERRIDE_VARS += CFLAGS_PERSONAL
BUILD_OVERRIDE_VAR_CFLAGS_PERSONAL = $(CFLAGS) $(CPPFLAGS)

TEST_OVERRIDE_VARS += LADD
TEST_OVERRIDE_VAR_LADD = $(LDFLAGS) -lm

BUILD64_LIBS_ONLY = 1

include gar/category.mk
