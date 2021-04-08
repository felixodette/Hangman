def check_email(string):
    return string.find(" ") == -1 \
        and string.find("@") != -1 \
        and string.find("@.") == -1 \
        and string.rfind("@") < string.rfind(".")
