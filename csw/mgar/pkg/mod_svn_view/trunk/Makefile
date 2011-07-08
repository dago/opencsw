NAME = mod_svn_view
VERSION = 0.0.0
GARTYPE = v1
CATEGORIES = server

DESCRIPTION = Subversion repository viewer
define BLURB
  mod_svn_view provides a web-based view of a Subversion repository, similar
  to Chora, or viewcvs. What makes mod_svn_view different is it uses the
  Subversion libraries directly instead of executing the command line client,
  and thus has tremendous speed. It is also written in C as an Apache 2.0
  module and generates a simple XML output that can be run through XSL
  Transformations via mod_transform to generate a customized look.
endef

#DEPENDS  = lib/libxml lib/libxslt server/mod_transform
#DEPENDS += server/mod_highlight server/apache2

# SVN only at this time
#MASTER_SITES = http://www.outoforder.cc/downloads/$(NAME)/
#MASTER_SITES = svn-http://svn.outoforder.cc/svn/$(NAME)/trunk/
#DISTFILES  = $(NAME)-$(VERSION).tar.gz
#DISTFILES += $(call admfiles,CSWap2modsvnview,)

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-apxs=$(prefix)/apache2/sbin/apxs

include gar/category.mk
