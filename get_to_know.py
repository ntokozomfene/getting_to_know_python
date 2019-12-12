#path_to_js_file = open

def list_all_js_function_names(path):
    name_ls = [] 
    counter = 0
    count = 0
    start = []
    end = [] 
    f = open(path, mode="r")
    data = f.readlines()
    for line in data:
        counter += 1
        if "function" in line and "=" in line:
            results = line.split("=")
            name_ls.append(results[0])
        if "function" in line:
            results = line.split(" ")
            target = results[1].split("(")
            name_ls.append(target[0])
            start.append(counter)
    for line in data:
        count += 1 
        if "}" in line:
            y = line.split("\n")
            if y[0] == "}":
                end.append(count)             
    f.close()
    equals_index = name_ls.index("=")
    if equals_index != -1:
        name_ls.remove("=")
    return [start,name_ls,end]
x = list_all_js_function_names("js_file.js")
start = x[0]
names = x[1]
end = x[0]

# output = {}
# output_ls = []

# for i, num, num in enumerate(start, end):
#     output = {"start": num, "name": names[i], "end": num }
#     output_ls.append(output)

# print(output_ls)
for a in zip(start, names, end):
    print(a)

    # """
    # path_to_js_file is a path to a file on your hard drive
    # This function will read the entire input file and then return a list of js function names as strings
    # """


#list_all_js_function_names(input("path_name?"))
