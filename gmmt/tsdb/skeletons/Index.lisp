;;;
;;; this file should be `Index.lisp' and reside in the directory containing the
;;; tsdb(1) test suite skeleton databases (typically a subdirectory `skeletons'
;;; in the tsdb(1) database root directory `*tsdb-home*').
;;;
;;; the file should contain a single un-quote()d Common-Lisp list enumerating
;;; the available skeletons, e.g.
;;;
;;;   (((:path . "english") (:content . "English TSNLP test suite"))
;;;    ((:path . "csli") (:content . "CSLI (ERGO) test suite"))
;;;    ((:path . "vm") (:content . "English VerbMobil data")))
;;;
;;; where the individual entries are assoc() lists with at least two elements:
;;;
;;;   - :path --- the (relative) directory name containing the skeleton;
;;;   - :content --- a descriptive comment.
;;;
;;; the order of entries is irrelevant as the `tsdb :skeletons' command sorts
;;; the list lexicographically before output.
;;;

(((:path . "epo") (:content . "Espertanto test suite from Ling 567"))
 ((:path . "hau") (:content . "Hausa MMT test sentences"))
 ((:path . "hau_gmmt") (:content . "Hausa GMMT test sentences"))
 ((:path . "heb_gmmt") (:content . "Hebrew GMMT test sentences"))
 ((:path . "isl_gmmt") (:content . "Icelandic GMMT test sentences"))
 ((:path . "ita_gmmt") (:content . "Italian GMMT test sentences"))
 ((:path . "zul_gmmt") (:content . "Zulu GMMT test sentences"))
 ((:path . "eng_gmmt") (:content . "English GMMT test suite"))
 ((:path . "epo_gmmt") (:content . "Esperanto GMMT test suite"))
 ((:path . "fas_gmmt") (:content . "Farsi GMMT test suite"))
 ((:path . "fin_gmmt") (:content . "Finnish GMMT test suite"))
 ((:path . "hye_gmmt") (:content . "Armenian GMMT test suite"))
 ((:path . "arb_567") (:content . "Modern Standard Arabic test suite from Ling 567"))
 ((:path . "fin_567") (:content . "Farsi test suite from Ling 567"))
 ((:path . "hau_567") (:content . "Hausa test suite from Ling 567"))
 ((:path . "isl_567") (:content . "Icelandic general test suite"))
 ((:path . "ita_567") (:content . "Italian test suite from Ling 567"))
 ((:path . "mal_567") (:content . "Malayalam test suite from Ling 567"))
 ((:path . "zul_567") (:content . "Zulu test suite from Ling 567")))
