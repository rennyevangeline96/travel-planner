# CrewAI Travel Planner Agent

A beginner CrewAI project where the user enters a city and a Travel Planner agent suggests 3 places to visit there.

## How it works

- **Agent**: a Travel Planner with a clear role, goal and backstory. The backstory targets first-time visitors on a short trip, so suggestions are iconic and practical. `verbose=True` shows the agent's work in the terminal.
- **Task**: asks for exactly 3 places in the given city. The `expected_output` forces a clean numbered list (`1. Place - short tip`) with no introduction or conclusion.
- **Crew**: bundles the agent and task and runs with `crew.kickoff()`. The city typed by the user fills the `{city}` placeholder in the task description.

## Tech stack

- Python 3.10 to 3.13
- CrewAI
- python-dotenv
- OpenAI API (`openai/gpt-4o-mini`)

## Setup

1. Clone the repo and open the folder.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # macOS / Linux
   ```
3. Install dependencies:
   ```bash
   pip install crewai python-dotenv
   ```
4. Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your-api-key-here
   MODEL=openai/gpt-4o-mini
   ```
   The `.env` file is listed in `.gitignore`, so the key is never committed.

## Run

```bash
python travel_planner.py
```

## Example

```
Which city? Agra
1. Taj Mahal - Visit at sunrise for breathtaking views and fewer crowds.
2. Agra Fort - Explore its stunning red sandstone architecture and rich Mughal history.
3. Mehtab Bagh - Enjoy a serene sunset view of the Taj Mahal from this beautiful garden.
```

## Project structure

```
travel-planner/
├── travel_planner.py   # agent, task, crew and run logic
├── .gitignore          # ignores .env, venv/, __pycache__/
└── README.md
```

## Security

The API key is read from an environment variable via `.env` and is never hard-coded or committed.