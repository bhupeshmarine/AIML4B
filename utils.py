import os
from IPython.display import Markdown, display
import subprocess

def question1():
    statement = (
        "True or False: \nAI is a subset of Machine Learning, and it focuses on "
        "building systems that can perform tasks which normally require human intelligence.\n\n"
        "Enter True or False: "
    )

    user_input = input(statement).strip().lower()
    print()
    display(Markdown("**Result**"))

    if user_input == "false":
        print("Good Job! Your answer is correct. ML is subset of AI")
    elif user_input == "true":
        print("Your answer is wrong because Machine Learning is a subset of AI, AI is not a subset of Machine Learning.")
    else:
        print("Invalid input. Please enter only True or False.")

        
def verify_present_working_directory(expected_first_file="aaa.txt"):
    files = sorted(os.listdir(os.getcwd()))
    if files[-1] == 'zzz.txt':
        display(Markdown("**Nice job!**"))
        print("your code worked perfectly. You have returned to the present working directory.")
    else:
        display(Markdown("**Ops! Test Failed**"))
        print("You are not in the correct directory yet. Please try your code again")

def question2():
    statement = (
        "True or False: \nDeep learning is a specialized branch of machine learning that uses multi-layer neural networks, and it is often treated separately because of its depth, complexity, and wide range of applications.\n\n"
        "Enter True or False: "
    )

    user_input = input(statement).strip().lower()
    print()
    display(Markdown("**Result**"))

    if user_input == "true":
        print("Your answer is correct. Deep Learning is a subfield of Machine Learning.")
    elif user_input == "false":
        print("Your answer is wrong. Deep Learning is a subfield of Machine Learning.")
    else:
        print("Invalid input. Please enter only True or False.")


def check_pandas_numpy_installed():
    missing_libraries = []

    try:
        import pandas
    except ImportError:
        missing_libraries.append("pandas")

    try:
        import numpy
    except ImportError:
        missing_libraries.append("NumPy")

    if not missing_libraries:
        print("pandas and NumPy are installed.")
    elif len(missing_libraries) == 1:
        print(f"{missing_libraries[0]} is not installed. Install it and then run again.")
    else:
        print(f"{' and '.join(missing_libraries)} are not installed. Install them and then run again.")



def verify_conda_environment(env_name="aiml_env"):
    try:
        result = subprocess.run(
            ["conda", "env", "list"],
            capture_output=True,
            text=True,
            check=True
        )
        
        output = result.stdout
        
        if env_name in output:
            display(Markdown("**Congratulations!!! You made it.**"))
            print(f"The environment '{env_name}' has been created successfully.")
        else:
            display(Markdown("**Test Failed. read instructions and create again**"))
            print(f"The environment '{env_name}' was not found.")
            
    except Exception as e:
        display(Markdown("**Ops!**"))
        print("Unable to check Conda environments.")
        print("Error:", e)


def verify_python_version_from_yaml(expected_version="3.11"):
    user_input = input("what is the Python version is in the YAML file (example: 2.11): ").strip()
    print()
    if user_input == expected_version:
        display(Markdown("**Good Job!**"))
        print("You have checked your YAML file correctly.")
    else:
        display(Markdown("**Nope! Check environment.yml file again**"))
        print("You did not check the YAML file correctly. Go and check it again and re-run this cell.")