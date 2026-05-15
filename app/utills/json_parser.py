import json
import re


def parse_json_response(response_text):
    # remove markdown
    text = re.sub(r"```json|```", "", response_text).strip()
    try:
        data = json.loads(text)

        # 🧠 if double-encoded JSON (VERY common issue)
        if isinstance(data, str):
            data = json.loads(data)

        return data

    except Exception as e:
        print("PARSE ERROR:", e)
        return None