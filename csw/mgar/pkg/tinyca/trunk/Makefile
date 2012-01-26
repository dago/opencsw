# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
NAME = tinyca2
VERSION = 0.7.5
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Graphical userinterface to manage a small CA
define BLURB
  TinyCA is a graphical tool written in Perl/Gtk to manage a small Certification Authority (CA) using openssl.
  TinyCA supports - creation and revocation of x509 - S/MIME certificates.
  - PKCS#10 requests.
  - exporting certificates as PEM, DER, TXT, and PKCS#12.
  - server certificates for use in web servers, email servers, IPsec, and more.
  - client certificates for use in web browsers, email clients, IPsec, and more.
  - creation and management of SubCAs
endef

MASTER_SITES = http://tinyca.sm-zone.net/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTFILES += COPYING
PATCHFILES = 0001-Hardcode-pathes-to-CSW.patch

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

RUNTIME_DEP_PKGS = CSWperl CSWpmgtk2 CSWosslutils CSWzip CSWgtar

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = custom
TEST_SCRIPTS = 

ARCHALL = 1

CHECKPKG_OVERRIDES_CSWtinyca2 += surplus-dependency|CSWzip
CHECKPKG_OVERRIDES_CSWtinyca2 += surplus-dependency|CSWosslutils
CHECKPKG_OVERRIDES_CSWtinyca2 += surplus-dependency|CSWgtar
CHECKPKG_OVERRIDES_CSWtinyca2 += surplus-dependency|CSWpmgtk2

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -m 755 $(WORKSRC)/tinyca2 $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)/opt/csw/share/tinyca2
	cp -rp $(WORKSRC)/lib $(DESTDIR)/opt/csw/share/tinyca2/
	cp -rp $(WORKSRC)/templates $(DESTDIR)/opt/csw/share/tinyca2/
	ginstall -d $(DESTDIR)$(libdir)
	cp -rp $(WORKSRC)/locale $(DESTDIR)$(libdir)
	@$(MAKECOOKIE)

