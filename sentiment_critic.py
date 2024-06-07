import requests
import re

def query(payload):
    response = requests.post("https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1",
                             headers={"Authorization": "Bearer HUGGINGFACE_API_TOKEN"}, json=payload)
    return response.json()

def main(post, sentiment, reacts):
        user_query = '''You are given a post- \"'''
        post_text = post
        user_query += "\n" + post_text
        user_query += f'\".\nFor this post the sentiment "{sentiment}" was given by AI. The most counted reactions on the original post on linkedin were {reacts[0]}, {reacts[1]} and {reacts[2]} in descending order. Now compare the AI generated reaction and these three reactions and reply which one of this three reaction is the most suitable.'
        # print(user_query)
        #print('==================================================')
        output = query({"inputs": (user_query), "max_new_tokens": 1, "return_full_text": False, "temperature": 0.2})

        cleaned_response = (output[0]['generated_text']).replace(user_query, "").strip()


        reaction_words = ['like', 'support', 'love', 'insightful', 'celebrate', 'funny', 'yes', 'no']

        pattern = r'\b(?:' + '|'.join(reaction_words) + r')\b'

        match = re.search(pattern, cleaned_response, flags=re.IGNORECASE)

        if match:
            return match.group(0)
        else:
            return 'like'


