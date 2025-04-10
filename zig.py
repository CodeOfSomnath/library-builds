from llvm import install_llvm
import os
import subprocess
import argparse


def install_zig(cwd, install_dir):

    subprocess.run(["sudo", "apt", "install", "-y", "build-essential"])

    # installing llvm for the output
    # install_llvm(cwd)
    subprocess.run(["ls", "-al"])
    # clone the git
    subprocess.run(["git", "clone", "https://github.com/ziglang/zig.git"])
    os.chdir("./zig")
    os.mkdir("build")
    subprocess.run(["cmake", "-S", ".", "-B", "build", f"-DCMAKE_INSTALL_PREFIX={install_dir}"])
    os.chdir("./build")
    subprocess.run(["make", "-j8"])
    subprocess.run(["make", "install"])

    # resetting the path
    os.chdir(cwd)



if __name__ == "__main__":
    parser = argparse.ArgumentParser("zig.py", "zig build script") 
    parser.add_argument("-o", "--outpath", type=str, help="the install path", default="bin")
    args = parser.parse_args()
    cwd = os.getcwd()
    install_zig(cwd, args.outpath)