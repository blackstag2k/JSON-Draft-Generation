import google.genai as genai

client = genai.Client(api_key="ENTER_API_KEY")

def generate_outline(topic):
    prompt = f"Generate an outline for a draft for the topic: \n\n{topic}"
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response. text

def generate_draft(outline):
    prompt = f"Generate a draft using the outline generated from prompt 1: \n\n{outline}"
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response. text

def generate_critique(draft):
    prompt = f"Critique the draft generated in prompt 2. Highlight the issues and list out the fixes for them so we can improve this draft: \n\n{draft}"
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response. text

topic = "5 Best Ways to Master Influencer Marketing",
outline = generate_outline(topic),
draft = generate_draft(outline),
critique = generate_critique(draft)

import json

blog_generation_result = {
    "topic": topic,
    "outline": outline,
    "draft": draft,
    "critique": critique
}

with open("output.json", "w") as f:
    json.dump(blog_generation_result, f, indent=4)

print(json.dumps(blog_generation_result, indent=4))