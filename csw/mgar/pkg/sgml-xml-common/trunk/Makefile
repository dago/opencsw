GARNAME = sgml-common
GARVERSION = 0.6.3
#since categories are a bit of a relic and this doesn't fit better anywhere
#else anyway...
CATEGORIES = xtra

DESCRIPTION = A collection of entities and DTDs
define BLURB
The sgml-common package contains a collection of entities and DTDs
that are useful for processing SGML, but that don't need to be
included in multiple packages.  Sgml-common also includes an
up-to-date Open Catalog file.
endef

PREREQUISITE_PKGS = CSWautomake CSWautoconf

ARCHALL = 1

PACKAGES = CSWxmlcommon CSWsgmlcommon

SPKG_DESC_CSWsgmlcommon = A collection of sgml entities and DTDs
SPKG_DESC_CSWxmlcommon = A collection of xml entities and DTDs

CATALOGNAME_CSWsgmlcommon = sgmlcommon
CATALOGNAME_CSWxmlcommon = xmlcommon

PKGFILES_CSWsgmlcommon =  .*sgmlwhich.* .*install-catalog.*
PKGFILES_CSWsgmlcommon += /opt/csw/share/sgml/.* /etc/opt/csw/sgml/sgml.conf
PKGFILES_CSWsgmlcommon += /opt/csw/share/doc/sgml.*

PKGFILES_CSWxmlcommon = /etc/opt/csw/xml/.* /opt/csw/share/xml.* /etc/opt/csw/sgml/docbook/xmlcatalog

REQUIRED_PKGS_CSWsgmlcommon = CSWbash CSWggrep CSWgsed

EXTRA_FILES = xml.dcl html.dcl xml.soc html.soc

MASTER_SITES = ftp://sources.redhat.com/pub/docbook-tools/new-trials/SOURCES/
DISTFILES  = $(GARNAME)-$(GARVERSION).tgz
DISTFILES += $(EXTRA_FILES)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PATCHFILES = sgml-common-0.6.3-docdir.patch sgml-common-automake.patch
PATCHFILES += sgml-common-quotes.patch sgml-common-umask.patch
PATCHFILES += sgml-common-xmldir.patch install-catalog-sanity.patch
PATCHFILES += sgmlwhich-sanity.patch configure-man.patch
PATCHFILES += install-catalog-man.patch sgml-conf-autoconf.patch
PATCHFILES += configure-sgml-conf.patch

CONFIGURE_ARGS = $(DIRPATHS) --with-docdir=$(datadir)/doc

TEST_TARGET =

# The redhat tarball includes specific links to their standard automake
# install location.  We'll need to reset some of these to be appropriate
# to CSW
RH_AM_LINKS = install-sh missing mkinstalldirs

# a destination xml catalog
XMLCATALOG=$(DESTDIR)/$(sysconfdir)/xml/catalog

sysconfdir=/etc/opt/csw/

include gar/category.mk

# fix up auto* stuff
pre-configure-modulated:
	( cd $(WORKSRC)/; \
		for f in $(RH_AM_LINKS); do \
			rm $$f; \
		done; \
		aclocal; \
		autoconf; \
		automake --add-missing --copy )
	@$(MAKECOOKIE)

post-install-modulated:
	# this is almost 100% copy from the sgml-common rpm spec from rhel5
	mkdir -p $(DESTDIR)/$(sysconfdir)/xml
	mkdir -p $(DESTDIR)/$(datadir)/sgml/docbook
	# create empty xml catalog
	xmlcatalog --noout --create $(XMLCATALOG)
	# now put the common docbook entries in it
	xmlcatalog --noout --add "delegatePublic" \
		"-//OASIS//ENTITIES DocBook XML" \
		"file://$(datadir)/sgml/docbook/xmlcatalog" $(XMLCATALOG)
	xmlcatalog --noout --add "delegatePublic" \
		"-//OASIS//DTD DocBook XML" \
		"file://$(datadir)/sgml/docbook/xmlcatalog" $(XMLCATALOG)
	xmlcatalog --noout --add "delegatePublic" \
		"ISO 8879:1986" \
		"file://$(datadir)/sgml/docbook/xmlcatalog" $(XMLCATALOG)
	xmlcatalog --noout --add "delegateSystem" \
		"http://www.oasis-open.org/docbook/" \
		"file://$(datadir)/sgml/docbook/xmlcatalog" $(XMLCATALOG)
	xmlcatalog --noout --add "delegateURI" \
		"http://www.oasis-open.org/docbook/" \
		"file://$(datadir)/sgml/docbook/xmlcatalog" $(XMLCATALOG)
	# Also create the common DocBook catalog
	xmlcatalog --noout --create \
		$(DESTDIR)/$(datadir)/sgml/docbook/xmlcatalog
	rm -f $(DESTDIR)/$(datadir)/sgml/xml.dcl
	for f in $(EXTRA_FILES); do \
		ginstall -m0644 $(WORKSRC)/../$$f $(DESTDIR)/$(datadir)/sgml; \
	done
	rm -rf $(DESTDIR)/$(datadir)/xml/*
	@$(MAKECOOKIE)

inst-clean:
	rm -rf $(DESTDIR)
