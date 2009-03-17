
###  Package Section  ###
PACKAGES  = CSWgcc4core CSWgcc4corert CSWgcc4docs
PACKAGES += CSWgcc4gfortran CSWgcc4gfortranrt CSWgcc4java CSWgcc4javart 
PACKAGES += CSWgcc4objc CSWgcc4objcrt CSWgcc4g++ CSWgcc4g++rt

## Define Package Catalog Names
CATALOGNAME_CSWgcc4core = gcc4core
CATALOGNAME_CSWgcc4corert = gcc4corert
CATALOGNAME_CSWgcc4core = gcc4coredocs
CATALOGNAME_CSWgcc4g++ = gcc4g++
CATALOGNAME_CSWgcc4g++rt = gcc4g++rt
CATALOGNAME_CSWgcc4gfortran = gcc4gfortran
CATALOGNAME_CSWgcc4gfortranrt = gcc4gfortranrt
CATALOGNAME_CSWgcc4java = gcc4java
CATALOGNAME_CSWgcc4javart = gcc4javart
CATALOGNAME_CSWgcc4objc = gcc4objc
CATALOGNAME_CSWgcc4objcrt = gcc4obcrt

## Define Package Descriptions
SPKG_DESC_CSWgcc4core = GNU C Compiler
SPKG_DESC_CSWgcc4corert = GNU C Compiler Run Time
SPKG_DESC_CSWgcc4coredocs = GNU C Compiler Documtation and man pages
SPKG_DESC_CSWgcc4g++ = GNU C++ Compiler
SPKG_DESC_CSWgcc4g++rt = GNU C++ Compiler Run Time
SPKG_DESC_CSWgcc4gfortran = GNU Fortran Compiler
SPKG_DESC_CSWgcc4gfortranrt = GNU Fortran Compiler Run Time
SPKG_DESC_CSWgcc4java = GNU Java Compiler
SPKG_DESC_CSWgcc4javart = GNU Java Compiler Run Time
SPKG_DESC_CSWgcc4objc = GNU Objective C Compiler
SPKG_DESC_CSWgcc4objcrt = GNU Objective C Compiler Run Time

## Define Dependencies 
REQUIRED_PKGS_CSWgcc4corert = CSWggettextrt CSWiconv CSWlibgmp CSWlibmpfr
REQUIRED_PKGS_CSWgcc4core = CSWgcc4corert
REQUIRED_PKGS_CSWgcc4g++rt = CSWgcc4core
REQUIRED_PKGS_CSWgcc4g++ = CSWgcc4g++rt
REQUIRED_PKGS_CSWgcc4gfortranrt = CSWgcc4core
REQUIRED_PKGS_CSWgcc4gfortran95 = CSWgcc4gfortranrt
REQUIRED_PKGS_CSWgcc4javart = CSWgcc4core
REQUIRED_PKGS_CSWgcc4java = CSWgcc4javart
REQUIRED_PKGS_CSWgcc4objcrt = CSWgcc4core
REQUIRED_PKGS_CSWgcc4objc = CSWgcc4objcrt

PKG_DIR = /opt/csw/gcc4
## Define the Contents of the Packages
## GNU Compiler Suite Docs
PKGFILES_CSWgcc4docs += $(PKG_DIR)/man/.*
PKGFILES_CSWgcc4docs += $(PKG_DIR)/info/.*

## gcc4objc Definitions
PKGFILES_CSWgcc4objc  = /opt/csw/share/doc/gcc4objc/license
PKGFILES_CSWgcc4objc += $(PKG_DIR)/libexec/.*/cc1obj
PKGFILES_CSWgcc4objc += $(PKG_DIR)/lib/.*/objc/.*
PKGFILES_CSWgcc4objc += $(PKG_DIR)/lib/.*/gcj/libgcj.*
## gcc4objc Runtime
PKGFILES_CSWgcc4objcrt  = /opt/csw/share/doc/gcc4objcrt/license
PKGFILES_CSWgcc4objcrt += $(PKG_DIR)/lib/.*libobjc.*

