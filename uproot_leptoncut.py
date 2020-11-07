import uproot as ROOT
import uproot_methods as upm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import font_manager
import mplhep as hep
import sys


## argument check
try:
  input = raw_input
except:
  pass



if len(sys.argv) < 2:
	print(" running method: macro_file_name.py input_file_name.root")

## Read your Tree
dat1 = ROOT.open(sys.argv[1])["Delphes"]
dat2 = ROOT.open(sys.argv[2])["Delphes"]
dat3 = ROOT.open(sys.argv[3])["Delphes"]
dat4 = ROOT.open(sys.argv[4])["Delphes"]
dat5 = ROOT.open(sys.argv[5])["Delphes"]
dat6 = ROOT.open(sys.argv[6])["Delphes"]
dat7 = ROOT.open(sys.argv[7])["Delphes"]

## Convert ROOT to jagged arrays
MET1_arr, Elec1_PT_arr, Muon1_PT_arr = dat1.arrays(['MissingET.MET', 'Electron.PT', 'Muon.PT'],outputtype=tuple)
MET2_arr, Elec2_PT_arr, Muon2_PT_arr = dat2.arrays(['MissingET.MET', 'Electron.PT', 'Muon.PT'],outputtype=tuple)
MET3_arr, Elec3_PT_arr, Muon3_PT_arr = dat3.arrays(['MissingET.MET', 'Electron.PT', 'Muon.PT'],outputtype=tuple)
MET4_arr, Elec4_PT_arr, Muon4_PT_arr = dat4.arrays(['MissingET.MET', 'Electron.PT', 'Muon.PT'],outputtype=tuple)
MET5_arr, Elec5_PT_arr, Muon5_PT_arr = dat5.arrays(['MissingET.MET', 'Electron.PT', 'Muon.PT'],outputtype=tuple)
MET6_arr, Elec6_PT_arr, Muon6_PT_arr = dat6.arrays(['MissingET.MET', 'Electron.PT', 'Muon.PT'],outputtype=tuple)
MET7_arr, Elec7_PT_arr, Muon7_PT_arr = dat7.arrays(['MissingET.MET', 'Electron.PT', 'Muon.PT'],outputtype=tuple)



## Normalization factor
x_ttbar = 50.9
x_ww = 5.142
x_wz = 2.075
x_zz = 0.397
x_singletop = 2.289
x_dm10 = 0.0002683
x_dm100 = 0.0002523
lumi = 150000

tot_evt = 10000.0
tot_evt2 = 100000.0


ttbar = MET1_arr.flatten()
ww = MET2_arr.flatten()
wz = MET3_arr.flatten()
zz = MET4_arr.flatten()
sintop = MET5_arr.flatten()
dm10 = MET6_arr.flatten()
dm100 = MET7_arr.flatten()


weight_ttbar = np.ones(ttbar.shape) * x_ttbar * lumi / tot_evt2
weight_ww = np.ones(ww.shape) * x_ww * lumi / tot_evt
weight_wz = np.ones(wz.shape) * x_wz * lumi / tot_evt
weight_zz = np.ones(zz.shape) * x_zz * lumi / tot_evt
weight_singletop = np.ones(sintop.shape) * x_singletop * lumi / tot_evt
weight_dm10 = np.ones(dm10.shape) * x_dm10 * lumi / tot_evt
weight_dm100 = np.ones(dm100.shape) * x_dm100 * lumi / tot_evt


x = [sintop,zz,wz,ww,ttbar]
we = [weight_singletop,weight_zz,weight_wz,weight_ww,weight_ttbar]
co = ['yellow','purple', 'limegreen', 'cyan', 'blue']
la = ['Single top', 'ZZ', 'WZ', 'WW', 'top pair']
## UNDER DEBUGGING


## Draw histogram
plt.style.use(hep.style.ROOT)
plt.rcParams["figure.figsize"] = (8,8)
plt.xlim(0,500)
plt.ylim(0.01, 100000000)
plt.hist(x, range=(0,500), weights=we, bins=8, color=co, label = la, stacked=True)
plt.hist(dm10, range=(0,500),weights=weight_dm10, bins=8, label='$M$$_{\chi}$ = 10 GeV',color='red', histtype='step')
plt.hist(dm100, range=(0,500),weights=weight_dm100, bins=8, label='$M$$_{\chi}$ = 100 GeV',color='darkred', histtype='step')


plt.yscale('log')
plt.rc('xtick',labelsize=10)
plt.rc('ytick',labelsize=10)
plt.title("$\sqrt{s}$ = 13 TeV, L = 150 fb$^{-1}$", loc='left',fontsize=15)
plt.xlabel("$E$$^{miss}_{T}$ [GeV]", fontsize=15)
plt.ylabel("Expected Number of Events | 40 GeV", fontsize=15)
plt.minorticks_on()
plt.legend(fontsize=12)
plt.savefig("met_lepcut.png")

