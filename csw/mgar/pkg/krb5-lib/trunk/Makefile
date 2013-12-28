# $Id$
#
# ! The build links against the version of libkdb5 installed in the system,
# instead of the one built.
#

NAME    = krb5
VERSION = 1.11.4
CATEGORIES = server
GARTYPE = v2

DESCRIPTION = MIT Kerberos 5 core libraries
define BLURB
  Kerberos is a network authentication protocol. It is designed to
  provide strong authentication for client/server applications by
  using secret-key cryptography. A free implementation of this protocol
  is available from the Massachusetts Institute of Technology.
  Kerberos is available in many commercial products as well.
endef

MASTER_SITES = http://web.mit.edu/kerberos/dist/krb5/$(shell echo $(VERSION) | awk -F. '{print $$1"."$$2}')/
DISTFILES  = $(NAME)-$(VGARCOMPILER = GCC4

BUILD_DEP_PKGS += CSWggettext
BUILD_DEP_PKGS += CSWtcl
 = Unused package 4

PACKAGES += CSWlibkrb5-dev
SPKG_DESC_CSWlibkrb5-dev      = MIT Kerberos 5 developer libraries
RUNTIME_DEP_PKGS_CSWlibkrb5-dev += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWlibkrb5-dev += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWlibkrb5-dev += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWlibkrb5-dev += CSWlibkrb5support0
RUNTIME_DEP_PKGS_CSWlverto0v += CSWlibkrb5-priv
PKGFILES_CSWlibkrb5-dev  = $(mandir)/man8/sserver.8
PKGFILES_CSWlibkrb5-dev += $(mandir)/man1/(sclient|krb5-config|compile_et)\.1
PKGFILES_CSWlibkrb5-dev += $(sbindir)/(uuserver|sserver|sim_server|gss-server)
PKGFILES_CSWlibkrb5-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibkrb5-dev += $(bindir)/(uuclient|sim_client|sclient|krb5-config|gssRUNTIME_DEP_PKGS_CSWlibkrb5-dev += CSWlibintl8s-client|compile_et)
OBSOLETED_BY_CSWlibkrb5-dev = CSWkrb5libdev
CATALOGNAME_CSWkrb5libdev # On unstable10x, that lib does not appear to be linked
#CHECKPKG_OVERRIDES_CSWlibkrb5-dev += surplus-dependency|CSWlibintl8 /man/man8/sserver.8

PACKAGES += CSWlibcom-err3
CATALOGNAME_CSWlibcom-err3 = libcom_err3
PKGFILES_CSWlibcom-err3 +=  $(call baseisadirs,$(libdir),libcom_err\.so\.3(\.\d+)*)
SPKG_DESC_CSWlibcom-err3 += MIT Kerberos 5 core libraries, libcom_err.so.3
OBSOLETED_BY_CSWlibcom-err3 = CSWkrb5lib
RUNTIME_DEP_PKGS_CSWlibcom-err3 +=RUNTIME_DEP_PKGS_CSWlibcom-err3 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibcom-err3 += CSWlibgcc-s1= #PACKAGES += CSWlibgssapi-krb5-2
#CATALOGNAME_CSWlibgssapi-krb5-2 = libgssapi_krb5_2
# = libgssapi_krb5_2
PKGFILES_CSWlibgssapi-krb5-2 +=  $(call baseisadirs,$(libdir),libgssapi_k#SPKG_DESC_CSWlibgssapi-krb5-2 += MIT Kerberos 5 core libraries, libgssapi_krb5.so.2
#OBSOLETED_BY_CSWlibgssapi-krb5-2 = CSWkrb5lib
#RUNTIME_DEP_PKGS_CSWlibgssapi-krb5-2 += CSWlibkrb5-3
#RUNTIME_DEP_PKGS_CSWlibgssapi-krb5-2 += CSWlibcom-err3
#RUNTIME_DEP_PKGS_CSWlibgssapi-krb5-2 += CSWlibk5crypto3
#RUNTIME_DEP_PKGS_CSWlibgssapi-krb5-2 += CSWlibkrb5support0
#RUNTIME_DEP_PKGS_CSWlibgssapi-krb5-2 += CSWlibintl8
#RUNTIME_DEP_PKGS_CSWlibgssapi-krb5-2 += CSWlibgcc-s1= CSWlibkrb5support0

PACKAGES += CSWlibk5crypto3
CATALOGNAME_CSWlibk5crypto3 = libk5crypto3
PKGFILES_CSWlibk5crypto3 += $(call baseisadirs,$(libdir),libk5crypto\.so\.3(\.\d+)*)
SPKG_DESC_CSWlibk5crypto3 += MIT Kerberos 5 core libraries, libk5crypto.so.3
RUNTIME_DEP_PKGS_CSWlibk5crypto3 +=RUNTIME_DEP_PKGS_CSWlibk5crypto3 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibk5crypto3 += CSWlibgcc-s1= CSWlibkrb5support0
OBSOLETED_BY_CSWlibk5cr# It would be nice to have this as a separate package again, but the deps
# are difficult to handle without a full Kerberos package
#PACKAGES += CSWlibkrb5-priv
# += CSWlibkrb5-priv
SPKG_DESC_CSWlibkrb5-priv = Kerberos private shared libraries, do not link a#PKGFILES_CSWlibkrb5-priv += $(call baseisadirs,$(libdir),libgssrpc\.so\.\d+(\.\d+)*)
#PKGFILES_CSWlibkrb5-priv += $(call baseisadirs,$(libdir),libkadm5clnt_mit\.so\.\d+(\.\d+)*)
#t\.so\.\d+(\.\d+)*)
PKGFILES_CSWlibkrb5-priv += $(call baseisadirs,$(libdir),libkadm5srv_mi#PKGFILES_CSWlibkrb5-priv += $(call baseisadirs,$(libdir),libkdb5\.so\.\d+(\.\d+)*)
#PKGFILES_CSWlibkrb5-priv += $(call baseisadirs,$(libdir),krb5.*)
## Private libraries in one common package.
#CHECKPKG_OVERRIDES_CSWlibkrb5-priv += shared-lib-pkgname-mismatch
#CHECKPKG_OVERRIDES_CSWlibkrb5-priv += soname-not-part-of-filename
#RUNTIME_DEP_PKGS_CSWlibkrb5-priv += CSWlibssl1-0-0
#RUNTIME_DEP_PKGS_CSWlibkrb5-priv += CSWlibgssapi-krb5-2
#RUNTIME_DEP_PKGS_CSWlibkrb5-priv += CSWlibkrb5support0
#RUNTIME_DEP_PKGS_CSWlibkrb5-priv += CSWlibcom-err3
#RUNTIME_DEP_PKGS_CSWlibkrb5-priv += CSWlibk5crypto3
#RUNTIME_DEP_PKGS_CSWlibkrb5-priv += CSWlibintl8
#RUNTIME_DEP_PKGS_CSWlibkrb5-priv += CSWlibgcc-s1
#versions-in-package

PACKAGES += CSWlibkrb5-3
CATALOGNAME_CSWlibkrb5-3 = libkrb5_3
PKGFILES_CSWlibkrb5-3 += $(call baseisadirs,$(libdir),libkPKGFILES_CSWlibkrb5-3 += $(sysconfdir)/krb5.conf
PKGFILES_CSWlibkrb5-3 += $(mandir)/man5/krb5.conf.5k# Include this lib in this package
PKGFILES_CSWlibkrb5-3 += $(call baseisadirs,$(libdir),libgssapi_krb5\.so\.2(\.\d+)*)k# Include the private bits in this package
PKGFILES_CSWlibkrb5-3 += $(call baseisadirs,$(libdir),libgssrpc\.so\.\d+(\.\d+)*)
PKGFILES_CSWlibkrb5-3ILES_CSWlibkrb5-priv += $(call baseisadirs,$(libdir),libkadm5clnt_mit\.so\.\d+(\.\d+)*)
3 += $(call baseisadirs,$(libdir),libkadm5srv_mit\.so\.\d+(\.\d+)*)
PKGFILES_CSWlibkrb5-3 += $(call baseisadirs,$(libdir),libkdb5\.so\.\d+(\.\d+)*)
PKGFILES_CSWlibkrb5-3 += $(call baseisadirs,$(libdir),krb5.*)
SPKG_DESC_CSWlibkrb5-3 += MIT Kerberos 5 core and private libraries, libkrb5.so.3
OBSOLETED_BY_CSWlibkrb5-3 += CSWkrb5lib
OBSOLETED_BY_CSWlibkrb5-3 += CSWlibkrb5-privbOBSOLETED_BY_CSWlibkrb5-3 += CSWlibgssapi-krb5-2bkrb5-3 = CSWkrb5lib
RUNTIME_DEP_PKGS_CSWlibkrb5-3 += CSWlibkrb5support0
RUNTIME_DEP_PKGS_CSWlibkrb5-3 += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWlibkrb5-3RUNTIME_DEP_PKGS_CSWlibkrb5-3 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibkrb5-3 += CSWlibgcc-s13RUNTIME_DEP_PKGS_CSWlibkrb5-3 += CSWlibssl1-0-0
CHECKPKG_OVERRIDES_CSWlibkrb5-3 += soname-not-part-of-filename
CHECKPKG_OVERRIDES_CSWlibkrb5-3 += shared-lib-pkgname-mismatch3 += CSWlibk5crypto3

PACKAGES += CSWlibkrb5support0
CATALOGNAME_CSWlibkrb5support0 = libkrb5support0
PKGFILES_CSWlibkrb5support0 += $(call baseisadirs,$(libdir),libkrb5support\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibkrb5support0 += MIT Kerberos 5 core libraries, RUNTIME_DEP_PKGS_CSWlibkrb5support0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibkrb5support0 += CSWlibgcc-s1 kPACKAGES += CSWlibverto0
CATALOGNAME_CSWlibverto0 = libverto0
PKGFILES_CSWlibverto0 += $(call baseisadirs,$(libdir),libverto\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibverto0 += MIT Kerberos 5 core libraries, libverto.so.0
RUNTIME_DEP_PKGS_CSWlibverto0 += CSWlibgcc-s1bkrb5-3 = CSWkrb5lib

LICErst

EXTRA_CFLAGS   += -std=gnu99
EXTRA_CPPFLAGS += -D__EXTENSIONS__
EXTRA_LDFLAGS  += -L$(libdir) -lintl += -D__EXTENSIONS__

CONFIGURE_SCRIPTS = $(WORKSRC)/src/configure

BUIted in the library.
NODIRPATHS = --docdir
CONFIGURE_CONFIGURE_ARGS += --enable-dns-for-realmsable-thread-support
CONFIGURE_ARGS += --enable-thread-support
CONFIGURE_ARGS += --disable-static --disable-profiled
CONF-readline
# To pick the right tclConfig.sh
CONFIGURE_ARGS += --with-tcl=$(libdir)
# Must be explicitly disabled or else the already installed version is
# considered to be system
CONFIGURE_ARGS += --with-system-verto=no

SKIPTEST = 1

BUILD_SCRIPTSEL))

BUILD_SCRIPTS  = $(WORKSRC)/src/Makefile

TEST_SCRIPTS = $(WORINSTALL_SCRIPTS = $(WORKSRC)/src/Makefile5lib = krb5_lib_stub

include gar/category.mk

post-extract-modulated:
	@# TODO: Check signature
	cd $(WORKDIR) && (gzip -c -d $(NAME)-$(VERSION).tar.gz | tar xf -)
	@# libcrypto.so is part of openssl and expected to be linkable without setting a linker search path
	perl -pi -e 's,-lcrypto,-L$(libdir) -lcrypto,' \
		$(WORKSRC)/src/plugins/preauth/pkinit/Makefile
post-install-modulated:
	# Remove Studio-specific arch references
	gsed -i \
		-e '/^[^#]/s/-xO[0-5][^ ]* *//g' \
		-e '/^[^#]/s/-xarch=[^ ]* *//g' \
		-e '/^[^#]/s/-xchip=[^ ]* *//g' \
		-e '/^[^#]/s/-norunpath[^ ]* *//g' \
		-e '/^[^#]/s/-lCrun[^ ]* *//g' \
		-e '/^[^#]/s/-lCstd[^ ]* *//g' \
		-e '/^[^#]/s/-mtune=[^ ]* *//g' \
		-e '/^[^#]/s/-march=[^ ]* *//g' \
		-e '/^[^#]/s/-Wall *//g' \
		-e '/^[^#]/s/-pipe *//g' \
		-e '/^[^#]/s/-KPIC/-fPIC/g' \
		$(DESTDIR)$(bindir)/krb5-config
	# Add a link to the system's Kerberos configuration
	ginstall -m 755 -d $(DESTDIR)$(sysconfdir)
	gln -s ../../krb5/krb5.conf $(DESTDIR)$(sysconfdir)/krb5.conf
	@$(MAKECOOKIE)
