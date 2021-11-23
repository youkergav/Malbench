class Message:
    def __init__(self, verbose=False):
        self.verbose = verbose

    def banner(self, version):
        print("\n" + self.blue("mMMMMMMMMMMMMMM") + "          ll bb                                  hh")
        print(self.blue("mM  MM.  MM.  M") + "          ll bb                                  hh")
        print(self.blue("mM  MMM  MMM  M") + " .aaaaaa. ll bbbbbbb. .eeeeee. nnnnnnn. .cccccc. hhhhhhh.")
        print(self.blue("mM  MMM  MMM  M") + " aa'  `aa ll bb'  `bb eeeeeeee nn'  `nn cc'  `\"\" hh'  `hh")
        print(self.blue("mM  MMM  MMM  M") + " aa.  .aa ll bb.  .bb ee.  ... nn    nn cc.  ... hh    hh")
        print(self.blue("mM  MMM  MMM  M") + " `aaaaaaa ll bbbbbbb' `eeeeee' nn    nn `cccccc' hh    hh")
        print(self.blue("mMMMMMMMMMMMMMM"))
        print("                                                          v{}\n".format(version))

    def red(self, text):
        return "\033[91m{}\033[00m".format(text)

    def green(self, text):
        return "\033[92m{}\033[00m".format(text)

    def blue(self, text):
        return "\033[94m{}\033[00m".format(text)

    def good(self, message):
        print("[{}] {}".format(self.green("+"), message))

    def bad(self, message):
        print("[{}] {}".format(self.red("-"), message))

    def info(self, message):
        if self.verbose:
            print("[{}] {}".format(self.blue("*"), message))
