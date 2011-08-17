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
TOOLS_DIR="$${TOOLS_DIR}/$${OS_TARGET}/$(VERSION)/install-tools"
MKHEADERS_CMD="$${PKG_INSTALL_ROOT}/opt/csw/gcc4/bin/mkheaders"
INCLUDE_DIR="$${PKG_INSTALL_ROOT}/opt/csw/gcc4/lib/gcc"
INCLUDE_DIR="$${INCLUDE_DIR}/$${OS_TARGET}/$(VERSION)/include"

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
