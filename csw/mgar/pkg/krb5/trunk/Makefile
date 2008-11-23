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
DISTFILES += $(call admfiles,CSWkrb5adminserver)
DISTFILES += $(call admfiles,CSWkrb5doc)
DISTFILES += $(call admfiles,CSWkrb5kdc)
DISTFILES += $(call admfiles,CSWkrb5lib)
DISTFILES += $(call admfiles,CSWkrb5libdev)
DISTFILES += $(call admfiles,CSWkrb5user)

PATCHFILES = patch-man2html-perl.diff

CONFIGURE_SCRIPTS = $(WORKSRC)/src/configure

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-kdc-replay-cache --enable-dns-for-realm
CONFIGURE_ARGS += --disable-thread-support
CONFIGURE_ARGS += --disable-static

BUILD_SCRIPTS  = $(WORKSRC)/src/Makefile
BUILD_SCRIPTS += $(WORKSRC)/doc/Makefile

TEST_SCRIPTS = $(WORKSRC)/src/Makefile
TEST_TARGET = check

INSTALL_SCRIPTS = $(WORKSRC)/src/Makefile custom

include gar/category.mk

# The flags must not contain additional spaces or the build freaks out
CFLAGS := $(strip $(CFLAGS) -L$(libdir))
LDFLAGS := $(strip $(LDFLAGS))

post-extract:
	@# TODO: Check signature
	@cd $(WORKDIR) && (gzip -c -d $(GARNAME)-$(GARVERSION).tar.gz | tar xf -)
	@$(MAKECOOKIE)

install-custom:
	@echo " ==> Installing documentation"
