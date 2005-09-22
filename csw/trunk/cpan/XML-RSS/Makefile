GARNAME = XML-RSS
GARVERSION = 1.05
CATEGORIES = cpan
AUTHOR = KELLAN

DESCRIPTION = creates and updates RSS files
define BLURB
  This module provides a basic framework for creating and maintaining RDF Site
  Summary (RSS) files. This distribution also contains many examples that
  allow you to generate HTML from an RSS, convert between 0.9, 0.91, and 1.0
  version, and other nifty things. This might be helpful if you want to
  include news feeds on your Web site from sources like Slashot and Freshmeat
  or if you want to syndicate your own content.
endef

DISTFILES += CSWpmxmlrss.gspec CSWpmxmlrss.depend

DEPENDS += cpan/XML-Parser
BUILDDEPS += cpan/Test-Manifest

include ../category.mk
