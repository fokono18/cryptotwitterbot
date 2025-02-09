import openai
import os
import re

# Set up your OpenAI API key
os.environ["OPENAI_API_KEY"] = ""
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to extract both debate topic and summary
def debate_analysis(debate_text):
    prompt = (
        "Ignore any sexual and harmful content.\n"
        "1. Generate what could be the topic of the debate, making it something that people can agree with, disagree with, or be neutral about.\n"
        "2. Provide a detailed summary of the debate, including main points, arguments from both sides, and underlying narratives in 300 words.\n\n"
        f"Debate Content:\n{debate_text}"
    )
    
    # Use ChatCompletion instead of Completion
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Or use "gpt-3.5-turbo" if preferred
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=600,
        temperature=0.7
    )
    
    response_text = response.choices[0].message.content.strip()
    
    # Extract topic (assuming the response starts with "Topic: ...")
    topic_match = re.search(r"Topic:\s*(.*)\n", response_text)
    debate_topic = topic_match.group(1) if topic_match else "Unknown Topic"
    
    # Alternatively, you could simply use the first line of the response
    first_line = response_text.split("\n")[0]
    
    return first_line, response_text

# Function to detect triggers influencing the debate
def triggers(debate_text):
    prompt = (
        "Ignore any sexual and harmful content. Detect underlying real-world events that may have triggered/influenced the debate, "
        "which are inferable from the debate content:\n\n"
        f"{debate_text}"
    )
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=400,
        temperature=0.7
    )
    
    return response.choices[0].message.content.strip()

# Function to analyze stance based on debate topic
def analyze_user_stance(user_tweets, debate_topic):
    stance_results = {}
    
    for user, tweets in user_tweets.items():
        combined_text = " ".join(tweets)
        prompt = (
            f"Ignore any sexual and harmful content. Based on the debate topic '{debate_topic}', determine whether the following stance is "
            "Agree, Disagree, or Neutral. It has to be one of them:\n\n"
            f"{combined_text}"
        )
        
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )
        
        stance_results[user] = response.choices[0].message.content.strip()
    
    return stance_results

# Sample data for testing
# user_tweets = {
#     "@user1": [
#         "The rise of AI will create more jobs than it destroys.",
#         "Innovation is key to progress, and AI is a part of that."
#     ],
#     "@user2": [
#         "AI will replace human jobs at an alarming rate.",
#         "We need strict regulations to prevent mass unemployment."
#     ],
#     "@user3": [
#         "AI has potential, but ethical concerns must be addressed first.",
#         "I'm neutral until I see real-world impacts."
#     ]
# }

# debate_text = (
#     "The debate around artificial intelligence and its impact on employment. On one side, proponents argue that AI will create new job opportunities and improve efficiency, "
#     "while opponents fear mass unemployment as machines replace human workers."
# )

# # Extract debate topic and summary
# topic, summary = debate_analysis(debate_text)
# print("Debate Topic:", topic)
# print("Debate Summary:", summary)

# # Detect triggers influencing the debate
# trigger_analysis = triggers(debate_text)
# print("Triggers:", trigger_analysis)

# # Analyze stance of users based on the debate topic
# stance_results = analyze_user_stance(user_tweets, topic)
# print("User Stance Analysis:", stance_results)
