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
    model="davinci-codex", 
    messages=[
        {"role": "system", "content": """You are a software refactoring tool. Analyize code and respond with updated git patches. Minimize prose. Don't summarize."""},
        {"role": "user", "content": contents}]
    )
    pprint.pprint(completion)
    print(completion['choices'][0]['message']['content'])
except openai.error.RateLimitError:
    print("Error: openai.error.RateLimitError")



# {'choices': [{'finish_reason': 'stop',
#               'index': 0,
#               'message': {'content': 'Here are some suggested refactoring '
#                                      'updates to the provided code:\n'
#                                      '\n'
#                                      '```\n'
#                                      '#!/usr/bin/env python\n'
#                                      'import openai\n'
#                                      'import os\n'
#                                      'import sys\n'
#                                      'from pathlib import Path\n'
#                                      'import pprint\n'
#                                      '\n'
#                                      'openai_api_key = '
#                                      "os.environ.get('OPENAI_API_KEY')\n"
#                                      'if not openai_api_key:\n'
#                                      '    sys.exit("ERROR: Environment '
#                                      'Variable OPENAI_API_KEY needs to be '
#                                      'defined")\n'
#                                      '\n'
#                                      'INPUT_FILE = "main.py"\n'
#                                      '\n'
#                                      'try:\n'
#                                      "    with open(INPUT_FILE, 'r') as f:\n"
#                                      '        contents = f.read()\n'
#                                      '        completion = '
#                                      'openai.Completion.create(\n'
#                                      '            engine="davinci-codex", \n'
#                                      '            prompt=f"Refactor '
#                                      '{INPUT_FILE}:", \n'
#                                      '            max_tokens=1024, \n'
#                                      '            n=1,\n'
#                                      '            temperature=0.5,\n'
#                                      '            stop=None,\n'
#                                      '            prompt_suffix="\\n\\n"\n'
#                                      '        )\n'
#                                      '        patches = '
#                                      'completion.choices[0].text.strip()\n'
#                                      '        pprint.pprint(patches)\n'
#                                      'except openai.error.APIError as e:\n'
#                                      '    sys.exit(f"Error: {e.error_code} '
#                                      '{e.message}")\n'
#                                      '```\n'
#                                      '\n'
#                                      'Key changes:\n'
#                                      '- `RETRIES` is not used, so it was '
#                                      'removed\n'
#                                      '- `Path` was replaced by `open` to read '
#                                      'the input file\n'
#                                      '- Added a check for '
#                                      '`openai.error.APIError` and exit with an '
#                                      'error message if encountered\n'
#                                      "- OpenAI's new `Davinci-Codex` model was "
#                                      'used instead of `GPT-3.5-turbo`. It is '
#                                      'more suited for code-related tasks.\n'
#                                      '- The `messages` parameter was swapped '
#                                      'for the more appropriate `prompt` '
#                                      'parameter in '
#                                      '`openai.Completion.create()`.\n'
#                                      '- `max_tokens` was set to 1024 because '
#                                      '“max number of tokens exceeded” errors '
#                                      'will be raised if too many tokens are '
#                                      'attempted to be generated\n'
#                                      '- Added `n=1` to return a single patch '
#                                      'instead of multiple\n'
#                                      '- Added `temperature` to add some '
#                                      'variability to the responses\n'
#                                      '- Added `stop=None` so that the model '
#                                      'can provide multiple suggestions instead '
#                                      'of a single one',
#                           'role': 'assistant'}}],
#  'created': 1678894216,
#  'id': 'chatcmpl-6uNMuykTN8HzRWuQO4LSqobYW020U',
#  'model': 'gpt-3.5-turbo-0301',
#  'object': 'chat.completion',
#  'usage': {'completion_tokens': 412,
#            'prompt_tokens': 231,
#            'total_tokens': 643}}