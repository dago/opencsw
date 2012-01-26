NAME = mod_fcgid
VERSION = 2.3.5
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = FastCGI module with fine grained process spawn/lifetime control
define BLURB
  mod_fcgid is a high performance alternative to mod_cgi or mod_cgid,
  which starts a sufficient number instances of the CGI program to handle
  concurrent requests, and these programs remain running to handle further
  incoming requests. It is favored by the PHP developers, for example, as
  a preferred alternative to running mod_php in-process, delivering very
  similar performance. 
endef

VENDOR_URL   = http://httpd.apache.org/mod_fcgid/
MASTER_SITES = http://apache.mirroring.de/httpd/mod_fcgid/
DISTFILES    = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
LICENSE      = LICENSE-FCGID

PACKAGES = CSWap2modfcgid
CATALOGNAME = ap2_modfcgid
RUNTIME_DEP_PKGS = CSWap2prefork

CONFIGURE_SCRIPTS = custom
TEST_SCRIPTS =

include gar/category.mk
include ../../apache2/trunk/files/extensionbuild.mk

configure-custom:
	cd $(WORKSRC) && APXS=$(APXS) ./configure.apxs
	@$(MAKECOOKIE)

# Install changelog.CSW
post-merge: $(foreach P,$(_PKG_SPECS),install-changelog-$P)
install-changelog-%:
	ginstall -D $(FILEDIR)/changelog.CSW \
		$(PKGROOT)$(docdir)/$(call catalogname,$*)/changelog.CSW
	@$(MAKECOOKIE)
