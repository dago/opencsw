GARNAME = ca-certificates
GARVERSION = $(shell date '+%Y%m%d')
CATEGORIES = xtra

DESCRIPTION = CA certificates
define BLURB
  CA certificates
endef

MASTER_SITES = http://hg.mozilla.org/mozilla-central/raw-file/default/security/nss/lib/ckfw/builtins/
DISTFILES  = certdata.txt certdata2pem.pl update-ca-certificates
DISTFILES += $(call admfiles,CSWcacertificates,depend postinstall)

# We define upstream file regex so we can be notifed of new upstream software release
# UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = 
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

SPKG_CLASSES = none cswpreserveconf

include gar/category.mk


install-custom:
	ginstall -d "$(DESTDIR)/$(sysconfdir)/ssl/certs"
	ginstall -d "$(DESTDIR)/$(sharedstatedir)/ca-certificates"
	ginstall -D "$(CURDIR)/$(WORKDIR)/update-ca-certificates" "$(DESTDIR)/$(sbindir)/update-ca-certificates"
	cd "$(DESTDIR)/$(sharedstatedir)/ca-certificates" && perl "$(CURDIR)/$(WORKDIR)/certdata2pem.pl" < "$(CURDIR)/$(WORKDIR)/certdata.txt"
	cd "$(DESTDIR)/$(sharedstatedir)/ca-certificates" && ls -1 > "$(CURDIR)/$(WORKDIR)/ca-certificate.conf"
	sed -ne '/BEGIN LICENSE BLOCK/,/END LICENSE BLOCK/p' "$(CURDIR)/$(WORKDIR)/certdata.txt" | grep -v "LICENSE BLOCK" \
		> "$(CURDIR)/$(WORKDIR)/LICENSE"
