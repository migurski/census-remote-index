adjoined.csv: \
	 adjoined/20151ak.csv adjoined/20151hi.csv adjoined/20151mi.csv adjoined/20151nv.csv \
     adjoined/20151tx.csv adjoined/20151al.csv adjoined/20151ia.csv adjoined/20151mn.csv \
     adjoined/20151ny.csv adjoined/20151us.csv adjoined/20151ar.csv adjoined/20151id.csv \
     adjoined/20151mo.csv adjoined/20151oh.csv adjoined/20151ut.csv adjoined/20151az.csv \
     adjoined/20151il.csv adjoined/20151ms.csv adjoined/20151ok.csv adjoined/20151va.csv \
     adjoined/20151ca.csv adjoined/20151in.csv adjoined/20151mt.csv adjoined/20151or.csv \
     adjoined/20151vt.csv adjoined/20151co.csv adjoined/20151ks.csv adjoined/20151nc.csv \
     adjoined/20151pa.csv adjoined/20151wa.csv adjoined/20151ct.csv adjoined/20151ky.csv \
     adjoined/20151nd.csv adjoined/20151pr.csv adjoined/20151wi.csv adjoined/20151dc.csv \
     adjoined/20151la.csv adjoined/20151ne.csv adjoined/20151ri.csv adjoined/20151wv.csv \
     adjoined/20151de.csv adjoined/20151ma.csv adjoined/20151nh.csv adjoined/20151sc.csv \
     adjoined/20151wy.csv adjoined/20151fl.csv adjoined/20151md.csv adjoined/20151nj.csv \
     adjoined/20151sd.csv adjoined/20151ga.csv adjoined/20151me.csv adjoined/20151nm.csv \
     adjoined/20151tn.csv
	cat \
	 adjoined/20151ak.csv adjoined/20151hi.csv adjoined/20151mi.csv adjoined/20151nv.csv \
     adjoined/20151tx.csv adjoined/20151al.csv adjoined/20151ia.csv adjoined/20151mn.csv \
     adjoined/20151ny.csv adjoined/20151us.csv adjoined/20151ar.csv adjoined/20151id.csv \
     adjoined/20151mo.csv adjoined/20151oh.csv adjoined/20151ut.csv adjoined/20151az.csv \
     adjoined/20151il.csv adjoined/20151ms.csv adjoined/20151ok.csv adjoined/20151va.csv \
     adjoined/20151ca.csv adjoined/20151in.csv adjoined/20151mt.csv adjoined/20151or.csv \
     adjoined/20151vt.csv adjoined/20151co.csv adjoined/20151ks.csv adjoined/20151nc.csv \
     adjoined/20151pa.csv adjoined/20151wa.csv adjoined/20151ct.csv adjoined/20151ky.csv \
     adjoined/20151nd.csv adjoined/20151pr.csv adjoined/20151wi.csv adjoined/20151dc.csv \
     adjoined/20151la.csv adjoined/20151ne.csv adjoined/20151ri.csv adjoined/20151wv.csv \
     adjoined/20151de.csv adjoined/20151ma.csv adjoined/20151nh.csv adjoined/20151sc.csv \
     adjoined/20151wy.csv adjoined/20151fl.csv adjoined/20151md.csv adjoined/20151nj.csv \
     adjoined/20151sd.csv adjoined/20151ga.csv adjoined/20151me.csv adjoined/20151nm.csv \
     adjoined/20151tn.csv \
     > $@

adjoined/%.csv:
	python adjoin.py $@ All_Geographies/g$*.csv All_Geographies/e$*???????.txt
