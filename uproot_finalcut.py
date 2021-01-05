import uproot as ROOT
import uproot_methods as upm
import numpy as np
import awkward1 as ak
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import font_manager
import mplhep as hep


## Read your Tree
dat1 = ROOT.open("/home/twkim/sample_delphes_backup/BKG_ttbar_pow_d.root")["Delphes"]
dat2 = ROOT.open("/home/twkim/sample_delphes_backup/BKG_Drellyan.root")["Delphes"]
dat3 = ROOT.open("/home/twkim/sample_delphes_backup/BKG_Diboson_WW_E5.root")["Delphes"]
dat4 = ROOT.open("/home/twkim/sample_delphes_backup/BKG_Diboson_WZ.root")["Delphes"]
dat5 = ROOT.open("/home/twkim/sample_delphes_backup/BKG_Diboson_ZZ.root")["Delphes"]
dat6 = ROOT.open("/home/twkim/sample_delphes_backup/BKG_Singletop.root")["Delphes"]
dat7 = ROOT.open("/home/twkim/sample_delphes_backup/DM_10GeV_scalar_d.root")["Delphes"]
dat8 = ROOT.open("/home/twkim/sample_delphes_backup/DM_1GeV_0p5TeV.root")["Delphes"]


## Convert ROOT to jagged arrays
MET1_arr, Elec1_PT_arr, Muon1_PT_arr, Jet1_PT_arr = dat1.arrays(['MissingET.MET', 'Electron.PT', 'Muon.PT', 'Jet.PT'],outputtype=tuple)
MET2_arr, Elec2_PT_arr, Muon2_PT_arr, Jet2_PT_arr = dat2.arrays(['MissingET.MET', 'Electron.PT', 'Muon.PT', 'Jet.PT'],outputtype=tuple)
MET3_arr, Elec3_PT_arr, Muon3_PT_arr, Jet3_PT_arr = dat3.arrays(['MissingET.MET', 'Electron.PT', 'Muon.PT', 'Jet.PT'],outputtype=tuple)
MET4_arr, Elec4_PT_arr, Muon4_PT_arr, Jet4_PT_arr = dat4.arrays(['MissingET.MET', 'Electron.PT', 'Muon.PT', 'Jet.PT'],outputtype=tuple)
MET5_arr, Elec5_PT_arr, Muon5_PT_arr, Jet5_PT_arr = dat5.arrays(['MissingET.MET', 'Electron.PT', 'Muon.PT', 'Jet.PT'],outputtype=tuple)
MET6_arr, Elec6_PT_arr, Muon6_PT_arr, Jet6_PT_arr = dat6.arrays(['MissingET.MET', 'Electron.PT', 'Muon.PT', 'Jet.PT'],outputtype=tuple)
MET7_arr, Elec7_PT_arr, Muon7_PT_arr, Jet7_PT_arr = dat7.arrays(['MissingET.MET', 'Electron.PT', 'Muon.PT', 'Jet.PT'],outputtype=tuple)
MET8_arr, Elec8_PT_arr, Muon8_PT_arr, Jet8_PT_arr = dat8.arrays(['MissingET.MET', 'Electron.PT', 'Muon.PT', 'Jet.PT'],outputtype=tuple)

