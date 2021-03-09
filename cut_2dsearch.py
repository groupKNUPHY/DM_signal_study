## Pseudocode ##

for i in range(1000):
        for j in range(1000):
                mask = (met_tt > i) & (ht_tt > j)
                tt = met_tt[mask]
                mask = (met_ttV > i) & (ht_ttV > j)
                ttV = met_ttV[mask]
                mask = (met_dy > i) & (ht_dy > j)
                dy = met_dy[mask]
                mask = (met_ww > i) & (ht_ww > j)
                ww = met_ww[mask]
                mask = (met_wz > i) & (ht_wz > j)
                wz = met_wz[mask]
                mask = (met_zz > i) & (ht_zz > j)
                zz = met_zz[mask]
                mask = (met_st > i) & (ht_st > j)
                st = met_st[mask]
                mask = (met_dm > i) & (ht_dm > j)
                dm = met_dm[mask]
                wght_tt = x_tt * lumi/ tt_gen_evt
                wght_ttV = x_ttV *lumi/ another_evt
                wght_dy =  x_dy *lumi/ another_evt
                wght_ww =  x_ww *lumi/ another_evt
                wght_wz = x_wz *lumi/ another_evt
                wght_zz =  x_zz *lumi/ another_evt
                wght_st =  x_st *lumi/ another_evt
                wght_dm =  x_dm1t *lumi/ another_evt
                bkg = np.sqrt(len(tt)*wght_tt+len(ttV)*wght_ttV+len(dy)*wght_dy+len(ww)*wght_ww+len(wz)*wght_wz+len(zz)*wght_zz+len(st)*wght_st+len(dm)*wght_dm)
                sig = len(dm)*wght_dm
                sn = sig / bkg
                x1.append(i)
                y1.append(j)
                z1.append(sn)

