PyChumil
========

Ch'umil means star in kaqchikel. This is a small python library to process some common and simple data about stars. Right now it just converts from celestial coords to horizon coords. 

I've made this for my astronomy homework. The functions used were ported from javascript; thanks to the work of Stephen R. Schmitt http://mysite.verizon.net/res148h4j/javascript/script_celestial2horizon.html. 

As a program, it shows the 20 most bright stars as seen from Guatemala. You can pass other value for lat and lon.

This uses the HYG catalog found here http://www.astronexus.com/hyg.

Right now, ("Thu Jul 31 2014 18:05:21 GMT-0600 (CST)") the output is this:

```
UTC:2014-08-01 00:06:19.479921, lat: 14.613000, lon: -90.535000
Arcturus (Gliesse Gl 541)  (BayerFlamsteed 16Alp Boo) Magnitud=-0.050000
                  [Altitud 82.160894, Azimuth 306.619433 ] 
Rigel Kentaurus A (Gliesse Gl 559  A)  (BayerFlamsteed Alp1Cen) Magnitud=-0.010000
                  [Altitud 14.550036, Azimuth 180.329142 ] 
Vega (Gliesse Gl 721)  (BayerFlamsteed 3Alp Lyr) Magnitud=0.030000
                  [Altitud 33.391350, Azimuth 52.884108 ] 
Hadar (Gliesse )  (BayerFlamsteed Bet Cen) Magnitud=0.610000
                  [Altitud 14.615503, Azimuth 184.896667 ] 
Altair (Gliesse Gl 768)  (BayerFlamsteed 53Alp Aql) Magnitud=0.760000
                  [Altitud 14.596208, Azimuth 84.449730 ] 
Acrux (Gliesse )  (BayerFlamsteed Alp1Cru) Magnitud=0.770000
                  [Altitud 7.949360, Azimuth 194.771299 ] 
Spica (Gliesse )  (BayerFlamsteed 67Alp Vir) Magnitud=0.980000
                  [Altitud 57.918572, Azimuth 217.574070 ] 
Antares (Gliesse )  (BayerFlamsteed 21Alp Sco) Magnitud=1.060000
                  [Altitud 41.396959, Azimuth 147.465466 ] 
 (Gliesse )  (BayerFlamsteed Bet Cru) Magnitud=1.250000
                  [Altitud 12.169437, Azimuth 194.329256 ] 
Deneb (Gliesse )  (BayerFlamsteed 50Alp Cyg) Magnitud=1.250000
                  [Altitud 10.476665, Azimuth 45.689336 ] 
Rigel Kentaurus B (Gliesse Gl 559  B)  (BayerFlamsteed Alp2Cen) Magnitud=1.350000
                  [Altitud 14.545677, Azimuth 180.332253 ] 
Regulus (Gliesse )  (BayerFlamsteed 32Alp Leo) Magnitud=1.360000
                  [Altitud 23.549979, Azimuth 276.898797 ] 
 (Gliesse )  (BayerFlamsteed Gam Cru) Magnitud=1.590000
                  [Altitud 13.290231, Azimuth 197.583532 ] 
Shaula (Gliesse )  (BayerFlamsteed 35Lam Sco) Magnitud=1.620000
                  [Altitud 24.443786, Azimuth 143.448043 ] 
Alioth (Gliesse )  (BayerFlamsteed 77Eps UMa) Magnitud=1.760000
                  [Altitud 43.740776, Azimuth 339.355827 ] 
Kaus Australis (Gliesse )  (BayerFlamsteed 20Eps Sgr) Magnitud=1.790000
                  [Altitud 18.070988, Azimuth 134.344690 ] 
Dubhe (Gliesse )  (BayerFlamsteed 50Alp UMa) Magnitud=1.810000
                  [Altitud 29.161758, Azimuth 333.766602 ] 
Alkaid (Gliesse )  (BayerFlamsteed 85Eta UMa) Magnitud=1.850000
                  [Altitud 53.535290, Azimuth 344.955053 ] 
 (Gliesse )  (BayerFlamsteed The Sco) Magnitud=1.860000
                  [Altitud 19.823956, Azimuth 147.474665 ] 
 (Gliesse )  (BayerFlamsteed Alp TrA) Magnitud=1.910000
                  [Altitud 3.407485, Azimuth 169.173653 ] 
```
