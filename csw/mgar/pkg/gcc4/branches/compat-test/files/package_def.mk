###  Package Section  ###

# Ada awaits being built.

PACKAGES  = CSWgcc4ada
CATALOGNAME_CSWgcc4ada        = gcc4ada
SPKG_DESC_CSWgcc4ada        = GNU C ADA Compiler
PKGFILES_CSWgcc4ada  = $(libexecdir)/.*gnat1
PKGFILES_CSWgcc4ada += $(libdir)/.*libgnat.*a
PKGFILES_CSWgcc4ada += $(libdir)/.*libgnarl.*a
PKGFILES_CSWgcc4ada += .*/gcc4/.*/adalib/.*
PKGFILES_CSWgcc4ada += .*/gcc4/.*/adainclude/.*
PKGFILES_CSWgcc4ada += .*/gcc4/info/.*gnat.*
PKGFILES_CSWgcc4ada += $(bindir)/gnat(?!ive).*
RUNTIME_DEP_PKGS_CSWgcc4ada = CSWgcc4adart
RUNTIME_DEP_PKGS_CSWgcc4ada += CSWlibmpfr4
RUNTIME_DEP_PKGS_CSWgcc4ada += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWgcc4ada += CSWlibgmp10

# PACKAGES += CSWgcc4adart
# CATALOGNAME_CSWgcc4adart      = gcc4adart
# SPKG_DESC_CSWgcc4adart      = GNU C ADA Compiler Run Time
# PKGFILES_CSWgcc4adart  = $(libdir)/.*libgnat.*\.so.*
# PKGFILES_CSWgcc4adart += $(libdir)/.*libgnarl.*\.so.*
# RUNTIME_DEP_PKGS_CSWgcc4adart       = CSWgcc4corert

# PACKAGES += CSWgcc4core
# CATALOGNAME_CSWgcc4core       = gcc4core
# SPKG_DESC_CSWgcc4core       = GNU C Compiler
# RUNTIME_DEP_PKGS_CSWgcc4core = CSWgcc4corert CSWbinutils
# RUNTIME_DEP_PKGS_CSWgcc4core += CSWlibmpfr4
# RUNTIME_DEP_PKGS_CSWgcc4core += CSWlibiconv2
# RUNTIME_DEP_PKGS_CSWgcc4core += CSWlibgmp10

# PACKAGES += CSWgcc4corert
# CATALOGNAME_CSWgcc4corert     = gcc4corert
# SPKG_DESC_CSWgcc4corert     = GNU C Compiler Run Time
# PKGFILES_CSWgcc4corert  = $(libdir)/.*libgcc_s.*\.so.*
# PKGFILES_CSWgcc4corert += $(libdir)/.*libgomp.*\.so.*
# PKGFILES_CSWgcc4corert += $(libdir)/.*libssp.*\.so.*

# PACKAGES += CSWgcc4g++rt
# CATALOGNAME_CSWgcc4g++rt = gcc4g++rt
# SPKG_DESC_CSWgcc4g++rt = GNU C++ Compiler Run Time
# RUNTIME_DEP_PKGS_CSWgcc4g++rt = CSWgcc4corert
# PKGFILES_CSWgcc4g++rt  = $(libdir)/.*libstdc.*\.so.*
# supc was not found anywhere
# PKGFILES_CSWgcc4g++rt += $(libdir)/.*libsupc\+\+.*\.so.*

# PACKAGES += CSWgcc4gfortranrt
# CATALOGNAME_CSWgcc4gfortranrt = gcc4gfortranrt
# SPKG_DESC_CSWgcc4gfortranrt = GNU Fortran Compiler Run Time
# RUNTIME_DEP_PKGS_CSWgcc4gfortranrt  = CSWgcc4corert
# PKGFILES_CSWgcc4gfortranrt  = $(libdir)/.*libgfortran.*\.so.*

# PACKAGES += CSWgcc4javart
# CATALOGNAME_CSWgcc4javart     = gcc4javart
# SPKG_DESC_CSWgcc4javart     = GNU Java Compiler Run Time
# RUNTIME_DEP_PKGS_CSWgcc4javart      = CSWgcc4corert CSWgcc4g++rt
# PKGFILES_CSWgcc4javart  = $(libdir)/.*libgij.*\.so.*
# PKGFILES_CSWgcc4javart += $(libdir)/.*libffi.*\.so.*
# PKGFILES_CSWgcc4javart += $(libdir)/.*lib-gnu-awt.*\.so.*
# PKGFILES_CSWgcc4javart += $(libdir)/.*security/classpath.*
# PKGFILES_CSWgcc4javart += $(libdir)/.*logging.properties
# PKGFILES_CSWgcc4javart += $(libdir)/.*pkgconfig.*
# PKGFILES_CSWgcc4javart += $(libdir)/.*gcj.*\.so.*
# PKGFILES_CSWgcc4javart += $(libdir)/.*libgcj.*\.so.*

# PACKAGES += CSWgcc4objcrt
# CATALOGNAME_CSWgcc4objcrt     = gcc4objcrt
# SPKG_DESC_CSWgcc4objcrt     = GNU Objective C Compiler Run Time
# RUNTIME_DEP_PKGS_CSWgcc4objcrt      = CSWgcc4corert
# PKGFILES_CSWgcc4objcrt = $(libdir)/.*libobjc.*\.so.*
 
# No idea what was that for.
DISTFILES += CSWgcc4core.space