## Make data arrays for TLorentzvector
Elec1_Eta_arr, Elec1_Phi_arr, Muon1_Eta_arr, Muon1_Phi_arr = dat1.arrays(['Electron.Eta', 'Electron.Phi', 'Muon.Eta', 'Muon.Phi'],outputtype=tuple)
Elec2_Eta_arr, Elec2_Phi_arr, Muon2_Eta_arr, Muon2_Phi_arr = dat2.arrays(['Electron.Eta', 'Electron.Phi', 'Muon.Eta', 'Muon.Phi'],outputtype=tuple)
Elec3_Eta_arr, Elec3_Phi_arr, Muon3_Eta_arr, Muon3_Phi_arr = dat3.arrays(['Electron.Eta', 'Electron.Phi', 'Muon.Eta', 'Muon.Phi'],outputtype=tuple)
Elec4_Eta_arr, Elec4_Phi_arr, Muon4_Eta_arr, Muon4_Phi_arr = dat4.arrays(['Electron.Eta', 'Electron.Phi', 'Muon.Eta', 'Muon.Phi'],outputtype=tuple)
Elec5_Eta_arr, Elec5_Phi_arr, Muon5_Eta_arr, Muon5_Phi_arr = dat5.arrays(['Electron.Eta', 'Electron.Phi', 'Muon.Eta', 'Muon.Phi'],outputtype=tuple)
Elec6_Eta_arr, Elec6_Phi_arr, Muon6_Eta_arr, Muon6_Phi_arr = dat6.arrays(['Electron.Eta', 'Electron.Phi', 'Muon.Eta', 'Muon.Phi'],outputtype=tuple)
Elec7_Eta_arr, Elec7_Phi_arr, Muon7_Eta_arr, Muon7_Phi_arr = dat7.arrays(['Electron.Eta', 'Electron.Phi', 'Muon.Eta', 'Muon.Phi'],outputtype=tuple)
Elec8_Eta_arr, Elec8_Phi_arr, Muon8_Eta_arr, Muon8_Phi_arr = dat8.arrays(['Electron.Eta', 'Electron.Phi', 'Muon.Eta', 'Muon.Phi'],outputtype=tuple)


## make 0 arrays for estabilishing TLorentzvectorArray
Elec1_M_arr = np.zeros(Elec1_PT_arr.shape)
Elec2_M_arr = np.zeros(Elec2_PT_arr.shape)
Muon1_M_arr = np.zeros(Muon1_PT_arr.shape)
Muon2_M_arr = np.zeros(Muon2_PT_arr.shape)


## TLorentzvector
Elec1_Vec_arr = upm.TLorentzVectorArray.from_ptetaphim(Elec1_PT_arr, Elec1_Eta_arr, Elec1_Phi_arr, Elec1_M_arr)
Elec2_Vec_arr = upm.TLorentzVectorArray.from_ptetaphim(Elec2_PT_arr, Elec2_Eta_arr, Elec2_Phi_arr, Elec2_M_arr)
Elec3_Vec_arr = upm.TLorentzVectorArray.from_ptetaphim(Elec3_PT_arr, Elec3_Eta_arr, Elec3_Phi_arr, Elec1_M_arr)
Elec4_Vec_arr = upm.TLorentzVectorArray.from_ptetaphim(Elec4_PT_arr, Elec4_Eta_arr, Elec4_Phi_arr, Elec2_M_arr)
Elec5_Vec_arr = upm.TLorentzVectorArray.from_ptetaphim(Elec5_PT_arr, Elec5_Eta_arr, Elec5_Phi_arr, Elec2_M_arr)
Elec6_Vec_arr = upm.TLorentzVectorArray.from_ptetaphim(Elec6_PT_arr, Elec6_Eta_arr, Elec6_Phi_arr, Elec2_M_arr)
Elec7_Vec_arr = upm.TLorentzVectorArray.from_ptetaphim(Elec7_PT_arr, Elec7_Eta_arr, Elec7_Phi_arr, Elec2_M_arr)
Elec8_Vec_arr = upm.TLorentzVectorArray.from_ptetaphim(Elec8_PT_arr, Elec8_Eta_arr, Elec8_Phi_arr, Elec2_M_arr)

Muon1_Vec_arr = upm.TLorentzVectorArray.from_ptetaphim(Muon1_PT_arr, Muon1_Eta_arr, Muon1_Phi_arr, Muon1_M_arr)
Muon2_Vec_arr = upm.TLorentzVectorArray.from_ptetaphim(Muon2_PT_arr, Muon2_Eta_arr, Muon2_Phi_arr, Muon2_M_arr)
Muon3_Vec_arr = upm.TLorentzVectorArray.from_ptetaphim(Muon3_PT_arr, Muon3_Eta_arr, Muon3_Phi_arr, Muon1_M_arr)
Muon4_Vec_arr = upm.TLorentzVectorArray.from_ptetaphim(Muon4_PT_arr, Muon4_Eta_arr, Muon4_Phi_arr, Muon2_M_arr)
Muon5_Vec_arr = upm.TLorentzVectorArray.from_ptetaphim(Muon5_PT_arr, Muon5_Eta_arr, Muon5_Phi_arr, Muon2_M_arr)
Muon6_Vec_arr = upm.TLorentzVectorArray.from_ptetaphim(Muon6_PT_arr, Muon6_Eta_arr, Muon6_Phi_arr, Muon2_M_arr)
Muon7_Vec_arr = upm.TLorentzVectorArray.from_ptetaphim(Muon7_PT_arr, Muon7_Eta_arr, Muon7_Phi_arr, Muon2_M_arr)
Muon8_Vec_arr = upm.TLorentzVectorArray.from_ptetaphim(Muon8_PT_arr, Muon8_Eta_arr, Muon8_Phi_arr, Muon2_M_arr)


