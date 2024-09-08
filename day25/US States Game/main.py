import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = r"US States Game\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv(r"US States Game\50_states.csv")
all_states = data['state'].to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", 
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        # it can be simply done with list comprehension as:
        missing_states = [state for state in all_states if state not in guessed_states]
        missed_states = pandas.DataFrame(missing_states)
        missed_states.to_csv("US States Game\missed_states.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

screen.mainloop()