NAME = Mail-SPF-Query
VERSION = 1.999.1
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = JMEHNLE

DESCRIPTION = Query Sender Policy Framework for an IP,email,helo
define BLURB
  The SPF protocol relies on sender domains to describe their designated
  outbound mailers in DNS. Given an email address, Mail::SPF::Query determines
  the legitimacy of an SMTP client IP.
endef

MASTER_SITES = $(addsuffix mail-spf-query/,$(CPAN_MIRRORS))

DISTFILES = COPYING

PACKAGES = CSWpmmailspfqry
CATALOGNAME = pm_mailspfqry

DEP_PKGS = CSWpmnetcidrlite CSWpmnetdns CSWpmsyshostnamelong CSWpmuri

ARCHALL = 1

include gar/category.mk
