from flask import Flask, render_template, Blueprint
import pandas as pd
app = Flask(__name__)






a_to_d_mapping = {
    "Abraham Lincoln": "icons/Abraham_Lincoln_29.webp",
    "Alexander": "icons/Alexander_29.webp",
    "Amanitore": "icons/Amanitore_29.webp",
    "Ambiorix": "icons/Ambiorix_29.webp",
    "Basil II": "icons/Basil_II_29.webp",
    "Bà Triệu": "icons/B3Fu_29.webp",
    "Catherine de Medici (Black Queen)": "icons/Catherine_de_Medici_29.webp",
    "Catherine de Medici (Magnificence)": "icons/Catherine_de_Medici_29_29.webp",
    "Chandragupta": "icons/Chandragupta_29.webp",
    "Cleopatra (Egyptian)": "icons/Cleopatra_29.webp",
    "Cleopatra (Ptolemaic)": "icons/Cleopatra_29_29.webp",
    "Cyrus": "icons/Cyrus_29.webp",
    "Dido": "icons/Dido_29.webp",
    "Eleanor of Aquitaine (French)": "icons/Eleanor_of_Aquitaine_29_29-fr.webp",
    "Eleanor of Aquitaine (English)": "icons/Eleanor_of_Aquitaine_29_29.webp",
    "Elizabeth I": "icons/Elizabeth_I_29.webp",
    "Frederick Barbarossa": "icons/Frederick_Barbarossa_29.webp",
    "Gandhi": "icons/Gandhi_29.webp",
    "Genghis Khan": "icons/Genghis_Khan_29.webp",
    "Gilgamesh": "icons/Gilgamesh_29.webp",
    "Gitarja": "icons/Gitarja_29.webp",
    "Gorgo": "icons/Gorgo_29.webp",
    "Hammurabi": "icons/Hammurabi_29.webp",
    "Harald Hardrada (Konge)": "icons/Harald_Hardrada_29.webp",
    "Harald Hardrada (Varangian)": "icons/Harald_Hardrada_29_29.webp",
    "Hojo Tokimune": "icons/Hojo_Tokimune_29.webp",
    "Jadwiga": "icons/Jadwiga_29.webp",
    "Jayavarman VII": "icons/Jayavarman_VII_29.webp",
    "João III": "icons/Jo28Civ6%29.webp",
    "John Curtin": "icons/John_Curtin_29.webp",
    "Julius Caesar": "icons/Julius_Caesar_29.webp",
    "Kristina": "icons/Kristina_29.webp",
    "Kublai Khan (Mongolian)": "icons/Kublai_Khan_29_29-mon.webp",
    "Kublai Khan (Chinese)": "icons/Kublai_Khan_29_29.webp",
    "Kupe": "icons/Kupe_29.webp",
    "Lady Six Sky": "icons/Lady_Six_Sky_29.webp",
    "Lautaro": "icons/Lautaro_29.webp",
    "Ludwig II": "icons/Ludwig_II_29.webp",
    "Mansa Musa": "icons/Mansa_Musa_29.webp",
    "Matthias Corvinus": "icons/Matthias_Corvinus_29.webp",
    "Menelik II": "icons/Menelik_II_29.webp",
    "Montezuma": "icons/Montezuma_29.webp",
    "Mvemba a Nzinga": "icons/Mvemba_a_Nzinga_29.webp",
    "Nader Shah": "icons/Nader_Shah_29.webp",
    "Nzinga Mbande": "icons/Nzinga_Mbande_29.webp",
    "Pachacuti": "icons/Pachacuti_29.webp",
    "Pedro II": "icons/Pedro_II_29.webp",
    "Pericles": "icons/Pericles_29.webp",
    "Peter": "icons/Peter_29.webp",
    "Philip II": "icons/Philip_II_29.webp",
    "Poundmaker": "icons/Poundmaker_29.webp",
    "Qin Shi Huang (Mandate of Heaven)": "icons/Qin_Shi_Huang_29.webp",
    "Qin Shi Huang (Unifier)": "icons/Qin_Shi_Huang_29_29.webp",
    "Ramses II": "icons/Ramses_II_29.webp",
    "Robert the Bruce": "icons/Robert_the_Bruce_29.webp",
    "Saladin (Sultan)": "icons/Saladin_29_29.webp",
    "Saladin (Vizier)": "icons/Saladin_29.webp",
    "Sejong": "icons/Sejong_29.webp",
    "Seondeok": "icons/Seondeok_29.webp",
    "Shaka": "icons/Shaka_29.webp",
    "Simón Bolívar": "icons/Sim3Fvar_29.webp",
    "Suleiman (Kanuni)": "icons/Suleiman_29.webp",
    "Suleiman (Muhteşem)": "icons/Suleiman_3Fem28Civ6%29.webp",
    "Sundiata Keita": "icons/Sundiata_Keita_29.webp",
    "Tamar": "icons/Tamar_29.webp",
    "Teddy Roosevelt (Rough Rider)": "icons/Teddy_Roosevelt_29_29.webp",
    "Teddy Roosevelt (Bull Moose)": "icons/Teddy_Roosevelt_29.webp",
    "Theodora": "icons/Theodora_29.webp",
    "Tokugawa": "icons/Tokugawa_29.webp",
    "Tomyris": "icons/Tomyris_29.webp",
    "Trajan": "icons/Trajan_29.webp",
    "Victoria (Age of Empire)": "icons/Victoria_29.webp",
    "Victoria (Age of Steam)": "icons/Victoria_29_29.webp",
    "Wilfrid Laurier": "icons/Wilfrid_Laurier_29.webp",
    "Wilhelmina": "icons/Wilhelmina_29.webp",
    "Wu Zetian": "icons/Wu_Zetian_29.webp",
    "Yongle": "icons/Yongle_29.webp"
}

