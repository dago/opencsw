# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = tlsinterposer
VERSION = 1.1.0
GARTYPE = v2

DESCRIPTION = OpenSSL library interposer to make existing binary software use more secure TLS protocol variants

MASTER_SITES = https://github.com/Netfuture/tlsinterposer/archive/
DISTFILES  = v$(VERSION).tar.gz

LICENSE = LICENSE.txt

BUILD_DEP_PKGS += CSWlibssl-dev

PACKAGES += CSWtlsinterposer
SPKG_DESC_CSWtlsinterposer = OpenSSL library interposer to make existing binary software use more secure TLS protocol variants
RUNTIME_DEP_PKGS_CSWtlsinterposer += CSWlibgcc-s1
# PKGFILES is catchall
# This is an interposing library, hence no SONAME
CHECKPKG_OVERRIDES_CSWtlsinterposer += no-direct-binding
CHECKPKG_OVERRIDES_CSWtlsinterposer += soname-equals-filename

# With Sun Studio there seems always be an immediate linking happening resulting in SSL_CTX_ctrl being undefined
GARCOMPILER = GNU

BUILD64 = 1
NORUNPATH = 1

# Make sure to use relocatable code
#EXTRA_CFLAGS += -xcode=pic13

# Do not use direct linking as it goes against lazy load for interposed libs
LINKER_DIRECT =
LINKER_IGNORE =

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

build-custom:
	#cd $(WORKSRC) && $(BUILD_ENV) $(CC) $(CPPFLAGS) $(CFLAGS) -c tlsinterposer.c
	#cd $(WORKSRC) && $(BUILD_ENV) $(CC) $(LDFLAGS) -G -o tlsinterposer.so tlsinterposer.o -ldl
	cd $(WORKSRC) && $(BUILD_ENV) $(CC) $(CPPFLAGS) $(CFLAGS) $(LDFLAGS) -g -Wall -fPIC -shared -o tlsinterposer.so tlsinterposer.c -ldl
	@$(MAKECOOKIE)

install-custom:
	ginstall -d -m 0755 $(DESTDIR)$(libdir)
	ginstall -D -m 0755 $(WORKSRC)/tlsinterposer.so $(DESTDIR)$(libdir)/tlsinterposer.so
	ginstall -d -m 0755 $(DESTDIR)$(docdir)/$(NAME)
	cd $(WORKSRC) && ginstall -D -m 0644 CHANGES.txt README.md $(DESTDIR)$(docdir)/$(NAME)
	cd $(WORKSRC) && ginstall -D -m 0644 TLS\ Interposer\ Logo.png $(DESTDIR)$(docdir)/$(NAME)/TLSInterposerLogo.png
	@$(MAKECOOKIE)

