def main():
    #gereftan voroodi az karbar
    text = input('text:')
    convert(text)



#tabdil imoji be sticker
def convert(e):
    e = e.replace(":)", "🙂")
    e = e.replace(":(", "🙁")
    print(e)

main()
