GARNAME = mysql-ruby
GARVERSION = 2.7
CATEGORIES = lang

DESCRIPTION = Ruby MySQL Extension
define BLURB
  #Blurb
endef

MASTER_SITES  = http://tmtm.org/downloads/mysql/ruby/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz 
DISTFILES += $(call admfiles,CSWrbmysql,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

#DEPENDS += lang/ruby server/mysql4

CONFIGURE_SCRIPTS = ruby
TEST_SCRIPTS      = ruby

CONFIGURE_ARGS = --with-mysql-config

include gar/category.mk

configure-ruby:
	( cd $(WORKSRC) ; $(CONFIGURE_ENV) ruby extconf.rb $(CONFIGURE_ARGS) )

test-ruby:
	( cd $(WORKSRC) ; $(TEST_ENV) ruby test.rb $(TEST_ARGS) )
