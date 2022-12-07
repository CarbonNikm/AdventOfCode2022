
### Preparation ###
stream = ""
with open("day6input") as file:
    for line in file:
        stream = line.strip()
print(stream)

packet_marker = [c for c in stream[:4]]
chars_processed = 0
for char in stream:
    chars_processed += 1
    packet_marker.pop(0)
    packet_marker.append(char)
    if len(set(packet_marker)) == 4:
        break
print(chars_processed)

message_marker = [c for c in stream[:14]]
chars_processed = 0
for char in stream:
    chars_processed += 1
    message_marker.pop(0)
    message_marker.append(char)
    if len(set(message_marker)) == 14:
        break
print(chars_processed)