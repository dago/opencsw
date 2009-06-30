*** p7zip_4.65.orig/install.sh	Sun Mar  2 14:35:05 2008
--- p7zip_4.65/install.sh	Tue Jun 30 10:24:02 2009
***************
*** 166,172 ****
    echo "- installing HTML help in ${DEST_DIR}${DEST_SHARE_DOC}/DOCS"
    mkdir -p "${DEST_DIR}${DEST_SHARE_DOC}"
    cp -r DOCS "${DEST_DIR}${DEST_SHARE_DOC}/DOCS"
!   find "${DEST_DIR}${DEST_SHARE_DOC}/DOCS" -type d -exec chmod 555 {} \;
    find "${DEST_DIR}${DEST_SHARE_DOC}/DOCS" -type f -exec chmod 444 {} \;
  fi
  
--- 166,172 ----
    echo "- installing HTML help in ${DEST_DIR}${DEST_SHARE_DOC}/DOCS"
    mkdir -p "${DEST_DIR}${DEST_SHARE_DOC}"
    cp -r DOCS "${DEST_DIR}${DEST_SHARE_DOC}/DOCS"
!   find "${DEST_DIR}${DEST_SHARE_DOC}/DOCS" -type d -exec chmod 755 {} \;
    find "${DEST_DIR}${DEST_SHARE_DOC}/DOCS" -type f -exec chmod 444 {} \;
  fi
  
