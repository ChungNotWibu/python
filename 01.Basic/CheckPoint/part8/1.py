GameCharacter = {
"Name"      : "Light",
"Age"       : 17,
"Strength"  : 8,
"Defense"   : 10,
"HP"        : 100,
"Backpack"  : "Shield , Bread Loaf",
"Gold"      : 100,
"Level"     : 2
}


GameCharacterSkill = {
    "Skill 1" :
    {
        "Name" : "Tackle",
        "Minimum level" : 1,
        "Damage" : 5,
        "Hit rate" : 0.3
    },
    "Skill 2" :
    {
        "Name" : "Quick Atack",
        "Minimum level" : 2,
        "Damage" : 3,
        "Hit rate" : 0.5
    },
    "Skill 3" :
    {
        "Name" : "Tackle",
        "Minimum level" : 4,
        "Damage" : 9,
        "Hit rate" : 0.2
    }
}

for i in GameCharacterSkill:
    print(f'{i}: {GameCharacterSkill[i]["Name"]} ')

a = int(input("Choose skill by number:"))

match a:
    case 1:
        skill = GameCharacterSkill["Skill 1"]
    case 2:
        skill = GameCharacterSkill["Skill 2"]
    case 3:
        skill = GameCharacterSkill["Skill 3"]

print(f"You chose {skill["Name"]}")
if skill["Minimum level"] > GameCharacter["Level"]:
    print("Cannot deploy. Required level" ,{skill["Minimum level"]})
else:
    print("Damage:", {GameCharacterSkill["DAMAGE"]})