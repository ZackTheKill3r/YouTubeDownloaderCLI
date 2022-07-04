settings = open("settings.txt", "r")
language_settings = settings.readline()

if "Language = English" in language_settings:
    language = "English"
elif "Language = Portuguese" in language_settings:
    language = "Portuguese"
elif "Language = Japanese" in language_settings:
    language = "Japanese"
else:
    language = "English"

settings.close()