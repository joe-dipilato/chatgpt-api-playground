#!/usr/bin/env python
import openai
import os
import sys
from pathlib import Path
import pprint
openai_api_key = os.environ.get('OPENAI_API_KEY',None)
if not openai_api_key:
    print("ERROR: Environment Variable OPENAI_API_KEY needs to be defined")
    sys.exit(1)
INPUT_FILE="main.py"
RETRIES=3
contents=Path(INPUT_FILE).read_text()
done = False
try:
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[
        {"role": "system", "content": """You are an advanced software DevOps and refactoring tool. Analyize code and respond with just the changed lines of code. Minimize prose."""},
        {"role": "user", "content": contents}]
    )
    print(completion)   
except openai.error.RateLimitError:
    print("Error: openai.error.RateLimitError")