# dm/llm.py

import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def query_llm(model: str, system_prompt: str, user_prompt: str) -> str:
    """
    Sends a prompt to Ollama and returns the model's response.

    model: llama3.2, phi3, mistral, etc.
    system_prompt: DM rules
    user_prompt: current game state + player action
    """

    payload = {
        "model": model,
        "prompt": f"{system_prompt}\n\n{user_prompt}",
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    return response.json()["response"]
