import winreg, vdf, os

def GetRootPath():
    result = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, "SOFTWARE\\Valve\\Steam", 0, winreg.KEY_READ)

    base = winreg.QueryValueEx(result, "SteamPath")[0]

    final_path = base + "\\steamapps\\common\\Rust\\cfg"

    if (os.path.exists(final_path)):
        return final_path

    with open(base + "\\steamapps\\libraryfolders.vdf") as f:
        libaryfile = vdf.load(f)["LibraryFolders"].values()

        for path in libaryfile:
            if "Steam" in path:
                return path + "\\steamapps\\common\\Rust"
        f.close()
        
