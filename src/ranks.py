def get_rank(sr):

    if sr < 600:
        return {
            "name": "Bronze",
             "image": "assets/ranks/bronze.png",
            "min": 0,
             "max": 600,
             "next": "Argent"
        }
    elif sr < 1700:
        return {
            "name": "Argent",
            "image": "assets/ranks/argent.png",
             "min": 900,
            "max": 1700,
            "next": "Or"
        }

    elif sr < 3100:
        return {
            "name": "Or",
            "image": "assets/ranks/or.png",
            "min": 2100,
            "max": 3100,
            "next": "Platinum"
        }

    elif sr < 4800:
        return {
            "name": "Platinum",
            "image": "assets/ranks/platinum.png",
            "min": 3600,
            "max": 4800,
            "next": "Diamant"
        }

    elif sr < 6800:
        return {
            "name": "Diamant",
            "image": "assets/ranks/diams.png",
            "min": 5400,
            "max": 6800,
            "next": "Crimson"
        }

    elif sr < 9100:
        return {
            "name": "Crimson",
            "image": "assets/ranks/crimson.png",
            "min": 7500,
            "max": 9100,
            "next": "Iridescent"
        }

    elif sr < 20000:
        return {
            "name": "Iridescent",
            "image": "assets/ranks/iridescent.png",
            "min": 10000,
            "max": 20000,
            "next": "Top250"
        }

    return {
        "name": "Top 250",
        "image": "assets/ranks/top250.png",
        "min": 20000,
        "max": 99999,
        "next": "None"
    }

def get_division(sr):

    rank = get_rank(sr)

    if rank["name"] in ["Iridescent", "Top 250"]:
        return ""

    span = rank["max"] - rank["min"]

    step = span / 3

    value = sr - rank["min"]

    if value < step:
        return "I"

    elif value < step * 2:
        return "II"

    return "III"