## gcc4java Definitions
PKGFILES_CSWgcc4java  = /opt/csw/share/doc/gcc4java/license
PKGFILES_CSWgcc4java  += $(PKG_DIR)/share/java.*
PKGFILES_CSWgcc4java  += $(PKG_DIR)/libexec/.*/jvgenmain
PKGFILES_CSWgcc4java  += $(PKG_DIR)/libexec/.*/jc1
PKGFILES_CSWgcc4java  += $(PKG_DIR)/lib/pkgconfig/libgcj.pc
PKGFILES_CSWgcc4java  += $(PKG_DIR)/include/.*/ffi.h
PKGFILES_CSWgcc4java  += $(PKG_DIR)/include/.*/org/.*
PKGFILES_CSWgcc4java  += $(PKG_DIR)/include/.*/java.*/.*
PKGFILES_CSWgcc4java  += $(PKG_DIR)/include/.*/gcj/.*
PKGFILES_CSWgcc4java  += $(PKG_DIR)/include/.*/classpath/.*
PKGFILES_CSWgcc4java  += $(PKG_DIR)/include/.*/awt/.*
PKGFILES_CSWgcc4java  += $(PKG_DIR)/include/.*/gnu/.*
PKGFILES_CSWgcc4java  += $(PKG_DIR)/bin/.*gcj.*
PKGFILES_CSWgcc4java  += $(PKG_DIR)/bin/jv-scan
PKGFILES_CSWgcc4java  += $(PKG_DIR)/bin/jv-convert
PKGFILES_CSWgcc4java  += $(PKG_DIR)/bin/jcf-dump
PKGFILES_CSWgcc4java  += $(PKG_DIR)/bin/grmi.*
PKGFILES_CSWgcc4java  += $(PKG_DIR)/bin/grepjar
PKGFILES_CSWgcc4java  += $(PKG_DIR)/bin/gjnih
PKGFILES_CSWgcc4java  += $(PKG_DIR)/bin/gij
PKGFILES_CSWgcc4java  += $(PKG_DIR)/bin/fastjar
PKGFILES_CSWgcc4java  += $(PKG_DIR)/bin/gjar.*
PKGFILES_CSWgcc4java  += $(PKG_DIR)/bin/gjavah
PKGFILES_CSWgcc4java  += $(PKG_DIR)/bin/gorbd
PKGFILES_CSWgcc4java  += $(PKG_DIR)/bin/addr2name.awk
PKGFILES_CSWgcc4java  += $(PKG_DIR)/bin/gappletviewer
PKGFILES_CSWgcc4java  += $(PKG_DIR)/bin/gkeytool
PKGFILES_CSWgcc4java  += $(PKG_DIR)/bin/gserialver
PKGFILES_CSWgcc4java  += $(PKG_DIR)/bin/gtnameserv
PKGFILES_CSWgcc4java  += $(PKG_DIR)/bin/gnative2ascii
PKGFILES_CSWgcc4java  += $(PKG_DIR)/bin/gc-analyze
## gcc4java RunTime
PKGFILES_CSWgcc4javart = /opt/csw/share/doc/gcc4javart/license
PKGFILES_CSWgcc4javart += $(PKG_DIR)/share/java/.*
PKGFILES_CSWgcc4javart += $(PKG_DIR)/lib/.*libgij.*
PKGFILES_CSWgcc4javart += $(PKG_DIR)/lib/.*libffi.*
PKGFILES_CSWgcc4javart += $(PKG_DIR)/lib/.*lib-gnu-awt.*
PKGFILES_CSWgcc4javart += $(PKG_DIR)/lib/security/libgcj.*
PKGFILES_CSWgcc4javart += $(PKG_DIR)/lib/security/classpath.*
PKGFILES_CSWgcc4javart += $(PKG_DIR)/lib/logging.properties
PKGFILES_CSWgcc4javart += $(PKG_DIR)/lib/gcj.*/classmap.db

## gcc4gfortran Definitions
PKGFILES_CSWgcc4gfortran = /opt/csw/share/doc/gcc4gfortran/license
PKGFILES_CSWgcc4gfortran  += $(PKG_DIR)/lib/.*/f951
PKGFILES_CSWgcc4gfortran  += $(PKG_DIR)/lib/.*gfortran
## gcc4gfortran RunTime
PKGFILES_CSWgcc4gfortranrt = /opt/csw/share/doc/gcc4gfortranrt/license
PKGFILES_CSWgcc4gfortranrt = $(PKG_DIR)/lib/.*libgfortran.*

## gcc4g++ Definitions
PKGFILES_CSWgcc4g++ = /opt/csw/share/doc/gcc4g++/license
PKGFILES_CSWgcc4g++ += $(PKG_DIR)/libexec/.*/cc1plus
PKGFILES_CSWgcc4g++ += $(PKG_DIR)/include/c++/.*
PKGFILES_CSWgcc4g++ += $(PKG_DIR)/bin/.*g++
PKGFILES_CSWgcc4g++ += $(PKG_DIR)/bin/.*c++
EXTRA_PKGFILES_EXCLUDED_CSWgcc4g++ += $(PKG_DIR)/include/.*/org/.*
EXTRA_PKGFILES_EXCLUDED_CSWgcc4g++ += $(PKG_DIR)/include/.*/java.*/.*
EXTRA_PKGFILES_EXCLUDED_CSWgcc4g++ += $(PKG_DIR)/include/.*/gcj/.*
EXTRA_PKGFILES_EXCLUDED_CSWgcc4g++ += $(PKG_DIR)/include/.*/classpath/.*
EXTRA_PKGFILES_EXCLUDED_CSWgcc4g++ += $(PKG_DIR)/include/.*/awt/.*
EXTRA_PKGFILES_EXCLUDED_CSWgcc4g++ += $(PKG_DIR)/include/.*/gnu/.*
## gcc4g++ RunTime
PKGFILES_CSWgcc4g++rt = /opt/csw/share/doc/gcc4g++rt/license
PKGFILES_CSWgcc4g++rt += $(PKG_DIR)/lib/.*libstdc.*

## gcc4core RunTime
PKGFILES_CSWgcc4corert = /opt/csw/share/doc/gcc4corert/license
PKGFILES_CSWgcc4corert = $(PKG_DIR)/lib/.*libgcc_s.*

