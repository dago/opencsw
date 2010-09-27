GARNAME = krb5
GARVERSION = 1.8.3
CATEGORIES = server

DESCRIPTION = MIT Kerberos 5
define BLURB
  Kerberos is a network authentication protocol. It is designed to
  provide strong authentication for client/server applications by
  using secret-key cryptography. A free implementation of this protocol
  is available from the Massachusetts Institute of Technology.
  Kerberos is available in many commercial products as well.
endef

MASTER_SITES = http://web.mit.edu/kerberos/dist/krb5/$(shell echo $(GARVERSION) | awk -F. '{print $$1"."$$2}')/
DISTFILES  = $(GARNAME)-$(GARVERSION)-signed.tar

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)-signed.tar

PATCHFILES  = patch-man2html-perl.patch
PATCHFILES += 0002-libintl-for-kproplog.patch
# PATCHFILES += 0003-local-libraries-first-when-linking.patch
PATCHFILES += 0004-libkdb_ldap-isblank-define.patch
PATCHFILES += 0005-Add-strings.h-to-setenv.c-for-strlen-and-other-stuff.patch

BUILD_DEP_PKGS = CSWtcl

PACKAGES = CSWkrb5lib CSWkrb5libdev

CATALOGNAME_CSWkrb5lib         = krb5_lib
CATALOGNAME_CSWkrb5libdev      = krb5_lib_dev

SPKG_DESC_CSWkrb5lib         = MIT Kerberos 5 core libraries
SPKG_DESC_CSWkrb5libdev      = MIT Kerberos 5 developer libraries

RUNTIME_DEP_PKGS_CSWkrb5libdev = CSWkrb5lib

LICENSE = doc/copyright.texinfo

CONFIGURE_SCRIPTS = $(WORKSRC)/src/configure

NOISAEXEC = 1
BUILD64 = 1

# We turn off almost everything as we are just interested in the library.
NODIRPATHS = --docdir
CONFIGURE_ARGS  = $(DIRPATHS)
# --enable-ipv6 is deprecated and autodetected
#CONFIGURE_ARGS += --enable-ipv6
CONFIGURE_ARGS += --enable-kdc-replay-cache --enable-dns-for-realm
CONFIGURE_ARGS += --disable-thread-support
CONFIGURE_ARGS += --disable-static --disable-profiled
CONFIGURE_ARGS += --without-ldap

CONFIGURE_ARGS-32 += --with-tcl=$(prefix)
CONFIGURE_ARGS-64 += --without-tcl
CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(MEMORYMODEL))

BUILD_SCRIPTS  = $(WORKSRC)/src/Makefile

TEST_SCRIPTS = $(WORKSRC)/src/Makefile
TEST_TARGET = check

SKIPTEST ?= 1

INSTALL_SCRIPTS = $(WORKSRC)/src/Makefile

PKGFILES_CSWkrb5lib  = $(PKGFILES_RT)
PKGFILES_CSWkrb5lib += $(datadir)/checkpkg/overrides/krb5_lib

PKGFILES_CSWkrb5libdev  = $(mandir)/man8/sserver.8
PKGFILES_CSWkrb5libdev += $(mandir)/man1/(sclient|krb5-config|compile_et)\.1
PKGFILES_CSWkrb5libdev += $(sbindir)/(uuserver|sserver|sim_server|gss-server)
PKGFILES_CSWkrb5libdev += $(includedir)/.*
PKGFILES_CSWkrb5libdev += $(bindir)/(uuclient|sim_client|sclient|krb5-config|gss-client|compile_et)

include gar/category.mk

# The flags must not contain additional spaces or the build freaks out
CFLAGS := $(strip $(CFLAGS) -L$(libdir) -D__EXTENSIONS__)
CXXFLAGS := $(strip $(CXXFLAGS) -D__EXTENSIONS__)
#LDFLAGS := $(strip $(LDFLAGS))

LD_OPTIONS =
EXTRA_LINKER_FLAGS = $(RUNPATH_LINKER_FLAGS)

post-extract-modulated:
	@# TODO: Check signature
	@cd $(WORKDIR) && (gzip -c -d $(GARNAME)-$(GARVERSION).tar.gz | tar xf -)
	@$(MAKECOOKIE)
