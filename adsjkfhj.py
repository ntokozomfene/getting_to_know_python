def list_all_js_function_names(path):
    f = open(path, mode="r")
    y = f.readlines()
    end = []
    counter = 0
    for line in y:
        counter +=1
        if "}" in line:
            yy = line.split("\n")
            if yy[0] == "}":
                end.append(counter)
    f.close()
    return(end)
x = list_all_js_function_names("Untitled-123.js")
print(x)

