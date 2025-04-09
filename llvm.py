import subprocess
import os
import sys
import argparse


def install_llvm(cwd, install_dir = None, release = "Debug"):
    # install build dependencies
    subprocess.run(["sudo", "apt", "update"])
    subprocess.run(["sudo", "apt", "install", "-y", "cmake", "python3-yaml"])

    # clone the git project
    subprocess.run(["git", "clone", "https://github.com/llvm/llvm-project.git"])


    # setup and configure
    os.chdir("./llvm-project")
    if install_dir == None:
        subprocess.run(["cmake", "-S", "llvm", "-B", "build", f"-DCMAKE_BUILD_TYPE={release.capitalize()}"])
    else:
        subprocess.run(["cmake", "-S", "llvm", "-B", "build", f"-DCMAKE_INSTALL_PREFIX={install_dir}", f"-DCMAKE_BUILD_TYPE={release}"])

    # build
    os.chdir("build")
    subprocess.run(["make"])
    subprocess.run(["make", "install"])
    
    # creating a tar file
    if os.path.exists("bin"):
        subprocess.run(["tar", "-cJf", "llvm-x86_64.tar.xz", "-C", "bin", "."])
    else:
        os.chdir("..")
        subprocess.run(["tar", "-cJf", "llvm-x86_64.tar.xz", "-C", "bin", "."])


if __name__ == "__main__":
    parser = argparse.ArgumentParser("llvm.py", "llvm build script") 
    parser.add_argument("-o", "--outpath", type=str, help="the install path", default=None)
    parser.add_argument("-t", "--type", type=str, help="the type of release mode by default it is RELEASE [DEBUG, RELEASE options]", default="RELEASE")
    args = parser.parse_args()
    cwd = os.getcwd()
    # print(args.outpath)
    install_llvm(cwd, args.outpath, args.type)