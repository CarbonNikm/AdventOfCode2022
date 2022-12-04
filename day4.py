
### Preparation ###
first_elf = []
second_elf = []
with open("day4input") as file:
    for line in file:
        line = line.strip()
        first_elf.append(line.split(",")[0]) # get left half of array
        second_elf.append(line.split(",")[1]) # get right half of array
print(first_elf)
print(second_elf)
print(len(first_elf))

fully_contained_count = 0
for i in range(len(first_elf)):
    first_elf_first_number = int(first_elf[i].split("-")[0])
    first_elf_second_number = int(first_elf[i].split("-")[1])
    second_elf_first_number = int(second_elf[i].split("-")[0])
    second_elf_second_number = int(second_elf[i].split("-")[1])
    if first_elf_first_number >= second_elf_first_number and first_elf_second_number <= second_elf_second_number:
        fully_contained_count += 1
        continue
    if second_elf_first_number >= first_elf_first_number and second_elf_second_number <= first_elf_second_number:
        fully_contained_count += 1
        continue
print(fully_contained_count)

overlapped_at_all = 0
for i in range(len(first_elf)):
    first_elf_first_number = int(first_elf[i].split("-")[0])
    first_elf_second_number = int(first_elf[i].split("-")[1])
    second_elf_first_number = int(second_elf[i].split("-")[0])
    second_elf_second_number = int(second_elf[i].split("-")[1])
    if first_elf_first_number >= second_elf_first_number and first_elf_first_number <= second_elf_second_number: #overlaps, but not contained
        overlapped_at_all += 1
        continue
    if first_elf_second_number >= second_elf_first_number and first_elf_second_number <= second_elf_second_number: #overlaps, but not contained
        overlapped_at_all += 1
        continue
    if first_elf_first_number >= second_elf_first_number and first_elf_second_number <= second_elf_second_number: #fully contained
        overlapped_at_all += 1
        continue
    if second_elf_first_number >= first_elf_first_number and second_elf_second_number <= first_elf_second_number: #fully contained
        overlapped_at_all += 1
        continue
print(overlapped_at_all)
