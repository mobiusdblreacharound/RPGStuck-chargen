def main():
    print "Character Information Form"
    information = { "name": {"first": "", "last": ""} }
    information["name"]["first"] = raw_input("First name: ")
    information["name"]["last"] = raw_input("Last name: ")
    print "Race:"
    print "T for troll, H for human"
    toh = ""
    while toh != "t" and toh != "h":
        toh = raw_input("Race: ")
        if toh != "t" and toh != "h":
            print "Please enter T or H."
    if toh.lower() == "t":
        information["race"] = "Troll"
        print "Blood Colors are:"
        print "Burgundy Bronze Gold   Lime"
        print "Jade     Olive  Teal   Cobalt"
        print "Indigo   Purple Violet Fuchsia"
        bloodColor = ""
        bloodColors = ["burgundy", "bronze", "gold", "lime", "jade", "olive", "teal", "cobalt", "indigo", "purple", "violet", "fuchsia"]
        while bloodColor != any(color in x for x in bloodColors):
            bloodColor = raw_input("Blood Color: ")
            
