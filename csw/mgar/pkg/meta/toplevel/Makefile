GARNAME = toplevel
GARVERSION = 1.0
CATEGORIES = meta

DESCRIPTION = Blastwave automated build
define BLURB
  This packge defines the major package sets to be built as part of
  an automated build.  This directory itself does not produce any packages
  (althought it could).
endef

# Bootstrap
#DEPENDS += devel/m4

# Solaris Apache MySQL PHP/Perl/Python
DEPENDS += meta/SAMP

# Perl bundles
DEPENDS += cpan/Cache-Memcached
DEPENDS += cpan/SVK
DEPENDS += cpan/XML-Twig
DEPENDS += cpan/Cache
DEPENDS += cpan/XML-Smart
DEPENDS += cpan/Config-IniFiles
DEPENDS += cpan/Digest-SHA1
DEPENDS += cpan/Digest-HMAC
DEPENDS += cpan/HTML-Tagset
DEPENDS += cpan/HTML-Parser
#DEPENDS += cpan/IO-Socket-SSL
#DEPENDS += cpan/libwww-perl
DEPENDS += cpan/MailTools
DEPENDS += cpan/Net-DNS
#DEPENDS += cpan/Net-SSLeay
DEPENDS += cpan/Params-Validate
DEPENDS += cpan/URI
DEPENDS += cpan/WWW-Mechanize

include ../category.mk

