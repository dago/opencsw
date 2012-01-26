NAME = yasm
VERSION = 1.2.0
CATEGORIES = devel
GARTYPE = v2

DESCRIPTION = A complete rewrite of the NASM assembler
define BLURB
  Yasm is a complete rewrite of the NASM assembler under the "new" BSD License
  (some portions are under other licenses, see COPYING for details). Yasm currently
  supports the x86 and AMD64 instruction sets, accepts NASM and GAS assembler syntaxes,
  outputs binary, ELF32, ELF64, 32 and 64-bit Mach-O, RDOFF2, COFF, Win32, and Win64
  object formats, and generates source debugging information in STABS, DWARF 2, and
  CodeView 8 formats. Yasm can be easily integrated into Visual Studio 2005 (see
  VisualStudio2005) for assembly of NASM or GAS syntax code into Win32 or Win64 object files.
endef

MASTER_SITES = http://www.tortall.net/projects/yasm/releases/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

RUNTIME_DEP_PKGS_CSWyasm += CSWlibintl8

include gar/category.mk
