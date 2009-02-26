
###  Package Section  ###
PACKAGES  = CSWgcc4core CSWgcc4corert CSWgcc4docs
PACKAGES += CSWgcc4g95 CSWgcc4g95rt CSWgcc4java CSWgcc4javart 
PACKAGES += CSWgcc4objc CSWgcc4objcrt CSWgcc4g++ CSWgcc4g++rt

## Define Package Catalog Names
CATALOGNAME_CSWgcc4core   = gcc4core
CATALOGNAME_CSWgcc4corert = gcc4corert
CATALOGNAME_CSWgcc4core   = gcc4coredocs
CATALOGNAME_CSWgcc4g++    = gcc4g++
CATALOGNAME_CSWgcc4g++rt  = gcc4g++rt
CATALOGNAME_CSWgcc4g95    = gcc4g95
CATALOGNAME_CSWgcc4g95rt  = gcc4g95rt
CATALOGNAME_CSWgcc4java   = gcc4java
CATALOGNAME_CSWgcc4javart = gcc4javart
CATALOGNAME_CSWgcc4objc   = gcc4objc
CATALOGNAME_CSWgcc4objcrt = gcc4obcrt

## Define Package Descriptions
SPKG_DESC_CSWgcc4core     = GNU C Compiler
SPKG_DESC_CSWgcc4corert   = GNU C Compiler Run Time
SPKG_DESC_CSWgcc4coredocs = GNU C Compiler Documtation and man pages
SPKG_DESC_CSWgcc4g++      = GNU C++ Compiler
SPKG_DESC_CSWgcc4g++rt    = GNU C++ Compiler Run Time
SPKG_DESC_CSWgcc4g95      = GNU Fortran Compiler
SPKG_DESC_CSWgcc4g95rt    = GNU Fortran Compiler Run Time
SPKG_DESC_CSWgcc4java     = GNU Java Compiler
SPKG_DESC_CSWgcc4javart   = GNU Java Compiler Run Time
SPKG_DESC_CSWgcc4objc     = GNU Objective C Compiler
SPKG_DESC_CSWgcc4objcrt   = GNU Objective C Compiler Run Time

## Define Dependencies 
REQUIRED_PKGS_CSWgcc4corert = CSWggettextrt CSWiconv CSWlibgmp CSWlibmpfr
REQUIRED_PKGS_CSWgcc4core   = CSWgcc4corert
REQUIRED_PKGS_CSWgcc4g++rt  = CSWgcc4core
REQUIRED_PKGS_CSWgcc4g++    = CSWgcc4g++rt
REQUIRED_PKGS_CSWgcc4g95rt  = CSWgcc4core
REQUIRED_PKGS_CSWgcc4g95    = CSWgcc4g95rt
REQUIRED_PKGS_CSWgcc4javart = CSWgcc4core
REQUIRED_PKGS_CSWgcc4java   = CSWgcc4javart
REQUIRED_PKGS_CSWgcc4objcrt = CSWgcc4core
REQUIRED_PKGS_CSWgcc4objc   = CSWgcc4objcrt

## Define the Contents of the Packages
## GNU Compiler Suite Docs
PKGFILES_CSWgcc4docs  = $(datadir)/doc/.*
PKGFILES_CSWgcc4docs += $(mandir)/.*
PKGFILES_CSWgcc4docs += $(infodir)/.*

## gcc4objc Definitions
PKGFILES_CSWgcc4objc  = $(libexecdir)/.*/cc1obj
PKGFILES_CSWgcc4objc += $(libdir)/.*/objc/.*
PKGFILES_CSWgcc4objc += $(libdir)/.*/gcj/libgcj.*
## gcc4objc Runtime
PKGFILES_CSWgcc4objcrt  = $(libdir)/.*libobjc.*

