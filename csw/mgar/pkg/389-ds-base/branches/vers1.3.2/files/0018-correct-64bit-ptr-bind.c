--- a/ldap/servers/slapd/bind.c
+++ b/ldap/servers/slapd/bind.c
@@ -119,7 +119,8 @@ do_bind( Slapi_PBlock *pb )
 {
     BerElement	*ber = pb->pb_op->o_ber;
     int		err, isroot;
-    ber_tag_t 	method = LBER_DEFAULT;
+    ber_tag_t 	ber_method = LBER_DEFAULT;
+    int 	method = 0;
     ber_int_t	version = -1;
     int		auth_response_requested = 0;
     int		pw_response_requested = 0;
@@ -162,7 +163,7 @@ do_bind( Slapi_PBlock *pb )
      *	}
      */
 
-    ber_rc = ber_scanf( ber, "{iat", &version, &rawdn, &method );
+    ber_rc = ber_scanf( ber, "{iat", &version, &rawdn, &ber_method );
     if ( ber_rc == LBER_ERROR ) {
         LDAPDebug( LDAP_DEBUG_ANY,
                    "ber_scanf failed (op=Bind; params=Version,DN,Method)\n",
@@ -173,6 +174,8 @@ do_bind( Slapi_PBlock *pb )
         slapi_ch_free_string(&rawdn);
         return;
     }
+    /* (int) = (long) */
+    method = (int)(ber_method & 0xffff);
     /* Check if we should be performing strict validation. */
     if (rawdn && config_get_dn_validate_strict()) { 
         /* check that the dn is formatted correctly */
