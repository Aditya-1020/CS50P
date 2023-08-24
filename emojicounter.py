import emoji

def count_emoji(User_input):
    count = 0
    for character in User_input:
        if character in emoji.UNICODE_EMOJI:
            count += 1
    return count

user_input = input("Enter a sentence: ")

emoji_count = count_emoji(user_input)

print("Number of emojis:", emoji_count)
