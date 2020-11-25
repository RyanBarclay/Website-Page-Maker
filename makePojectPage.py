import os
import sys

def main():

    with os.scandir('in/') as entries:
        for entry in entries:
            path = "in/" + entry.name
            f = open(path, "r")
            file = f.read().splitlines()
            f.close()

            outputFile = "out/" + file[0].replace(' ', '-').upper() + ".html"
            f = open(outputFile , "w")

            print("Writing  {}".format(file[0].replace(' ', '-').upper() + '.html'))

            temp = open("template/Template1.txt","r")
            output = temp.readlines()
            temp.close()

            # process text here
            output += process(file)


            temp = open("template/Template2.txt","r")
            output += temp.readlines()
            temp.close()

            for i in output:
                f.write(i)

            print("Finished {}".format(file[0].replace(' ', '-').upper() + '.html'))

def process(file):
    newline = '\n'
    tab = "    "
    baseIndent = 6
    inlist = False
    output = None
    for line in file:
        if line == "":
            file.remove("")
    for line in file:
        if output is None:
            # first line
            output = (baseIndent * tab) + '<div class="title">' + newline
            baseIndent += 1
            output += (baseIndent * tab) + line.upper() + newline
            output += (baseIndent * tab) + "<br />" + newline
            output += (baseIndent * tab) + "--" + newline
            output += (baseIndent * tab) + "<br />" + newline
            baseIndent -= 1
            output += (baseIndent * tab) + "</div>" + newline *2
        else:
            if line is file[1]:
                # first line that is not the title
                output += (baseIndent * tab)+ '<div id="post">' + newline
                baseIndent += 1

            if line[0] == "*":
                if inlist is False:
                    # start of list
                    output += (baseIndent * tab) + "<p>" + newline
                    baseIndent += 1
                    output += (baseIndent * tab) + "- " + line[1:] +"<br />" + newline
                    inlist = True
                else:
                    output += (baseIndent * tab) + "- " + line[1:] +"<br />" + newline
                    if line is file[-1]:
                        # Check to see if we need to cap list off since end of file
                        baseIndent -= 1
                        output += (baseIndent * tab) + "</p>" + newline*2
                        inlist = False
            elif inlist is True:
                baseIndent -= 1
                output += (baseIndent * tab) + "</p>" + newline
                inlist = False
            elif line[0] == "@":
                # subtitle
                output += (baseIndent * tab) +'<p class="subtitle"><br />' + line[1:].upper() + '</p>' + newline
            else:
                # paragraph
                output += (baseIndent * tab) + '<p>' + line + '</p>' + newline*2

            if line is file[-1]:
                output += (baseIndent * tab) + '<p>' + newline
                output += (baseIndent * tab) + "--" + newline
                output += (baseIndent * tab) + '<br />' + "BY RYAN BARCLAY" + newline
                output += (baseIndent * tab) + "</p>" + newline
                baseIndent -= 1
                output += (baseIndent * tab)+ "</div>" + newline
                # last line in the doc



    return output



if __name__ == "__main__":
    main()
