load 3ugc.pdb

load_traj output.dcd, 3ugc

show cartoon
bg_color white
color blue, 3ugc

mplay

mset 1, 100  # Setting the number of keyframes (adjusted to the number of frames in the DCD file)
util.mroll  # Automatic camera scrolling

frame 1
mview store
frame 100
mview store
mview reinterpolate

mpng frame_
ffmpeg -r 30 -i frame_%04d.png -vcodec libx264 -pix_fmt yuv420p output_video.mp4