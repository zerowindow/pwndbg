# Table stolen from
# http://ps-2.kev009.com/wisclibrary/aix52/usr/share/man/info/en_US/a_doc_lib/aixassem/alangref/branch_mnem.htm
powerpc = """
      bc+             bc-             bca+            bca-
       bcctr+          bcctr-          bcctrl+         bcctrl-
       bcl+            bcl-            bcla+           bcla-
       bclr+           bclr-           bclrl+          bclrl-
       bdneq+          bdneq-          bdnge+          bdnge-
       bdngt+          bdngt-          bdnle+          bdnle-
       bdnlt+          bdnlt-          bdnne+          bdnne-
       bdnns+          bdnns-          bdnso+          bdnso-
       bdnz+           bdnz-           bdnza+          bdnza-
       bdnzf+          bdnzf-          bdnzfa+         bdnzfa-
       bdnzfl+         bdnzfl-         bdnzfla+        bdnzfla-
       bdnzflr+        bdnzflr-        bdnzflrl+       bdnzflrl-
       bdnzl+          bdnzl-          bdnzla+         bdnzla-
       bdnzlr+         bdnzlr-         bdnzlrl+        bdnzlrl-
       bdnzt+          bdnzt-          bdnzta+         bdnzta-
       bdnztl+         bdnztl-         bdnztla+        bdnztla-
       bdnztlr+        bdnztlr-        bdnztlrl+       bdnztlrl-
       bdz+            bdz-            bdza+           bdza-
       bdzeq+          bdzeq-          bdzf+           bdzf-
       bdzfa+          bdzfa-          bdzfl+          bdzfl-
       bdzfla+         bdzfla-         bdzflr+         bdzflr-
       bdzflrl+        bdzflrl-        bdzge+          bdzge-
       bdzgt+          bdzgt-          bdzl+           bdzl-
       bdzla+          bdzla-          bdzle+          bdzle-
       bdzlr+          bdzlr-          bdzlrl+         bdzlrl-
       bdzlt+          bdzlt-          bdzne+          bdzne-
       bdzns+          bdzns-          bdzso+          bdzso-
       bdzt+           bdzt-           bdzta+          bdzta-
       bdztl+          bdztl-          bdztla+         bdztla-
       bdztlr+         bdztlr-         bdztlrl+        bdztlrl-
       beq+            beq-            beqa+           beqa-
       beqctr+         beqctr-         beqctrl+        beqctrl-
       beql+           beql-           beqla+          beqla-
       beqlr+          beqlr-          beqlrl+         beqlrl-
       bf+             bf-             bfa+            bfa-
       bfctr+          bfctr-          bfctrl+         bfctrl-
       bfl+            bfl-            bfla+           bfla-
       bflr+           bflr-           bflrl+          bflrl-
       bge+            bge-            bgea+           bgea-
       bgectr+         bgectr-         bgectrl+        bgectrl-
       bgel+           bgel-           bgela+          bgela-
       bgelr+          bgelr-          bgelrl+         bgelrl-
       bgt+            bgt-            bgta+           bgta-
       bgtctr+         bgtctr-         bgtctrl+        bgtctrl-
       bgtl+           bgtl-           bgtla+          bgtla-
       bgtlr+          bgtlr-          bgtlrl+         bgtlrl-
       ble+            ble-            blea+           blea-
       blectr+         blectr-         blectrl+        blectrl-
       blel+           blel-           blela+          blela-
       blelr+          blelr-          blelrl+         blelrl-
       blt+            blt-            blta+           blta-
       bltctr+         bltctr-         bltctrl+        bltctrl-
       bltl+           bltl-           bltla+          bltla-
       bltlr+          bltlr-          bltlrl+         bltlrl-
       bne+            bne-            bnea+           bnea-
       bnectr+         bnectr-         bnectrl+        bnectrl-
       bnel+           bnel-           bnela+          bnela-
       bnelr+          bnelr-          bnelrl+         bnelrl-
       bng+            bng-            bnga+           bnga-
       bngctr+         bngctr-         bngctrl+        bngctrl-
       bngl+           bngl-           bngla+          bngla-
       bnglr+          bnglr-          bnglrl+         bnglrl-
       bnl+            bnl-            bnla+           bnla-
       bnlctr+         bnlctr-         bnlctrl+        bnlctrl-
       bnll+           bnll-           bnlla+          bnlla-
       bnllr+          bnllr-          bnllrl+         bnllrl-
       bns+            bns-            bnsa+           bnsa-
       bnsctr+         bnsctr-         bnsctrl+        bnsctrl-
       bnsl+           bnsl-           bnsla+          bnsla-
       bnslr+          bnslr-          bnslrl+         bnslrl-
       bnu+            bnu-            bnua+           bnua-
       bnuctr+         bnuctr-         bnuctrl+        bnuctrl-
       bnul+           bnul-           bnula+          bnula-
       bnulr+          bnulr-          bnulrl+         bnulrl-
       bnz+            bnz-            bnza+           bnza-
       bnzctr+         bnzctr-         bnzctrl+        bnzctrl-
       bnzl+           bnzl-           bnzla+          bnzla-
       bnzlr+          bnzlr-          bnzlrl+         bnzlrl-
       bso+            bso-            bsoa+           bsoa-
       bsoctr+         bsoctr-         bsoctrl+        bsoctrl-
       bsol+           bsol-           bsola+          bsola-
       bsolr+          bsolr-          bsolrl+         bsolrl-
       bt+             bt-             bta+            bta-
       btctr+          btctr-          btctrl+         btctrl-
       btl+            btl-            btla+           btla-
       btlr+           btlr-           btlrl+          btlrl-
       bun+            bun-            buna+           buna-
       bunctr+         bunctr-         bunctrl+        bunctrl-
       bunl+           bunl-           bunla+          bunla-
       bunlr+          bunlr-          bunlrl+         bunlrl-
       bz+             bz-             bza+            bza-
       bzctr+          bzctr-          bzctrl+         bzctrl-
       bzl+            bzl-            bzla+           bzla-
       bzlr+           bzlr-           bzlrl+          bzlrl-
""".strip().split()

branches = set(map(lambda x: x.rstrip('+-'), powerpc))
