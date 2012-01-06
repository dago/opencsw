# $Id$
#
NAME = mozldap
MAJOR = 6
MINOR = 0
SUBMIN = 7
VERSION = $(MAJOR).$(MINOR).$(SUBMIN)
GARTYPE = v2
CATEGORIES = lib

NSPR_NAME = nspr
NSPR_VERSION = 4.6
NSS_NAME = nss
NSS_VERSION = 3.11
SVRCORE_NAME = svrcore
SVR_CORE_VERSION = 4.0.3

DESCRIPTION = Mozilla LDAP C-SDK
define BLURB
The Mozilla LDAP C SDK is a set of libraries that
allow applications to communicate with LDAP directory
servers.  These libraries are derived from the University
of Michigan and Netscape LDAP libraries.  They use Mozilla
NSPR and NSS for crypto.
endef

MASTER_SITES = http://ftp.mozilla.org/pub/mozilla.org/directory/c-sdk/releases/v6.0.7/src
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += COPYING

BUILD_DEP_PKGS = CSWlibsvrcore0-dev
PACKAGING_PLATFORMS += solaris10-sparc
PACKAGING_PLATFORMS += solaris10-i386
GARCOMPILER = SOS12U2

PACKAGES += CSWlibldap60
CATALOGNAME_CSWlibldap60 = libldap60
PKGFILES_CSWlibldap60 += $(call baseisadirs,$(libdir),libldap60\.so)
PKGFILES_CSWlibldap60 += $(call baseisadirs,$(libdir),libldap60\.so(\.\d+)*)
SPKG_DESC_CSWlibldap60 += $(DESCRIPTION), libldap60.so
RUNTIME_DEP_PKGS_CSWlibldap60 += CSWsasl
CHECKPKG_OVERRIDES_CSWlibldap60 += soname-equals-filename|file=/opt/csw/lib/libldap60.so
CHECKPKG_OVERRIDES_CSWlibldap60 += soname-equals-filename|file=/opt/csw/lib/sparcv9/libldap60.so
CHECKPKG_OVERRIDES_CSWlibldap60 += soname-equals-filename|file=/opt/csw/lib/amd64/libldap60.so

PACKAGES += CSWlibldif60
CATALOGNAME_CSWlibldif60 = libldif60
PKGFILES_CSWlibldif60 += $(call baseisadirs,$(libdir),libldif60\.so)
PKGFILES_CSWlibldif60 += $(call baseisadirs,$(libdir),libldif60\.so(\.\d+)*)
SPKG_DESC_CSWlibldif60 += $(DESCRIPTION), libldif60.so
CHECKPKG_OVERRIDES_CSWlibldif60 += soname-equals-filename|file=/opt/csw/lib/libldif60.so
CHECKPKG_OVERRIDES_CSWlibldif60 += soname-equals-filename|file=/opt/csw/lib/sparcv9/libldif60.so
CHECKPKG_OVERRIDES_CSWlibldif60 += soname-equals-filename|file=/opt/csw/lib/adm64/libldif60.so

PACKAGES += CSWlibprldap60
CATALOGNAME_CSWlibprldap60 = libprldap60
PKGFILES_CSWlibprldap60 += $(call baseisadirs,$(libdir),libprldap60\.so)
PKGFILES_CSWlibprldap60 += $(call baseisadirs,$(libdir),libprldap60\.so(\.\d+)*)
SPKG_DESC_CSWlibprldap60 += $(DESCRIPTION), libprldap60.so
RUNTIME_DEP_PKGS_CSWlibprldap60 += CSWlibnspr4
RUNTIME_DEP_PKGS_CSWlibprldap60 += CSWlibplc4
RUNTIME_DEP_PKGS_CSWlibprldap60 += CSWlibplds4
RUNTIME_DEP_PKGS_CSWlibprldap60 += CSWlibldap60
CHECKPKG_OVERRIDES_CSWlibprldap60 += soname-equals-filename|file=/opt/csw/lib/libprldap60.so
CHECKPKG_OVERRIDES_CSWlibprldap60 += soname-equals-filename|file=/opt/csw/lib/sparcv9/libprldap60.so
CHECKPKG_OVERRIDES_CSWlibprldap60 += soname-equals-filename|file=/opt/csw/lib/amd64/libprldap60.so

