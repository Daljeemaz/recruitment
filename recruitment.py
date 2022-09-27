# This function returns a list of skills.
# This is the list that the user will choose from
# Add at least 3 random skills for the user to select from
def get_skills():
    skills = ["coding", "football", "photogragh", "running"]
    return skills

# This function pretty prints the skills to the user
# It takes the list of skills as an argument and prints them numbered
# This function doesn't return anything
def show_skills(skills):
    for count, skill in enumerate (skills):
        print(count, skill)

    


# Shows the available skills and have user pick from them two skills
# HINT: Use previous built functions to show the skills
# For example, if the user enters 1, the first skill in your list of skills will be added to the list
# Return a list of the two skills that the user inputted
def get_user_skills(skills):
    get_skills = []
    print ("Enter the Skills: ")
    skills = input(skills)
    get_skills.append(skills)
    return skills


# This function will get the user's cv from their inputs
# HINT: Use previous built functions to get the skills from the user
def get_user_cv(skills):
    cv = {
        "name": "Duaij",
        "age": 28,
        "experience": 4,
        "skills": get_user_skills(skills)
    }
    name = input("Enter the name: ")
    age = input("Enter the age: ")
    experience = input("Enter the years of the experience: ")
    return cv 


# This functions checks if the cv is acceptable or not, by checking the age, experience and skills and return a boolean (True or False) based on that
def check_acceptance(cv, desired_skill):
    if "age" > 25 and < 40:
        return True
    elif "experience" > 3:
        return True
    elif "desired_skill" == skills:
        return True
    else:
        return False
print(check_acceptance(cv,))

def main():
    # Write your main logic here by combining the functions above into the
    # desired outcome
    skills = get_skills()
    show_skills(skills)
    


if __name__ == "__main__":
    main()
