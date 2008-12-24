GARNAME = ca-certificates
GARVERSION = $(shell date '+%Y%m%d')
CATEGORIES = xtra

DESCRIPTION = CA certificates
define BLURB
  CA certificates
endef

MASTER_SITES = http://hg.mozilla.org/mozilla-central/raw-file/default/security/nss/lib/ckfw/builtins/
DISTFILES  = certdata.txt certdata2pem.pl update-ca-certificates ca-certificates.conf
DISTFILES += $(call admfiles,CSWcacertificates,depend postinstall postremove)

# We define upstream file regex so we can be notifed of new upstream software release
# UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = 
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

SPKG_CLASSES = none cswpreserveconf

include gar/category.mk

$(WORKDIR)/hash.db: $(WORKDIR)/certdata.txt
	rm -f $(WORKDIR)/hash.db
	find "$(DESTDIR)/$(sharedstatedir)/ca-certificates" -name *.pem | while read FILE; do \
		echo "`basename $$FILE`=`/opt/csw/bin/openssl x509 -hash -fingerprint -noout -in "$$FILE" | head -n 1`.0" >> hash.db; \
	done

$(WORKDIR)/LICENSE: $(WORKDIR)/certdata.txt
	sed -ne '/BEGIN LICENSE BLOCK/,/END LICENSE BLOCK/p' "$(WORKDIR)/certdata.txt" | grep -v "LICENSE BLOCK" \
		> "$(WORKDIR)/LICENSE"

install-custom: $(WORKDIR)/hash.db $(WORKDIR)/LICENSE
	ginstall -d "$(DESTDIR)/$(sysconfdir)/ssl/certs"
	ginstall -d "$(DESTDIR)/$(sharedstatedir)/ca-certificates"
	ginstall -D $(WORKDIR)/update-ca-certificates "$(DESTDIR)/$(sbindir)/update-ca-certificates"
	ginstall -D hash.db "$(DESTDIR)/$(sharedstatedir)/ca-certificates/hash.db"
	ginstall -d "$(DESTDIR)/$(sharedstatedir)/ca-certificates/mozilla"
	cd "$(DESTDIR)/$(sharedstatedir)/ca-certificates/mozilla" && perl "$(CURDIR)/$(WORKDIR)/certdata2pem.pl" < "$(CURDIR)/$(WORKDIR)/certdata.txt"