## Define New empty arrays
e1 = np.zeros(Elec1_PT_arr.shape)
e2 = np.zeros(Elec2_PT_arr.shape)
e3 = np.zeros(Elec3_PT_arr.shape)
e4 = np.zeros(Elec4_PT_arr.shape)
e5 = np.zeros(Elec5_PT_arr.shape)
e6 = np.zeros(Elec6_PT_arr.shape)
e7 = np.zeros(Elec7_PT_arr.shape)
e8 = np.zeros(Elec8_PT_arr.shape)

m1 = np.zeros(Muon1_PT_arr.shape)
m2 = np.zeros(Muon2_PT_arr.shape)
m3 = np.zeros(Muon3_PT_arr.shape)
m4 = np.zeros(Muon4_PT_arr.shape)
m5 = np.zeros(Muon5_PT_arr.shape)
m6 = np.zeros(Muon6_PT_arr.shape)
m7 = np.zeros(Muon7_PT_arr.shape)
m8 = np.zeros(Muon8_PT_arr.shape)

j1 = np.zeros(Jet1_PT_arr.shape)
j2 = np.zeros(Jet2_PT_arr.shape)
j3 = np.zeros(Jet3_PT_arr.shape)
j4 = np.zeros(Jet4_PT_arr.shape)
j5 = np.zeros(Jet5_PT_arr.shape)
j6 = np.zeros(Jet6_PT_arr.shape)
j7 = np.zeros(Jet7_PT_arr.shape)
j8 = np.zeros(Jet8_PT_arr.shape)

for i in range(0,len(Elec1_Vec_arr)):
	if Elec1_PT_arr.counts[i] >= 2:
		e1[i] = (((Elec1_Vec_arr[i,0] + Elec1_Vec_arr[i,1]).mass))
	else:
		e1[i] = 0

	if Muon1_PT_arr.counts[i] >= 2:
		m1[i] = (((Muon1_Vec_arr[i,0] + Muon1_Vec_arr[i,1]).mass))
	else:
		m1[i] = 0

	if Jet1_PT_arr.counts[i] >= 2:
		j1[i] = (Jet1_PT_arr[i,0] + Jet1_PT_arr[i,1])
	else:
		j1[i] = 0
print("DATA1 finished")


for i in range(0,len(Elec2_Vec_arr)):
	if Elec2_PT_arr.counts[i] >= 2:
		e2[i] = (((Elec2_Vec_arr[i,0] + Elec2_Vec_arr[i,1]).mass))
	else:
		e2[i] = 0

	if Muon2_PT_arr.counts[i] >= 2:
		m2[i] = (((Muon2_Vec_arr[i,0] + Muon2_Vec_arr[i,1]).mass))
	else:
		m2[i] = 0

	if Jet2_PT_arr.counts[i] >= 2:
                j2[i] = (Jet2_PT_arr[i,0] + Jet2_PT_arr[i,1])
	else:
                j2[i] = 0


print("DATA2 finished")


for i in range(0,len(Elec3_Vec_arr)):
	if Elec3_PT_arr.counts[i] >= 2:
		e3[i] = (((Elec3_Vec_arr[i,0] + Elec3_Vec_arr[i,1]).mass))
	else:
		e3[i] = 0

	if Muon3_PT_arr.counts[i] >= 2:
		m3[i] = (((Muon3_Vec_arr[i,0] + Muon3_Vec_arr[i,1]).mass))
	else:
		m3[i] = 0

	if Jet3_PT_arr.counts[i] >= 2:
                j3[i] = (Jet3_PT_arr[i,0] + Jet3_PT_arr[i,1])
	else:
                j3[i] = 0


print("DATA3 finished")


