def banner():
    print("\n" + blue("mMMMMMMMMMMMMMM") + "          ll bb                                  hh")
    print(blue("mM  MM.  MM.  M") + "          ll bb                                  hh")
    print(blue("mM  MMM  MMM  M") + " .aaaaaa. ll bbbbbbb. .eeeeee. nnnnnnn. .cccccc. hhhhhhh.")
    print(blue("mM  MMM  MMM  M") + " aa'  `aa ll bb'  `bb eeeeeeee nn'  `nn cc'  `\"\" hh'  `hh")
    print(blue("mM  MMM  MMM  M") + " aa.  .aa ll bb.  .bb ee.  ... nn    nn cc.  ... hh    hh")
    print(blue("mM  MMM  MMM  M") + " `aaaaaaa ll bbbbbbb' `eeeeee' nn    nn `cccccc' hh    hh")
    print(blue("mMMMMMMMMMMMMMM"))
    print("                                                          v0.0.1\n")

def red(text):
    return "\033[91m{}\033[00m".format(text)

def green(text):
    return "\033[92m{}\033[00m".format(text)

def blue(text):
    return "\033[94m{}\033[00m".format(text)

def good(message):
    print("[{}] {}".format(green("+"), message))

def bad(message):
    print("[{}] {}".format(red("!"), message))