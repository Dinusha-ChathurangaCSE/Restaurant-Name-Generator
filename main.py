import streamlit as st 
import langchain_helper

st.title("Restaurant Name Generator")
cuisine = st.sidebar.selectbox("Pick a cuisine",{'American','Indian','Mexican','Italian','Spanish'})


  
if cuisine:
  response = langchain_helper.generate_restaurant_name_and_items(cuisine)
  st.header(response['restaurant_name'])
  menu_items = response['menu_items'].split('\n')
  st.write("**Menu items**")
  
  for item in menu_items:
    if item.strip():
      st.write("-", item)