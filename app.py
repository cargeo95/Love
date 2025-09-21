from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# --- App ---
app = Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.FLATLY,
        "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css",
    ],
)
server = app.server

# --- CSS embebido ---
extra_css = dcc.Markdown(
    """
    <style>
      /* Fondo sutil */
      .hero-bg {
        background: linear-gradient(135deg, #f8fbff 0%, #eef5ff 50%, #e9f7f2 100%);
      }

      /* Tarjeta con presencia visual */
      .soft-card {
        border: 1px solid #e9ecef;
        border-radius: 16px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.06);
        transition: transform .2s ease, box-shadow .2s ease;
        min-width: 280px;     /* tamaño mínimo cómodo */
        min-height: 210px;    /* altura mínima */
      }
      .soft-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 26px rgba(0,0,0,0.10);
      }

      /* Tipografía de los cards */
      .soft-card h3 {
        font-size: 1.8rem;
        letter-spacing: .2px;
      }
      .soft-card p {
        font-size: 1.02rem;
      }

      /* Iconos dentro del card */
      .soft-card i {
        font-size: 2rem;      /* agranda iconos */
      }

      /* Signos de la ecuación */
      .eq-sign {
        font-weight: 700;
        line-height: 1;
        font-size: 2.2rem;
      }

      /* Footer fino */
      .footer {
        border-top: 1px solid #e9ecef;
      }

      /* Espaciado vertical entre filas */
      .equation-wrap {
        max-width: 1200px; /* limita ancho total para que no se disperse */
      }
    </style>
    """,
    dangerously_allow_html=True
)

# --- Hero ---
hero = dbc.Container(
    [
        html.Div(
            [
                html.H1("Tú + Yo + Digital = Nosotros", className="display-6 text-center mb-3"),
                html.P(
                    "Una ecuación sencilla, un hogar infinito.",
                    className="lead text-center text-muted mb-0",
                ),
            ],
            className="py-5"
        )
    ],
    fluid=True,
    class_name="hero-bg"
)

# --- Cards ---
card_tu = dbc.Card(
    dbc.CardBody(
        [
            html.Div(html.I(className="bi bi-heart-fill text-primary")),
            html.H3("Tú…", className="mt-3 mb-2 text-center"),
            html.Hr(className="my-2"),
            html.P("La mejor psicóloga del mundo", className="text-center mb-0"),
        ]
    ),
    class_name="text-center h-100 soft-card",
)

card_yo = dbc.Card(
    dbc.CardBody(
        [
            html.Div(html.I(className="bi bi-cpu-fill text-success")),
            html.H3("Yo…", className="mt-3 mb-2 text-center"),
            html.Hr(    className="my-2"),
            html.P("Un ingeniero", className="text-center mb-0"),
        ]
    ),
    class_name="text-center h-100 soft-card",
)

card_digital = dbc.Card(
    dbc.CardBody(
        [
            html.Div(html.I(className="bi bi-emoji-smile-fill text-warning")),
            html.H3("Digital", className="mt-3 mb-2 text-center"),
            html.Hr(className="my-2"),
            html.P("Nuestro hijo", className="text-center mb-0"),
        ]
    ),
    class_name="text-center h-100 soft-card",
)

card_nosotros = dbc.Card(
    dbc.CardBody(
        [
            html.Div(html.I(className="bi bi-house-heart-fill text-danger")),
            html.H3("Nosotros…", className="mt-3 mb-2 text-center"),
            html.Hr(className="my-2"),
            html.P("Nuestro hogar", className="text-center mb-0"),
        ]
    ),
    class_name="text-center h-100 soft-card",
)

# --- Fila superior (Tú + Yo + Digital) ---
equation_row_top = dbc.Row(
    [
        dbc.Col(card_tu, xs=12, md=3, class_name="mb-3"),
        dbc.Col(html.Div("+", className="eq-sign text-center my-3"), width="auto"),
        dbc.Col(card_yo, xs=12, md=3, class_name="mb-3"),
        dbc.Col(html.Div("+", className="eq-sign text-center my-3"), width="auto"),
        dbc.Col(card_digital, xs=12, md=3, class_name="mb-3"),
    ],
    class_name="align-items-center g-3 justify-content-center text-center"
)

# --- Fila inferior (= Nosotros) ---
equation_row_bottom = dbc.Row(
    [
        dbc.Col(html.Div("=", className="eq-sign text-center my-3"), width="auto"),
        dbc.Col(card_nosotros, xs=12, md=4, lg=5, class_name="mb-3"),
    ],
    class_name="align-items-center g-3 justify-content-center text-center"
)

# --- Footer ---
footer = html.Footer(
    dbc.Container(
        [
            html.P("© 2025 — Hecho con amor", className="text-center text-muted small mb-0"),
        ],
        class_name="py-4"
    ),
    className="footer"
)

# --- Layout ---
app.layout = html.Div(
    [
        extra_css,
        hero,
        dbc.Container(
            [
                dbc.Row(
                    dbc.Col(
                        [
                            equation_row_top,
                            html.Div(style={"height": "18px"}),  # separador sutil
                            equation_row_bottom,
                        ],
                        width=12,
                        class_name="equation-wrap mx-auto"
                    ),
                    class_name="justify-content-center"
                ),
            ],
            class_name="py-5"
        ),
        footer,
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
