# vim: ft=make ts=4 sw=4 noet
# This makefile is to be included from Makefiles in each category
# directory.

# This contains all directories containing packages
SUBDIRS = cpan xfce

FILTER_DIRS = CVS/

default:
	@echo "You are in the pkg/ directory."

%:
	@for i in $(filter-out $(FILTER_DIRS),$(wildcard */)) ; do \
		$(MAKE) -C $$i $* ; \
	done

paranoid-%:
	@for i in $(filter-out $(FILTER_DIRS),$(wildcard */)) ; do \
		$(MAKE) -C $$i $* || exit 2; \
	done

export BUILDLOG ?= $(shell pwd)/buildlog.txt

report-%:
	@for i in $(filter-out $(FILTER_DIRS),$(wildcard */)) ; do \
		$(MAKE) -C $$i $* || echo "	*** make $* in $$i failed ***" >> $(BUILDLOG); \
	done

# When the complete package tree is checked out there would be literally hundreds
# of instances of GAR as they are referenced as external references. Alternatively
# you can check out the tree with
#   svn co --ignore-externals https://.../pkg
# and then run
#   gmake garlinks
# to generate symbolic links instead of externally checked out dirs

# Lines returned by 'svn propget -R' look like this:
#
# gar/trunk - gar https://gar.svn.sf.net/svnroot/gar/csw/mgar/gar/v1
# gar-v1 https://gar.svn.sf.net/svnroot/gar/csw/mgar/gar/v1
# gar-v2 https://gar.svn.sf.net/svnroot/gar/csw/mgar/gar/v2
# 
# ...

garlinks:
	@(svn propget svn:externals -R | perl -ane 'next if( /^$$/ ); if( $$F[1] eq "-" ) { ($$path,$$sep,$$dir,$$link)=@F; } else { ($$dir,$$link) = @F; } ($$upsteps=$$path)=~s![^/]+!..!g;(($$linkdest=$$link))=~ s!https://gar.svn.sf.net/svnroot/gar/csw/mgar!$$upsteps!;print "Linking $$path/$$dir to ../$$linkdest", symlink("../$$linkdest","$$path/$$dir") ? "" : " failed", "\n";')

pkglist:
	@for i in $(filter-out $(FILTER_DIRS),$(foreach D,. $(SUBDIRS),$(wildcard $D/*/))) ; do \
		$(MAKE) -s -C $$i/trunk pkglist ; \
	done

newpkg-%:
	@svn mkdir $* $*/tags $*/branches $*/trunk $*/trunk/files
	@(echo "GARNAME = package";                                     								\
	echo "GARVERSION = 1.0";                                        								\
	echo "CATEGORIES = category";                                   								\
	echo "";                                                        								\
	echo "DESCRIPTION = Brief description";                         								\
	echo "define BLURB";                                            								\
	echo "  Long description";                                      								\
	echo "endef";                                                   								\
	echo "";                                                        								\
	echo "MASTER_SITES = ";                                         								\
	echo "DISTFILES  = $$(GARNAME)-$$(GARVERSION).tar.gz";          								\
	echo "DISTFILES += $$(call admfiles,CSWpackage,)";              								\
	echo "";                                                        								\
	echo "# We define upstream file regex so we can be notifed of new upstream software release";  	\
	echo "UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz";										\
	echo "";                                                        								\
	echo "# If the url used to check for software update is different of MASTER_SITES, then ";   	\
	echo "# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES"; 	\
	echo "# UPSTREAM_MASTER_SITES = ";                                         						\
	echo "";                                                        								\
	echo "CONFIGURE_ARGS = $$(DIRPATHS)";                          									\
	echo "";                                                        								\
	echo "include gar/category.mk";                                 								\
	) > $*/trunk/Makefile
	@svn add $*/trunk/Makefile
	@(echo "%var            bitname package";                       								\
	echo "%var            pkgname CSWpackage";                      								\
	echo "%include        url file://%{PKGLIB}/csw_dyndepend.gspec";								\
	echo "%copyright      url file://%{WORKSRC}/LICENSE";           								\
	) > $*/trunk/files/CSWpackage.gspec
	@echo "cookies\ndownload\nwork\n" | svn propset svn:ignore -F /dev/fd/0 $*/trunk
	@echo "gar https://gar.svn.sf.net/svnroot/gar/csw/mgar/gar/v1" | svn propset svn:externals -F /dev/fd/0 $*/trunk
	@svn co https://gar.svn.sf.net/svnroot/gar/csw/mgar/gar/v1 $*/trunk/gar
	@echo
	@echo "Your package is set up for editing at $*/trunk"
	@echo "Please don't forget to add the gspec-file!"

