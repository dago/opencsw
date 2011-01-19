NAME = krb5
VERSION = 1.9
CATEGORIES = server

DESCRIPTION = MIT Kerberos 5
define BLURB
  Kerberos is a network authentication protocol. It is designed to
  provide strong authentication for client/server applications by
  using secret-key cryptography. A free implementation of this protocol
  is available from the Massachusetts Institute of Technology.
  Kerberos is available in many commercial products as well.
endef

MASTER_SITES = http://web.mit.edu/kerberos/dist/krb5/$(shell echo $(VERSION) | awk -F. '{print $$1"."$$2}')/
DISTFILES  = $(NAME)-$(VERSION)-signed.tar

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*)-signed.tar

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


PACKAGES += CSWlibcom-err3
CATALOGNAME_CSWlibcom-err3 = libcom_err3
PKGFILES_CSWlibcom-err3 +=  $(call baseisadirs,$(libdir),libcom_err\.so\.3(\.\d+)*)
SPKG_DESC_CSWlibcom-err3 += MIT Kerberos 5 core libraries, libcom_err.so.3

PACKAGES += CSWlibgssapi-krb5-2
CATALOGNAME_CSWlibgssapi-krb5-2 = libgssapi_krb5_2
PKGFILES_CSWlibgssapi-krb5-2 +=  $(call baseisadirs,$(libdir),libgssapi_krb5\.so\.2(\.\d+)*)
SPKG_DESC_CSWlibgssapi-krb5-2 += MIT Kerberos 5 core libraries, libgssapi_krb5.so.2

# This is a private library
#PACKAGES += CSWlibgssrpc4
#CATALOGNAME_CSWlibgssrpc4 = libgssrpc4
#PKGFILES_CSWlibgssrpc4 += $(call baseisadirs,$(libdir),libgssrpc\.so\.4(\.\d+)*)
#SPKG_DESC_CSWlibgssrpc4 += MIT Kerberos 5 core libraries, libgssrpc.so.4

PACKAGES += CSWlibk5crypto3
CATALOGNAME_CSWlibk5crypto3 = libk5crypto3
PKGFILES_CSWlibk5crypto3 += $(call baseisadirs,$(libdir),libk5crypto\.so\.3(\.\d+)*)
SPKG_DESC_CSWlibk5crypto3 += MIT Kerberos 5 core libraries, libk5crypto.so.3

# This is a private library
#PACKAGES += CSWlibkadm5clnt-mit7
#CATALOGNAME_CSWlibkadm5clnt-mit7 = libkadm5clnt_mit7
#PKGFILES_CSWlibkadm5clnt-mit7 += $(call baseisadirs,$(libdir),libkadm5clnt_mit\.so\.7(\.\d+)*)
#SPKG_DESC_CSWlibkadm5clnt-mit7 += MIT Kerberos 5 core libraries, libkadm5clnt_mit.so.7

# This is a private library
#PACKAGES += CSWlibkadm5srv-mit7
#CATALOGNAME_CSWlibkadm5srv-mit7 = libkadm5srv_mit7
#PKGFILES_CSWlibkadm5srv-mit7 += $(call baseisadirs,$(libdir),libkadm5srv_mit\.so\.7(\.\d+)*)
#SPKG_DESC_CSWlibkadm5srv-mit7 += MIT Kerberos 5 core libraries, libkadm5srv_mit.so.7

# This is a private library
#PACKAGES += CSWlibkdb5-4
#CATALOGNAME_CSWlibkdb5-4 = libkdb5_4
#PKGFILES_CSWlibkdb5-4 += $(call baseisadirs,$(libdir),libkdb5\.so\.4(\.\d+)*)
#SPKG_DESC_CSWlibkdb5-4 += MIT Kerberos 5 core libraries, libkdb5.so.4

PACKAGES += CSWlibkrb5-3
CATALOGNAME_CSWlibkrb5-3 = libkrb5_3
PKGFILES_CSWlibkrb5-3 += $(call baseisadirs,$(libdir),libkrb5\.so\.3(\.\d+)*)
SPKG_DESC_CSWlibkrb5-3 += MIT Kerberos 5 core libraries, libkrb5.so.3

