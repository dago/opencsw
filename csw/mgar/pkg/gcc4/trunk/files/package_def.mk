###  Package Section  ###
PACKAGES  = CSWgcc4core CSWgcc4corert CSWgcc4gfortran 
PACKAGES += CSWgcc4gfortranrt CSWgcc4java CSWgcc4javart 
PACKAGES += CSWgcc4objc CSWgcc4objcrt CSWgcc4g++ CSWgcc4g++rt
 
## Define Package Catalog Names
CATALOGNAME_CSWgcc4ada        = gcc4ada
CATALOGNAME_CSWgcc4adart      = gcc4adart
CATALOGNAME_CSWgcc4core       = gcc4core
CATALOGNAME_CSWgcc4corert     = gcc4corert
CATALOGNAME_CSWgcc4g++        = gcc4g++
CATALOGNAME_CSWgcc4g++rt      = gcc4g++rt
CATALOGNAME_CSWgcc4gfortran   = gcc4gfortran
CATALOGNAME_CSWgcc4gfortranrt = gcc4gfortranrt
CATALOGNAME_CSWgcc4java       = gcc4java
CATALOGNAME_CSWgcc4javart     = gcc4javart
CATALOGNAME_CSWgcc4objc       = gcc4objc
CATALOGNAME_CSWgcc4objcrt     = gcc4objcrt

## Source URLs
SPKG_SOURCEURL_CSWgcc4ada        = http://gcc.gnu.org
SPKG_SOURCEURL_CSWgcc4adart      = http://gcc.gnu.org
SPKG_SOURCEURL_CSWgcc4core       = http://gcc.gnu.org
SPKG_SOURCEURL_CSWgcc4corert     = http://gcc.gnu.org
SPKG_SOURCEURL_CSWgcc4g++        = http://gcc.gnu.org
SPKG_SOURCEURL_CSWgcc4g++rt      = http://gcc.gnu.org
SPKG_SOURCEURL_CSWgcc4gfortran   = http://gcc.gnu.org
SPKG_SOURCEURL_CSWgcc4gfortranrt = http://gcc.gnu.org
SPKG_SOURCEURL_CSWgcc4java       = http://gcc.gnu.org
SPKG_SOURCEURL_CSWgcc4javart     = http://gcc.gnu.org
SPKG_SOURCEURL_CSWgcc4objc       = http://gcc.gnu.org
SPKG_SOURCEURL_CSWgcc4objcrt     = http://gcc.gnu.org

## Copyright File
LICENSE_CSWgcc4ada        = COPYING3
LICENSE_CSWgcc4adart      = COPYING3
LICENSE_CSWgcc4core       = COPYING3
LICENSE_CSWgcc4corert     = COPYING3
LICENSE_CSWgcc4g++        = COPYING3
LICENSE_CSWgcc4g++rt      = COPYING3
LICENSE_CSWgcc4gfortran   = COPYING3
LICENSE_CSWgcc4gfortranrt = COPYING3
LICENSE_CSWgcc4java       = COPYING3
LICENSE_CSWgcc4javart     = COPYING3
LICENSE_CSWgcc4objc       = COPYING3
LICENSE_CSWgcc4objcrt     = COPYING3

## Define Package Descriptions
SPKG_DESC_CSWgcc4ada        = GNU C ADA Compiler
SPKG_DESC_CSWgcc4adart      = GNU C ADA Compiler Run Time
SPKG_DESC_CSWgcc4core       = GNU C Compiler
SPKG_DESC_CSWgcc4corert     = GNU C Compiler Run Time
SPKG_DESC_CSWgcc4g++        = GNU C++ Compiler
SPKG_DESC_CSWgcc4g++rt      = GNU C++ Compiler Run Time
SPKG_DESC_CSWgcc4gfortran   = GNU Fortran Compiler
SPKG_DESC_CSWgcc4gfortranrt = GNU Fortran Compiler Run Time
SPKG_DESC_CSWgcc4java       = GNU Java Compiler
SPKG_DESC_CSWgcc4javart     = GNU Java Compiler Run Time
SPKG_DESC_CSWgcc4objc       = GNU Objective C Compiler
SPKG_DESC_CSWgcc4objcrt     = GNU Objective C Compiler Run Time

