GARNAME = xrestop
GARVERSION = 0.3
CATEGORIES = utils

DESCRIPTION = 'top' like staticstics for X11 server side resource usage
define BLURB
  Xrestop uses the X-Resource extension to provide 'top' like statistics of
  each connected X11 client's server side resource usage. It is intended as a
  developer tool to aid more efficient server resource usage and debug server
  side leakage.  It should work with any server supporting the X-Resource
  extension, including the freedesktop.org server and XFree86 4.3+. "xdpyinfo
  | grep Resource" should tell you if your server supports this extension. 
endef

MASTER_SITES = http://www.freedesktop.org/software/xrestop/
DISTFILES    = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES   += $(call admfiles,CSWxrestop,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

include gar/category.mk
