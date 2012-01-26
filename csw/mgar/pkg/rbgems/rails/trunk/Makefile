NAME = rails
VERSION = 2.3.8
CATEGORIES = rbgems
GARTYPE = v2

DESCRIPTION = A framework for building web-application
define BLURB
  Rails is a framework for building web-application using CGI, FCGI, mod_ruby, or WEBrick on top of either MySQL, PostgreSQL, SQLite, DB2, SQL Server, or Oracle with eRuby- or Builder-based templates.
endef

PACKAGES = CSWgem-rails
CATALOGNAME = gem_rails

GEM_DEPS = CSWgem-rake CSWgem-activesupport CSWgem-activerecord CSWgem-actionpack CSWgem-actionmailer CSWgem-activeres
RUNTIME_DEP_PKGS = $(GEM_DEPS)

ARCHALL = 1

include gar/category.mk
