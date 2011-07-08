NAME = mysql-ruby
VERSION = 2.7
GARTYPE = v1
CATEGORIES = lang

DESCRIPTION = Ruby MySQL Extension
define BLURB
  #Blurb
endef

MASTER_SITES  = http://tmtm.org/downloads/mysql/ruby/
DISTFILES  = $(NAME)-$(VERSION).tar.gz 
DISTFILES += $(call admfiles,CSWrbmysql,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

#DEPENDS += lang/ruby server/mysql4

CONFIGURE_SCRIPTS = ruby
TEST_SCRIPTS      = ruby

CONFIGURE_ARGS = --with-mysql-config

include gar/category.mk

configure-ruby:
	( cd $(WORKSRC) ; $(CONFIGURE_ENV) ruby extconf.rb $(CONFIGURE_ARGS) )

test-ruby:
	( cd $(WORKSRC) ; $(TEST_ENV) ruby test.rb $(TEST_ARGS) )
