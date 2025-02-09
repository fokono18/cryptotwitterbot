import google.generativeai as genai
import os
from textblob import TextBlob

# Set up your Gemini API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyDSYOy5AcTKGomV9fd5_q81HYzp7WrjMxU"

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to summarize debate text
def summarize_debate(debate_text):
    prompt = f"Ignore any sexual and harmful content.Generate detailed summaries of the debate including main points, arguments of both sides, and underlying narratives in 300 words:\n\n{debate_text}"
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text

# Function to get the main topic of the debate 
def debate_topic(debate_text):
    prompt = f"Ignore any sexual and harmful content.Generate what could be the topic of the debate make it something that people can agree with or disagree with or be neutral:\n\n{debate_text}"
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text

# Function to get the main topic of the debate 
def triggers(debate_text):
    prompt = f"Ignore any sexual and harmful content.Detect underlying real-world events that may have triggered/influenced the debate, that are inferrable from the debate content:\n\n{debate_text}"
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text

# Function to analyze stance based on debate topic
def analyze_user_stance(user_tweets, debate_topic):
    stance_results = {}
    model = genai.GenerativeModel("gemini-pro")
    
    for user, tweets in user_tweets.items():
        combined_text = " ".join(tweets)
        prompt = f"Ignore any sexual and harmful content. Based on the debate topic '{debate_topic}', determine whether the following stance is Agree, Disagree, or Neutral:\n\n{combined_text}"
        response = model.generate_content(prompt)
        stance_results[user] = response.text.strip()
    
    return stance_results


# Example usage
user_tweets = {
    "@user1": ["Crypto is the future of decentralized finance.", "It empowers individuals by eliminating intermediaries."],
    "@user2": ["The volatility of crypto makes it unreliable for mainstream adoption.", "Governments need to regulate it more."],
    "@user3": ["While regulation is not necessary, blockchain technology is revolutionary and should not be embraced." "i Don't agree with any of you"]
}

