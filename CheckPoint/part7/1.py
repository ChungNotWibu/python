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