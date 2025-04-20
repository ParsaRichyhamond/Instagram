def Valid_email(Email):
    if ((Email[-10:] == "@gmail.com") or (Email[-10:] == "@yahoo.com")) and len(Email) > 10:
        return True
    else:
        return False
