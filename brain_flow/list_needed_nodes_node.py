from promptflow.core import tool
import os
from dotenv import load_dotenv
from openai import AzureOpenAI

@tool
def list_needed_nodes(input: str) -> str:
    
    api_key = os.getenv("API_KEY")
    api_base = os.getenv("ENDPOINT") 
    api_type = 'azure'
    api_version = '2024-02-01'

    deployment_name = 'gpt-4o-mini-nonprod' 

    client = AzureOpenAI(
    api_key=api_key,  
    azure_endpoint=api_base,
    api_version=api_version
    )

    try:
        response = client.chat.completions.create(
                    model=deployment_name,
                    messages=[

                            {"role": "user", "content": f"{input}"}
                        ]
                    )
        return response.choices[0].message.content
    except:
        return "An exception has occurred at the list_needed_nodes_node."
