###  Package Section  ###
PACKAGES  = CSWgcc4ada CSWgcc4adart CSWgcc4gfortran CSWgcc4gfortranrt
PACKAGES += CSWgcc4java CSWgcc4javart CSWgcc4objc CSWgcc4objcrt
PACKAGES += CSWgcc4g++ CSWgcc4g++rt CSWgcc4corert CSWgcc4core
 
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
COMMON_REQUIRE                   = CSWiconv CSWlibgmp CSWlibmpfr CSWggettextrt
REQUIRED_PKGS_CSWgcc4adart       = CSWgcc4corert $(COMMON_REQUIRE)
REQUIRED_PKGS_CSWgcc4ada         = CSWgcc4core CSWgcc4corert 
REQUIRED_PKGS_CSWgcc4ada        += CSWgcc4adart $(COMMON_REQUIRE)
REQUIRED_PKGS_CSWgcc4corert      = $(COMMON_REQUIRE)
REQUIRED_PKGS_CSWgcc4core        = CSWgcc4corert CSWbinutils $(COMMON_REQUIRE) 
REQUIRED_PKGS_CSWgcc4g++rt       = CSWgcc4corert $(COMMON_REQUIRE)
REQUIRED_PKGS_CSWgcc4g++         = CSWgcc4core CSWgcc4corert 
REQUIRED_PKGS_CSWgcc4g++        += CSWgcc4g++rt $(COMMON_REQUIRE)
REQUIRED_PKGS_CSWgcc4gfortranrt  = CSWgcc4corert $(COMMON_REQUIRE)
REQUIRED_PKGS_CSWgcc4gfortran    = CSWgcc4core CSWgcc4corert 
REQUIRED_PKGS_CSWgcc4gfortran   += CSWgcc4gfortranrt $(COMMON_REQUIRE)
REQUIRED_PKGS_CSWgcc4javart      = CSWgcc4corert CSWgcc4g++rt $(COMMON_REQUIRE)
REQUIRED_PKGS_CSWgcc4java        = CSWgcc4core CSWgcc4corert 
REQUIRED_PKGS_CSWgcc4java       += CSWgcc4javart CSWzlib 
REQUIRED_PKGS_CSWgcc4java       += CSWgcc4g++ CSWgcc4g++rt $(COMMON_REQUIRE)
REQUIRED_PKGS_CSWgcc4objcrt      = CSWgcc4corert $(COMMON_REQUIRE)
REQUIRED_PKGS_CSWgcc4objc        = CSWgcc4core CSWgcc4corert 
REQUIRED_PKGS_CSWgcc4objc       += CSWgcc4objcrt $(COMMON_REQUIRE)

DISTFILES += CSWgcc4core.space

define CSWgcc4core_postinstall
#!/bin/sh

Error()
{
	echo "=====> postinstall Error: $$1" >&2
	exit 1
}

OS_REV="`/usr/bin/uname -r | sed -e 's/[^.]*//'`"
case `/usr/bin/uname -p` in
	"sparc") OS_TARGET="sparc-sun-solaris2.8" ;;
	 "i386") OS_TARGET="i386-pc-solaris2$${OS_REV}" ;;
esac

TOOLS_DIR="$${PKG_INSTALL_ROOT}/opt/csw/gcc4/libexec/gcc"
TOOLS_DIR="$${TOOLS_DIR}/$${OS_TARGET}/$(GARVERSION)/install-tools"
MKHEADERS_CMD="$${PKG_INSTALL_ROOT}/opt/csw/gcc4/bin/mkheaders"
INCLUDE_DIR="$${PKG_INSTALL_ROOT}/opt/csw/gcc4/lib/gcc"
INCLUDE_DIR="$${INCLUDE_DIR}/$${OS_TARGET}/$(GARVERSION)/include"

cat << _EOF_
******************************************************************************
* NOTICE: Fixing the system headers
*
* Do not forget: whenever your system headers change 
* Run the $${MKHEADERS_CMD} script!
******************************************************************************
_EOF_

if [ -f $${TOOLS_DIR}/mkheaders ]; then
	cp $${TOOLS_DIR}/mkheaders $${MKHEADERS_CMD}
	installf $${PKGINST} "$${MKHEADERS_CMD}"
else
	Error "$${TOOLS_DIR}/mkheaders Not Found"
fi

if [ -f $${MKHEADERS_CMD} ];then
	chmod 0755 $${MKHEADERS_CMD} 2>/dev/null
	chown root:bin $${MKHEADERS_CMD} 2>/dev/null
	"$${MKHEADERS_CMD}" || Error "$${MKHEADERS_CMD} Failed."
else
	Error "Could not find $${MKHEADERS_CMD}"
fi

if [ -d $${INCLUDE_DIR} ]; then
	chmod 0755 $${INCLUDE_DIR} || Error "Failed to chmod $${INCLUDE_DIR}"
	chown -R root:bin $${INCLUDE_DIR} || 
			Error "Failed to change ownership for $${INCLUDE_DIR}"
	find $${INCLUDE_DIR} -print | installf $${PKGINST} -
fi


cat << _EOF_
******************************************************************************
* NOTICE: Successfully fixed system headers
*
* Do not forget: whenever your system headers change 
* Run the $${MKHEADERS_CMD} script!
******************************************************************************
_EOF_
	
installf -f $${PKGINST}

exit 0
endef