a_to_c_mapping = {
    "Kupe": "Kupe_(Civ6)?file=Kupe_%28Civ6%29.png",
    "Chandragupta": "Chandragupta_(Civ6)?file=Chandragupta_%28Civ6%29.png",
    "Dido": "Dido_(Civ6)?file=Dido_%28Civ6%29.png",
    "Peter": "Peter_(Civ6)?file=Peter_%28Civ6%29.png",
    "Simón Bolívar": "Sim%C3%B3n_Bol%C3%ADvar_(Civ6)?file=Sim%C3%B3n_Bol%C3%ADvar_%28Civ6%29.png",
    "Harald Hardrada (Varangian)": "Harald_Hardrada_(Civ6)?file=Harald_Hardrada_%28Civ6%29.png",
    "Victoria (Age of Steam)": "Victoria_(Civ6)?file=Victoria_%28Civ6%29.png",
    "Kublai Khan (Mongolian)": "Kublai_Khan_(Civ6)?file=Kublai_Khan_%28Civ6%29.png",
    "Julius Caesar": "Julius_Caesar_(Civ6)?file=Julius_Caesar_%28Civ6%29.png",
    "Harald Hardrada (Konge)": "Harald_Hardrada_(Civ6)?file=Harald_Hardrada_%28Civ6%29.png",
    "Ambiorix": "Ambiorix_(Civ6)?file=Ambiorix_%28Civ6%29.png",
    "Hammurabi": "Hammurabi_(Civ6)?file=Hammurabi_%28Civ6%29.png",
    "Menelik II": "Menelik_II_(Civ6)?file=Menelik_II_%28Civ6%29.png",
    "Philip II": "Philip_II_(Civ6)?file=Philip_II_%28Civ6%29.png",
    "Wu Zetian": "Wu_Zetian_(Civ6)?file=Wu_Zetian_%28Civ6%29.png",
    "Eleanor of Aquitaine (English)": "Eleanor_of_Aquitaine_(Civ6)?file=Eleanor_of_Aquitaine_%28Civ6%29.png",
    "Tamar": "Tamar_(Civ6)?file=Tamar_%28Civ6%29.png",
    "Ludwig II": "Ludwig_II_(Civ6)?file=Ludwig_II_%28Civ6%29.png",
    "Eleanor of Aquitaine (French)": "Eleanor_of_Aquitaine_(Civ6)?file=Eleanor_of_Aquitaine_%28Civ6%29.png",
    "Saladin (Vizier)": "Saladin_(Civ6)?file=Saladin_%28Civ6%29.png",
    "Gilgamesh": "Gilgamesh_(Civ6)?file=Gilgamesh_%28Civ6%29.png",
    "Elizabeth I": "Elizabeth_I_(Civ6)?file=Elizabeth_I_%28Civ6%29.png",
    "Theodora": "Theodora_(Civ6)?file=Theodora_%28Civ6%29.png",
    "Jayavarman VII": "Jayavarman_VII_(Civ6)?file=Jayavarman_VII_%28Civ6%29.png",
    "Gandhi": "Gandhi_(Civ6)?file=Gandhi_%28Civ6%29.png",
    "Jadwiga": "Jadwiga_(Civ6)?file=Jadwiga_%28Civ6%29.png",
    "Montezuma": "Montezuma_(Civ6)?file=Montezuma_%28Civ6%29.png",
    "João III": "Jo%C3%A3o_III_(Civ6)?file=Jo%C3%A3o_III_%28Civ6%29.png",
    "Victoria (Age of Empire)": "Victoria_(Civ6)?file=Victoria_%28Civ6%29.png",
    "Suleiman (Muhteşem)": "Suleiman_(Civ6)?file=Suleiman_%28Civ6%29.png",
    "Matthias Corvinus": "Matthias_Corvinus_(Civ6)?file=Matthias_Corvinus_%28Civ6%29.png",
    "Tokugawa": "Tokugawa_(Civ6)?file=Tokugawa_%28Civ6%29.png",
    "Sundiata Keita": "Sundiata_Keita_(Civ6)?file=Sundiata_Keita_%28Civ6%29.png",
    "Cleopatra (Ptolemaic)": "Cleopatra_(Civ6)?file=Cleopatra_%28Civ6%29.png",
    "Cyrus": "Cyrus_(Civ6)?file=Cyrus_%28Civ6%29.png",
    "Poundmaker": "Poundmaker_(Civ6)?file=Poundmaker_%28Civ6%29.png",
    "Hojo Tokimune": "Hojo_Tokimune_(Civ6)?file=Hojo_Tokimune_%28Civ6%29.png",
    "Ramses II": "Ramses_II_(Civ6)?file=Ramses_II_%28Civ6%29.png",
    "Pedro II": "Pedro_II_(Civ6)?file=Pedro_II_%28Civ6%29.png",
    "Shaka": "Shaka_(Civ6)?file=Shaka_%28Civ6%29.png",
    "Kublai Khan (Chinese)": "Kublai_Khan_(Civ6)?file=Kublai_Khan_%28Civ6%29.png",
    "Frederick Barbarossa": "Frederick_Barbarossa_(Civ6)?file=Frederick_Barbarossa_%28Civ6%29.png",
    "Pericles": "Pericles_(Civ6)?file=Pericles_%28Civ6%29.png",
    "Lady Six Sky": "Lady_Six_Sky_(Civ6)?file=Lady_Six_Sky_%28Civ6%29.png",
    "Gorgo": "Gorgo_(Civ6)?file=Gorgo_%28Civ6%29.png",
    "Trajan": "Trajan_(Civ6)?file=Trajan_%28Civ6%29.png",
    "Wilhelmina": "Wilhelmina_(Civ6)?file=Wilhelmina_%28Civ6%29.png",
    "Nzinga Mbande": "Nzinga_Mbande_(Civ6)?file=Nzinga_Mbande_%28Civ6%29.png",
    "Wilfrid Laurier": "Wilfrid_Laurier_(Civ6)?file=Wilfrid_Laurier_%28Civ6%29.png",
    "Abraham Lincoln": "Abraham_Lincoln_(Civ6)?file=Abraham_Lincoln_%28Civ6%29.png",
    "Seondeok": "Seondeok_(Civ6)?file=Seondeok_%28Civ6%29.png",
    "Basil II": "Basil_II_(Civ6)?file=Basil_II_%28Civ6%29.png",
    "Bà Triệu": "B%C3%A0_Tri%E1%BB%87u_(Civ6)?file=B%C3%A0_Tri%E1%BB%87u_%28Civ6%29.png",
    "Suleiman (Kanuni)": "Suleiman_(Civ6)?file=Suleiman_%28Civ6%29.png",
    "Catherine de Medici (Magnificence)": "Catherine_de_Medici_(Civ6)?file=Catherine_de_Medici_%28Civ6%29.png",
    "Robert the Bruce": "Robert_the_Bruce_(Civ6)?file=Robert_the_Bruce_%28Civ6%29.png",
    "Qin Shi Huang (Mandate of Heaven)": "Qin_Shi_Huang_(Civ6)?file=Qin_Shi_Huang_%28Civ6%29.png",
    "Genghis Khan": "Genghis_Khan_(Civ6)?file=Genghis_Khan_%28Civ6%29.png",
    "Yongle": "Yongle_(Civ6)?file=Yongle_%28Civ6%29.png",
    "Saladin (Sultan)": "Saladin_(Civ6)?file=Saladin_%28Civ6%29.png",
    "Amanitore": "Amanitore_(Civ6)?file=Amanitore_%28Civ6%29.png",
    "Gitarja": "Gitarja_(Civ6)?file=Gitarja_%28Civ6%29.png",
    "Kristina": "Kristina_(Civ6)?file=Kristina_%28Civ6%29.png",
    "Teddy Roosevelt (Rough Rider)": "Teddy_Roosevelt_(Civ6)?file=Teddy_Roosevelt_%28Civ6%29.png",
    "Mansa Musa": "Mansa_Musa_(Civ6)?file=Mansa_Musa_%28Civ6%29.png",
    "Teddy Roosevelt (Bull Moose)": "Teddy_Roosevelt_(Civ6)?file=Teddy_Roosevelt_%28Civ6%29.png",
    "Nader Shah": "Nader_Shah_(Civ6)?file=Nader_Shah_%28Civ6%29.png",
    "Lautaro": "Lautaro_(Civ6)?file=Lautaro_%28Civ6%29.png",
    "Sejong": "Sejong_(Civ6)?file=Sejong_%28Civ6%29.png",
    "Alexander": "Alexander_(Civ6)?file=Alexander_%28Civ6%29.png",
    "Pachacuti": "Pachacuti_(Civ6)?file=Pachacuti_%28Civ6%29.png",
    "Catherine de Medici (Black Queen)": "Catherine_de_Medici_(Civ6)?file=Catherine_de_Medici_%28Civ6%29.png",
    "Tomyris": "Tomyris_(Civ6)?file=Tomyris_%28Civ6%29.png",
    "John Curtin": "John_Curtin_(Civ6)?file=John_Curtin_%28Civ6%29.png",
}