PACKAGES += CSWlibssldap60
CATALOGNAME_CSWlibssldap60 = libssldap60
PKGFILES_CSWlibssldap60 += $(call baseisadirs,$(libdir),libssldap60\.so)
PKGFILES_CSWlibssldap60 += $(call baseisadirs,$(libdir),libssldap60\.so(\.\d+)*)
SPKG_DESC_CSWlibssldap60 += $(DESCRIPTION), libssldap60.so
RUNTIME_DEP_PKGS_CSWlibssldap60 += CSWlibnspr4
RUNTIME_DEP_PKGS_CSWlibssldap60 += CSWlibnss3
RUNTIME_DEP_PKGS_CSWlibssldap60 += CSWlibplc4
RUNTIME_DEP_PKGS_CSWlibssldap60 += CSWlibplds4
RUNTIME_DEP_PKGS_CSWlibssldap60 += CSWlibldap60
RUNTIME_DEP_PKGS_CSWlibssldap60 += CSWlibprldap60
CHECKPKG_OVERRIDES_CSWlibssldap60 += soname-equals-filename|file=/opt/csw/lib/libssldap60.so
CHECKPKG_OVERRIDES_CSWlibssldap60 += soname-equals-filename|file=/opt/csw/lib/sparcv9/libssldap60.so
CHECKPKG_OVERRIDES_CSWlibssldap60 += soname-equals-filename|file=/opt/csw/lib/amd64/libssldap60.so

PACKAGES += CSWmozldap-tools
CATALOGNAME_CSWmozldap-tools= mozldap_tools
SPKG_DESC_CSWmozldap-tools += $(DESCRIPTION), command line utilities
PKGFILES_CSWmozldap-tools = $(call pkgfiles_bin,ldapsearch)
PKGFILES_CSWmozldap-tools = $(call pkgfiles_bin,ldapmodify)
PKGFILES_CSWmozldap-tools = $(call pkgfiles_bin,ldapdelete)
PKGFILES_CSWmozldap-tools = $(call pkgfiles_bin,ldapadd)
PKGFILES_CSWmozldap-tools = $(call pkgfiles_bin,ldapcmp)
PKGFILES_CSWmozldap-tools = $(call pkgfiles_bin,ldapcompare)
PKGFILES_CSWmozldap-tools = $(call pkgfiles_bin,ldappasswd)
PKGFILES_CSWmozldap-tools = $(call pkgfiles_etc,ldapfilter.conf)
PKGFILES_CSWmozldap-tools = $(call pkgfiles_etc,ldapsearchprefs.conf)
PKGFILES_CSWmozldap-tools = $(call pkgfiles_etc,ldaptemplates.conf)
PKGFILES_CSWmozldap-tools = $(call pkgfiles_etc,ldapfriendly)
RUNTIME_DEP_PKGS_CSWmozldap-tools += CSWlibssldap60
RUNTIME_DEP_PKGS_CSWmozldap-tools += CSWlibprldap60
RUNTIME_DEP_PKGS_CSWmozldap-tools += CSWlibldif60
RUNTIME_DEP_PKGS_CSWmozldap-tools += CSWlibldap60
RUNTIME_DEP_PKGS_CSWmozldap-tools += CSWlibnspr4
RUNTIME_DEP_PKGS_CSWmozldap-tools += CSWlibnss3
RUNTIME_DEP_PKGS_CSWmozldap-tools += CSWlibplc4
RUNTIME_DEP_PKGS_CSWmozldap-tools += CSWlibsvrcore0
RUNTIME_DEP_PKGS_CSWmozldap-tools += CSWsasl
RUNTIME_DEP_PKGS_CSWmozldap-tools += CSWlibplds4
RUNTIME_DEP_PKGS_CSWmozldap-tools += CSWlibiconv2

PACKAGES += CSWmozldap-dev
CATALOGNAME_CSWmozldap-dev = mozldap_dev
SPKG_DESC_CSWmozldap-dev += $(DESCRIPTION), development files
PKGFILES_DEVEL_SHAREDLIBLINK =
PKGFILES_CSWmozldap-dev = $(PKGFILES_DEVEL_INCLUDEDIR)
ARCHALL_CSWmozldap-dev = 1
RUNTIME_DEP_PKGS_CSWmozldap-dev += CSWlibssldap60
RUNTIME_DEP_PKGS_CSWmozldap-dev += CSWlibprldap60
RUNTIME_DEP_PKGS_CSWmozldap-dev += CSWlibldif60
RUNTIME_DEP_PKGS_CSWmozldap-dev += CSWlibldap60
# its a hack
CHECKPKG_OVERRIDES_CSWmozldap-dev += archall-devel-package

# Move the include files to include/nspr to prevent polluting the main
# header file namespace.

# override the standard paths
bindir=$(prefix)/bin/dirsrv
includedir=$(prefix)/include/dirsrv

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS_isa-sparcv9 = --enable-64bit
CONFIGURE_ARGS_isa-amd64 = --enable-64bit
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(MODULATION))
CONFIGURE_ARGS_OPT += --with-svrcore=$(prefix)
CONFIGURE_ARGS_OPT += --with-sasl
CONFIGURE_ARGS_OPT += --with-sasl-inc=$(prefix)/include/sasl
CONFIGURE_ARGS_OPT += --with-sasl-lib=$(libdir)
CONFIGURE_ARGS_OPT += --enable-clu
CONFIGURE_ARGS_OPT += --enable-optimize="-xO3"
CONFIGURE_ARGS_OPT += --disable-debug
CONFIGURE_ARGS_OPT += --enable-strip
CONFIGURE_ARGS_OPT += --with-nss-inc=$(prefix)/include/nss
CONFIGURE_ARGS_OPT += --with-nss-lib=$(libdir)
CONFIGURE_ARGS_OPT += --with-nspr-inc=$(prefix)/include/nspr
CONFIGURE_ARGS_OPT += --with-nspr-lib=$(libdir)
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GARFLAVOR))

