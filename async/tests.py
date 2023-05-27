def echo(str,repetition=3):
    echoed_text=""
    for x in range(repetition,0,-1):
          echoed_text += f"{text[-x:]}\n"

    return f"{echoed_text.lower()}."


if __name__=="__main__":
    text=input("Enter something to be yeleld at ")
    print(echo(text))