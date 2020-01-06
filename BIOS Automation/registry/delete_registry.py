import win32api
import win32con


def delete_registry(path, valuename):
    reg_root = win32con.HKEY_LOCAL_MACHINE
    reg_path = path
    reg_flags = win32con.WRITE_OWNER | win32con.KEY_WOW64_64KEY | win32con.KEY_ALL_ACCESS
    try:
        # 删除value
        key = win32api.RegOpenKeyEx(reg_root, reg_path, 0, reg_flags)
        win32api.RegDeleteValue(key, valuename)
        win32api.RegCloseKey(key)
        return True
    except:
        return False



