#!/bin/bash
#
# update-t4-patch - retrieve the last t4 engine patch from
#                   hg.openindiana.org repository 
#           

PKCS11_ENGINE_FILES="e_pk11.c e_pk11.h e_pk11_err.c e_pk11_err.h e_pk11_pub.c e_pk11_uri.c e_pk11_uri.h"
SOURCE_URL="http://buildfarm.opencsw.org/source/raw/solaris-userland/components/openssl/openssl-1.0.1/"
WGET_OPTIONS="--quiet"


if [[ -z "$1" ]]; then
	echo "Usage: update-pkcs11-patch.sh OPENSSL_VERSION"
	exit 1
fi

VERSION="$1"
PATCH_FILE="openssl-${VERSION}-pkcs11-engine.patch"
PATCH_DATE=$(date +"%Y-%m-%d %H:%M:%S.%N %z")

echo "Updating pkcs11 engine patch from ${SOURCE_URL}..."
(
	# ar in in /usr/ccs/bin under Solaris 9 and 10 so we change the path
	wget $WGET_OPTIONS --output-document=- ${SOURCE_URL}/patches/15-pkcs11_engine-0.9.8a.patch | \

		sed -e 's/\/usr\/bin\/ar/\/usr\/ccs\/bin\/ar/g'

	# in the repository, the new files are not part of the patch, but we merge them
	# in a single patch
	for FILE in $PKCS11_ENGINE_FILES; do \

		wget $WGET_OPTIONS --output-document="${PATCH_FILE}.tmp" "${SOURCE_URL}/engines/pkcs11/$FILE"
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



