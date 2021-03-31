import numpy as np
import matplotlib.pyplot as plt
import mplhep as hep

tt_gen_evt = 10000000
another_evt = 1000000
wght_tt = np.ones(tt.shape) * x_tt * lumi/ tt_gen_evt
wght_ttV = np.ones(ttV.shape) * x_ttV *lumi/ another_evt
wght_dy = np.ones(dy.shape) * x_dy *lumi/ another_evt
wght_ww = np.ones(ww.shape) * x_ww *lumi/ another_evt
wght_wz = np.ones(wz.shape) * x_wz *lumi/ another_evt
wght_zz = np.ones(zz.shape) * x_zz *lumi/ another_evt
wght_st = np.ones(st.shape) * x_st *lumi/ another_evt

wght_dm = np.ones(dm.shape) * x_dm1t *lumi/ another_evt
wght_dm2 = np.ones(dm2.shape) * x_dm2t *lumi/ another_evt



stak = [np.clip(st,0,1000,out=st),np.clip(zz,0,1000,out=zz),np.clip(wz,0,1000,out=wz),np.clip(ww,0,1000,out=ww),np.clip(dy,0,1000,out=dy),np.clip(ttV,0,1000,out=ttV),np.clip(tt,0,1000,out=tt)]
we = [wght_st,wght_zz, wght_wz, wght_ww, wght_dy, wght_ttV, wght_tt]
co = ['dodgerblue','green','yellow','violet','cyan','slategray','blue']
co2 = ['black','black','black', 'black', 'black','black','black']
la = ['Single top','ZZ','WZ','WW','Drell-Yan','Top pair + V','Top pair']


## Plotting
plt.style.use(hep.style.CMS)
plt.xlim(50,1000)
plt.ylim(0.00001, 10000000000000)
plt.hist(stak, range=(0,1000), weights=we, bins=20, color=co, label = la, stacked=True)
plt.hist(stak, range=(0,1000), weights=we, bins=20, color=co2,histtype='step', stacked=True)
plt.hist(np.clip(dm,0,1000,out=dm), range=(0,1000), weights=wght_dm, bins=20, color='red',histtype='step', label='$M$$_{\chi}$ = 10 GeV\n$M$$_{Y}$ = 0.1 TeV')
plt.hist(np.clip(dm2,0,1000,out=dm2), range=(0,1000), weights=wght_dm2, bins=20, color='darkred',histtype='step', label='$M$$_{\chi}$ = 10 GeV\n$M$$_{Y}$ = 1 TeV')
plt.yscale('log')
plt.rc('xtick',labelsize=10)
plt.rc('ytick',labelsize=10)
plt.title("$\sqrt{s}$ = 14 TeV, L = 300 fb$^{-1}$", loc='left',fontsize=15)
#plt.xlabel("$M$$_{T2}$ [GeV]", fontsize=15)
plt.xlabel("$E$$^{miss}_{T}$ [GeV]", fontsize=15)
plt.ylabel("Expected Number of Events | 50 GeV", fontsize=15)
plt.minorticks_on()
plt.legend(fontsize=12)
plt.savefig("met_new.png")

