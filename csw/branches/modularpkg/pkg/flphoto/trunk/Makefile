GARNAME = flphoto
GARVERSION = 1.2
CATEGORIES = apps

DESCRIPTION = basic image management and display program based on the FLTK toolkit
define BLURB
flPhoto is a basic image management and display program based on the FLTK toolkit and is provided under the terms of the GNU General Public License. It can read, write, and display digital camera EXIF information and supports the following image file formats: BMP CRW JPEG PhotoCD PNG
endef

MASTER_SITES = http://easynews.dl.sourceforge.net/sourceforge/fltk/
DISTFILES  = $(GARNAME)-$(GARVERSION)-source.tar.gz
DISTFILES += $(call admfiles,CSWflphoto, prototype)

PATCHFILES = Fl_Image_Display.cxx.diff
PATCHFILES = gamma.cxx.diff
PATCHFILES = export.cxx.diff
PATCHFILES = image.cxx.diff
PATCHFILES = Makefile.in.diff

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

include gar/category.mk
