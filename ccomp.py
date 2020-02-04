import os


def comphandle(filename, comp, arch, outfile):
    compile_dict = {
        "c" : "gcc",
        "cplusplus" : "g++",
        "cs" : "vstudio",
        "go" : "go"
    }

    arch_dict = {
        "mipsle" : "mipsle",
        "mipsbe" : "mipsbe",
        "armv7" : "armv7",
        "armv6" : "armv6",
        "ppc" : "ppc"
    }

    print("File selected for Compilation is {}".format(filename))

    for k, v in compile_dict.items():
        if comp.lower() == k.lower():
            print("Compiler is {} ".format(v))
            comp = v
    for k, v in arch_dict.items():
        if arch.lower() == k.lower():
            print("Arch is {}".format(v))
            arch = v

    parsed_in = "./input/" + filename
    parsed_out = "./output/" + outfile

    print("Command is:")
    print("sudo ./{} bash -c \'{} {} -o {}\'".format(arch, comp, filename, outfile))
    # File mgmt debug
    os.rename(parsed_in, parsed_out)
    print("Sending back file {}".format(outfile))


