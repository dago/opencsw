NAME = mysql
VERSION = 2.8.1
CATEGORIES = rbgems

DESCRIPTION = This is the MySQL API module for Ruby

define BLURB
  This is the MySQL API module for Ruby. It provides the same functionsfor Ruby programs that the MySQL C API provides for C programs. Thisis a conversion of tmtm's original extension into a proper RubyGems.
endef

RUNTIME_DEP_PKGS_CSWrb18-mysql-2-8-1 += CSWlibruby18-1
RUNTIME_DEP_PKGS_CSWrb18-mysql-2-8-1 += CSWlibz1
RUNTIME_DEP_PKGS_CSWrb18-mysql-2-8-1 += CSWlibmysqlclient15

GEM_BUILD_FLAGS = --with-mysql-config=$(abspath $(CURDIR))/mysql_config_wrapper

# the default license for ruby gems is MIT-LICENSE
LICENSE = COPYING

include gar/category.mk
