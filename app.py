from dash import Dash, html
import dash_bootstrap_components as dbc


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server



app.layout = dbc.Container([
    html.Br(),
    dbc.Row([
        
        # Columna izquierda - "Tú"
        dbc.Col([
            html.H1("Tú...", style={'textAlign': 'center'}),
            html.Hr(),
            html.H4("La mejor psicologa del mundo", style={'textAlign': 'center'}),
        ], width=3),  # Ajusta el ancho de la columna según sea necesario
        
        # Columna central - "Nosotros"
        dbc.Col([
            html.Br(),
            html.H1("+", style={'textAlign': 'center'}),
        ], width=1),  # Ajusta el ancho de la columna según sea necesario


        # Columna central - "Nosotros"
        dbc.Col([
            html.H1("Yo...", style={'textAlign': 'center'}),
            html.Hr(),
            html.H4("Un ingeniero", style={'textAlign': 'center'}),
        ], width=3),  # Ajusta el ancho de la columna según sea necesario
        
        # Columna central - "Nosotros"
        dbc.Col([
            html.Br(),
            html.H1("+", style={'textAlign': 'center'}),
        ], width=1),  # Ajusta el ancho de la columna según sea necesario


        # Columna derecha - "Yo"
        dbc.Col([
            html.H1("Nosotros...", style={'textAlign': 'center'}),
            html.Hr(),
            html.H4("El mejor team del mundo", style={'textAlign': 'center'}),
        ], width=4),  # Ajusta el ancho de la columna según sea necesario
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)