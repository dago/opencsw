GARNAME = xbill
GARVERSION = 2.1
CATEGORIES = apps

DESCRIPTION = Seek out and destroy all forms of Bill
define BLURB
  Ever get the feeling that nothing is going right? You're a sysadmin,
  and someone's trying to destroy your computers. The little people
  running around the screen are trying to infect your computers with
  Wingdows [TM], a virus cleverly designed to resemble a popular
  operating system. Additionally, some computers are connected with
  network cables. When one computer on a network becomes infected,
  a spark will be sent down the cable, and will infect the computer
  on the other end when it reaches there.
endef

MASTER_SITES = http://www.xbill.org/download/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

SPKG_SOURCEURL = http://www.xbill.org

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

REQUIRED_PKGS = CSWglib CSWgtk CSWxaw3d CSWxpm

CONFIGURE_ARGS = $(DIRPATHS)

EXTRA_LDFLAGS = -L$(libdir) -lXpm -lX11

TEST_SCRIPTS =

include gar/category.mk
