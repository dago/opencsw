NAME = opendmarc
VERSION = 1.1.3
GARTYPE = v2

DESCRIPTION = DMARC Milter Implementatin
define BLURB
  OpenDMARC is an open source implementation of Domain-based Message
  Authentication, Reporting & Conformance, or DMARC. It builds on the
  successes of technologies such as DomainKeys Identified Mail (DKIM)
  and the Sender Policy Framework (SPF) to create an infrastructure
  that enforces policy on domain names that are visible to end users,
  and creates a feedback framework for identifying and tracking
  fraudulent use of domain names in email.
  It includes a library for handling DMARC record parsing,
  a database schema and tools for aggregating and processing transaction
  history to produce DMARC reports, and a filter that ties it all together
  with an MTA using the milter protocol.
endef

MASTER_SITES = $(SF_MIRRORS)
VENDOR_URL = http://www.trusteddomain.org/opendmarc/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PATCHFILES += 0001-milterdir.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGING_PLATFORMS =  solaris10-sparc solaris10-i386

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-milter
CONFIGURE_ARGS += --with-sql-backend=mysql

PACKAGES = CSWopendmarc
CATALOGNAME_CSWopendmarc = opendmarc
SPKG_DESC_CSWopendmarc = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWopendmarc += CSWlibopendmarc1
RUNTIME_DEP_PKGS_CSWopendmarc += CSWlibidn11

PACKAGES += CSWlibopendmarc1
CATALOGNAME_CSWlibopendmarc1 = libopendmarc1
PKGFILES_CSWlibopendmarc1 += $(call baseisadirs,$(libdir),libopendmarc\.so\.1\.0\.1)
PKGFILES_CSWlibopendmarc1 += $(call baseisadirs,$(libdir),libopendmarc\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibopendmarc1 += $(DESCRIPTION), libopendmarc.so.1
RUNTIME_DEP_PKGS_CSWlibopendmarc1 += CSWlibidn11

PACKAGES += CSWopendmarc-dev
CATALOGNAME_CSWopendmarc-dev = opendmarc_dev
SPKG_DESC_CSWopendmarc-dev += $(DESCRIPTION), development files
PKGFILES_CSWopendmarc-dev += /opt/csw/lib/libopendmarc.so
RUNTIME_DEP_PKGS_CSWopendmarc-dev += CSWlibopendmarc1

include gar/category.mk

pre-configure-modulated:
	cd $(WORKSRC) && aclocal
	cd $(WORKSRC) && autoconf --force
	cd $(WORKSRC) && automake -a -c -f
	cd $(WORKSRC) && autoheader
	@$(MAKECOOKIE)
