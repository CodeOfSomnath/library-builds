from llvm import install_llvm
import os
import subprocess
import argparse


def install_zig(cwd, install_dir):

    subprocess.run(["sudo", "apt", "install", "-y", "build-essential"])

    # installing llvm for the output
    install_llvm(cwd)

    # clone the git and build
    subprocess.run(["git", "clone", "https://github.com/ziglang/zig.git"])
    subprocess.run(["ls", "-al"])
    os.chdir("./zig")
    # os.mkdir("build")
    # # subprocess.run(
    # #     ["cmake", "-S", ".", "-B", "build", f"-DCMAKE_INSTALL_PREFIX={install_dir}"]
    # # )
    # os.chdir("./build")
    # subprocess.run(["make", "-j8"])
    # subprocess.run(["make", "install"])

    subprocess.run(
        [
            "cmake",
            "-G",
            "Ninja",  # Use Ninja generator
            "-S",
            ".",
            "-B",
            "build",
            f"-DCMAKE_INSTALL_PREFIX={install_dir}",
        ],
        check=True
    )

    # Build using Ninja (automatically uses all available cores)
    subprocess.run(["ninja", "-C", "build"], check=True)

    # Install
    subprocess.run(["ninja", "-C", "build", "install"], check=True)

    # resetting the path
    os.chdir(cwd)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("zig.py", "zig build script")
    parser.add_argument(
        "-o", "--outpath", type=str, help="the install path", default="bin"
    )
    args = parser.parse_args()
    cwd = os.getcwd()
    install_zig(cwd, args.outpath)
