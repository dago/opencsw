GARNAME = alpine
GARVERSION = 2.0
CATEGORIES = apps

DESCRIPTION = Alpine Messaging System
define BLURB
	Alpine is a fast, easy to use email client that is suitable for both 
	the inexperienced email user as well as for the most demanding of power 
	users. Alpine is based on the Pine® Message System, which was also
   	developed at the University of Washington. Alpine can be learned by 
	exploration and the use of context-sensitive help. The user experience 
	is highly customizable through the use of the Alpine Setup command. 
endef

MASTER_SITES = http://www.washington.edu/alpine
SPKG_SOURCE_URL = ftp://ftp.cac.washington.edu/alpine/
DISTFILES  = $(GARNAME).tar.bz2

PACKAGES = CSWalpine
CATALOGNAME_CSWgd = alpine
SPKG_DESC_CSWgd = $(DESCRIPTION)

# We define upstream file regex so we can be notifed of new 
# upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

#BUILD64 = 1

CONFIGURE_ARGS  = $(DIRPATHS)

include gar/category.mk
