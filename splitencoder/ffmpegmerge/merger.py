import os
import subprocess
from subprocess import PIPE


def merge_slices(merge_job, movfolder):

    f = open("/pfs/out/fl.txt", "w")
    f.write("\n".join([str("file " + "'/pfs/converter/" + movfolder + "/" + elem + "'") for elem in merge_job]))
    f.close()

    output = subprocess.run(
        [
            "ffmpeg",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            "/pfs/out/fl.txt",
            "-c",
            "copy",
            os.path.join("/pfs/out", movfolder + ".mkv"),
        ],
        stdout=PIPE,
        stderr=PIPE,
    )

    # f2 = open("/pfs/out/f2.txt", "w")
    # f2.write("\n")
    # f2.write(str(os.listdir("/pfs/out")) + "\n")
    # print(str(os.listdir("/pfs/out")) + "\n")
    # f2.write("\n")
    # f2.write(str(output.stdout) + "\n" + str(output.stderr))
    # print(str(output.stdout) + "\n" + str(output.stderr))
    # f2.write("\n")
    # f2.close()
    os.remove("/pfs/out/fl.txt")


for i in os.listdir("/pfs/converter"):
    if os.path.isdir("/pfs/converter/" + i):
        merge_slices(sorted(os.listdir("/pfs/converter/" + i)), i)
