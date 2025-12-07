import sys
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    text = input("Input: ")
    print("Output:")
    print(figlet.renderText(text))
    sys.exit(0)

if len(sys.argv) == 3:
    o = sys.argv[1]
    font_name = sys.argv[2]


    if o not in ["-f", "--font"]:
        print("Invalid usage")
        sys.exit(1)

    if font_name not in figlet.getFonts():
        print("Invalid font")
        sys.exit(1)


    figlet.setFont(font=font_name)
    t = input("Input: ")
    print("Output:")
    print(figlet.renderText(t))
    sys.exit(0)



print("Invalid usage")
sys.exit(1)