for i in range(0,len(Elec4_Vec_arr)):
	if Elec4_PT_arr.counts[i] >= 2:
		e4[i] = (((Elec4_Vec_arr[i,0] + Elec4_Vec_arr[i,1]).mass))
	else:
		e4[i] = 0

	if Muon4_PT_arr.counts[i] >= 2:
		m4[i] = (((Muon4_Vec_arr[i,0] + Muon4_Vec_arr[i,1]).mass))
	else:
		m4[i] = 0

	if Jet4_PT_arr.counts[i] >= 2:
                j4[i] = (Jet4_PT_arr[i,0] + Jet4_PT_arr[i,1])
	else:
                j4[i] = 0


print("DATA4 finished")


for i in range(0,len(Elec5_Vec_arr)):
	if Elec5_PT_arr.counts[i] >= 2:
		e5[i] = (((Elec5_Vec_arr[i,0] + Elec5_Vec_arr[i,1]).mass))
	else:
		e5[i] = 0

	if Muon5_PT_arr.counts[i] >= 2:
		m5[i] = (((Muon5_Vec_arr[i,0] + Muon5_Vec_arr[i,1]).mass))
	else:
		m5[i] = 0

	if Jet5_PT_arr.counts[i] >= 2:
                j5[i] = (Jet5_PT_arr[i,0] + Jet5_PT_arr[i,1])
	else:
                j5[i] = 0


print("DATA5 finished")


for i in range(0,len(Elec6_Vec_arr)):
	if Elec6_PT_arr.counts[i] >= 2:
		e6[i] = (((Elec6_Vec_arr[i,0] + Elec6_Vec_arr[i,1]).mass))
	else:
		e6[i] = 0

	if Muon6_PT_arr.counts[i] >= 2:
		m6[i] = (((Muon6_Vec_arr[i,0] + Muon6_Vec_arr[i,1]).mass))
	else:
		m6[i] = 0

	if Jet6_PT_arr.counts[i] >= 2:
                j6[i] = (Jet6_PT_arr[i,0] + Jet6_PT_arr[i,1])
	else:
                j6[i] = 0


print("DATA6 finished")


for i in range(0,len(Elec7_Vec_arr)):
	if Elec7_PT_arr.counts[i] >= 2:
		e7[i] = (((Elec7_Vec_arr[i,0] + Elec7_Vec_arr[i,1]).mass))
	else:
		e7[i] = 0

	if Muon7_PT_arr.counts[i] >= 2:
		m7[i] = (((Muon7_Vec_arr[i,0] + Muon7_Vec_arr[i,1]).mass))
	else:
		m7[i] = 0

	if Jet7_PT_arr.counts[i] >= 2:
                j7[i] = (Jet7_PT_arr[i,0] + Jet7_PT_arr[i,1])
	else:
                j7[i] = 0


print("DATA7 finished")


for i in range(0,len(Elec8_Vec_arr)):
	if Elec8_PT_arr.counts[i] >= 2:
		e8[i] = (((Elec8_Vec_arr[i,0] + Elec8_Vec_arr[i,1]).mass))
	else:
		e8[i] = 0

	if Muon8_PT_arr.counts[i] >= 2:
		m8[i] = (((Muon8_Vec_arr[i,0] + Muon8_Vec_arr[i,1]).mass))
	else:
		m8[i] = 0

	if Jet8_PT_arr.counts[i] >= 2:
                j8[i] = (Jet8_PT_arr[i,0] + Jet8_PT_arr[i,1])
	else:
                j8[i] = 0


print("DATA8 finished")



## preselection
Lep1 = ((Elec1_PT_arr.count()) + (Muon1_PT_arr.count()) >= 2)
Lep2 = ((Elec2_PT_arr.count()) + (Muon2_PT_arr.count()) >= 2)
Lep3 = ((Elec3_PT_arr.count()) + (Muon3_PT_arr.count()) >= 2)
Lep4 = ((Elec4_PT_arr.count()) + (Muon4_PT_arr.count()) >= 2)
Lep5 = ((Elec5_PT_arr.count()) + (Muon5_PT_arr.count()) >= 2)
Lep6 = ((Elec6_PT_arr.count()) + (Muon6_PT_arr.count()) >= 2)
Lep7 = ((Elec7_PT_arr.count()) + (Muon7_PT_arr.count()) >= 2)
Lep8 = ((Elec8_PT_arr.count()) + (Muon8_PT_arr.count()) >= 2)

