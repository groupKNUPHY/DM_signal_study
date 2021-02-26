import uproot as ROOT
import uproot_methods as upm
import numpy as np
import awkward1 as ak

## usage
## lepton_global(elec_pt, muon_pt, elec_phi, muon_phi, elec_4vector, muon_4vector, met_4vector)
## pt_mask = (lead_pt > 25) & (sub_pt > 15)
## z_mask = (abs(z_mass - 91) > 15) & (z_mass >20)
## met_mask = (met_pt > 50)
## global_mask = pt_mask & z_mask & met_mask
## met_select = met_pt[global_mask]
##

def lepton_global(pt1,pt2,phi1,phi2,vec1,vec2,metvec):
        global lead_mt, sub_mt, di_mt, lead_pt, sub_pt, lead_phi, sub_phi, z_mass
        lead_mt = np.zeros(pt1.shape)
        sub_mt = np.zeros(pt1.shape)
        di_mt = np.zeros(pt1.shape)
        lead_pt = np.zeros(pt1.shape)
        sub_pt = np.zeros(pt1.shape)
        lead_phi = np.zeros(pt1.shape)
        sub_phi = np.zeros(pt1.shape)
        z_mass = np.zeros(pt1.shape)

        for i in range(0,len(pt1)):
                if (pt1.counts[i] + pt2.counts[i] >= 2):
                        if (pt1.counts[i] == 0):
                                lead_pt[i] = pt2[i,0]
                                sub_pt[i] = pt2[i,1]
                                lead_phi[i] = phi2[i,0]
                                sub_phi[i] = phi2[i,1]
                                z_mass[i] = (vec2[i,0] + vec2[i,1]).mass
                                lead_mt[i] = (vec2[i,0] + metvec[i,0]).mt
                                sub_mt[i] = (vec2[i,1] + metvec[i,0]).mt
                                di_mt[i] = (vec2[i,0] + vec2[i,1] + metvec[i,0]).mt
                        elif (pt2.counts[i] == 0):
                                lead_pt[i] = pt1[i,0]
                                sub_pt[i] = pt1[i,1]
                                lead_phi[i] = phi1[i,0]
                                sub_phi[i] = phi1[i,1]
                                z_mass[i] = (vec1[i,0] + vec1[i,1]).mass
                                lead_mt[i] = (vec1[i,0] + metvec[i,0]).mt
                                sub_mt[i] = (vec1[i,1] + metvec[i,0]).mt
                                di_mt[i] = (vec1[i,0] + vec1[i,1] + metvec[i,0]).mt
                        else:
                                di_mt[i] = (vec1[i,0] + vec2[i,0] + metvec[i,0]).mt
                                z_mass[i] = (vec1[i,0] + vec2[i,0]).mass
                                if (pt1[i,0] > pt2[i,0]):
                                        lead_pt[i] = pt1[i,0]
                                        sub_pt[i] = pt2[i,0]
                                        lead_phi[i] = phi1[i,0]
                                        sub_phi[i] = phi2[i,0]
                                        lead_mt[i] = (vec1[i,0] + metvec[i,0]).mt
                                        sub_mt[i] = (vec2[i,0] + metvec[i,0]).mt
                                else:
                                        lead_pt[i] = pt2[i,0]
                                        sub_pt[i] = pt1[i,0]
                                        lead_phi[i] = phi2[i,0]
                                        sub_phi[i] = phi1[i,0]
                                        lead_mt[i] = (vec2[i,0] + metvec[i,0]).mt
                                        sub_mt[i] = (vec1[i,0] + metvec[i,0]).mt



