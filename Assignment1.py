from typing import List
from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama


class Product(BaseModel):
    product_name: str = Field(description="Product name")
    product_details: str = Field(description="Product details")
    price: float = Field(description="Price in USD")


class ProductList(BaseModel):
    products: List[Product]


parser = PydanticOutputParser(pydantic_object=ProductList)
model = ChatOllama(model="llama3.2", temperature=0)


format_instructions = """
Output a JSON object (enclosed in curly braces) with one key 'products'  which is a list of **at least 5** product objects.
Do NOT output JSON arrays at the top level. The output must be a JSON object starting with '{' and ending with '}'.

Each product object must have these fields:
- product_name (string)
- product_details (string)
- price (number in USD)

Only output the JSON object. Do NOT output any text, explanation, or comments.

Example:
{
  "products": [
    {
      "product_name": "Galaxy S24 Ultra",
      "product_details": "Latest flagship smartphone with advanced camera features.",
      "price": 1199.99
    },
    {
      "product_name": "Galaxy A54",
      "product_details": "Mid-range Android smartphone with a large display and quad-camera setup.",
      "price": 499.99
    }
  ]
}
"""


prompt = PromptTemplate(
    input_variables=["query"],
    partial_variables={"format_instructions": format_instructions},
    template=(
        "Answer the following query by providing product information.\n"
        "{format_instructions}\n"
        "Query: {query}"
    )
)


def main():
    while True:
        user_query = input("Enter your product query (or type 'exit' to quit): ").strip()
        if user_query.lower() == "exit":
            print("Exiting...")
            break

        try:
            # Format the prompt text for the model
            prompt_text = prompt.format(query=user_query)
            # Invoke model (returns AIMessage)
            raw_response = model.invoke(prompt_text)

            # Extract the content string from AIMessage
            raw_text = raw_response.content

            print("\nRaw model output:\n", raw_text, "\n")

            # Parse JSON string into ProductList object
            result = parser.parse(raw_text)

            # Show only last 5 products if available
            if not result.products:
                print("No products found for this query.")
            else:
                print(f"Showing last {min(5, len(result.products))} products:\n")
                for product in result.products[-5:]:
                    print(f"Product Name: {product.product_name}")
                    print(f"Product Details: {product.product_details}")
                    print(f"Price: ${product.price}")
                    print("-" * 40)

        except Exception as e:
            print("Failed to parse response:", e)


if __name__ == "__main__":
    main()
