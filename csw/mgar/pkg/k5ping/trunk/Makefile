NAME = k5ping
VERSION = 9fb8c5
GARTYPE = v2

DESCRIPTION = A test that KDC is performing AS_REQs, TGS_REQs, and krb524

MASTER_SITES = http://oskt.secure-endpoints.com/
#DISTFILES += gitweb.cgi?p=k5ping;a=blob_plain;f=k5ping.c;hb=HEAD
#DISTFILES += gitweb.cgi?p=k5ping;a=blob_plain;f=k5ping.8;hb=HEAD
# GIT support is only included for Github at the moment
DISTFILES += k5ping.c
DISTFILES += k5ping.8

VENDOR_URL = http://oskt.secure-endpoints.com/k5ping.html

BUILD_DEP_PKGS += CSWlibkrb5-dev
BUILD_DEP_PKGS += CSWgroff

PACKAGES += CSWk5ping
SPKG_DESC_CSWk5ping = A test that KDC is performing AS_REQs, TGS_REQs, and krb524
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWk5ping += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWk5ping += CSWlibcom-err3

# There is no configure
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
# There is no testsuite
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

build-custom:
	cd $(WORKDIR) && $(BUILD_ENV) $(CC) $(CFLAGS) $(CPPFLAGS) $(LDFLAGS) -lkrb5 -lcom_err -o k5ping k5ping.c
	@$(MAKECOOKIE)

install-custom:
	ginstall -D -m 0755 $(WORKDIR)/k5ping $(DESTDIR)$(bindir)/k5ping
	@# The manpage uses special macro packages, preformat for now
	ginstall -d -m 0755 $(DESTDIR)$(mandir)/cat8
	$(bindir)/gnroff -man $(WORKDIR)/k5ping.8 >$(DESTDIR)$(mandir)/cat8/k5ping.8
	@$(MAKECOOKIE)
