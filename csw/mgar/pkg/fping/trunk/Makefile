NAME 		= fping
VERSION 	= 3.2
CATEGORIES 	= utils
GARTYPE 	= v2

#
# package definitions
#

PACKAGES		= CSWfping
SPKG_DESC_CSWfping	= A ping like program accepting any number of hosts
CATALOGNAME_CSWfping	= fping

#
# blurb
#

define BLURB
  fping is a ping(1) like program which uses the Internet Control
  Message Protocol (ICMP) echo request to determine if a host is up.
  fping is different from ping in that you can specify any number of
  hosts on the command line, or specify a file containing the lists
  of hosts to ping. Instead of trying one host until it timeouts or
  replies, fping will send out a ping packet and move on to the next
  host in a round-robin fashion. If a host replies, it is noted and
  removed from the list of hosts to check. If a host does not respond
  within a certain time limit and/or retry limit it will be considered
  unreachable.
endef

#
# download, distfiles, patchfiles
#

MASTER_SITES	= http://fping.org/dist/
DISTFILES	= $(NAME)-$(VERSION).tar.gz
VENDOR_URL	= http://fping.org/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

#
# reinplacements
#

REINPLACE_USRLOCAL	+= doc/fping*

#
# configure
#

CONFIGURE_ARGS = $(DIRPATHS)

#
# nothing to be done here for installation and packaging
#

include gar/category.mk

