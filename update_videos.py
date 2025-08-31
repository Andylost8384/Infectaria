import json

# videos.json file ka naam
file_name = "videos.json"

while True:
    title = input("Enter new title (or press Enter to exit): ")
    if not title:
        break

    position = input("Enter position (1 for first, 2 for second, etc.): ")
    if not position.isdigit():
        print("❌ Position number hona chahiye (1,2,3...)")
        continue

    position = int(position)

    # json load karo
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            videos = json.load(f)
    except FileNotFoundError:
        videos = []

    # new video object
    new_video = {
        "title": title,
        "previewUrl": "",
        "fullUrl": "",
        "fullUrl4k": ""
    }

    # position insert karna
    if position <= 0:
        videos.insert(0, new_video)
    elif position > len(videos):
        videos.append(new_video)
    else:
        videos.insert(position - 1, new_video)

    # json save karna
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(videos, f, indent=4, ensure_ascii=False)

    print(f"✅ '{title}' added at position {position}")