x_to_a_mapping = {
    "Maori": "Kupe",
    "Chandragupta": "Chandragupta",
    "Phoenicia": "Dido",
    "Russia": "Peter",
    "Gran-Colombia": "Simón Bolívar",
    "Harald-Varangian": "Harald Hardrada (Varangian)",
    "Victoria age of steam": "Victoria (Age of Steam)",
    "Kublai-Mongolia": "Kublai Khan (Mongolian)",
    "Julius-Caesar": "Julius Caesar",
    "Norway": "Harald Hardrada (Konge)",  # (Different variant of Harald)
    "Gaul": "Ambiorix",
    "Babylon": "Hammurabi",
    "Ethiopia": "Menelik II",
    "Spain": "Philip II",
    "Wu-Zetian": "Wu Zetian",
    "Eleanor-En": "Eleanor of Aquitaine (English)",
    "Georgia": "Tamar",
    "Ludwig": "Ludwig II",
    "Eleanor-Fr": "Eleanor of Aquitaine (French)",
    "Saladin-Vizier": "Saladin (Vizier)",
    "Sumeria": "Gilgamesh",
    "ElizabethI": "Elizabeth I",
    "Theodora": "Theodora",
    "Khmer": "Jayavarman VII",
    "Gandhi": "Gandhi",
    "Poland": "Jadwiga",
    "Aztec": "Montezuma",
    "Portugal": "João III",
    "Victoria": "Victoria (Age of Empire)",
    "Suleiman-Muhtesem": "Suleiman (Muhteşem)",
    "Hungary": "Matthias Corvinus",
    "Tokugawa": "Tokugawa",
    "Sundiata-Keita": "Sundiata Keita",
    "Ptolemaic-Cleopatra": "Cleopatra (Ptolemaic)",
    "Persia": "Cyrus",
    "Cree": "Poundmaker",
    "Hojo-Tokimune": "Hojo Tokimune",
    "Egypt": "Cleopatra (Egyptian)",  # Alternate: Cleopatra (Egyptian)
    "Brazil": "Pedro II",
    "Zulu": "Shaka",
    "Kublai-China": "Kublai Khan (Chinese)",
    "Germany": "Frederick Barbarossa",
    "Pericles": "Pericles",
    "Maya": "Lady Six Sky",
    "Gorgo": "Gorgo",
    "Rome": "Trajan",
    "Netherlands": "Wilhelmina",
    "Ramses": "Ramses II",
    "Qin-Unifier": "Qin Shi Huang (Unifier)",
    "Mbande": "Nzinga Mbande",
    "Canada": "Wilfrid Laurier",
    "Abraham-Lincoln": "Abraham Lincoln",
    "Korea": "Seondeok",  # Sejong is the other Korea leader
    "Byzantium": "Basil II",  # Theodora is another Byzantium leader
    "Vietnam": "Bà Triệu",
    "Suleiman-Kanuni": "Suleiman (Kanuni)",
    "Catherine-Magnificence": "Catherine de Medici (Magnificence)",
    "Mvemba-a-Nzinga": "Mvemba a Nzinga",
    "Scotland": "Robert the Bruce",
    "Qin-Mandate-of-Heaven": "Qin Shi Huang (Mandate of Heaven)",
    "Genghis-Khan": "Genghis Khan",
    "Yongle": "Yongle",
    "Saladin-Sultan": "Saladin (Sultan)",
    "Nubia": "Amanitore",
    "Indonesia": "Gitarja",
    "Sweden": "Kristina",
    "Teddy-RR": "Teddy Roosevelt (Rough Rider)",
    "Mali": "Mansa Musa",
    "Teddy-BM": "Teddy Roosevelt (Bull Moose)",
    "Nader-Shah": "Nader Shah",
    "Mapuche": "Lautaro",
    "Sejong": "Sejong",
    "Macedon": "Alexander",
    "Inca": "Pachacuti",
    "Catherine-BQ": "Catherine de Medici (Black Queen)",
    "Scythia": "Tomyris",
    "Australia": "John Curtin"
}

