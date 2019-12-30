from pathlib import Path
import matplotlib.pyplot as plt
from tqdm import tqdm

files = list(Path('datageneration').rglob('*.png'))
for filename in tqdm(files):
    im = plt.imread(str(filename))
    im[:,:,3] = 1
    plt.imsave(filename, im)