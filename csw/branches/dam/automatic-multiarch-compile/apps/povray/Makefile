GARNAME = povray
GARVERSION = 3.6
CATEGORIES = apps

DESCRIPTION = povray
define BLURB
endef

MASTER_SITES = http://www.povray.org/redirect/www.povray.org/ftp/pub/povray/Official/Unix/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWpovray,depend)

#PREREQUISITE_PKGS = CSWncurses CSWggettext

WORKSRC = $(WORKDIR)/$(GARNAME)-3.6.1

GARCOMPILER = GCC4

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += COMPILED_BY="$(SPKG_PACKAGER) <$(SPKG_EMAIL)>"

TEST_TARGET =

include ../category.mk


# for makefile in $(find . -name Makefile)
# do
#     gsed -i -e '/^CXXFLAGS.*/s//CXXFLAGS='"$FLAGS"' -xprofile=collect/'
# $makefile
# done
# 
# 
# rm -rf povray.profile
# gmake clean
# gmake -j $(psrinfo | wc -l)
# 
# for i in $(find scenes -name \*.pov)
# do
#     echo $i
#     echo ${i%/*}
#     unix/povray -D +A +L ./include/ +L ${i%/*}/ $i
# done
# 
# for makefile in $(find . -name Makefile)
# do
#    gsed -i -e 's~^CXXFLAGS.*~CXXFLAGS='"$FLAGS"'
# -xprofile=use:'$(pwd)'\/povray~' $makefile
# done
# 
# gmake clean
# gmake -j $(psrinfo | wc -l)
# 
# mkdir -p cswstage/opt/csw/bin/${ARCH}
# cp unix/povray cswstage/opt/csw/bin/${ARCH}
# 
# }
# 
# FLAGS='-fast -xnolibmopt -xspace -xtarget=ss20 -xarch=v8'
# ARCH=sparcv8
# build
# 
# FLAGS='-fast -xtarget=ultra2'
# ARCH=sparcv8plus+vis
# build
# 
# if isalist | grep vis2 ; then
# FLAGS='-fast -xtarget=ultra3i -xarch=v8plusb'
# ARCH=sparcv9+vis2
# build
# fi
# 
