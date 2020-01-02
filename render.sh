# BLENDER="/mnt/c/Program\ Files/Blender\ Foundation/Blender/blender.exe"
# "$BLENDER"
# alias blender='/mnt/c/Program\ Files/Blender\ Foundation/Blender/blender.exe'
# blender
blender="../blender-2.79b-linux-glibc219-x86_64/blender"
cd datageneration
$blender -b -t 1 -P main_part1.py -- --idx 0 --ishape 0 --stride 50
