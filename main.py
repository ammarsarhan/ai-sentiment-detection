from sentiment_words import sentiment_words

positive_count = 0
negative_count = 0
is_on = True
while is_on:
    passage = input("Enter the passage (or type 'exit' to quit): ")
    if passage.lower() == "exit":
        is_on = False
        break 
    for word in sentiment_words["positive"]:
        if word in passage:
            positive_count += 1
    for word in sentiment_words["negative"]:
        if word in passage:
            negative_count += 1    
    if negative_count > positive_count:
        print("The passage contains a high volume of offensive language.")
    elif positive_count > negative_count:
        print("The content is rich in positive and encouraging words.")     
    else:
        print("The passage exhibits a relatively balanced mix of positive and negative sentiment")           