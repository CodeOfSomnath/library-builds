import subprocess
import os

def join_path(per, p):
    return f"{per}{os.path.sep}{p}"


class Installer:

    def i(self, *args):
        _args = [arg for arg in args]
        subprocess.run(_args, check=True)

    def install(self):
        pass

    def build(self):
        pass

    def configure(self, *deps):
        self.i("sudo", "apt", "isntall", "-y", *deps)

    def get_source(self):
        # check if source path is set 
        if self.source_path != "":
            return

        # install the dependencies for copying the file
        self.i("sudo", "apt", "install", "-y", "git")

        # clone the project
        self.i("git", "clone", "--depth", "1", "--branch", "main", self.source_url)

        # setting the source path
        self.source_path = join_path(self.cwd, os.path.dirname(self.source_path))

        # cleanup the dependencies
        self.i("sudo", "apt", "remove", "-y", "git")

    
    def __init__(self, source_url, source_path, cwd, install_folder = "bin", build_folder = "build", os, arch, outfile_name):
        self.source_url = source_url # most likely a git host path like github
        self.source_path = source_path
        self.cwd = cwd
        self.install_folder = join_path(self.cwd, install_folder)
        self.build_folder = join_path(self.cwd, build_folder)
        self.os = os
        self.arch = arch
        self.outfile_name = outfile_name




class CMakeInstaller(Installer):


    def build(self):
        pass        


    def configure(self, *deps):
        # use the base installer setup
        super().configure(*deps)

        # cmake configure



    def __init__(self):
        super().__init__()
        