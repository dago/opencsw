# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = rootsh
VERSION = 1.5.3
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = Rootsh is a wrapper for shells which logs all echoed keystrokes and terminal output to a file
define BLURB
Rootsh is a wrapper for shells which logs all echoed keystrokes and terminal output to a file and/or to syslog. It's main purpose is the auditing of users who need a shell with root privileges. They start rootsh through the sudo mechanism. 
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(DISTNAME).tar.gz
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS) --with-logdir=/var/opt/csw/rootsh

PROTOTYPE_MODIFIERS = rootsshdir 
PROTOTYPE_FILES_rootsshdir =  $(localstatedir)/rootsh  # a normal Perl regexp. Watch out for links!
PROTOTYPE_PERMS_rootsshdir = 0733
PROTOTYPE_USER_rootsshdir = root
PROTOTYPE_GROUP_rootsshdir = root

include gar/category.mk

post-install-modulated:
	@ginstall -d $(DESTDIR)$(localstatedir)/rootsh
	@$(MAKECOOKIE)
