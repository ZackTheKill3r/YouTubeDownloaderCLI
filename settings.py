import locale
import ctypes
windll = ctypes.windll.kernel32
windll.GetUserDefaultUILanguage()

settings = open("settings.txt", "r")
language_settings = settings.readline()
auto_lang = settings.readline()
os_lang = locale.windows_locale[ windll.GetUserDefaultUILanguage() ]

if "AutoLang = True" in auto_lang:
    if "en" in os_lang:
        language = "English"
    elif "pt" in os_lang:
        language = "Portuguese"
    elif "jp" in os_lang:
        language = "Japanese"
    else:
        language = "English"
else:
    if "Language = English" in language_settings:
        language = "English"
    elif "Language = Portuguese" in language_settings:
        language = "Portuguese"
    elif "Language = Japanese" in language_settings:
        language = "Japanese"
    else:
        language = "English"

settings.close()