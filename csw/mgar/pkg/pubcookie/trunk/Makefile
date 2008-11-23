GARNAME = pubcookie
GARVERSION = 3.3.3
CATEGORIES = server

DESCRIPTION = Open-source software for intra-institutional web authentication
define BLURB
  Pubcookie consists of a standalone login server and modules
  for common web server platforms like Apache and Microsoft IIS.
  Together, these components can turn existing authentication
  services (like Kerberos, LDAP, or NIS) into a solution for
  single sign-on authentication to websites throughout an institution.
endef

MASTER_SITES = http://www.pubcookie.org/downloads/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWpubcookie)

PREREQUISITE_PKGS = CSWapache2-devel

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-apxs=/opt/csw/apache2/sbin/apxs

include gar/category.mk

