# agentic_chatbot

LangGraph: a small framework for building stateful, agentic chatbots and tools.

Overview
--

This repository contains a demo project that builds an agentic chatbot using a
graph-based approach. It includes LLM adapters, node definitions, state
management, and a Streamlit UI for quick experimentation.

Key features
--

- Graph-based agent orchestration
- Pluggable LLM adapters (Groq example included)
- Simple Streamlit UI for interaction and demos

Requirements
--

- Python 3.10+ (recommended)
- See `requirements.txt` for Python dependencies

Quickstart
--

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Configure secrets (do not store secrets in the repo):

- Create a `.env` file (recommended) with any API keys you need, for example:

```ini
# .env
GROQ_API_KEY=your_groq_api_key_here
```

- Update the code to read from environment variables or use an external
  configuration file that is excluded from git. The project includes
  `src/langgraphpagenticai/ui/uiconfigfile.ini` — ensure any keys are removed
  from committed files.

3. Run the app (example):

```bash
python app.py
# or if using the Streamlit UI
streamlit run src/langgraphpagenticai/ui/streamlitui/loadui.py
```

Security note
--

Sensitive keys were previously committed and then removed from history. If you
were using the exposed Groq API key, rotate/revoke it now in your provider
dashboard. Always keep keys in environment variables or an ignored `.env`.

Repository layout
--

- `app.py` - entrypoint for running the demo
- `requirements.txt` - Python dependencies
- `src/` - library and app source
  - `langgraphpagenticai/` - core implementation
    - `graph/` - graph builder and helpers
    - `LLMS/` - LLM adapter(s)
    - `nodes/` - node implementations for the graph
    - `state/` - state management
    - `ui/` - UI code (Streamlit)

Contributing
--

Contributions welcome. Please follow these rules:

- Open an issue before major changes
- Keep secrets out of commits
- Add tests for new behavior where appropriate

License
--

This project currently has no license file. If you want to make it public,
add a `LICENSE` file (for example MIT) to clarify terms.

Next steps (recommended)
--

- Add `.env` support and update code to read secrets from environment
- Add `.gitignore` entries for environment/config files
- Rotate any exposed API keys

## End to End Project Agentic AI project