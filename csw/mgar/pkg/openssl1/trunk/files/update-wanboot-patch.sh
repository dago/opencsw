#!/bin/bash
#
# update-wanboot-patch - retrieve the last wanboot patch from
#                        hg.openindiana.org repository 
#           

WANBOOT_FILES=""
#SOURCE_URL="http://buildfarm.opencsw.org/source/raw/solaris-userland/components/openssl/openssl-1.0.1/"
SOURCE_URL="https://hg.openindiana.org/upstream/oracle/userland-gate/raw-file/default/components/openssl/openssl-1.0.1/"
WGET_OPTIONS="--quiet"


if [[ -z "$1" ]]; then
	echo "Usage: update-wanboot-patch.sh OPENSSL_VERSION"
	exit 1
fi

VERSION="$1"
PATCH_FILE="openssl-${VERSION}-wanboot.patch"
PATCH_DATE=$(date +"%Y-%m-%d %H:%M:%S.%N %z")

echo "Updating wanboot engine patch from ${SOURCE_URL}..."
(
	# ar in in /usr/ccs/bin under Solaris 9 and 10 so we change the path
	# we also remove the makefile part as we will not really compile wanboot
	wget $WGET_OPTIONS --output-document=- ${SOURCE_URL}/patches/102-wanboot.patch | \

		gsed -e 's/\/usr\/bin\/ar/\/usr\/ccs\/bin\/ar/g'  | \
		perl -ne 'if (/^--- .*Makefile/) { $makefile=1 } else { $makefile=0 if /^---/; }; print $_ if not $makefile'

	# in the repository, the new files are not part of the patch, but we merge them
	# in a single patch
	for FILE in $WANBOOT_FILES; do \

		wget $WGET_OPTIONS --output-document="${PATCH_FILE}.tmp" "${SOURCE_URL}/wanboot-openssl/$FILE"
		NB_LINES=$(wc -l "${PATCH_FILE}.tmp" | awk '{ print $1 }')

		echo "Index: crypto/$DIR/$FILE"
		echo "==================================================================="
		echo "diff -uNr openssl-${VERSION}/engines/$FILE openssl-${VERSION}/engines/$FILE"
		echo "--- openssl-${VERSION}/engines/$FILE 1970-01-01 01:00:00.000000000 +0100"
		echo "+++ openssl-${VERSION}/engines/$FILE ${PATCH_DATE}"
		echo "@@ -0,0 +1,${NB_LINES} @@"
		sed -e 's/^/+/' "${PATCH_FILE}.tmp"
	done
) > "${PATCH_FILE}"

rm -f "${PATCH_FILE}.tmp"
echo "Updated patch in ${PATCH_FILE}"



