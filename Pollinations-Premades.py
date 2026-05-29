class Polly:
    def __init__(self, key):
        import requests
        import json

        self.requests = requests
        self.json = json
        self.key = key

    def gen_text(self, prompt, model="openai-fast", system="You are a helpful assistant.", stream=False):
        url = "https://gen.pollinations.ai/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {self.key}"
        }

        data = {
            "model": model,
            "stream": stream,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": prompt}
            ]
        }

        response = self.requests.post(
            url,
            headers=headers,
            json=data,
            stream=stream
        )

        if not stream:
            return response.json()["choices"][0]["message"]["content"]

        for line in response.iter_lines():
            if line:
                line = line.decode("utf-8")

                if line.startswith("data: "):
                    content = line[6:]

                    if content == "[DONE]":
                        break

                    try:
                        chunk = self.json.loads(content)

                        delta = chunk["choices"][0]["delta"]

                        if "content" in delta:
                            yield delta["content"]

                    except:
                        pass