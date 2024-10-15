import pandas as pd
from flask import Blueprint, render_template

main = Blueprint('main', __name__)

# Load and process data
def load_data():
    # Load the data (replace this with actual loading logic)
    df = pd.read_excel('data/processed_data.xlsx')
    
    # Clean up the data by removing any newline characters
    df = df.replace(r'\n','', regex=True)

    return df

@main.route('/')
def show_table():
    df = load_data()  # Your function to load data

    # Clean the DataFrame by removing any extra newlines
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    return render_template('index.html', tables=[df.to_html(classes='data')], titles=df.columns.values)
