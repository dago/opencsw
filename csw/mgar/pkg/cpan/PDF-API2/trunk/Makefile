GARNAME = PDF-API2
GARVERSION = 0.73
CATEGORIES = cpan
AUTHOR = AREIBENS

DESCRIPTION = create and modify PDF files
define BLURB
  A Perl Module Chain to faciliate the Creation and Modification of
  High-Quality "Portable Document Format (aka. PDF)" Files.
endef

PACKAGES    = CSWpmpdfapi2
CATALOGNAME = pm_pdfapi2

ARCHALL_CSWpmpdfapi2 = 1

REQUIRED_PKGS_CSWpmpdfapi2 += CSWpmcompresszlib

LICENSE = COPYING

include gar/category.mk

post-extract:
	@chmod o+r $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/*/COPYING 
	@$(MAKECOOKIE)

