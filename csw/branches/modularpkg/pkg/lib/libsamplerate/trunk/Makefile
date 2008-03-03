GARNAME = libsamplerate
GARVERSION = 0.1.2
CATEGORIES = lib

DESCRIPTION = Secret Rabbit Code (aka libsamplerate) is a Sample Rate Converter for audio
define BLURB
SRC is capable of arbitrary and time varying conversions ; from
downsampling by a factor of 256 to upsampling by the same factor.
Arbitrary in this case means that the ratio of input and output sample
rates can be an irrational number. The conversion ratio can also vary
with time for speeding up and slowing down effects.
endef

MASTER_SITES = http://www.mega-nerd.com/SRC
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWlibsamplerate,prototype depend)

PATCHFILES += $(notdir $(wildcard $(FILEDIR)/*.patch))

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-static

include gar/category.mk
