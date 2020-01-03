import win32api, win32con


def check_registry_exist(path, value):
    reg_root = win32con.HKEY_LOCAL_MACHINE
    reg_path = path
    reg_flags = win32con.WRITE_OWNER | win32con.KEY_WOW64_64KEY | win32con.KEY_ALL_ACCESS
    try:
        key = win32api.RegOpenKeyEx(reg_root, reg_path, 0, reg_flags)
        value, _ = win32api.RegQueryValueEx(key, value)
        return True
    except:
        return False


print(check_registry_exist("software\\test_key","1"))

