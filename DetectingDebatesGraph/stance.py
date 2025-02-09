import google.generativeai as genai
import os
import re

# Set up your Gemini API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyBNPqMRj5ttT6UXWiDqHs67WlqPswc51qs"

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to extract both debate topic and summary
def debate_analysis(debate_text):
    prompt = (f"Ignore any sexual and harmful content.\n"
              f"1. Generate what could be the topic of the debate, making it something that people can agree with, disagree with, or be neutral about.\n"
              f"2. Provide a detailed summary of the debate, including main points, arguments from both sides, and underlying narratives in 300 words.\n\n"
              f"Debate Content:\n{debate_text}")
    
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    
    response_text = response.text.strip()
    topic_match = re.search(r"Topic:\s*(.*)\n", response_text)
    debate_topic = topic_match.group(1) if topic_match else "Unknown Topic"
    
    return debate_topic, response_text

# Function to detect triggers influencing the debate
def triggers(debate_text):
    prompt = (f"Ignore any sexual and harmful content. Detect underlying real-world events that may have triggered/influenced the debate, which are inferable from the debate content:\n\n"
              f"{debate_text}")
    
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text

# Function to analyze stance based on debate topic
def analyze_user_stance(user_tweets, debate_topic):
    stance_results = {}
    model = genai.GenerativeModel("gemini-pro")
    
    for user, tweets in user_tweets.items():
        combined_text = " ".join(tweets)
        prompt = (f"Ignore any sexual and harmful content. Based on the debate topic '{debate_topic}', determine whether the following stance is Agree, Disagree, or Neutral:\n\n"
                  f"{combined_text}")
        response = model.generate_content(prompt)
        stance_results[user] = response.text.strip()
    
    return stance_results



user_tweets = {
    "@user1": ["The rise of AI will create more jobs than it destroys.", "Innovation is key to progress, and AI is a part of that."],
    "@user2": ["AI will replace human jobs at an alarming rate.", "We need strict regulations to prevent mass unemployment."],
    "@user3": ["AI has potential, but ethical concerns must be addressed first.", "I'm neutral until I see real-world impacts."]
}

