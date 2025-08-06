## 📅 What I Learned Today (2025-08-05)

✅ **LangChain Basics**  
- Used `ChatPromptTemplate` to structure conversations.  
- Built chains using `|` operator: `prompt | llm | output_parser`.

✅ **LCEL (LangChain Expression Language)**  
- Learned how LCEL simplifies chaining steps using the `|` operator.  
- Built modular, readable pipelines for prompt → LLM → parser workflows.  
- Understood how LCEL improves code reusability and flexibility.

✅ **Ollama LLM Integration**  
- Used Ollama with `gemma:2b` model for local inference.  
- Installed and imported `langchain_community.llms.Ollama`.

✅ **Output Parsing**  
- Learned to use `StrOutputParser` to extract clean text from LLM responses.

✅ **Streamlit App**  
- Created a basic Streamlit UI for user question input.  
- Displayed LLM responses dynamically.

✅ **Fixed Common Errors**  
- Solved `ModuleNotFoundError` by installing missing modules.  
- Understood module structure: `langchain_core`, `langchain_community`, etc.