def get_icon_url(leader_name):
    # Return the local path from the A -> D mapping
    #print(a_to_d_mapping.get(leader_name, ""))
    return a_to_d_mapping.get(leader_name, "")

def load_data(filename):
    # Replace this with the actual path to your Excel file
    df = pd.read_excel(filename)
    return df


# Monthly Stats Route
@app.route('/')
@app.route('/monthly_stats')
def show_monthly_stats():
    # Load the data from your Excel file or database
    df = load_data('data/processed_data.xlsx')

    # Update Civilization Leader names using X -> A mapping
    df['Civilization Leader'] = df['Civilization Leader'].apply(lambda x: x_to_a_mapping.get(x, x))
    
    # Add a column for icon URLs using the A -> D mapping
    df['Icon URL'] = df['Civilization Leader'].apply(get_icon_url)

    # Convert DataFrame to a list of dictionaries (rows) for rendering
    data = df.to_dict(orient='records')

    # Render the HTML with the data passed directly
    return render_template('index.html', data=data)

# Top 100 Route
@app.route('/top100')
def show_top100_stats():
    # Load the data from your Excel file or database
    df = load_data('data/top100_data.xlsx')

    # Update Civilization Leader names using X -> A mapping
    df['Civilization Leader'] = df['Civilization Leader'].apply(lambda x: x_to_a_mapping.get(x, x))
    
    # Add a column for icon URLs using the A -> D mapping
    df['Icon URL'] = df['Civilization Leader'].apply(get_icon_url)

    # Convert DataFrame to a list of dictionaries (rows) for rendering
    data = df.to_dict(orient='records')

    # Render the HTML with the data passed directly
    return render_template('top100.html', data=data)