## Define Dependencies 
COMMON_REQUIRE                   = CSWiconv CSWlibgmp CSWlibmpfr
REQUIRED_PKGS_CSWgcc4adart       = CSWggettextrt $(COMMON_REQUIRE)
REQUIRED_PKGS_CSWgcc4ada         = CSWgcc4adart $(COMMON_REQUIRE)
REQUIRED_PKGS_CSWgcc4corert      = CSWggettextrt $(COMMON_REQUIRE)
REQUIRED_PKGS_CSWgcc4core        = CSWgcc4corert $(COMMON_REQUIRE)
REQUIRED_PKGS_CSWgcc4g++rt       = CSWgcc4corert CSWiconv
REQUIRED_PKGS_CSWgcc4g++         = CSWgcc4g++rt $(COMMON_REQUIRE)
REQUIRED_PKGS_CSWgcc4gfortranrt  = CSWgcc4corert CSWiconv
REQUIRED_PKGS_CSWgcc4gfortran    = CSWgcc4gfortranrt $(COMMON_REQUIRE)
REQUIRED_PKGS_CSWgcc4javart      = CSWgcc4corert CSWgcc4g++rt CSWiconv
REQUIRED_PKGS_CSWgcc4java        = CSWgcc4javart CSWgcc4corert 
REQUIRED_PKGS_CSWgcc4java       += CSWzlib $(COMMON_REQUIRE)
REQUIRED_PKGS_CSWgcc4objcrt      = CSWgcc4corert CSWiconv
REQUIRED_PKGS_CSWgcc4objc        = CSWgcc4objcrt $(COMMON_REQUIRE)

## Define the Contents of the Packages

## gcc4ada Definitions
PKGFILES_CSWgcc4ada  = .*/libexec/.*gnat1
PKGFILES_CSWgcc4ada += .*/adalib/.*
PKGFILES_CSWgcc4ada += .*/adainclude/.*
PKGFILES_CSWgcc4ada += .*/info/.*gnat.*
PKGFILES_CSWgcc4ada += .*/bin/gnat.*

## gcc4gfortran Definitions
PKGFILES_CSWgcc4gfortran  = .*/bin/.*gfortran
PKGFILES_CSWgcc4gfortran += .*/libexec/.*f951
PKGFILES_CSWgcc4gfortran += .*/man1/gfortran.1
PKGFILES_CSWgcc4gfortran += .*/info/gfortran.*

## gcc4g++ Definitions
PKGFILES_CSWgcc4g++  = .*/bin/.*g\+\+
PKGFILES_CSWgcc4g++ += .*/bin/.*c\+\+
PKGFILES_CSWgcc4g++ += .*/libexec/.*cc1plus
PKGFILES_CSWgcc4g++ += .*/man1/g\+\+.1
PKGFILES_CSWgcc4g++ += .*/include/c\+\+/(\d+(?:\.\d+)*)/[a-fA-F,h-iH-I,k-nI-N,p-zP-Z,]+.*
PKGFILES_CSWgcc4g++ += .*/include/c\+\+/(\d+(?:\.\d+)*)/ostream.*

