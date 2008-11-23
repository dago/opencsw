GARNAME = Catalyst
GARVERSION = 5.61
CATEGORIES = cpan
AUTHOR = SRI

DESCRIPTION = The Elegant MVC Web Application Framework
define BLURB
  Catalyst is an elegant web application framework, extremely flexible yet
  extremely simple. It's similar to Ruby on Rails, Spring (Java) and Maypole,
  upon which it was originally based.
endef

DISTFILES += $(call admfiles,CSWpmcatalyst,)

DEPENDS += cpan/Class-Accessor
DEPENDS += cpan/Class-Inspector
DEPENDS += cpan/CGI
DEPENDS += cpan/File-Modified
DEPENDS += cpan/HTML-Parser
DEPENDS += cpan/HTTP-Body
DEPENDS += cpan/libwww-perl

include gar/category.mk
