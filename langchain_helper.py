from langchain.agents import AgentType, initialize_agent
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.chains import SequentialChain
import os
from secret_key import api_key
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
os.environ['API_KEY']= api_key
load_dotenv()
GOOGLE_API_KEY = os.getenv("API_KEY")
llm = ChatGoogleGenerativeAI(google_api_key=GOOGLE_API_KEY, model="gemini-pro", temperature=0.6)



def generate_restaurant_name_and_items(cuisine):
  
  prompt_template_name = PromptTemplate(
    input_variables =['cuisine'],
    template = "I want to open a restaurant for {cuisine} food. Suggest a fency name for this.Please give only one name"
  )

  name_chain =LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

  prompt_template_items = PromptTemplate(
      input_variables = ['restaurant_name'],
      template="Suggest some menu items for {restaurant_name}."
  )

  food_items_chain =LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

  chain = SequentialChain(
      chains = [name_chain, food_items_chain],
      input_variables = ['cuisine'],
      output_variables = ['restaurant_name', "menu_items"]
  )

  response = chain({"cuisine": "Indian"})
  return response
  
if __name__ == "__main__":
  # print(generate_restaurant_name_and_items('Indian'))
  print("Restaurant Name and Menu Items:")
  content_dict = generate_restaurant_name_and_items('Indian')
  print(f"Restaurant Name: {content_dict['restaurant_name']}")
  print("Menu Items:")
  for item in content_dict['menu_items'].split('\n'):
    print(f"- {item}")