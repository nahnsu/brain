
from promptflow import tool

@tool
def my_python_tool(input: str) -> str:
    intial = f"""
        Write step-by-step instructions to fulfil this request or answer this question:
        {input}

        Keep your response precise and to the point.
        Do not output anything other than a list of instructions.
        Do not give examples of how to complete the task in the instructions.
        Make sure there as little overlap between steps as possible.
        Make instructions that you think are plauspible for an LLM agent.
    """

     # TODO: PAG: 