CPPFLAGS=

CONFIGURE_SCRIPTS = c-sdk
BUILD_SCRIPTS = c-sdk
INSTALL_SCRIPTS = c-sdk
TEST_TARGET = 
TEST_SCRIPTS = 
BUILD64 = 1
EXTRA_LINKER_FLAGS = -liconv

configure-c-sdk:
	(cd $(WORKSRC) && mkdir -p build inst)
	(cd $(WORKSRC)/build && $(CONFIGURE_ENV) ../c-sdk/configure $(CONFIGURE_ARGS))
	@$(MAKECOOKIE)

build-c-sdk:
	(cd $(WORKSRC)/build && $(BUILD_ENV) gmake)

install-c-sdk:
	ginstall -m 755 -d $(DESTDIR)/$(bindir)
	ginstall -m 755 -d $(DESTDIR)/$(libdir)/pkgconfig
	ginstall -m 755 -d $(DESTDIR)/$(sysconfdir)
	ginstall -m 755 -d $(DESTDIR)/$(includedir)
	ginstall -m 755 $(WORKSRC)/../dist/lib/libldif60.so $(DESTDIR)$(libdir)
	ginstall -m 755 $(WORKSRC)/../dist/lib/libldap60.so $(DESTDIR)$(libdir)
	ginstall -m 755 $(WORKSRC)/../dist/lib/libprldap60.so $(DESTDIR)$(libdir)
	ginstall -m 755 $(WORKSRC)/../dist/lib/libssldap60.so $(DESTDIR)$(libdir)
	ginstall -m 755 $(WORKSRC)/../dist/bin/ldapsearch $(DESTDIR)$(bindir)
	ln -s $(DESTDIR)$(bindir)/ldapsearch $(DESTDIR)$(prefix)/bin/ldapsearch389
	ginstall -m 755 $(WORKSRC)/../dist/bin/ldapmodify $(DESTDIR)$(bindir)
	ln -s $(DESTDIR)$(bindir)/ldapmodify $(DESTDIR)$(prefix)/bin/ldapmodify389
	ginstall -m 755 $(WORKSRC)/../dist/bin/ldapdelete $(DESTDIR)$(bindir)
	ln -s $(DESTDIR)$(bindir)/ldapdelete $(DESTDIR)$(prefix)/bin/ldapdelete389
	ginstall -m 755 $(WORKSRC)/../dist/bin/ldapcmp $(DESTDIR)$(bindir)
	ln -s $(DESTDIR)$(bindir)/ldapcmp $(DESTDIR)$(prefix)/bin/ldapcmp389
	ginstall -m 755 $(WORKSRC)/../dist/bin/ldappasswd $(DESTDIR)$(bindir)
	ln -s $(DESTDIR)$(bindir)/ldappasswd $(DESTDIR)$(prefix)/bin/ldappasswd389
	ginstall -m 755 $(WORKSRC)/c-sdk/mozldap.pc.in $(DESTDIR)$(libdir)/pkgconfig
	@for f in $(WORKSRC)/../dist/etc/*; do \
		ginstall -m 644 $$f  $(DESTDIR)$(sysconfdir); \
	done
	@for f in $(WORKSRC)/../dist/public/ldap/*h; do \
		ginstall -m 644 $$f  $(DESTDIR)$(includedir); \
	done
	@gsed -i -e 's,%libdir%,$(libdir),g' \
          -e 's,%prefix%,$(prefix),g' \
          -e "s,%major%,$(MAJOR),g" \
          -e "s,%minor%,$(MINOR),g" \
          -e "s,%submin%,$(SUBMIN),g" \
          -e "s,%libsuffix%,$(libdir),g" \
          -e "s,%bindir%,$(bindir),g" \
          -e "s,%exec_prefix%,$(bindir),g" \
          -e "s,%includedir%,$(includedir),g" \
          -e "s,%NSPR_VERSION%,$(NSPR_VERSION),g" \
          -e "s,%NSS_VERSION%,$(NSS_VERSION),g" \
          -e "s,%SVRCORE_VERSION%,$(SVRCORE_VERSION),g" \
          -e "s,%MOZLDAP_VERSION%,$(VERSION),g" \
     		$(DESTDIR)/$(libdir)/pkgconfig/$(NAME).pc.in
	@mv $(DESTDIR)/$(libdir)/pkgconfig/$(NAME).pc.in $(DESTDIR)/$(libdir)/pkgconfig/$(NAME).pc
	@$(MAKECOOKIE)

include gar/category.mk
