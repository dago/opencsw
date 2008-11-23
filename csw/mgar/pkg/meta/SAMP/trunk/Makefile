GARNAME = SAMP
GARVERSION = 1.0
CATEGORIES = meta

DESCRIPTION = Solaris Mysql Perl/PHP/Python (SAMP)
define BLURB
  The SAMP bundle package is a collection of utilities and servers that can be
  used to create dynamic web content.  This is similar to existing LAMP
  platforms (Linux + Apache + MySQL + Perl/PHP/Python).
endef

DISTFILES += $(call admfiles,CSWsamp,depend prototype)

# Apache
DEPENDS += server/apache2

# Languages
#DEPENDS += lang/perl
DEPENDS += lang/php5
#DEPENDS += lang/python
#DEPENDS += lang/ruby

# Database
#DEPENDS += server/mysql4
#DEPENDS += server/pgsql

# Database Integration
#DEPENDS += cpan/DBD-mysql
#DEPENDS += lang/mysql-ruby
DEPENDS += lang/mysql-python
#DEPENDS += cpan/DBD-SQLite
#DEPENDS += cpan/DBD-Pg

# Language Integration
DEPENDS += cpan/mod_perl2
DEPENDS += cpan/libapreq2
DEPENDS += server/mod_python
#DEPENDS += server/mod_ruby
#DEPENDS += server/rails

# Additional Servers
DEPENDS += net/memcached
DEPENDS += cpan/Cache-Memcached
#DEPENDS += net/squid

include gar/category.mk
