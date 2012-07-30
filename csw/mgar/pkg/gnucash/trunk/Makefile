# $Id$

NAME = gnucash
VERSION = 2.4.11
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = A personal and small-business financial-accounting software
define BLURB
  GnuCash is personal and small-business financial-accounting software, freely
  licensed under the GNU GPL and available for GNU/Linux, BSD, Solaris,
  Mac OS X and Microsoft Windows.

  Designed to be easy to use, yet powerful and flexible, GnuCash allows you to
  track bank accounts, stocks, income and expenses. As quick and intuitive to
  use as a checkbook register, it is based on professional accounting
  principles to ensure balanced books and accurate reports.

  Feature Highlights

    Double-Entry Accounting
    Stock/Bond/Mutual Fund Accounts
    Small-Business Accounting
    Reports, Graphs
    QIF/OFX/HBCI Import, Transaction Matching
    Scheduled Transactions
    Financial Calculations
endef

MASTER_SITES	=	$(SF_MIRRORS)
DISTFILES		=	$(DISTNAME).tar.bz2

BUILD_DEP_PKGS	+=	CSWlibgconf-dev
BUILD_DEP_PKGS	+=	CSWlibglib2-dev
BUILD_DEP_PKGS	+=	CSWlibgtk2-dev
BUILD_DEP_PKGS	+=	CSWguile
BUILD_DEP_PKGS	+=	CSWlibart
BUILD_DEP_PKGS	+=	CSWlibglade2
BUILD_DEP_PKGS	+=	CSWlibgnomeprint
BUILD_DEP_PKGS	+=	CSWlibgnomeui-devel
BUILD_DEP_PKGS	+=	CSWlibgsf-dev
BUILD_DEP_PKGS	+=	CSWlibxml2-dev
BUILD_DEP_PKGS	+=	CSWpangodevel
BUILD_DEP_PKGS	+=	CSWswig
BUILD_DEP_PKGS	+=	CSWgtkhtml31
BUILD_DEP_PKGS	+=	CSWlibdbi-dev
BUILD_DEP_PKGS	+=	CSWlibgnome-dev
BUILD_DEP_PKGS	+=	CSWlibgtkhtml
BUILD_DEP_PKGS	+=	CSWlibgnomecanvas-dev

GARCOMPILER		=	GNU
CONFIGURE_ARGS	=	$(DIRPATHS)

PACKAGING_PLATFORMS	=	solaris10-sparc
PACKAGING_PLATFORMS	+=	solaris10-i386

include gar/category.mk

PATH := /opt/csw/gnu:/opt/csw/libexec/flex-2.5.35/bin:$(PATH)

# this is private and not available publicly
mydependencies:
	for package in $(PACKAGES); do echo '___' $${package}; $(HOME)/bin/ocswdeplist --depth 1 --dependencies --packaging --csw --prototype $(HOME)/opencsw/$(NAME)/trunk/work/build-global/$${package}.prototype --target $(HOME)/opencsw/$(NAME)/trunk/work/pkgroot; done
