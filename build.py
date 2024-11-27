import os
import shutil
import subprocess
import re


version = "1.0"
build_dir = "bismih-theme_" + version + "_amd64"


def edit_version():
    global version
    file = "DEBIAN/control"
    with open(file, "r") as f:
        data = f.read()

    # Version satırını değiştirme
    new_data = re.sub(r"(?<=^Version: ).*", version, data, flags=re.MULTILINE)

    # Standards-Version satırını değiştirme
    new_data = re.sub(
        r"(?<=^Standards-Version: ).*", version, new_data, flags=re.MULTILINE
    )
    with open(file, "w") as f:
        f.write(new_data)
    print(f"Version: {version}")


if __name__ == '__main__':
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    os.makedirs(build_dir)
    edit_version()

    # Copy files
    shutil.copytree("DEBIAN", build_dir + "/DEBIAN")

    os.makedirs(build_dir + "/usr/share/wallpapers/")
    shutil.copytree("Bismih_Theme", build_dir + "/usr/share/wallpapers/Bismih_Theme")
    shutil.copytree("b_wallpapers", build_dir + "/usr/share/wallpapers/b_wallpapers")

    os.makedirs(build_dir + "/usr/share/icons/")
    shutil.copy("bismih.svg", build_dir + "/usr/share/icons/bismih.svg")

    subprocess.run(["dpkg-deb", "--build", build_dir])
    shutil.rmtree(build_dir)