# TBD:
# - Recipe not ready, does not compile due to missing strsep and possibly other things

NAME = mod_httpbl
VERSION = 1.5
CATEGORIES = server
GARTYPE = v2

DESCRIPTION = Apache blacklist module
define BLURB
  The mod_httpbl Apache module is ideal for leveraging the Project Honey pot http:BL services
  within the context of an Apache web server. Built on the Apache APIs, the mod enables web
  admins to block comment spammers, harvesters, and other maliciousECT IPs.
endef

SF_PROJ = httpbl
# Project for download on CVS
MASTER_SITES = http://httpbl.cvs.sourceforge.net/viewvc/httpbl/mod_httpbl_for_apache_2.0/mod_httpbl_source/
DISTNAME =
DISTFILES += mod_httpbl.c
DISTFILES += install.txt

VENDOR_URL = http://sourceforge.net/projects/httpbl/
#LICENSE = LICENSE

PACKAGES = CSWap2modhttpbl
CATALOGNAME = ap2_mod_httpbl
RUNTIME_DEP_PKGS_CSWap2modhttpbl += CSWapache2
CHECKPKG_OVERRIDES_CSWap2modhttpbl += surplus-dependency|CSWapache2

# Apache paths
AP2_ROOT      = $(prefix)/apache2
AP2_LIBEXEC   = $(DESTDIR)$(AP2_ROOT)/libexec
AP2_APXS      = $(AP2_ROOT)/sbin/apxs

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
INSTALL_SCRIPTS = custom

# The package does not provide a check
TEST_SCRIPTS =

AP2_MODS = 1
AP2_MODFILES += \*auth_kerb\*so

include gar/category.mk

build-custom:
	$(AP2_APXS) -c $(WORKSRC)/mod_httpbl.c
 
# install:
#-       ./apxs.sh "${CPPFLAGS}" "${LDFLAGS}" "${SPNEGO_SRCS}" "${APXS}" "-c -i" "src/mod_auth_kerb.c"
#+       ./apxs.sh "${CPPFLAGS}" "${LDFLAGS}" "" "${APXS}" "-i -S LIBEXECDIR=$(AP2_LIBEXEC)" "src/mod_auth_kerb.la"


install-custom:
	ginstall -d $(AP2_LIBEXEC)
	ginstall 
	ginstall -d $(DESTDIR)$(docdir)/$(CATALOGNAME)
	#ginstall $(WORKSRC)/README $(WORKSRC)/INSTALL $(DESTDIR)$(docdir)/$(CATALOGNA