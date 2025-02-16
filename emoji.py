emoji_dict = {
    "positive": ["😊", "😃", "😁", "😍", "🥰", "🤩", "🎉", "👍", "🙌", "😇", "🤗", "🥳", "💖", "🌟", "✨"],
    "negative": ["😢", "😭", "😡", "😠", "😞", "😔", "😖", "💔", "👎", "😨", "😱", "🤬", "😣", "😩", "😓"]
}

is_on = True
contain_positive = 0
contain_negative = 0
while is_on:
    passage = input("Enter the passage (or type 'exit' to quit): ")
    if passage.lower() == "exit":
        is_on = False
        break 
    for emoji in emoji_dict["negative"]:
        if emoji in passage:
            contain_positive = "The passage contain negative emoji"
            break
    for emoji in emoji_dict["positive"]:
        if emoji in passage:
            contain_negative = "The passage contain positive emoji"
            break    
    if contain_negative and contain_positive:
            print("The passage contains both positive and negative emojis.")
    elif contain_positive:
            print("The passage contains positive emojis.")
    elif contain_negative:
            print("The passage contains negative emojis.")    
    else:
            print("The passage doesn't contain any emojis.")                     