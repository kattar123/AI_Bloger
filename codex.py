#nimport streamlit
import streamlit as st

#app title
st.title('AI blogger app')
st.subheader('Find the best restrants near to you')

with st.expander('seltion 1  - choose the place'):
    places = ['Restaurant', 'cafe','Both']
    place = st.selectbox('where do you want to go?', places)


#user input
using_uber = ['yes, call me uber','no, show me location','yes, call me uber and show me location']

with st.sidebar:
    st.selectbox('Do you want to use uber',using_uber)
    distans = st.slider(
        'what is the maximum distance for this place? (km)',
        min_value=1,
        max_value=30,
        value=10 )



with st.expander('selection 2 - choose the meal'):
    st.write('you can choose one of the following meals')
    col1, col2, = st.columns(2)
            
    with col1:
        if place !='cafe':
            meals = ['breakfast', 'lunch', 'dinner', 'dessert']
            meal_choice = st.selectbox('what type you want to eat?', meals)

            if meal_choice == 'breakfast':
                breakfast = ['Egyptions(Foul & tamia', 'eggs', 'milk and cheeese']
                breakfast_choice = st.selectbox('what do you want to eat?', breakfast)

            elif meal_choice == 'lunch':
                lunch = ['grilled chicken', 'fish', 'pizza', 'pasta','koshari']
                lunch_choice = st.selectbox('what do you want to eat?', lunch)

            elif meal_choice == 'dinner': 
                dinner = ['grilled chicken', 'fish', 'pizza', 'pasta','koshari']
                dinner_choice = st.selectbox('what do you want to eat?', dinner)

            elif meal_choice == 'dessert':
                dessert = ['cake', 'ice cream', 'fruit salad','pudding','cheesecake','rice pudding']
                dessert_choice = st.selectbox('what do you want to eat?', dessert)
        else:
            categories = ['hot drinks', 'cold drinks', 'dessert']
            category_choice = st.selectbox('what do you want to drink?', categories)

            if category_choice == 'hot drinks':
                hot_drinks = ['tea', 'coffee', 'hot chocolate','latte','cappuccino']
                hot_drink_choice = st.selectbox('what do you want to drink?', hot_drinks)

            elif category_choice == 'cold drinks':
                cold_drinks = ['juice', 'soda', 'iced coffee','iced tea']
                cold_drink_choice = st.selectbox('what do you want to drink?', cold_drinks)
            else:
                desserts = ['cake', 'ice cream', 'fruit salad','pudding','cheesecake','rice pudding']
                dessert_choice = st.selectbox('what do you want to drink?', desserts)


    with col2:
        if st.button('submit order'):
            st.success('your order is placed successfully')
        else:
            st.warning('hurry up! we will be closed within 30 min')