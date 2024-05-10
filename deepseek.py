
import os
import json
from openai import OpenAI

from .constants import get_project_category, get_project_name, project_root

configFile = os.path.join(project_root, 'config.json')
with open(configFile, 'r') as file:
    data = file.read()
json_data = json.loads(data)
key = json_data["DEEPSEEK_KEY"]

NODE_CATEGORY = get_project_category("llm")

class DeepSeekChat:
    NAME = get_project_name('DeepSeek')
    CATEGORY = NODE_CATEGORY
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "doWork"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True}),
                 "model": (["deepseek-chat","deepseek-coder"],{"default": "deepseek-chat"}),
            },
        }

    def doWork(self,  prompt, model):
        client = OpenAI(api_key=key, base_url="https://api.deepseek.com/")
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": prompt},
            ]
        )
        print(response.choices[0].message.content)
        return {"result": (response.choices[0].message.content,)}
