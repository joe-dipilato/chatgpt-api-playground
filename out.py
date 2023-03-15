#!/usr/bin/env python
import openai
import os
import sys
from pathlib import Path
import pprint

openai_api_key = os.environ.get('OPENAI_API_KEY')
if not openai_api_key:
    sys.exit("ERROR: Environment Variable OPENAI_API_KEY needs to be defined")

INPUT_FILE = "main.py"

try:
    with open(INPUT_FILE, 'r') as f:
        contents = f.read()
        completion = openai.Completion.create(
            engine="davinci-codex", 
            prompt=f"Refactor {INPUT_FILE}:", 
            max_tokens=1024, 
            n=1,
            temperature=0.5,
            stop=None,
            prompt_suffix="\n\n"
        )
        patches = completion.choices[0].text.strip()
        pprint.pprint(patches)
except openai.error.APIError as e:
    sys.exit(f"Error: {e.error_code} {e.message}")