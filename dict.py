
def check(cauldron):
    match cauldron:
        case "Power":
            return power_bubbles
        case "Quicc":
            return quicc_bubbles
        case "High-IQ":
            return iq_bubbles
        case "Kazam":
            return kazam_bubbles



power_bubbles = [["Roid Raging", "Add", 1, 0, ""], ["Warriors rule", "DecayMult", 2, 50, "x"], ["Hearty Diggy", "Decay", 50, 100, "%"], ["Wyoming blood", "BigBase", 23.5, 1.5, "%"],
                 ["Reely Smart", "Decay", 100, 80, "%"], ["Big Meaty Claws", "Add", 1, 0.02, ""], ["Sploosh Sploosh", "BigBase", 23.5, 1.5, "%"], ["Stronk Tool", "Decay", 65, 70, "%"],
                 ["FMJ", "Add", 0.5, 0, "%"], ["Bappity boopity", "Decay", 35, 100, "%"], ["Brittley Spears", "Decay", 40, 50, "%"], ["Call me bob", "BigBase", 25, 2.5, "%"],
                 ["Carpenter", "Decay", 2, 50, "%"], ["Buff boi talent", "BigBase", 5, 1, ""], ["Orange Bargin", "Decay", 40, 12, "%"], ["Penny of Strength", "Decay", 18, 30, "%"], 
                 ["MultOrange", "DecayMult", 1.4, 30, "x"], ["Dream of Ironfish", "Decay", 12, 30, "%"], ["Shimmeron", "Decay", 80, 40, "%"], ["Bite but not chew", "Decay", 50, 40, "%"], 
                 ["Spear Powah", "Decay", 40, 60, "%"], ["Slabi orefish", "Decay", 3, 60, ""], ["Gamer at heart", "Decay", 20, 60, "%"], ["Slabi Strength", "Decay", 25, 60, ""], 
                 ["Power Trione", "Decay", 23, 50, "%"]]

quicc_bubbles = [["Swift Steppin", "Add", 1, 0, ""], ["Archer or bust", "DecayMult", 2, 50, "x"], ["Hammer Hammer", "BigBase", 23, 2, "%"], ["Lil big damage", "Decay", 20, 100, "%"],
                 ["Anvilnomics", "Decay", 40, 100, "%"], ["Quick slap", "Add", 1, 0.02, ""], ["Sanic Tools", "Decay", 65, 70, "%"], ["Bug", "BigBase", 23.5, 1.5, "%"], 
                 ["Shaquracy", "Add", 1, 0, "%"], ["Cheap shot", "Decay", 7, 100, "%"], ["Bow jack", "Decay", 40, 50, "%"], ["Call me ash", "BigBase", 25, 2, "%"], 
                 ["cuz i catch em all", "DecayMult", 3, 100, "x"], ["Fast boi talent", "BigBase", 5, 1, ""], ["Green bargain", "Decay", 40, 12, "%"], ["Dollar of agility", "Decay", 18, 30, "%"], 
                 ["Premigreen", "DecayMult", 1.4, 30, "x"], ["Fly in mind", "Decay", 12, 40, "%"], ["Kill per kill", "Decay", 70, 40, "%"], ["Afk expexp", "Decay", 40, 40, "%"], 
                 ["Bow power", "Decay", 40, 60, "%"], ["Slabo critterbug", "Decay", 3, 60, ""], ["Sailer at heart", "Decay", 16, 60, "%"], ["Slabo agility", "Decay", 25, 60, ""],
                 ["Power Tritwo", "Decay", 23, 50, "%"]]

iq_bubbles = [["Stable jenius", "Add", 1, 0, ""], ["Mage is best", "DecayMult", 2, 50, "x"], ["Hocus choppus", "Decay", 50, 100, "%"], ["Molto loggo", "BigBase", 23.5, 1.5, "%"],
              ["Noodubble", "Decay", 100, 60, "%"], ["Name I guess", "Add", 1, 0.02, ""], ["Le brain tools", "Decay", 65, 70, "%"], ["Cookin roadkill", "Decay", 120, 70, "%"],
              ["Brewstachio", "Decay", 50, 100, "%"], ["All for kill", "Decay", 40, 100, "%"], ["matty stafford", "Decay", 40, 50, "%"], ["Call me pope", "DecayMult", 2.4, 70, "x"],
              ["Gospel leader", "Decay", 60, 30, "%"], ["Smart boi talent", "BigBase", 5, 1, ""], ["Purple bargain", "Decay", 40, 12, "%"], ["Nickel of wisdom", "Decay", 18, 30, "%"],
              ["Servapurple", "DecayMult", 1.4, 30, "x"], ["Tree sleeper", "Decay", 12, 40, "%"], ["Hyperswift", "Decay", 30, 30, "%"], ["Matrix evolved", "Decay", 60, 40, "%"],
              ["Wand pawur", "Decay", 40, 60, "%"], ["Slabe logsoul", "Decay", 3, 60, ""], ["Pious at heart", "Decay", 300, 100, "%"], ["Slabe wisdom", "Decay", 25, 60, ""],
              ["Power Trithree", "Decay", 23, 50, "%"]]


kazam_bubbles = [["Lotto skills", "Add", 1, 0, ""], ["Droppin loads", "Decay", 40, 70, "%"], ["Startue exp", "Decay", 25, 60, "%"], ["Level up gift", "Decay", 100, 30, "%"],
                 ["Prowesessary", "DecayMult", 1.5, 60, ""], ["Stamp tramp", "Add", 1, 0, ""], ["Undeveloped costs", "Decay", 40, 70, "%"], ["Da daily drip", "Decay", 30, 100, ""],
                 ["Grind time", "BigBase", 9.7, 0.3, "%"], ["Laaarrrryyyy", "Decay", 120, 100, "%"], ["Cogs for hands", "Add", 4, 0, "%"], ["Sample it", "Decay", 12, 40, "%"], 
                 ["Big game hunter", "Decay", 60, 30, "%"], ["Ignore overdues", "Decay", 100, 60, "%"], ["Yellow bargain", "Decay", 40, 12, "%"], ["Mr massacre", "Decay", 90, 50, "%"], 
                 ["Egg ink", "Decay", 40, 40, "%"], ["Diamond chef", "DecayMult", 0.3, 13, "x"], ["Card champ", "Decay", 100, 40, "%"], ["Petting the rift", "Decay", 15, 50, "x"], 
                 ["Boaty bubble", "Decay", 135, 70, "%"], ["Big P", "DecayMult", 0.5, 60, "x"], ["Bit by bit", "Decay", 50, 70, "%"], ["Gifts abound", "Decay", 40, 60, "%"], 
                 ["Atom Split", "Decay", 14, 40, "%"]]

