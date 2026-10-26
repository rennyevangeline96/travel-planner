from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, Task, Crew

city = input("Which city? ")

planner = Agent(
    role="Travel Planner",
    goal="Suggest memorable, must-visit places that give travelers a real feel for a city",
    backstory=(
        "You are a well-traveled local guide who has spent years helping "
        "first-time visitors discover the best of a city in a short trip. "
        "You skip generic tourist traps and give short, practical tips "
        "that help people enjoy each place."
    ),
    verbose=True,
)

task = Task(
    description="Suggest exactly 3 places to visit in {city}.",
    expected_output=(
    "A numbered list of exactly 3 places in the format "
    "'1. Place Name - short reason or tip'. "
    "Keep each item to one line. "
    "No introduction, no conclusion, nothing else."
),
    agent=planner,
)

crew = Crew(agents=[planner], tasks=[task])
result = crew.kickoff(inputs={"city": city})

print(result)