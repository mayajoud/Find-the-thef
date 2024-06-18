facts = [
    "The car belonged to a responsible person.",
    "The thief didn't know the car belonged to a responsible person.",
    "The thief is one of the four suspects.",
    "Six of the suspects' statements are true, and six are false.",
]

suspects = [
    {
        "name": "الف",
        "statements": [
            "I have often committed crimes with J in the past.",
            "B is the thief.",
            "The thief didn't know the car belonged to a responsible person.",
        ],
    },
    {
        "name": "ب",
        "statements": [
            "I am the thief.",
            "The third statement is a lie.",
            "I am not negligent.",
        ],
    },
    {
        "name": "ج",
        "statements": [
            "I have never seen A before today.",
            "B is not guilty.",
            "The thief is skilled at driving.",
        ],
    },
    {
        "name": "د",
        "statements": [
            "The first statement is a lie.",
            "I am not skilled at driving.",
            "A committed this crime.",
        ],
    },
]


def identify_thief(suspects, facts):
    scores = {}
    punishment = 0
    for suspect in suspects:
        score = 0
        for statement in suspect["statements"]:
            if statement in facts:
                score += 1
            elif not statement.startswith("The thief "):
                score -= punishment
        scores[suspect["name"]] = score
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    if len(sorted_scores) > 0:
        return sorted_scores[0][0]
    else:
        return "No thief identified"


thief = identify_thief(suspects, facts)
print(f"The thief is {thief}")
