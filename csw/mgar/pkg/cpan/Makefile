default:
	@echo "You are in the pkg/cpan directory."

newpkg-%:
	@svn mkdir $* $*/tags $*/branches $*/trunk $*/trunk/files
	@(echo "GARNAME = My-Perl-Module";			\
	echo "GARVERSION = 1.234";				\
	echo "CATEGORIES = cpan";				\
	echo "AUTHOR = CPAUTH";					\
	echo "";						\
	echo "DESCRIPTION = Brief description";			\
	echo "define BLURB";					\
  	echo "  Long description";				\
	echo "endef";						\
	echo "";						\
	echo "DISTFILES += $$(call admfiles,CSWpmmyperlmod,)";	\
	echo "";						\
	echo "include gar/category.mk";				\
	) > $*/trunk/Makefile
	@svn add $*/trunk/Makefile
	@(echo "%var            bitname pm_myperlmod";		\
	echo "%var            pkgname CSWpmmyperlmod";		\
	echo "%var            arch all";			\
	echo "%include        url file://%{PKGLIB}/csw_cpan.gspec"; \
	echo "%copyright      url file://%{WORKSRC}/COPYING";	\
	) > $*/trunk/files/CSWpmmyperlmod.gspec
	@echo "cookies\ndownload\nwork\n" | svn propset svn:ignore -F /dev/fd/0 $*/trunk
	@echo "gar https://gar.svn.sf.net/svnroot/gar/csw/mgar/gar/v1" | svn propset svn:externals -F /dev/fd/0 $*/trunk
	@svn co https://gar.svn.sf.net/svnroot/gar/csw/mgar/gar/v1 $*/trunk/gar
	@echo
	@echo "Your package is set up for editing at $*/trunk"
	@echo "Please don't forget to add the gspec-file!"

