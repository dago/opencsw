GARNAME = xdebug
GARVERSION = 2.0.4
CATEGORIES = application

DESCRIPTION = Xdebug Extention for PHP
define BLURB
The Xdebug extension helps you debugging your script by providing a lot of valuable debug information. The debug information that Xdebug can provide includes the following:

    * stack traces and function traces in error messages with:
          o full parameter display for user defined functions
          o function name, file name and line indications
          o support for member functions
    * memory allocation
    * protection for infinite recursions
endef

MASTER_SITES = http://www.xdebug.org/
SPKG_SOURCEURL = http://www.xdebug.org/files/
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tgz

CONFIGURE_ARGS = $(DIRPATHS)

post-extract:
	@( cd $(WORKSRC) ; phpize )
	$(DONADA)