Jet1 = ((Jet1_PT_arr.count()) >= 2)
Jet2 = ((Jet2_PT_arr.count()) >= 2)
Jet3 = ((Jet3_PT_arr.count()) >= 2)
Jet4 = ((Jet4_PT_arr.count()) >= 2)
Jet5 = ((Jet5_PT_arr.count()) >= 2)
Jet6 = ((Jet6_PT_arr.count()) >= 2)
Jet7 = ((Jet7_PT_arr.count()) >= 2)
Jet8 = ((Jet8_PT_arr.count()) >= 2)



## scalar sum of lepton pt
lep1_pt_sum = ak.sum(Elec1_PT_arr,axis=-1) + ak.sum(Muon1_PT_arr,axis=-1) > 120
lep2_pt_sum = ak.sum(Elec2_PT_arr,axis=-1) + ak.sum(Muon2_PT_arr,axis=-1) > 120
lep3_pt_sum = ak.sum(Elec3_PT_arr,axis=-1) + ak.sum(Muon3_PT_arr,axis=-1) > 120
lep4_pt_sum = ak.sum(Elec4_PT_arr,axis=-1) + ak.sum(Muon4_PT_arr,axis=-1) > 120
lep5_pt_sum = ak.sum(Elec5_PT_arr,axis=-1) + ak.sum(Muon5_PT_arr,axis=-1) > 120
lep6_pt_sum = ak.sum(Elec6_PT_arr,axis=-1) + ak.sum(Muon6_PT_arr,axis=-1) > 120
lep7_pt_sum = ak.sum(Elec7_PT_arr,axis=-1) + ak.sum(Muon7_PT_arr,axis=-1) > 120
lep8_pt_sum = ak.sum(Elec8_PT_arr,axis=-1) + ak.sum(Muon8_PT_arr,axis=-1) > 120


## scalar sum of jet pt
jet1_pt_sum = j1 < 400
jet2_pt_sum = j2 < 400
jet3_pt_sum = j3 < 400
jet4_pt_sum = j4 < 400
jet5_pt_sum = j5 < 400
jet6_pt_sum = j6 < 400
jet7_pt_sum = j7 < 400
jet8_pt_sum = j8 < 400
 


## opening angle cut
deltaphi1 = abs(ak.sum(Elec1_Phi_arr,axis=-1) - ak.sum(Muon1_Phi_arr,axis=-1)) < 2
deltaphi2 = abs(ak.sum(Elec2_Phi_arr,axis=-1) - ak.sum(Muon2_Phi_arr,axis=-1)) < 2
deltaphi3 = abs(ak.sum(Elec3_Phi_arr,axis=-1) - ak.sum(Muon3_Phi_arr,axis=-1)) < 2
deltaphi4 = abs(ak.sum(Elec4_Phi_arr,axis=-1) - ak.sum(Muon4_Phi_arr,axis=-1)) < 2
deltaphi5 = abs(ak.sum(Elec5_Phi_arr,axis=-1) - ak.sum(Muon5_Phi_arr,axis=-1)) < 2
deltaphi6 = abs(ak.sum(Elec6_Phi_arr,axis=-1) - ak.sum(Muon6_Phi_arr,axis=-1)) < 2
deltaphi7 = abs(ak.sum(Elec7_Phi_arr,axis=-1) - ak.sum(Muon7_Phi_arr,axis=-1)) < 2
deltaphi8 = abs(ak.sum(Elec8_Phi_arr,axis=-1) - ak.sum(Muon8_Phi_arr,axis=-1)) < 2


## DY supress cut
dye1 = abs(e1 - 91) > 15
dym1 = abs(m1 - 91) > 15
dye2 = abs(e2 - 91) > 15
dym2 = abs(m2 - 91) > 15
dye3 = abs(e3 - 91) > 15
dym3 = abs(m3 - 91) > 15
dye4 = abs(e4 - 91) > 15
dym4 = abs(m4 - 91) > 15
dye5 = abs(e5 - 91) > 15
dym5 = abs(m5 - 91) > 15
dye6 = abs(e6 - 91) > 15
dym6 = abs(m6 - 91) > 15
dye7 = abs(e7 - 91) > 15
dym7 = abs(m7 - 91) > 15
dye8 = abs(e8 - 91) > 15
dym8 = abs(m8 - 91) > 15








