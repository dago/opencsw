default:
	@echo "You are in the pkg/ directory."

newpkg-%:
	@svn mkdir $* $*/tags $*/branches $*/trunk $*/trunk/files
	@(echo "GARNAME = package";                                     \
	echo "GARVERSION = 1.0";                                        \
	echo "CATEGORIES = category";                                   \
	echo "";                                                        \
	echo "DESCRIPTION = Brief description";                         \
	echo "define BLURB";                                            \
	echo "  Long description";                                      \
	echo "endef";                                                   \
	echo "";                                                        \
	echo "MASTER_SITES = ";                                         \
	echo "DISTFILES  = $$(GARNAME)-$$(GARVERSION).tar.gz";          \
	echo "DISTFILES += $$(call admfiles,CSWpackage,)";              \
	echo "";                                                        \
	echo "CONFIGURE_ARGS = $$(DIRPATHS)";                           \
	echo "";                                                        \
	echo "include gar/category.mk";                                 \
	) > $*/trunk/Makefile
	@svn add $*/trunk/Makefile
	@(echo "%var            bitname package";                       \
	echo "%var            pkgname CSWpackage";                      \
	echo "%include        url file://%{PKGLIB}/csw_dyndepend.gspec";\
	echo "%copyright      url file://%{WORKSRC}/LICENSE";           \
	) > $*/trunk/files/CSWpackage.gspec
	@echo "cookies\ndownload\nwork\n" | svn propset svn:ignore -F /dev/fd/0 $*/trunk
	@echo "gar https://gar.svn.sf.net/svnroot/gar/csw/mgar/gar/v1" | svn propset svn:externals -F /dev/fd/0 $*/trunk
	@svn co https://gar.svn.sf.net/svnroot/gar/csw/mgar/gar/v1 $*/trunk/gar
	@echo
	@echo "Your package is set up for editing at $*/trunk"
	@echo "Please don't forget to add the gspec-file!"