## gcc4java Definitions
PKGFILES_CSWgcc4java  = .*/bin/.*gcj.*
PKGFILES_CSWgcc4java += .*/bin/.*jv-scan
PKGFILES_CSWgcc4java += .*/bin/.*jv-convert
PKGFILES_CSWgcc4java += .*/bin/.*jcf-dump
PKGFILES_CSWgcc4java += .*/bin/.*grmi.*
PKGFILES_CSWgcc4java += .*/bin/.*grepjar
PKGFILES_CSWgcc4java += .*/bin/.*gjnih
PKGFILES_CSWgcc4java += .*/bin/.*gij
PKGFILES_CSWgcc4java += .*/bin/.*fastjar
PKGFILES_CSWgcc4java += .*/bin/.*gjar.*
PKGFILES_CSWgcc4java += .*/bin/.*gjavah
PKGFILES_CSWgcc4java += .*/bin/.*gorbd
PKGFILES_CSWgcc4java += .*/bin/.*addr2name.awk
PKGFILES_CSWgcc4java += .*/bin/.*gappletviewer
PKGFILES_CSWgcc4java += .*/bin/.*gkeytool
PKGFILES_CSWgcc4java += .*/bin/.*gserialver
PKGFILES_CSWgcc4java += .*/bin/.*gtnameserv
PKGFILES_CSWgcc4java += .*/bin/.*gnative2ascii
PKGFILES_CSWgcc4java += .*/bin/.*gc-analyze
PKGFILES_CSWgcc4java += .*/man1/gcj.*
PKGFILES_CSWgcc4java += .*/man1/gij.*
PKGFILES_CSWgcc4java += .*/man1/jv.*
PKGFILES_CSWgcc4java += .*/man1/jcf.*
PKGFILES_CSWgcc4java += .*/man1/grmi.*
PKGFILES_CSWgcc4java += .*/man1/.*jar.*
PKGFILES_CSWgcc4java += .*/man1/.*jni.*
PKGFILES_CSWgcc4java += .*/man1/.*java.*
PKGFILES_CSWgcc4java += .*/man1/gorbd.*
PKGFILES_CSWgcc4java += .*/man1/gapplet.*
PKGFILES_CSWgcc4java += .*/man1/gkeytool.*
PKGFILES_CSWgcc4java += .*/man1/gserialver.*
PKGFILES_CSWgcc4java += .*/man1/gtnameserv.*
PKGFILES_CSWgcc4java += .*/man1/gnative2ascii.*
PKGFILES_CSWgcc4java += .*/man1/gc-analyze.*
PKGFILES_CSWgcc4java += .*/libexec/.*collect.*
PKGFILES_CSWgcc4java += .*/libexec/.*jvgenmain
PKGFILES_CSWgcc4java += .*/libexec/.*jc1.*
PKGFILES_CSWgcc4java += .*/info/gcj.*
PKGFILES_CSWgcc4java += .*/include/.*gcj/.*
PKGFILES_CSWgcc4java += .*/include/.*awt/.*
PKGFILES_CSWgcc4java += .*/include/.*classpath/.*
PKGFILES_CSWgcc4java += .*/include/.*java.*
PKGFILES_CSWgcc4java += .*/include/.*ffi.h
PKGFILES_CSWgcc4java += .*/include/.*org/.*

## gcc4objc Definitions
PKGFILES_CSWgcc4objc  = .*/libexec/.*cc1obj
PKGFILES_CSWgcc4objc += .*/include/.*objc/.*

#######  RunTime Packages

## gcc4adart
PKGFILES_CSWgcc4adart = .*/lib/.*libgnat.*
PKGFILES_CSWgcc4adart = .*/lib/.*libgnarl.*

## gcc4corert
PKGFILES_CSWgcc4corert  = .*/lib/.*libgcc_s.*
PKGFILES_CSWgcc4corert += .*/lib/.*libgomp.*
PKGFILES_CSWgcc4corert += .*/lib/.*libiberty.*
PKGFILES_CSWgcc4corert += .*/lib/.*libssp.*

## gcc4gfortranrt 
PKGFILES_CSWgcc4gfortranrt  = .*/lib/.*libgfortran.*

## gcc4g++rt
PKGFILES_CSWgcc4g++rt  = .*/lib/.*libstdc.*
PKGFILES_CSWgcc4g++rt += .*/lib/.*libsupc\+\+.*

## gcc4javart
PKGFILES_CSWgcc4javart  = .*/share/java/.*
PKGFILES_CSWgcc4javart += .*/lib/.*libgij.*
PKGFILES_CSWgcc4javart += .*/lib/.*libffi.*
PKGFILES_CSWgcc4javart += .*/lib/.*lib-gnu-awt.*
PKGFILES_CSWgcc4javart += .*/lib/.*security/classpath.*
PKGFILES_CSWgcc4javart += .*/lib/.*logging.properties
PKGFILES_CSWgcc4javart += .*/lib/.*pkgconfig.*
PKGFILES_CSWgcc4javart += .*/lib/.*gcj.*
PKGFILES_CSWgcc4javart += .*/lib/.*libgcj.*

## gcc4objc Runtime
PKGFILES_CSWgcc4objcrt = .*/lib/.*libobjc.*
