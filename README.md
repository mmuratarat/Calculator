# Calculator
A basic calculator using Python, FastAPI and Streamlit


For running the FastAPI server we need to run the following command:

```
uvicorn fast_api:app --reload
```

Tested using Postman with JSON input.

REST protocol separates the data storage(back-end) and the UI(front-end) from the server thus allowing the client and server to be independent.

For creating the UI we use Streamlit.

For running the streamlit server we need to run the following command:

```
streamlit run stream_lit.py
```
