import requests
import re

def query(payload):
    response = requests.post("https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1",
                             headers={"Authorization": "Bearer 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"}, json=payload)
    return response.json()

def main(post):
        user_query = '''You are given a post- \"'''
        post_text = post
        user_query += "\n" + post_text
        user_query += '\".\nThe reacts in linkedin are- like, celebrate, support, love, insightful. You are assigned to read a post and provide a necessary reaction from the 5 reactions available. What is the suitable linkedin reaction for the given post? You have to choose your reacton from-(like, celebrate, support, love, insightful).'
        # print(user_query)
        #print('==================================================')
        output = query({"inputs": (user_query), "max_new_tokens": 1, "return_full_text": False, "temperature": 0.2})

        cleaned_response = (output[0]['generated_text']).replace(user_query, "").strip()


        reaction_words = ['like', 'support', 'love', 'insightful', 'celebrate', 'funny']

        pattern = r'\b(?:' + '|'.join(reaction_words) + r')\b'

        match = re.search(pattern, cleaned_response, flags=re.IGNORECASE)

        if match:
            return match.group(0)
        else:
            return 'like'