## gcc4java Definitions
PKGFILES_CSWgcc4java   = $(datadir)/java.*
PKGFILES_CSWgcc4java  += $(libexecdir)/.*/jvgenmain
PKGFILES_CSWgcc4java  += $(libexecdir)/.*/jc1
PKGFILES_CSWgcc4java  += $(libdir)/pkgconfig/libgcj.pc
PKGFILES_CSWgcc4java  += $(includedir)/.*/ffi.h
PKGFILES_CSWgcc4java  += $(includedir)/.*/org/.*
PKGFILES_CSWgcc4java  += $(includedir)/.*/java.*/.*
PKGFILES_CSWgcc4java  += $(includedir)/.*/gcj/.*
PKGFILES_CSWgcc4java  += $(includedir)/.*/classpath/.*
PKGFILES_CSWgcc4java  += $(includedir)/.*/awt/.*
PKGFILES_CSWgcc4java  += $(includedir)/.*/gnu/.*
PKGFILES_CSWgcc4java  += $(bindir)/.*gcj.*
PKGFILES_CSWgcc4java  += $(bindir)/jv-scan
PKGFILES_CSWgcc4java  += $(bindir)/jv-convert
PKGFILES_CSWgcc4java  += $(bindir)/jcf-dump
PKGFILES_CSWgcc4java  += $(bindir)/grmi.*
PKGFILES_CSWgcc4java  += $(bindir)/grepjar
PKGFILES_CSWgcc4java  += $(bindir)/gjnih
PKGFILES_CSWgcc4java  += $(bindir)/gij
PKGFILES_CSWgcc4java  += $(bindir)/fastjar
PKGFILES_CSWgcc4java  += $(bindir)/gjar.*
PKGFILES_CSWgcc4java  += $(bindir)/gjavah
PKGFILES_CSWgcc4java  += $(bindir)/gorbd
PKGFILES_CSWgcc4java  += $(bindir)/addr2name.awk
PKGFILES_CSWgcc4java  += $(bindir)/gappletviewer
PKGFILES_CSWgcc4java  += $(bindir)/gkeytool
PKGFILES_CSWgcc4java  += $(bindir)/gserialver
PKGFILES_CSWgcc4java  += $(bindir)/gtnameserv
PKGFILES_CSWgcc4java  += $(bindir)/gnative2ascii
PKGFILES_CSWgcc4java  += $(bindir)/gc-analyze
## gcc4java RunTime
PKGFILES_CSWgcc4javart  = $(datadir)/java/.*
PKGFILES_CSWgcc4javart += $(libdir)/.*libgij.*
PKGFILES_CSWgcc4javart += $(libdir)/.*libffi.*
PKGFILES_CSWgcc4javart += $(libdir)/.*lib-gnu-awt.*
PKGFILES_CSWgcc4javart += $(libdir)/security/libgcj.*
PKGFILES_CSWgcc4javart += $(libdir)/security/classpath.*
PKGFILES_CSWgcc4javart += $(libdir)/logging.properties
PKGFILES_CSWgcc4javart += $(libdir)/gcj.*/classmap.db

## gcc4g95 Definitions
PKGFILES_CSWgcc4g95   = $(libexecdir)/.*/f951
PKGFILES_CSWgcc4g95  += $(bindir)/.*gfortran
## gcc4g95 RunTime
PKGFILES_CSWgcc4g95rt = $(libdir)/.*libgfortran.*

## gcc4g++ Definitions
PKGFILES_CSWgcc4g++  = $(libexecdir)/.*/cc1plus
PKGFILES_CSWgcc4g++ += $(includedir)/c\+\+/.*
PKGFILES_CSWgcc4g++ += $(bindir)/.*g\+\+
PKGFILES_CSWgcc4g++ += $(bindir)/.*c\+\+
EXTRA_PKGFILES_EXCLUDED_CSWgcc4g++ += $(includedir)/.*/org/.*
EXTRA_PKGFILES_EXCLUDED_CSWgcc4g++ += $(includedir)/.*/java.*/.*
EXTRA_PKGFILES_EXCLUDED_CSWgcc4g++ += $(includedir)/.*/gcj/.*
EXTRA_PKGFILES_EXCLUDED_CSWgcc4g++ += $(includedir)/.*/classpath/.*
EXTRA_PKGFILES_EXCLUDED_CSWgcc4g++ += $(includedir)/.*/awt/.*
EXTRA_PKGFILES_EXCLUDED_CSWgcc4g++ += $(includedir)/.*/gnu/.*
## gcc4g++ RunTime
PKGFILES_CSWgcc4g++rt  = $(libdir)/.*libstdc.*

## gcc4core RunTime
PKGFILES_CSWgcc4corert = $(libdir)/.*libgcc_s.*

