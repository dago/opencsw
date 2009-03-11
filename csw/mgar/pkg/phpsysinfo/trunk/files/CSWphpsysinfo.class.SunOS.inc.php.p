--- class.SunOS.inc.php.071122	Wed Nov 21 07:34:15 2007
+++ class.SunOS.inc.php	Wed Nov 21 09:00:27 2007
@@ -153,20 +153,27 @@
 
         preg_match('/^(\D+)(\d+)$/', $ar_buf[0], $intf);
         $prefix = $intf[1] . ':' . $intf[2] . ':' . $intf[1] . $intf[2] . ':';
-        $cnt = $this->kstat($prefix . 'drop');
+        $tmp = $this->kstat($prefix);
+        if (preg_match('/:drop/',$tmp)) {
+          $cnt = $this->kstat($prefix . 'drop');
 
-        if ($cnt > 0) {
-          $results[$ar_buf[0]]['rx_drop'] = $cnt;
-        } 
-        $cnt = $this->kstat($prefix . 'obytes64');
+          if ($cnt > 0) {
+            $results[$ar_buf[0]]['rx_drop'] = $cnt;
+          } 
+        }
+        if (preg_match('/:obytes64/',$tmp)) {
+          $cnt = $this->kstat($prefix . 'obytes64');
 
-        if ($cnt > 0) {
-          $results[$ar_buf[0]]['tx_bytes'] = $cnt;
-        } 
-        $cnt = $this->kstat($prefix . 'rbytes64');
+          if ($cnt > 0) {
+            $results[$ar_buf[0]]['tx_bytes'] = $cnt;
+          } 
+        }
+        if (preg_match('/:rbytes64/',$tmp)) {
+          $cnt = $this->kstat($prefix . 'rbytes64');
 
-        if ($cnt > 0) {
-          $results[$ar_buf[0]]['rx_bytes'] = $cnt;
+          if ($cnt > 0) {
+            $results[$ar_buf[0]]['rx_bytes'] = $cnt;
+          }
         }
       } 
     } 
@@ -211,6 +218,10 @@
       if (hide_mount($ar_buf[5])) {
         continue;
       }
+
+      if (hide_fstype(trim($ty_buf[1]))) {
+        continue;
+      }
 
       $results[$j] = array();
 
