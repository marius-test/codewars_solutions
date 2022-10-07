def are_you_playing_banjo(name):
    list1 = list(name)
    if list1[0] in ["r", "R"]:
        conclusion = name + " plays banjo"
    else:
        conclusion = name + " does not play banjo"
    return conclusion
