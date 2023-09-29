import streamlit as st
import time
from simpleai.search import CspProblem, backtrack
import re


st.title("🧩 Charles Nana Kwakye's Cryptoarithmetic Puzzle")

user_input = st.text_input(label="Enter puzzle")
state = st.button(label="Find Solution", on_click=None, type="primary", use_container_width=False)
# import time
# import streamlit as st

# with st.spinner('Wait for it...'):
#     time.sleep(5)
# st.success('Done!')

if state:
    try:
        with st.spinner('Looking for solutions ...'):
                user_input = user_input.replace(" ", "")

                equal_sign_index = user_input.index("=")

                factor = user_input[:equal_sign_index+1]
                result = user_input[equal_sign_index+1:]


                all_words = re.findall("[a-zA-Z]+", user_input)

                not_zero_letters = set([word[0] for word in all_words])

                variables = tuple(set(tuple(input_str for s in all_words for input_str in s)))

                domains = {}

                for variable in variables:
                    if variable in not_zero_letters:
                        domains[variable] = list(range(1, 10))
                    else:
                        domains[variable] = list(range(0, 10))



                def constraint_unique(variables, values):
                    return len(values) == len(set(values))  # remove repeated values and count

                def constraint_dynamic_operation(variables, values):
                    int_list_processed_factor = []
                    str_list_processed_operations =[]
                    int_processed_result = int
                    processed_factor = ""
                    processed_result = ""
                    for char in factor:
                    # if the character is a letter, find its index in the tuple and append it to the output
                        if char.isalpha():
                            processed_factor += str(values[variables.index(char)])
                    # if the character is an operator, add it to the list
                        else:
                            int_list_processed_factor.append(int(processed_factor))
                            if char != "=":
                                str_list_processed_operations.append(str(char))
                            processed_factor = ""
                    

                    for char in result:
                        processed_result += str(values[variables.index(char)])
                    int_processed_result = int(processed_result)

                    string = ""
                    for i in range(len(int_list_processed_factor)):
                        string+= str(int_list_processed_factor[i])
                        if i < len(str_list_processed_operations):
                            string+= str_list_processed_operations[i]
                    return eval(string)== int_processed_result



                constraints = [
                    (variables, constraint_unique),
                    (variables, constraint_dynamic_operation)
                ]


                problem = CspProblem(variables, domains, constraints)

                output = backtrack(problem)
                nums_output = ""
                for char in user_input:
                    if char.isalpha():
                        nums_output+= str(output.get(char))
                    else:
                        nums_output+=char
                if output != "None":
                    st.success("Successfull", icon="😁")
                    
                    st.markdown(":red[Problem:] " + user_input)
                    st.markdown(":red[Solution:] " + nums_output)
                    for key, value in output.items():
                        st.header(key + " = " + str(value))
                    
                else:
                    st.error("Sorry, no solution available ", icon='🙁')
        
    except:
        st.error("Sorry, no solution available ", icon='🙁')