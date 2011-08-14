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

# this is build-time detection
CHECKPKG_OVERRIDES_CSWrb18-mysql-2-8-1 += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/gems/1.8/gems/mysql-2.8.1/ext/mysql_api/extconf.rb
# the hashbang isn't updated in the test file
CHECKPKG_OVERRIDES_CSWrb18-mysql-2-8-1 += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/gems/1.8/gems/mysql-2.8.1/test/test_mysql.rb
# don't worry about the readme files
CHECKPKG_OVERRIDES_CSWrb18-mysql-2-8-1 += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/gems/1.8/gems/mysql-2.8.1/extra/README.html
CHECKPKG_OVERRIDES_CSWrb18-mysql-2-8-1 += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/gems/1.8/gems/mysql-2.8.1/extra/README_ja.html

include gar/category.mk
