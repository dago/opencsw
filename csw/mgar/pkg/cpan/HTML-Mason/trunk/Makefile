GARNAME = HTML-Mason
GARVERSION = 1.35
CATEGORIES = cpan
AUTHOR = DROLSKY

DESCRIPTION = high-performance, dynamic web site authoring system
define BLURB
  Mason is a tool for building, serving and managing large web sites. Its
  features make it an ideal backend for high load sites serving dynamic
  content, such as online newspapers or database driven e-commerce sites.
endef

DISTFILES += CSWpmhtmlmason.gspec CSWpmhtmlmason.depend

DEPENDS += cpan/Params-Validate cpan/Exception-Class cpan/Cache-Cache
DEPENDS += cpan/Class-Container cpan/CGI cpan/Scalar-List-Utils

include gar/category.mk
