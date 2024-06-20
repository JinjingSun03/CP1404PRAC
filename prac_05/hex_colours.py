COLORS_DICT = {
    "ALICEBLUE": "#F0F8FF",
    "BEIGE": "#F5F5DC",
    "CORAL": "#FF7F50",
    "DARKGREEN": "#006400",
    "GOLDENROD": "#DAA520",
    "LAVENDER": "#E6E6FA",
    "MAGENTA": "#FF00FF",
    "ORCHID": "#DA70D6",
    "SIENNA": "#A0522D",
    "TOMATO": "#FF6347",
}

def lookup_color_code(color_name):
    return COLORS_DICT.get(color_name.upper(), "Color not found")

# Main program loop
while True:
    color_input = input("Enter a color name (or blank to stop): ").strip()

    if not color_input:
        break

    color_code = lookup_color_code(color_input)
    print(f"The hexadecimal color code for {color_input.upper()} is {color_code}")
