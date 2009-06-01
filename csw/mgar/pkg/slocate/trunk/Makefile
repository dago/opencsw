# Todo
# * Build fails due to missing fts.h -> incooperate from gnulib
# * Go through README to implement correct file ownership / modes
# * Use cswusergroups to add slocate group
GARNAME = slocate
GARVERSION = 3.1
CATEGORIES = utils

DESCRIPTION = Secure locate alternative
define BLURB
  Secure locate provides a secure way to index and quickly search for
  files on your system. It uses incremental encoding just like GNU locate
  to compress its database to make searching faster, but it will also
  check file permissions and ownership so that users will not see files
  they do not have access to.
endef

MASTER_SITES = http://slocate.trakker.ca/files/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
SPKG_SOURCEURL = http://slocate.trakker.ca/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_SCRIPTS =
BUILD_ARGS = PATH=/opt/csw/gnu:$(PATH) \
		CC=$(CC) CFLAGS="$(CFLAGS)" LDFLAGS="$(LDFLAGS)"

INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	# tbd
	@$(MAKECOOKIE)
