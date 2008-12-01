GARNAME = krb5
GARVERSION = 1.6.3
CATEGORIES = server

DESCRIPTION = MIT Kerberos 5
define BLURB
  Kerberos is a network authentication protocol. It is designed to
  provide strong authentication for client/server applications by
  using secret-key cryptography. A free implementation of this protocol
  is available from the Massachusetts Institute of Technology.
  Kerberos is available in many commercial products as well.
endef

MASTER_SITES = http://web.mit.edu/kerberos/dist/krb5/1.6/
DISTFILES  = $(GARNAME)-$(GARVERSION)-signed.tar
DISTFILES += $(call admfiles,CSWkrb5adminserver,depend)
DISTFILES += $(call admfiles,CSWkrb5doc)
DISTFILES += $(call admfiles,CSWkrb5kdc,depend)
DISTFILES += $(call admfiles,CSWkrb5lib)
DISTFILES += $(call admfiles,CSWkrb5libdev,depend)
DISTFILES += $(call admfiles,CSWkrb5user,depend)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)-signed.tar

PATCHFILES  = patch-man2html-perl.diff
PATCHFILES += patch-ldap-const.diff

PREREQUISITE_PKGS = CSWtcl

CONFIGURE_SCRIPTS = $(WORKSRC)/src/configure

CONFIGURE_ARGS  = $(DIRPATHS)
ifeq ($(ISA),i386)
CONFIGURE_ARGS += --with-tcl=$(prefix)
endif
# --enable-ipv6 is deprecated and autodetected
#CONFIGURE_ARGS += --enable-ipv6
CONFIGURE_ARGS += --enable-kdc-replay-cache --enable-dns-for-realm
CONFIGURE_ARGS += --disable-thread-support
CONFIGURE_ARGS += --disable-static --disable-profiled
CONFIGURE_ARGS += --with-ldap

BUILD64 = 1

BUILD_SCRIPTS  = $(WORKSRC)/src/Makefile
BUILD_SCRIPTS += $(WORKSRC)/doc/Makefile

TEST_SCRIPTS = $(WORKSRC)/src/Makefile
TEST_TARGET = check

INSTALL_SCRIPTS = $(WORKSRC)/src/Makefile custom

ADMINSERVER_BINS = kprop|kadmind|kadmin\.local
PKGFILES_CSWkrb5adminserver  = $(mandir)/man8/($(ADMINSERVER_BINS))\.8
PKGFILES_CSWkrb5adminserver += $(sbindir)/($(ADMINSERVER_BINS))

PKGFILES_CSWkrb5doc  = $(mandir)/man5/(krb5.conf|kdc.conf)\.5

KDC_BINS = krb5kdc|krb524d|kpropd|kdb5_util
PKGFILES_CSWkrb5kdc  = $(mandir)/man8/($(KDC_BINS))\.8
PKGFILES_CSWkrb5kdc += $(sharedstatedir)/examples/krb5/.*
PKGFILES_CSWkrb5kdc += $(sbindir)/($(KDC_BINS))

PKGFILES_CSWkrb5lib = $(PKGFILES_RT)

PKGFILES_CSWkrb5libdev  = $(mandir)/man8/sserver.8
PKGFILES_CSWkrb5libdev += $(mandir)/man1/(sclient|krb5-config|compile_et)\.1
PKGFILES_CSWkrb5libdev += $(sbindir)/(uuserver|sserver|sim_server|gss-server)
PKGFILES_CSWkrb5libdev += $(includedir)/.*
PKGFILES_CSWkrb5libdev += $(bindir)/(uuclient|sim_client|sclient|krb5-config|gss-client|compile_et)

# User gets all the rest
#USER_BINS = kvno|ksu|krb524init|kpasswd|klist|kinit|kdestroy 
#USER_SBINS = ktutil|kadmin|k5srvutil 
#PKGFILES_CSWkrb5user  = $(mandir)/man8/($(USER_SBINS))\.8
#PKGFILES_CSWkrb5user += $(mandir)/man1/($(USER_BINS))\.1
#PKGFILES_CSWkrb5user += $(sharedstatedir)/examples/krb5/krb5.conf
#PKGFILES_CSWkrb5user += $(bindir)/($(USER_BINS))

include ../category.mk

# The flags must not contain additional spaces or the build freaks out
CFLAGS := $(strip $(CFLAGS) -L$(libdir)/$(MM_LIBDIR))
#LDFLAGS := $(strip $(LDFLAGS))

post-extract-modulated:
	@# TODO: Check signature
	@cd $(WORKDIR) && (gzip -c -d $(GARNAME)-$(GARVERSION).tar.gz | tar xf -)
	@$(MAKECOOKIE)

install-custom:
	@echo " ==> Installing documentation"
