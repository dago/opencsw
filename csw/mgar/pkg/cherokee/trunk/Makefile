# $Id$
NAME = cherokee
VERSION = 1.2.2
CATEGORIES = server
GARTYPE = v2

DESCRIPTION = Extremely fast and flexible web server
define BLURB
  Cherokee is a very fast, flexible and easy to configure Web Server. It 
  supports the widespread technologies nowadays: FastCGI, SCGI, PHP, CGI, TLS
  and SSL encrypted connections, Virtual hosts, Authentication, on the fly
  encoding, Load balancing, Apache compatible log files, and much more. A user
  friendly interface called cherokee-admin is provided for a no-hassle
  configuration of the server.
endef

VENDOR_URL = http://www.cherokee-project.com/
MASTER_SITES = http://www.cherokee-project.com/download/1.2/$(VERSION)/
DISTFILES  = $(DISTNAME).tar.gz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

# Does not build on Solaris 9
PACKAGING_PLATFORMS +=  solaris10-sparc solaris10-i386

GARCOMPILER = GCC4

CONFIGURE_ARGS = $(DIRPATHS)

# Does not build
CONFIGURE_ARGS += --with-geoip=no

# Does not run at the moment
SKIPTEST = 1

include gar/category.mk
