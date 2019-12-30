import numpy as np
import pdb

# Use this script to check the content inside smpl_data.npz.

# load poses and shapes
def load_body_data(smpl_data, idx=0):
    # load MoSHed data from CMU Mocap (only the given idx is loaded)
    # create a dictionary with key the sequence name and values the pose and trans
    cmu_keys = []
    for seq in smpl_data.files:
        if seq.startswith('pose_'):
            cmu_keys.append(seq.replace('pose_', ''))
    
    name = sorted(cmu_keys)[idx % len(cmu_keys)]
    
    cmu_parms = {}
    for seq in smpl_data.files:
        if seq == ('pose_' + name):
            cmu_parms[seq.replace('pose_', '')] = {'poses':smpl_data[seq],
                                                   'trans':smpl_data[seq.replace('pose_','trans_')]}

    return cmu_parms

datafile = './datageneration/smpl_data/smpl_data.npz' 
# datafile = './datageneration/smpl_data/xsens.npz'
smpl_data = np.load(datafile)
print(smpl_data.files)
pdb.set_trace()
data = load_body_data(smpl_data, 0)
smpl_data['pose_01_01'] # 2751, 72 -> 72 / 3 = 24
smpl_data['trans_01_01'] # 2751, 3