PACKAGES += CSWlibkrb5support0
CATALOGNAME_CSWlibkrb5support0 = libkrb5support0
PKGFILES_CSWlibkrb5support0 += $(call baseisadirs,$(libdir),libkrb5support\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibkrb5support0 += MIT Kerberos 5 core libraries, libkrb5support.so.0

RUNTIME_DEP_PKGS_CSWkrb5libdev = CSWkrb5lib
RUNTIME_DEP_PKGS_CSWkrb5lib += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWkrb5lib += CSWlibgssapi-krb5-2
RUNTIME_DEP_PKGS_CSWkrb5lib += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWkrb5lib += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWkrb5lib += CSWlibkrb5support0

ARCHALL_CSWkrb5lib = 1
RUNTIME_DEP_PKGS_CSWlibgssapi-krb5-2 += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWlibgssapi-krb5-2 += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWlibgssapi-krb5-2 += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWlibgssapi-krb5-2 += CSWlibkrb5support0
RUNTIME_DEP_PKGS_CSWlibcom-err3 += CSWlibkrb5support0
RUNTIME_DEP_PKGS_CSWlibkrb5-3 += CSWlibkrb5support0
RUNTIME_DEP_PKGS_CSWlibkrb5-3 += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWlibkrb5-3 += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWlibk5crypto3 += CSWlibkrb5support0

RUNTIME_DEP_PKGS_CSWkrb5libdev += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWkrb5libdev += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWkrb5libdev += CSWlibgssapi-krb5-2
RUNTIME_DEP_PKGS_CSWkrb5libdev += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWkrb5libdev += CSWlibkrb5support0

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

PKGFILES_CSWkrb5lib  = NOFILES

PKGFILES_CSWkrb5libdev  = $(mandir)/man8/sserver.8
PKGFILES_CSWkrb5libdev += $(mandir)/man1/(sclient|krb5-config|compile_et)\.1
PKGFILES_CSWkrb5libdev += $(sbindir)/(uuserver|sserver|sim_server|gss-server)
PKGFILES_CSWkrb5libdev += $(includedir)/.*
PKGFILES_CSWkrb5libdev += $(bindir)/(uuclient|sim_client|sclient|krb5-config|gss-client|compile_et)

# This name is so old that there it is not recognized as devel-package
CHECKPKG_OVERRIDES_CSWkrb5libdev += surplus-dependency|CSWkrb5lib

# This is the "collect all" legacy lib, no other reason for the dependencies.
CHECKPKG_OVERRIDES_CSWkrb5lib += surplus-dependency|CSWlibkrb5support0
CHECKPKG_OVERRIDES_CSWkrb5lib += surplus-dependency|CSWlibcom-err3
CHECKPKG_OVERRIDES_CSWkrb5lib += surplus-dependency|CSWlibgssapi-krb5-2
CHECKPKG_OVERRIDES_CSWkrb5lib += surplus-dependency|CSWlibkrb5-3
CHECKPKG_OVERRIDES_CSWkrb5lib += surplus-dependency|CSWlibk5crypto3

include gar/category.mk

# The flags must not contain additional spaces or the build freaks out
CFLAGS := $(strip $(CFLAGS) -L$(libdir) -D__EXTENSIONS__)
CXXFLAGS := $(strip $(CXXFLAGS) -D__EXTENSIONS__)
#LDFLAGS := $(strip $(LDFLAGS))

LD_OPTIONS =
EXTRA_LINKER_FLAGS = $(RUNPATH_LINKER_FLAGS)

post-extract-modulated:
	@# TODO: Check signature
	@cd $(WORKDIR) && (gzip -c -d $(NAME)-$(VERSION).tar.gz | tar xf -)
	@$(MAKECOOKIE)
