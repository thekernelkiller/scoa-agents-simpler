# Simplified SCOA using CrewAI Agents

## Setup
1. Install [pipx](https://pipx.pypa.io/stable/installation/)
2. Install [poetry](https://python-poetry.org/docs/) using pipx
3. make sure everything is in path: `poetry --version` to check
4. clone this [repo](https://github.com/thekernelkiller/scoa-agents-simpler)
5. go to your terminal -> pyproject.toml -> check if python version is matching
6. if all good, perform: 
	1. `poetry install`  
	2. `poetry shell`
7. set API key:
	1. rename `.env_example` file to `.env`
	2. in `GOOGLE_API_KEY`, get API from [Google AI Studio](https://aistudio.google.com/app/) 
	3. set in `.env`
8. to run: `python main.py`

## References
1. [CrewAI docs](https://docs.crewai.com/)
2. [Youtube Tutorial for poetry env setup](https://youtu.be/sPzc6hMg7So?si=zuTlNwuJIcRWkz4Q&t=885)