# Easy Lobby Route (Pro Players)
@app.route('/easy-lobby')
def show_easy_lobby_stats():
    # Load the data from your Excel file or database
    df = load_data('data/easyL.xlsx')

    # Update Civilization Leader names using X -> A mapping
    df['Civilization Leader'] = df['Civilization Leader'].apply(lambda x: x_to_a_mapping.get(x, x))
    
    # Add a column for icon URLs using the A -> D mapping
    df['Icon URL'] = df['Civilization Leader'].apply(get_icon_url)

    # Convert DataFrame to a list of dictionaries (rows) for rendering
    data = df.to_dict(orient='records')

    # Render the HTML with the data passed directly
    return render_template('easy_lobby.html', data=data)

# Hard Lobby Route (Noob Players)
@app.route('/hard-lobby')
def show_hard_lobby_stats():
    # Load the data from your Excel file or database
    df = load_data('data/hardL.xlsx')

    # Update Civilization Leader names using X -> A mapping
    df['Civilization Leader'] = df['Civilization Leader'].apply(lambda x: x_to_a_mapping.get(x, x))
    
    # Add a column for icon URLs using the A -> D mapping
    df['Icon URL'] = df['Civilization Leader'].apply(get_icon_url)

    # Convert DataFrame to a list of dictionaries (rows) for rendering
    data = df.to_dict(orient='records')

    # Render the HTML with the data passed directly
    return render_template('hard_lobby.html', data=data)

# Hard Lobby Route (Noob Players)
@app.route('/teamers')
def show_teamers_stats():
    # Load the data from your Excel file or database
    df = load_data('data/teamers_data.xlsx')

    # Update Civilization Leader names using X -> A mapping
    df['Civilization Leader'] = df['Civilization Leader'].apply(lambda x: x_to_a_mapping.get(x, x))
    
    # Add a column for icon URLs using the A -> D mapping
    df['Icon URL'] = df['Civilization Leader'].apply(get_icon_url)

    # Convert DataFrame to a list of dictionaries (rows) for rendering
    data = df.to_dict(orient='records')

    # Render the HTML with the data passed directly
    return render_template('teamers.html', data=data)

# About Page Route
@app.route('/about')
def show_about_page():
    return render_template('about.html', title="About", description="All data are from CivPlayers Leagues.")

if __name__ == '__main__':
    app.run(debug=True)