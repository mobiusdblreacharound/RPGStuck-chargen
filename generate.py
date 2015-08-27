def main():
    print "Character Information Form"
    # Name
    information = { "gender": "GIRAFFES", "name": {"first": "paul ball", "last": "mall call"}, "race": "2nd place" }
    information["name"]["first"] = raw_input("First name: ")
    information["name"]["last"] = raw_input("Last name:  ")
    if information["name"]["first"].lower() == "vorpas" and information["name"]["last"] == "jabwak":
        print "oh hi"
    # Race
    print "Race:"
    print "T for troll, H for human"
    toh = ""
    while toh != "t" and toh != "h":
        toh = raw_input("Race: ").lower()
        if toh != "t" and toh != "h":
            print "Please enter T or H."
    if toh.lower() == "t":
        information["race"] = "Troll"
        print "Blood Colors are:"
        print "Burgundy Bronze Gold   Lime"
        print "Jade     Olive  Teal   Cobalt"
        print "Indigo   Purple Violet Fuchsia"
        bloodColor = "null"
        bloodColors = ["burgundy", "bronze", "gold", "lime", "jade", "olive", "teal", "cobalt", "indigo", "purple", "violet", "fuchsia"]
        while bloodColor not in bloodColors: # well duh why was i using any() i can use in
            bloodColor = raw_input("Blood Color: ").lower()
        information["bloodColor"] = bloodColor
    else:
        information["race"] = "Human"
    # Gender
    print "Gender:"
    print "M for male, F for female, O for other."
    availgend = ["m", "f", "o"]
    morfo = ""
    while morfo not in availgend:
        morfo = raw_input("Gender: ")
        if morfo not in availgend:
            print "Please type M, F, or O."
    if morfo = "m":
        information["gender"] = "Male"
    elif morfo = "f":
        information["gender"] = "Female"
    elif morfo = "o":
        print "Please enter the other gender:"
        information["gender"] = raw_input("Other:  ")
    # Stats
    print "When you create a character, you are given an array of BASE STATS you can apply."
    print "The base stats are 15, 14, 13, 12, 10, and 8."
    print ""
