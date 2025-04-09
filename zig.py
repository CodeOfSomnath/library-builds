from llvm import install_llvm
import os
import subprocess
import argparse


def install_zig(install_dir):

    subprocess.run(["sudo", "apt", "install", "-y", "build-essential"])

    # installing llvm for the output
    install_llvm()



    # clone the git
    subprocess.run(["git", "clone", "https://github.com/ziglang/zig.git"])


    os.chdir("./zig")
    os.mkdir("build")
    # os.mkdir("bin")
    subprocess.run(["cmake", "-S", ".", "-B", "build", f"-DCMAKE_INSTALL_PREFIX={install_dir}"])
    # subprocess.run(["mkdir"])
    os.chdir("./build")
    subprocess.run(["make"])
    subprocess.run(["make", "install"])



if __name__ == "__main__":
    parser = argparse.ArgumentParser("llvm.py", "llvm build script") 
    parser.add_argument("-o", "--outpath", type=str, help="the install path", default="bin")
    # parser.add_argument("-t", "--type", type=str, help="the type of release mode by default it is RELEASE [DEBUG, RELEASE options]", default="RELEASE")
    args = parser.parse_args()
    
    # print(args.outpath)
    # install_llvm(args.outpath, args.type)
    install_zig(args.outpath)
