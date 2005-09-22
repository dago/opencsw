GARNAME = Mail-SPF-Query
GARVERSION = 1.997
CATEGORIES = cpan
AUTHOR = FREESIDE

DESCRIPTION = query sender policy framework
define BLURB
  The SPF protocol relies on sender domains to describe their designated
  outbound mailers in DNS. Given an email address, Mail::SPF::Query determines
  the legitimacy of an SMTP client IP.
endef

DISTFILES += CSWpmmailspfqry.gspec CSWpmmailspfqry.depend

DEPENDS += cpan/Net-DNS cpan/Net-CIDR-Lite cpan/Sys-Hostname-Long cpan/URI

include ../category.mk
