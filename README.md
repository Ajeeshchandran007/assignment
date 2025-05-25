# Product Info Extractor using LLM (LLaMA 3.2 via Ollama)

This Python script allows you to interact with a local LLM (LLaMA 3.2 via Ollama) to extract structured product information from user queries. It parses the response using Pydantic models to ensure the output adheres to a consistent format.

---

## Features

- 🔍 Accepts natural language product queries.
- 🤖 Uses LLaMA 3.2 (via `ChatOllama`) to generate product data.
- ✅ Parses and validates output using `PydanticOutputParser`.
- 🧾 Outputs clean, structured product information (name, details, price).
- ♻️ Interactive loop with graceful exit (`exit` command).

---

## Requirements

Install the following dependencies:

```bash
pip install langchain langchain-core langchain-ollama pydantic
```

Ensure you have [Ollama](https://ollama.com/) installed and running locally with the LLaMA 3.2 model available:

```bash
ollama run llama3.2
```

---

## Usage

### Run the script interactively:

```bash
python main.py
```

### Example Query

```text
Enter your product query (or type 'exit' to quit): Show me 5 smartphones with details and prices
```

### Output Example

```text
Product Name: Galaxy S24 Ultra
Product Details: Latest flagship smartphone with advanced camera features.
Price: $1199.99
----------------------------------------
Product Name: Pixel 8 Pro
Product Details: High-end Google phone with AI photography tools.
Price: $999.00
----------------------------------------
...
```

---

## File Structure

```
main.py          # Core script for querying the model and parsing results
README.md        # This file
```

---

## Notes

- The model output is expected to be a JSON object with a top-level `"products"` list.
- The script only displays the last 5 products even if more are returned.
- Errors are caught and logged gracefully if JSON is malformed or doesn't meet schema requirements.

---

## License

MIT License — Feel free to modify and use this project for any purpose.
