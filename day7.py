### Preparation ###
all_folders = {}
class folder:
    branches: dict[str, "folder"]
    leaves: dict[str, int]

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.branches = {} #subdirs
        self.leaves = {} #files


    def __getitem__(self, item: str):
        if item in self.leaves.keys():
            return self.leaves[item]
        else:
            return self.branches[item]

    def __iter__(self):
        return self.branches.keys().__iter__()

    def get_total_size(self):
        total_size = 0
        for file in self.leaves.keys():
            total_size += self[file]
        for dir in self.branches.keys():
            total_size += self[dir].get_total_size()
        full_name_builder = self.name
        curr = self
        curr_parent = self.parent
        while curr.parent != None:
            full_name_builder = curr_parent.name + "/" + full_name_builder
            curr = curr_parent
            curr_parent = curr_parent.parent
        all_folders.update({full_name_builder:total_size})
        return total_size

    def print_tree(self, indent="- "):
        print(indent + self.name + " (dir, size=" + str(self.get_total_size()) + ")")
        indent = "  " + indent
        for dir in self.branches.keys():
            self[dir].print_tree(indent)
        for file in self.leaves.keys():
            print(indent + file + " (file, size=" + str(self[file]) + ")")



filesystem_root = folder("/",None)
pwd = filesystem_root
double_check_total_filesystem_size = 0
with open("day7input") as file:
    for line in file:
        command = line.strip()
        if command.startswith("$ cd"):
            arg = command.replace("$ cd ","")
            if arg == "..":
                pwd = pwd.parent
            elif arg == "/":
                pwd = filesystem_root
            else: #arg is a folder name
                pwd = pwd[arg]
        elif command == "$ ls":
            continue
        elif command.startswith("dir"):
            dir = command.replace("dir ","")
            if dir in pwd:
                continue #not a new dir
            else:
                pwd.branches.update({dir:folder(dir,pwd)}) #give curr dir a new branch
        else: #probably a file
            file_name = command.split(" ")[1]
            file_size = int(command.split(" ")[0])
            pwd.leaves.update({file_name:file_size})


#filesystem_root.print_tree() #calls get_total_size() #comment this line out for a 5 millisecond speed boost
total_size = filesystem_root.get_total_size()
print(all_folders)
total_size_of_dirs_at_most_100000 = 0
for dir in all_folders.keys():
    if all_folders[dir] <= 100000:
        total_size_of_dirs_at_most_100000 += all_folders[dir]
print(total_size_of_dirs_at_most_100000)
free_space = 70000000 - total_size
space_still_needed = 30000000 - free_space

#part2
dir_sizes = all_folders.values()
best_folder_size_to_delete = 30000000
for dir_size in all_folders.values():
    if dir_size < space_still_needed:
        continue
    best_folder_size_to_delete = min(dir_size,best_folder_size_to_delete)
print(best_folder_size_to_delete)