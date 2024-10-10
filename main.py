import turtle
import pandas

ALIGNMENT = "center"
FONT = ("Ariel", 8, "normal")
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
all_states = states_data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        writer = turtle.Turtle()
        writer.ht()
        writer.penup()
        state_data = states_data[states_data.state == answer_state]
        writer.goto(int(state_data.x), int(state_data.y))
        writer.write(answer_state, True, align=ALIGNMENT, font=FONT)