### Cutting

#j2_nl2_cut_MET1 = MET1_arr[Lep1 & Jet1 & die1 & dim1 & lep1_pt_sum & jet1_pt_sum & deltaphi1]
#j2_nl2_cut_MET2 = MET2_arr[Lep2 & Jet2 & die2 & dim2 & lep2_pt_sum & jet2_pt_sum & deltaphi2]
#j2_nl2_cut_MET3 = MET3_arr[Lep3 & Jet3 & die3 & dim3 & lep3_pt_sum & jet3_pt_sum & deltaphi3]
#j2_nl2_cut_MET4 = MET4_arr[Lep4 & Jet4 & die4 & dim4 & lep4_pt_sum & jet4_pt_sum & deltaphi4] 
#j2_nl2_cut_MET5 = MET5_arr[Lep5 & Jet5 & die5 & dim5 & lep5_pt_sum & jet5_pt_sum & deltaphi5]
#j2_nl2_cut_MET6 = MET6_arr[Lep6 & Jet6 & die6 & dim6 & lep6_pt_sum & jet6_pt_sum & deltaphi6]
#j2_nl2_cut_MET7 = MET7_arr[Lep7 & Jet7 & die7 & dim7 & lep7_pt_sum & jet7_pt_sum & deltaphi7]
#j2_nl2_cut_MET8 = MET8_arr[Lep8 & Jet8 & die8 & dim8 & lep8_pt_sum & jet8_pt_sum & deltaphi8]

j2_nl2_cut_MET1 = MET1_arr[Lep1 & Jet1 & lep1_pt_sum & jet1_pt_sum & deltaphi1 & dye1 & dym1]
j2_nl2_cut_MET2 = MET2_arr[Lep2 & Jet2 & lep2_pt_sum & jet2_pt_sum & deltaphi2 & dye2 & dym2]
j2_nl2_cut_MET3 = MET3_arr[Lep3 & Jet3 & lep3_pt_sum & jet3_pt_sum & deltaphi3 & dye3 & dym3]
j2_nl2_cut_MET4 = MET4_arr[Lep4 & Jet4 & lep4_pt_sum & jet4_pt_sum & deltaphi4 & dye4 & dym4]
j2_nl2_cut_MET5 = MET5_arr[Lep5 & Jet5 & lep5_pt_sum & jet5_pt_sum & deltaphi5 & dye5 & dym5]
j2_nl2_cut_MET6 = MET6_arr[Lep6 & Jet6 & lep6_pt_sum & jet6_pt_sum & deltaphi6 & dye6 & dym6]
j2_nl2_cut_MET7 = MET7_arr[Lep7 & Jet7 & lep7_pt_sum & jet7_pt_sum & deltaphi7 & dye7 & dym7]
j2_nl2_cut_MET8 = MET8_arr[Lep8 & Jet8 & lep8_pt_sum & jet8_pt_sum & deltaphi8 & dye8 & dym8]

Final1 = []
Final2 = []
Final3 = []
Final4 = []
Final5 = []
Final6 = []
Final7 = []
Final8 = []


for i in range(0, len(j2_nl2_cut_MET1)):
	if j2_nl2_cut_MET1[i] > 320:
		Final1.append(j2_nl2_cut_MET1[i])
Final1 = np.array(Final1)
print(len(Final1), "Final selected Event of DATA1")


for i in range(0, len(j2_nl2_cut_MET2)):
        if j2_nl2_cut_MET2[i] > 320:
                Final2.append(j2_nl2_cut_MET2[i])
Final2 = np.array(Final2)
print(len(Final2), "Final selected Event of DATA2")

for i in range(0, len(j2_nl2_cut_MET3)):
        if j2_nl2_cut_MET3[i] > 320:
                Final3.append(j2_nl2_cut_MET3[i])
Final3 = np.array(Final3)
print(len(Final3), "Final selected Event of DATA3")

for i in range(0, len(j2_nl2_cut_MET4)):
        if j2_nl2_cut_MET4[i] > 320:
                Final4.append(j2_nl2_cut_MET4[i])
