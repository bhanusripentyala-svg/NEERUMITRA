def irrigation_advice(soil, rain):

    soil = soil.lower()
    rain = rain.lower()

    if soil == "dry" and rain == "no":
        return "Irrigation may be needed. Check crop water requirements."

    elif soil == "dry" and rain == "yes":
        return "Check expected rainfall timing before irrigation."

    elif soil == "moist" and rain == "yes":
        return "Recheck soil before deciding to irrigate."

    elif soil == "moist" and rain == "no":
        return "Continue monitoring soil conditions."

    elif soil == "moderate":
        return "Monitor the field and check crop water requirements."

    else:
        return "Please enter valid soil and rainfall details."