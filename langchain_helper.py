import os
import io
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate


load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

prompt_template_name = PromptTemplate(
    input_variables=["cuisine"],
    template="Suggest ONE fancy restaurant name for {cuisine} cuisine. Return ONLY the name."
)

prompt_template_menu = PromptTemplate(
    input_variables=["restaurant_name"],
    template="Suggest 8 menu items for {restaurant_name}. Return ONLY as comma separated values."
)

prompt_template_recommendation = PromptTemplate(
    input_variables=["cuisine","menu_items"],
    template="Based on the indian {cuisine} common weather and menu items {menu_items}, suggest 1 dish suitable,give only the name of the dish and small description."
)


def generate_restaurant_name_and_items(cuisine):
    
    name_chain = prompt_template_name | llm
    name_output = name_chain.invoke({"cuisine": cuisine})
    restaurant_name = name_output.content.strip()

    
    menu_chain = prompt_template_menu | llm
    menu_output = menu_chain.invoke({"restaurant_name": restaurant_name})
    menu_items = menu_output.content.strip()

    recomendation_chain = prompt_template_recommendation | llm
    recomendation_output = recomendation_chain.invoke({"cuisine": cuisine, "menu_items": menu_items})
    recomendation = recomendation_output.content.strip()    

    return {
        "restaurant_name": restaurant_name,
        "menu_items": menu_items,
        "recommendation": recomendation
    }

if __name__ == "__main__":
    # Test the logic
    result = generate_restaurant_name_and_items("Italian")
    print(f"Restaurant Name: {result['restaurant_name']}")
    print(f"Menu Items: {result['menu_items']}")
        # result['logo'].show() # Uncomment to see the image locally