Final4 = np.array(Final4)
print(len(Final4), "Final selected Event of DATA4")

for i in range(0, len(j2_nl2_cut_MET5)):
        if j2_nl2_cut_MET5[i] > 320:
                Final5.append(j2_nl2_cut_MET5[i])
Final5 = np.array(Final5)
print(len(Final5), "Final selected Event of DATA5")

for i in range(0, len(j2_nl2_cut_MET6)):
        if j2_nl2_cut_MET6[i] > 320:
                Final6.append(j2_nl2_cut_MET6[i])
Final6 = np.array(Final6)
print(len(Final6), "Final selected Event of DATA6")

for i in range(0, len(j2_nl2_cut_MET7)):
        if j2_nl2_cut_MET7[i] > 320:
                Final7.append(j2_nl2_cut_MET7[i])
Final7 = np.array(Final7)
print(len(Final7), "Final selected Event of DATA7")

for i in range(0, len(j2_nl2_cut_MET8)):
        if j2_nl2_cut_MET8[i] > 320:
                Final8.append(j2_nl2_cut_MET8[i])
Final8 = np.array(Final8)
print(len(Final8), "Final selected Event of DATA8")


## Normalization factor
x_ttbar = 50.9
x_dy = 1013
x_ww = 5.142
x_wz = 2.075
x_zz = 0.397
x_singletop = 2.289
x_dm10 = 0.0002683
#x_dm100 = 0.05199 #dm 1GeV med 10GeV
#x_dm100 = 0.03649 #dm 1GeV med 50GeV
#x_dm100 = 0.01757 #dm 1GeV med 100GeV
x_dm100 = 0.001214 #dm 1GeV med 500GeV
#x_dm100 = 0.01641 #med0p1T
#x_dm100 = 0.004954 #med0p2T
#x_dm100 = 0.001229 #med0p5T
#x_dm100 = 0.0002523 #dm100gev
#x_dm100 = 0.0000009932 #med3T
#x_dm100 = 0.000000007504 #med5T
lumi = 150000
tot_evt = 10000.0
tot_evt2 = 100000.0

#cal significance
yield1 = len(Final1) * x_ttbar * lumi / tot_evt2
yield2 = len(Final3) * x_ww * lumi / tot_evt2
yield3 = len(Final8) * x_dm10 * lumi / tot_evt
yield4 = len(Final4) * x_wz * lumi / tot_evt
yield5 = len(Final5) * x_zz * lumi / tot_evt
signi = yield3 / np.sqrt(yield1 + yield2 + yield3 + yield4 + yield5)
print("BKG Yield = ", yield1 + yield2 + yield4 + yield5)
print("SG Yield = ", yield3)

print("Significande = ", signi)

'''
ttbar = Final1.flatten()
dy = Final2.flatten()
ww = Final3.flatten()
wz = Final4.flatten()
zz = Final5.flatten()
sintop = Final6.flatten()
dm10 = Final7.flatten()
dm100 = Final8.flatten()

'''

ttbar = j2_nl2_cut_MET1.flatten()
dy = j2_nl2_cut_MET2.flatten()
ww = j2_nl2_cut_MET3.flatten()
wz = j2_nl2_cut_MET4.flatten()
zz = j2_nl2_cut_MET5.flatten()
sintop = j2_nl2_cut_MET6.flatten()
dm10 = j2_nl2_cut_MET7.flatten()
dm100 = j2_nl2_cut_MET8.flatten()

