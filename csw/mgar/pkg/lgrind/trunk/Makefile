# $Id$

NAME	=	lgrind
VERSION	=	3.67
GARTYPE	=	v2

DESCRIPTION	=	Produce beautiful listings of source code with LaTeX
define BLURB
  LGrind is a descendant of the Unix utility vgrind. It prepares
  various programming language source code (e.g., C, C++, Pascal,
  BASIC, Modula2, Fortran, RATFOR Yacc, PostScript, Prolog, MLisp,
  Icon, LaTeX, Perl, CSH Bourne Shell, assembler, 68000 assembler,
  asm68, VMS assembler, ISP, LDL, Linda, MODEL, MatLab, Russell) for
  pretty-printing within LaTeX. Options for producing includable files
  and processing embedded listings in LaTeX texts are provided.
endef

DISTNAME		=	lgrind
MASTER_SITES	=	http://mirror.ctan.org/support/
DISTFILES		=	$(DISTNAME).zip
DISTFILES		+=	COPYING
PATCHFILES		+=	0001-adapt-to-OCSW-file-tree.patch

BUILD_DEP_PKGS	=	CSWtexlive

GARCOMPILER		=	GNU

LINKER_MAP_RELEASE	=
LINKER_MAPS			=
LINKER_DIRECT		=
LINKER_IGNORE		=

CONFIGURE_SCRIPTS	=
TEST_SCRIPTS		=

RUNTIME_DEP_PKGS_CSWlgrind		=	CSWtexlive
CHECKPKG_OVERRIDES_CSWlgrind	+=	surplus-dependency|CSWtexlive

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

