import ffmpeg
import os
import subprocess
from subprocess import PIPE


def convert_slice(job):
    probe = ffmpeg.probe(job)
    movfolder = os.path.split(job)[0].split("/")[3]
    tail = os.path.split(job)[1].rstrip(".mp4")

    if not os.path.exists(os.path.join("/pfs/out", movfolder)):
        os.makedirs(os.path.join("/pfs/out", movfolder))

    output = subprocess.run(
        ["ffmpeg", "-i", job, "-c:v", "copy", "-c:a", "copy", os.path.join("/pfs/out", movfolder, tail + ".mkv")],
        stdout=PIPE,
        stderr=PIPE,
    )


for dirpath, dirs, files in os.walk("/pfs/splitter"):
    for file in files:
        convert_slice(os.path.join(dirpath, file))