'''
ttbar = Elec1_PT_arr.flatten()
dy = Elec2_PT_arr.flatten()
ww = Elec3_PT_arr.flatten()
wz = Elec4_PT_arr.flatten()
zz = Elec5_PT_arr.flatten()
sintop = Elec6_PT_arr.flatten()
dm10 = Elec7_PT_arr.flatten()
dm100 = Elec8_PT_arr.flatten()


ttbar = Muon1_PT_arr.flatten()
dy = Muon2_PT_arr.flatten()
ww = Muon3_PT_arr.flatten()
wz = Muon4_PT_arr.flatten()
zz = Muon5_PT_arr.flatten()
sintop = Muon6_PT_arr.flatten()
dm10 = Muon7_PT_arr.flatten()
dm100 = Muon8_PT_arr.flatten()


ttbar = ak.to_numpy(jet1_pt_sum)
dy = ak.to_numpy(jet2_pt_sum)
ww = ak.to_numpy(jet3_pt_sum)
wz = ak.to_numpy(jet4_pt_sum)
zz = ak.to_numpy(jet5_pt_sum)
sintop = ak.to_numpy(jet6_pt_sum)
dm10 = ak.to_numpy(jet7_pt_sum)
dm100 = ak.to_numpy(jet8_pt_sum)


ttbar =  ak.to_numpy(deltaphi1)
dy =  ak.to_numpy(deltaphi2)
ww =  ak.to_numpy(deltaphi3)
wz =  ak.to_numpy(deltaphi4)
zz =  ak.to_numpy(deltaphi5)
sintop =  ak.to_numpy(deltaphi6)
dm10 =  ak.to_numpy(deltaphi7)
dm100 =  ak.to_numpy(deltaphi8)
'''

weight_ttbar = np.ones(ttbar.shape) * x_ttbar * lumi / tot_evt2
weight_dy = np.ones(dy.shape) * x_dy * lumi / tot_evt
weight_ww = np.ones(ww.shape) * x_ww * lumi / tot_evt2
weight_wz = np.ones(wz.shape) * x_wz * lumi / tot_evt
weight_zz = np.ones(zz.shape) * x_zz * lumi / tot_evt
weight_singletop = np.ones(sintop.shape) * x_singletop * lumi / tot_evt
weight_dm10 = np.ones(dm10.shape) * x_dm10 * lumi / tot_evt
weight_dm100 = np.ones(dm100.shape) * x_dm100 * lumi / tot_evt

#print(weight_ttbar, "BKG expected event")
#print(weight_dm10, "Y=1, expected event")
#print(weight_dm100,"Y=3, expected event")

## stack variables setting
x = [np.clip(sintop,0,500,out=sintop),np.clip(zz,0,500,out=zz),np.clip(wz,0,500,out=wz),np.clip(ww,0,500,out=ww),np.clip(dy,0,500,out=dy),np.clip(ttbar,0,500,out=ttbar)]
we = [weight_singletop,weight_zz,weight_wz,weight_ww,weight_dy,weight_ttbar]
co = ['dodgerblue','green','yellow', 'violet', 'cyan', 'blue']
la = ['Single top', 'ZZ', 'WZ', 'WW','Drell-Yan', 'top pair']

co2 = ['black','black','black','black','black','black']

## Draw histogram
plt.style.use(hep.style.ROOT)
plt.rcParams["figure.figsize"] = (8,8)
plt.xlim(0,500)
plt.ylim(0.0000001, 100000000)

plt.hist(x, range=(0,500), weights=we, bins=10, color=co, label = la, stacked=True)
plt.hist(x, range=(0,500), weights=we, bins=10, color=co2,histtype='step', stacked=True)

plt.hist(np.clip(dm10,0,500,out=dm10), range=(0,500),weights=weight_dm10, bins=10, label='$M$$_{\chi}$ = 10 GeV, $M$$_{Y}$ = 1 TeV',color='red', histtype='step')
plt.hist(np.clip(dm100,0,500,out=dm100), range=(0,500),weights=weight_dm100, bins=10, label='$M$$_{\chi}$ = 10 GeV, $M$$_{Y}$ = 3 TeV',color='darkred', histtype='step')

plt.yscale('log')
plt.rc('xtick',labelsize=10)
plt.rc('ytick',labelsize=10)
plt.title("$\sqrt{s}$ = 13 TeV, L = 150 fb$^{-1}$", loc='left',fontsize=15)
plt.xlabel("$E$$^{miss}_{T}$ [GeV]", fontsize=15)
#plt.xlabel("Scalar sum of Jet $p$$_{T}$ [GeV]", fontsize=15)
#plt.xlabel("$\Delta$$\phi$$_{ll}$",fontsize=15)
#plt.xlabel("Electron $p$$_{T}$ [GeV]", fontsize=15)
#plt.xlabel("Muon $p$$_{T}$ [GeV]", fontsize=15)
plt.ylabel("Expected Number of Events | 50 GeV", fontsize=15)
plt.minorticks_on()
plt.legend(fontsize=12)
plt.savefig("heo.png")
