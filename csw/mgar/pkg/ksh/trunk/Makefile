NAME = ksh
VERSION = 93t+
CATEGORIES = devel
GARTYPE = v2

DESCRIPTION = The KornShell Command and Programming Language
define BLURB
  The KornShell language was designed and developed by David G. Korn at AT&T
  Bell Laboratories. It is an interactive command language that provides
  access to the UNIX system and to many other systems, on the many different
  computers and workstations on which it is implemented.
endef

# Main archive location
MASTER_SITES = http://www2.research.att.com/~gsf/download/tgz/
DISTFILES += ast-ksh.2011-02-08.tgz
DISTFILES += INIT.2012-01-01.tgz
#DISTFILES  = $(NAME)-$(VERSION).tar.gz

WGET_OPTS = --user="I accept www.opensource.org/licenses/eclipse" --password="."
# We define upstream file regex so we can be notifed of new upstream software release
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

