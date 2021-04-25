import os
import subprocess
from subprocess import PIPE


def split_source(source):
    tail = os.path.split(source)[1].rstrip(".mp4")
    if not os.path.exists(os.path.join("/pfs/out", tail)):
        os.makedirs(os.path.join("/pfs/out", tail))
    subprocess.run(
        [
            "ffmpeg",
            "-i",
            source,
            "-c",
            "copy",
            "-map",
            "0",
            "-segment_time",
            "120",
            "-f",
            "segment",
            os.path.join("/pfs/out", tail, "job-id_%04d.mp4"),
        ]
    )
    # subprocess.run(["ffmpeg", "-i", source, "-vcodec", "libx265", "-crf", "28", os.path.join("/pfs/out", tail + ".mp4")], stdout=PIPE, stderr=PIPE)


for dirpath, dirs, files in os.walk("/pfs/videos"):
    for file in files:
        split_source(os.path.join(dirpath, file))
