import win32api
import win32con


def create_registry(path, valuename):
    reg_root = win32con.HKEY_LOCAL_MACHINE
    reg_path = path
    reg_flags = win32con.WRITE_OWNER | win32con.KEY_WOW64_64KEY | win32con.KEY_ALL_ACCESS
    try:
        key = win32api.RegOpenKeyEx(reg_root, reg_path, 0, reg_flags)
        win32api.RegSetValueEx(key, valuename, 0, win32con.REG_SZ, '')
        win32api.RegCloseKey(key)
        return True
    except:
        return False


