from teachingAssistant import teachingAssistant, instructor


def createAccount(name, title):
    if title == "instructor":
        a = instructor(name)
        return a
    elif title == "ta":
        a = teachingAssistant(name)
        return a
    else:
        raise ValueError(title + "is not a valid title")
