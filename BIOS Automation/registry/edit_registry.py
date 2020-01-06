import win32api
import win32con


def edit_registry(path, valuename, value):
    reg_root = win32con.HKEY_LOCAL_MACHINE
    reg_path = path
    reg_flags = win32con.WRITE_OWNER | win32con.KEY_WOW64_64KEY | win32con.KEY_ALL_ACCESS

    if check_registry_exist(path, valuename):
        key = win32api.RegOpenKeyEx(reg_root, reg_path, 0, reg_flags)
        win32api.RegSetValueEx(key, valuename, 0, win32con.REG_SZ, value)
        win32api.RegCloseKey(key)
        return True
    else:
        return False


