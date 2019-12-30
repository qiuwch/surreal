# Script to convert xsens data to SMPL format.
import sys
sys.path.append('./unrealdb')
from tqdm import tqdm
import numpy as np
print(sys.argv) # Check inside blender or not

import mocap.bvh
import mocap.smpl
import mocap.data

npy_filename = 'xsens_data.npz'

bvh_filename = './unrealdb/data/bvh/abandon package.bvh'
bvh_data = mocap.smpl.BvhData(bvh_filename)
bones = bvh_data.get_all_bones()
print(bones)

# Convert the data to rotation axis, then save to npy.
# Need to map the order of bones.

# key: value -> bone order: SMPL model bone
# part_match = {'root':'root', 'bone_00':'Pelvis', 'bone_01':'L_Hip', 'bone_02':'R_Hip',
#               'bone_03':'Spine1', 'bone_04':'L_Knee', 'bone_05':'R_Knee', 'bone_06':'Spine2',
#               'bone_07':'L_Ankle', 'bone_08':'R_Ankle', 'bone_09':'Spine3', 'bone_10':'L_Foot',
#               'bone_11':'R_Foot', 'bone_12':'Neck', 'bone_13':'L_Collar', 'bone_14':'R_Collar',
#               'bone_15':'Head', 'bone_16':'L_Shoulder', 'bone_17':'R_Shoulder', 'bone_18':'L_Elbow',
#               'bone_19':'R_Elbow', 'bone_20':'L_Wrist', 'bone_21':'R_Wrist', 'bone_22':'L_Hand', 'bone_23':'R_Hand'}

SMPL_bones = [
'Pelvis', 'L_Hip', 'R_Hip', 'Spine1', 'L_Knee', 'R_Knee', 'Spine2',
'L_Ankle', 'R_Ankle', 'Spine3', 'L_Foot', 'R_Foot', 'Neck', 
'L_Collar', 'R_Collar', 'Head', 'L_Shoulder', 'R_Shoulder', 
'L_Elbow', 'R_Elbow', 'L_Wrist', 'R_Wrist', 'L_Hand', 'R_Hand'
]

nframe = len(bvh_data)
pose = np.zeros((nframe, 72))
trans = np.zeros((nframe, 3))
assert(len(SMPL_bones) * 3 == 72)

npz_data = dict()
nframe = 100

clip = range(3400, 3700)
nframe = len(clip)
for fi, frame_id in enumerate(tqdm(clip)):
    frame_data = np.zeros((1, 72))
    for ji, smpl_bone_name in enumerate(SMPL_bones):
        bvh_bone_name = mocap.data.smpl2bvh.get(smpl_bone_name)
        if bvh_bone_name:
            r = bvh_data.get_local_rot(bvh_bone_name, frame_id)
        else:
            # print('Can not find bone %s' % smpl_bone_name)
            pass
        rotvec = r.as_rotvec()
        frame_data[0, ji*3:(ji+1)*3] = rotvec
    pose[fi, :] = frame_data

orig = np.load('./datageneration/smpl_data/smpl_data.npz')
npz_data['pose_abandon_package'] = pose
npz_data['trans_abandon_package'] = trans
npz_data['maleshapes'] = orig['maleshapes']
npz_data['femaleshapes'] = orig['femaleshapes']
npz_data['regression_verts'] = orig['regression_verts']
npz_data['joint_regressor'] = orig['joint_regressor']
# Save npz_data to npz file
np.savez('datageneration/smpl_data/xsens.npz', **npz_data)