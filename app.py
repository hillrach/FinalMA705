
import pandas as pd
import dash
from dash import dcc
from dash import html
from dash import dash_table as dt
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import collections

infosport = pd.read_pickle('/Users/rachelhill/Desktop/infosport.pkl')
infoevent = pd.read_pickle('/Users/rachelhill/Desktop/infoevent.pkl')
olympics = pd.read_pickle('/Users/rachelhill/Desktop/olympics.pkl')

olympics_US =  olympics[olympics['NOC']=='USA']

olym_ser = olympics.drop(columns=['Code', 'Gender', 'Discipline', 'Medal', 'Unnamed: 0', 'Gold', 'Silver', 'Bronze', 'Name', 'Age', 'Rank', 'Country', 'NOC'])
olym_dict = {} 
for i in olym_ser["Sport"].unique():
    olym_dict[i] = [olym_ser["Event"][j] for j in olym_ser[olym_ser["Sport"]==i].index]
olym_dict = { key : list(set(value)) for key, value in olym_dict.items()}
    

stylesheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#Olympics to html table
def olympics_table(olympics, max_rows=20000):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in olympics.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(olympics.iloc[i][col]) for col in olympics.columns
            ]) for i in range(min(len(olympics), max_rows))
        ])
    ])

#Olympics_US to html table
def olympics_US_table(olympics_US, max_rows=20000):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in olympics_US.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(olympics_US.iloc[i][col]) for col in olympics_US.columns
            ]) for i in range(min(len(olympics_US), max_rows))
        ])
    ])

#Infosport to html table
def infosport_table(infosport, max_rows=46):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in infosport.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(infosport.iloc[i][col]) for col in infosport.columns
            ]) for i in range(min(len(infosport), max_rows))
        ])
    ])

#Infoevent to html table
def infoevent_table(infoevent, max_rows=500):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in infoevent.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(infoevent.iloc[i][col]) for col in infoevent.columns
            ]) for i in range(min(len(infoevent), max_rows))
        ])
    ])

app = dash.Dash(__name__, external_stylesheets=stylesheet)


all_options = {'Cycling Road': ["Cycling Road: Women's Individual Time Trial", "Cycling Road: Men's Road Race", "Cycling Road: Women's Road Race", "Cycling Road: Men's Individual Time Trial"], 'Artistic Gymnastics': ["Artistic Gymnastics: Men's Floor Exercise", "Artistic Gymnastics: Women's All-Around", "Artistic Gymnastics: Men's Pommel Horse", "Artistic Gymnastics: Women's Vault", "Artistic Gymnastics: Women's Floor Exercise", "Artistic Gymnastics: Men's Horizontal Bar", "Artistic Gymnastics: Men's Team", "Artistic Gymnastics: Men's Parallel Bars", "Artistic Gymnastics: Men's Vault", "Artistic Gymnastics: Men's Rings", "Artistic Gymnastics: Women's Uneven Bars", "Artistic Gymnastics: Women's Team", "Artistic Gymnastics: Women's Balance Beam", "Artistic Gymnastics: Men's All-Around"], 'Rowing': ["Rowing: Women's Four Team", "Rowing: Lightweight Men's Double Sculls Team", "Rowing: Women's Single Sculls", "Rowing: Men's Single Sculls", "Rowing: Women's Quadruple Sculls Team", "Rowing: Women's Pair Team", "Rowing: Men's Eight Team", "Rowing: Men's Double Sculls Team", "Rowing: Men's Four Team", "Rowing: Women's Eight Team", "Rowing: Lightweight Women's Double Sculls Team", "Rowing: Men's Quadruple Sculls Team", "Rowing: Men's Pair Team", "Rowing: Women's Double Sculls Team"], 'Basketball': ['Basketball: Men Team', 'Basketball: Women Team'], 'Handball': ['Handball: Men Team', 'Handball: Women Team'], 'Swimming': ["Swimming: Women's 200m Freestyle", "Swimming: Men's 100m Butterfly", "Swimming: Men's 1500m Freestyle", "Swimming: Women's 200m Backstroke", "Swimming: Men's 200m Breaststroke", "Swimming: Women's 400m Individual Medley", "Swimming: Women's 200m Individual Medley", "Swimming: Women's 100m Freestyle", "Swimming: Women's 100m Butterfly", "Swimming: Men's 100m Breaststroke", "Swimming: Men's 4 x 100m Medley Relay Team", "Swimming: Men's 4 x 200m Freestyle Relay Team", "Swimming: Men's 400m Freestyle", "Swimming: Men's 200m Individual Medley", 'Swimming: Mixed 4 x 100m Medley Relay Team', "Swimming: Men's 100m Freestyle", "Swimming: Men's 100m Backstroke", "Swimming: Women's 4 x 100m Freestyle Relay Team", "Swimming: Women's 100m Breaststroke", "Swimming: Women's 4 x 200m Freestyle Relay Team", "Swimming: Women's 200m Breaststroke", "Swimming: Women's 400m Freestyle", "Swimming: Women's 200m Butterfly", "Swimming: Women's 4 x 100m Medley Relay Team", "Swimming: Men's 200m Backstroke", "Swimming: Men's 200m Butterfly", "Swimming: Women's 800m Freestyle", "Swimming: Men's 4 x 100m Freestyle Relay Team", "Swimming: Women's 50m Freestyle", "Swimming: Women's 1500m Freestyle", "Swimming: Women's 100m Backstroke", "Swimming: Men's 50m Freestyle", "Swimming: Men's 400m Individual Medley", "Swimming: Men's 200m Freestyle", "Swimming: Men's 800m Freestyle"], 'Karate': ["Karate: Men's Kumite -67kg", "Karate: Men's Kumite -75kg", "Karate: Women's Kumite -55kg", "Karate: Women's Kata", "Karate: Women's Kumite -61kg", "Karate: Men's Kata", "Karate: Men's Kumite +75kg", "Karate: Women's Kumite +61kg"], 'Wrestling': ["Wrestling: Men's Freestyle 86kg", "Wrestling: Men's Freestyle 57kg", "Wrestling: Men's Greco-Roman 97kg", "Wrestling: Women's Freestyle 50kg", "Wrestling: Men's Greco-Roman 87kg", "Wrestling: Men's Greco-Roman 130kg", "Wrestling: Men's Greco-Roman 67kg", "Wrestling: Women's Freestyle 68kg", "Wrestling: Men's Greco-Roman 77kg", "Wrestling: Men's Freestyle 74kg", "Wrestling: Men's Greco-Roman 60kg", "Wrestling: Men's Freestyle 125kg", "Wrestling: Women's Freestyle 76kg", "Wrestling: Women's Freestyle 62kg", "Wrestling: Women's Freestyle 53kg", "Wrestling: Women's Freestyle 57kg", "Wrestling: Men's Freestyle 65kg", "Wrestling: Men's Freestyle 97kg"], 'Rhythmic Gymnastics': ['Rhythmic Gymnastics: Individual All-Around', 'Rhythmic Gymnastics: Group All-Around Team'], 'Baseball/Softball': ['Baseball/Softball: Baseball Team', 'Baseball/Softball: Softball Team'], 'Athletics': ["Athletics: Men's 10,000m", "Athletics: Women's Pole Vault", "Athletics: Men's Long Jump", "Athletics: Women's 400m Hurdles", "Athletics: Men's 400m Hurdles", "Athletics: Men's 4 x 100m Relay Team", "Athletics: Men's 400m", "Athletics: Men's 800m", "Athletics: Women's Long Jump", "Athletics: Women's 4 x 400m Relay Team", "Athletics: Women's 5000m", "Athletics: Women's 200m", "Athletics: Men's 3000m Steeplechase", "Athletics: Men's High Jump", "Athletics: Women's 20km Race Walk", "Athletics: Women's Heptathlon", "Athletics: Men's 110m Hurdles", "Athletics: Women's 100m", "Athletics: Women's Triple Jump", "Athletics: Women's 10,000m", "Athletics: Women's Discus Throw", "Athletics: Men's 20km Race Walk", "Athletics: Women's 800m", "Athletics: Women's 1500m", "Athletics: Men's Hammer Throw", "Athletics: Men's 5000m", "Athletics: Women's Hammer Throw", "Athletics: Women's 4 x 100m Relay", "Athletics: Men's Decathlon", 'Athletics: 4 x 400m Relay Mixed', "Athletics: Women's Javelin Throw", "Athletics: Men's 4 x 100m Relay", 'Athletics: 4 x 400m Relay Mixed Team', "Athletics: Men's 1500m", "Athletics: Men's 4 x 400m Relay Team", "Athletics: Women's 400m", "Athletics: Women's Shot Put", "Athletics: Men's 200m", "Athletics: Men's Javelin Throw", "Athletics: Men's Marathon", "Athletics: Men's Triple Jump", "Athletics: Women's Marathon", "Athletics: Men's Discus Throw", "Athletics: Women's High Jump", "Athletics: Women's 4 x 400m Relay", "Athletics: Men's Shot Put", "Athletics: Women's 3000m Steeplechase", "Athletics: Men's 50km Race Walk", "Athletics: Women's 100m Hurdles", "Athletics: Men's Pole Vault", "Athletics: Men's 100m", "Athletics: Women's 4 x 100m Relay Team", "Athletics: Men's 4 x 400m Relay"], 'Judo': ['Judo: Men +100 kg', 'Judo: Women -63 kg', 'Judo: Women -70 kg', 'Judo: Men -81 kg', 'Judo: Mixed Team', 'Judo: Men -73 kg', 'Judo: Men -60 kg', 'Judo: Men -66 kg', 'Judo: Women -78 kg', 'Judo: Women -48 kg', 'Judo: Men -100 kg', 'Judo: Women -57 kg', 'Judo: Women +78 kg', 'Judo: Men -90 kg', 'Judo: Women -52 kg'], 'Shooting': ['Shooting: 10m Air Pistol Mixed Team', 'Shooting: 10m Air Rifle Men', 'Shooting: 25m Pistol Women', 'Shooting: 10m Air Rifle Mixed Team', 'Shooting: Trap Women', 'Shooting: 50m Rifle 3 Positions Men', 'Shooting: Skeet Men', 'Shooting: Trap Men', 'Shooting: 10m Air Pistol Women', 'Shooting: 10m Air Pistol Men', 'Shooting: Skeet Women', 'Shooting: 50m Rifle 3 Positions Women', 'Shooting: 10m Air Rifle Women', 'Shooting: 25m Rapid Fire Pistol Men', 'Shooting: Trap Mixed Team'], 'Table Tennis': ['Table Tennis: Mixed Doubles Team', "Table Tennis: Women's Team", "Table Tennis: Women's Singles", "Table Tennis: Men's Team", "Table Tennis: Men's Singles"], 'Football': ['Football: Men Team', 'Football: Women Team'], 'Taekwondo': ['Taekwondo: Women -57kg', 'Taekwondo: Women -67kg', 'Taekwondo: Women -49kg', 'Taekwondo: Men -58kg', 'Taekwondo: Men -68kg', 'Taekwondo: Men -80kg', 'Taekwondo: Men +80kg', 'Taekwondo: Women +67kg'], 'Fencing': ["Fencing: Men's Foil Team", "Fencing: Men's Sabre Individual", "Fencing: Women's Sabre Team", "Fencing: Men's Épée Individual", "Fencing: Men's Foil Individual", "Fencing: Men's Sabre Team", "Fencing: Women's Épée Individual", "Fencing: Women's Épée Team", "Fencing: Women's Foil Individual", "Fencing: Men's Épée Team", "Fencing: Women's Sabre Individual", "Fencing: Women's Foil Team"], 'Badminton': ["Badminton: Women's Doubles Team", 'Badminton: Mixed Doubles Team', "Badminton: Men's Doubles Team", "Badminton: Women's Singles", "Badminton: Men's Singles"], 'Boxing': ["Boxing: Men's Middle (69-75kg)", "Boxing: Men's Super Heavy (+91kg)", "Boxing: Men's Fly (48-52kg)", "Boxing: Women's Middle (69-75kg)", "Boxing: Men's Light (57-63kg)", "Boxing: Women's Light (57-60kg)", "Boxing: Men's Heavy (81-91kg)", "Boxing: Men's Welter (63-69kg)", "Boxing: Men's Light Heavy (75-81kg)", "Boxing: Women's Feather (54-57kg)", "Boxing: Men's Feather (52-57kg)", "Boxing: Women's Welter (64-69kg)", "Boxing: Women's Fly (48-51kg)"], 'Weightlifting': ["Weightlifting: Men's 81kg", "Weightlifting: Men's 73kg", "Weightlifting: Women's 55kg", "Weightlifting: Women's 59kg", "Weightlifting: Women's 76kg", "Weightlifting: Men's 67kg", "Weightlifting: Men's +109kg", "Weightlifting: Men's 96kg", "Weightlifting: Women's 49kg", "Weightlifting: Men's 109kg", "Weightlifting: Women's 87kg", "Weightlifting: Men's 61kg", "Weightlifting: Women's 64kg", "Weightlifting: Women's +87kg"], 'Archery': ["Archery: Women's Individual", "Archery: Women's Team", 'Archery: Mixed Team', "Archery: Men's Team", "Archery: Men's Individual"], 'Diving': ["Diving: Men's Synchronised 10m Platform Team", "Diving: Men's 3m Springboard", "Diving: Women's Synchronised 10m Platform Team", "Diving: Men's Synchronised 3m Springboard Team", "Diving: Women's Synchronised 3m Springboard Team", "Diving: Women's 10m Platform", "Diving: Women's 3m Springboard", "Diving: Men's 10m Platform"], 'Beach Volleyball': ['Beach Volleyball: Men Team', 'Beach Volleyball: Women Team'], 'Sailing': ['Sailing: Mixed Multihull - Nacra 17 Foiling Team', "Sailing: Men's One Person Dinghy - Laser", "Sailing: Men's Windsurfer - RS:X", "Sailing: Men's Skiff - 49er Team", "Sailing: Women's One Person Dinghy - Laser Radial", "Sailing: Women's Skiff - 49er  Team", "Sailing: Women's Two Person Dinghy - 470 Team", "Sailing: Men's Two Person Dinghy - 470 Team", "Sailing: Men's One Person Dinghy (Heavyweight) - Finn", "Sailing: Women's Windsurfer - RS:X"], 'Hockey': ['Hockey: Women Team', 'Hockey: Men Team'], 'Trampoline Gymnastics': ['Trampoline Gymnastics: Men', 'Trampoline Gymnastics: Women'], 'Marathon Swimming': ["Marathon Swimming: Women's 10km", "Marathon Swimming: Men's 10km"], 'Triathlon': ["Triathlon: Women's Individual", 'Triathlon: Mixed Relay Team', "Triathlon: Men's Individual"], 'Canoe Slalom': ["Canoe Slalom: Men's Canoe", "Canoe Slalom: Women's Kayak", "Canoe Slalom: Women's Canoe", "Canoe Slalom: Men's Kayak"], 'Water Polo': ['Water Polo: Women Team', 'Water Polo: Men Team'], 'Surfing': ['Surfing: Women', 'Surfing: Men'], 'Canoe Sprint': ["Canoe Sprint: Men's Kayak Single 200m", "Canoe Sprint: Women's Kayak Single 500m", "Canoe Sprint: Women's Kayak Single 200m", "Canoe Sprint: Men's Canoe Double 1000m Team", "Canoe Sprint: Women's Kayak Double 500m Team", "Canoe Sprint: Men's Kayak Four 500m Team", "Canoe Sprint: Men's Canoe Single 1000m", "Canoe Sprint: Men's Kayak Single 1000m", "Canoe Sprint: Women's Kayak Four 500m Team", "Canoe Sprint: Women's Canoe Single 200m", "Canoe Sprint: Women's Canoe Double 500m Team", "Canoe Sprint: Men's Kayak Double 1000m Team"], 'Cycling BMX Racing': ['Cycling BMX Racing: Men', 'Cycling BMX Racing: Women'], 'Rugby': ['Rugby: Women Team', 'Rugby: Men Team'], 'Volleyball': ['Volleyball: Men Team', 'Volleyball: Women Team'], 'Equestrian': ['Equestrian: Dressage Individual', 'Equestrian: Jumping Individual', 'Equestrian: Dressage Team', 'Equestrian: Jumping Team', 'Equestrian: Eventing Individual', 'Equestrian: Eventing Team'], 'Tennis': ["Tennis: Women's Singles", 'Tennis: Mixed Doubles Team', "Tennis: Men's Singles", "Tennis: Men's Doubles Team", "Tennis: Women's Doubles Team"], 'Artistic Swimming': ['Artistic Swimming: Team', 'Artistic Swimming: Duet Team'], 'Cycling Track': ["Cycling Track: Men's Sprint", "Cycling Track: Men's Keirin", "Cycling Track: Men's Team Pursuit Team", "Cycling Track: Men's Omnium", "Cycling Track: Women's Keirin", "Cycling Track: Women's Madison", "Cycling Track: Women's Team Sprint Team", "Cycling Track: Women's Sprint", "Cycling Track: Women's Omnium", "Cycling Track: Women's Madison Team", "Cycling Track: Women's Team Pursuit Team", "Cycling Track: Men's Madison Team", "Cycling Track: Men's Team Sprint Team"], 'Golf': ["Golf: Women's Individual Stroke Play", "Golf: Men's Individual Stroke Play"], 'Skateboarding': ["Skateboarding: Men's Street", "Skateboarding: Women's Street", "Skateboarding: Men's Park", "Skateboarding: Women's Park"], 'Modern Pentathlon': ["Modern Pentathlon: Women's Individual", "Modern Pentathlon: Men's Individual"], 'Cycling Mountain Bike': ["Cycling Mountain Bike: Women's Cross-country", "Cycling Mountain Bike: Men's Cross-country"], '3x3 Basketball': ['3x3 Basketball: Men Team', '3x3 Basketball: Women Team'], 'Cycling BMX Freestyle': ["Cycling BMX Freestyle: Men's Park", "Cycling BMX Freestyle: Women's Park"], 'Sport Climbing': ["Sport Climbing: Men's Combined", "Sport Climbing: Women's Combined"]}
all_options = collections.OrderedDict(sorted(all_options.items()))


children_list = [
    html.Div(className='mat-card', style={"display": "block", "margin": "15px"},
        children=[html.H1(children="Tokyo 2020 Dashboard", style={'textAlign': 'left', 'color': 'gray', 'font-style': 'bold'}),
                  dcc.Markdown('''**MA705 Project | Rachel Hill**''')]),
    html.Hr(),
    html.Div(className='mat-card', style={"display": "block", "margin": "5px"},
         children=[html.H5("Sport and Event to Display:", style={'marginLeft': '1.5em', 'marginRight': '1.5em'}),
             html.Div([ 
                      dcc.Dropdown(
                        id='sports-dropdown', style={'marginBottom': '1.5em', 'marginLeft': '1.5em', 'marginRight': '1.5em'},
                        options=[{'label': k, 'value': k} for k in all_options.keys()],
                        value='Wrestling'),
                      dcc.Dropdown(id='events-dropdown', style={'marginBottom': '1.5em', 'marginLeft': '1.5em', 'marginRight': '1.5em'})]),
             html.Div(id='display-selected-values', 
                  style={'marginBottom': '1.5em', 'marginLeft': '2.5em', 'marginRight': '2.5em'})
             ]),
html.Div([
dcc.Tabs([
    dcc.Tab(label='All Medals', children=[
            html.Div([
                dcc.Graph(id="sports_plot", 
                          style={'marginBottom': '1.5em', 'marginLeft': '1.5em','height': 400})], 
                className="six columns"),
            html.Div([        
                dcc.Graph(id="events_plot", 
                          style={'marginBottom': '1.5em', 'marginRight': '1.5em', 'height': 400})],
                className="six columns")]),
    dcc.Tab(label='US Medals', children=[
            html.Div([
                dcc.Graph(id="US_sports_plot", 
                          style={'marginBottom': '1.5em', 'marginLeft': '1.5em','height': 400})
            ], className="six columns"),
            html.Div([
                dcc.Graph(id="US_events_plot",
                          style={'marginBottom': '1.5em', 'marginRight': '1.5em', 'height': 400})
            ], className="six columns")
            ], 
        ),
            ])
]),
    html.Div(className='mat-card', style={"display": "block", "margin": "15px"},
        children=[html.H5(children='Event Information Table:'),
            dt.DataTable(id='data-table',
                               style_cell={'textAlign': 'left', }, 
                               style_data={'color': 'black', 'backgroundColor': 'white', 'whiteSpace': 'normal', 'height': 'auto', 'lineHeight': '15px'},
                               sort_action="native", 
                               fixed_rows={'headers': True},
                               style_table={'height': 250},
                               style_header={'backgroundColor': 'rgb(210, 210, 210)','color': 'black','fontWeight': 'bold'},
                               style_cell_conditional=[
                                   {'if': {'column_id': 'SPORT'},'width': '100px'},
                                   {'if': {'column_id': 'EVENT'},'width': '170px'},
                                   {'if': {'column_id': 'NO. OF ATHLETES'},'width': '130px'},
                                   {'if': {'column_id': 'YOUNGEST ATHLETE AGE'},'width': '130px'},
                                   {'if': {'column_id': 'OLDEST ATHLETE AGE'},'width': '130px'},
                                   {'if': {'column_id': 'AVERAGE ATHLETE AGE'},'width': '130px'},
                                   {'if': {'column_id': 'NO. RANKED ATHLETES'},'width': '130px'},
                                   {'if': {'column_id': 'AVERAGE ATHLETE RANK'},'width': '130px'},],
                               columns=[{'id': c, 'name': c} for c in infoevent.columns.values]),
        html.Br(),
    html.Div(className='mat-card', style={"display": "block", "margin": "15px"},
        children=[html.H5(children='About this Dashboard:'),
                  dcc.Markdown('''This dashboard summarizes information from the Tokyo 2020 Olympics, 
                               specifically highlighting sports, events, and medal counts.'''),
                dcc.Markdown('''To use this dashboard: 
                             '''),
                dcc.Markdown('''
                             * Pick a sport and event 
                             * Graphs show the total medals given out of each color
                             * "All Medals" tab shows all medals awarded and "US Medals" tab shows only medals won by the United States
                             * Event Information Table gives more details about the athletes who competed in each event 
                             '''),
                  html.A("For more information on the Tokyo 2020 Olympics", href = "https://olympics.com/en/olympic-games/tokyo-2020", target="blank"),
                  html.Br(),
                  html.A("Source for athlete and medal information (csv file)", href = "https://www.kaggle.com/aliaamiri/2020-summer-olympics-dataset", target="blank"),
                  html.Br(),
                  html.A("Source for sports and event information (API)", href = "https://olypi.com", target="blank")
            ]),
        
        ])]

app.layout = html.Div(children=children_list)


#Populates events and sports dropdowns
@app.callback(Output('events-dropdown', 'options'),
              [Input('sports-dropdown', 'value')])
def set_events_options(selected_sport):
    return [{'label': i, 'value': i} for i in all_options[selected_sport]]

@app.callback(Output('events-dropdown', 'value'),
              [Input('events-dropdown', 'options')])
def set_events_value(available_options):
    return available_options[0]['value']

@app.callback(Output('display-selected-values', 'children'),
              [Input('sports-dropdown', 'value'),
              Input('events-dropdown', 'value')])
def set_display_children(selected_sport, selected_event):
    return u"{} is a great choice, take a look at some stats and visualizations!".format(
        selected_event)


#Populates table
@app.callback(Output('data-table', 'data'),
              [Input('sports-dropdown', 'value')])
def update_rows(selected_value):
    data = infoevent[infoevent['SPORT'] == selected_value]
    return data.to_dict('records')


#Populates sports plot
@app.callback(Output("sports_plot", "figure"),
              [Input("sports-dropdown", "value")],)
def update_sports(Sport):
    filtered_s1 = olympics[olympics["Sport"] == Sport]
    filtered_s2 = olympics[olympics["Sport"] == Sport]
    filtered_s3 = olympics[olympics["Sport"] == Sport]
    trace1 = go.Bar(
        x=filtered_s1["Sport"].unique(),
        y=filtered_s1.groupby("Sport")["Gold"].agg(sum),
        text=filtered_s1.groupby("Sport")["Gold"].agg(sum),
        textposition="outside",
        marker_color=px.colors.qualitative.Dark2[5],
        name="Gold", showlegend=False
    )
    trace2 = go.Bar(
        x=filtered_s2["Sport"].unique(),
        y=filtered_s2.groupby("Sport")["Silver"].agg(sum),
        text=filtered_s2.groupby("Sport")["Silver"].agg(sum),
        textposition="outside",
        marker_color=px.colors.qualitative.Dark2[7],
        name="Silver", showlegend=False
    )
    trace3 = go.Bar(
        x=filtered_s3["Sport"].unique(),
        y=filtered_s3.groupby("Sport")["Bronze"].agg(sum),
        text=filtered_s3.groupby("Sport")["Bronze"].agg(sum),
        textposition="outside",
        marker_color=px.colors.qualitative.Dark2[6],
        name="Bronze", showlegend=False
    )
    data = [trace1, trace2, trace3]
    layout = go.Layout(barmode="group", title="Medals Awarded by Sport")
    sports_plot = go.Figure(data=data, layout=layout)
    sports_plot.update_layout(
        title=dict(x=0.5),
        xaxis_title="Sport",
        yaxis_title="Total Medals",
        paper_bgcolor="aliceblue",
        margin=dict(l=20, r=20, t=60, b=20),
    )
    sports_plot.update_traces(texttemplate="%{text:.2s}")
    return sports_plot


#Populates events plot
@app.callback(Output("events_plot", "figure"),
              [Input("events-dropdown", "value")],)
def update_events(Event):
    filtered_s1 = olympics[olympics["Event"] == Event]
    filtered_s2 = olympics[olympics["Event"] == Event]
    filtered_s3 = olympics[olympics["Event"] == Event]
    trace1 = go.Bar(
        x=filtered_s1["Event"].unique(),
        y=filtered_s1.groupby("Event")["Gold"].agg(sum),
        text=filtered_s1.groupby("Event")["Gold"].agg(sum),
        textposition="outside",
        marker_color=px.colors.qualitative.Dark2[5],
        name="Gold",
    )
    trace2 = go.Bar(
        x=filtered_s2["Event"].unique(),
        y=filtered_s2.groupby("Event")["Silver"].agg(sum),
        text=filtered_s2.groupby("Event")["Silver"].agg(sum),
        textposition="outside",
        marker_color=px.colors.qualitative.Dark2[7],
        name="Silver",
    )
    trace3 = go.Bar(
        x=filtered_s3["Event"].unique(),
        y=filtered_s3.groupby("Event")["Bronze"].agg(sum),
        text=filtered_s3.groupby("Event")["Bronze"].agg(sum),
        textposition="outside",
        marker_color=px.colors.qualitative.Dark2[6],
        name="Bronze",
    )
    data = [trace1, trace2, trace3]
    layout = go.Layout(barmode="group", title="Medals Awarded by Event")
    events_plot = go.Figure(data=data, layout=layout)
    events_plot.update_layout(
        title=dict(x=0.5),
        xaxis_title="Event",
        yaxis_title="Total Medals",
        paper_bgcolor="aliceblue",
        margin=dict(l=20, r=20, t=60, b=20),
    )
    events_plot.update_traces(texttemplate="%{text:.2s}")
    return events_plot


#Populates US sports plot
@app.callback(Output("US_sports_plot", "figure"),
              [Input("sports-dropdown", "value")],)
def update_US_sports(Sport):
    filtered_s1 = olympics_US[olympics_US["Sport"] == Sport]
    filtered_s2 = olympics_US[olympics_US["Sport"] == Sport]
    filtered_s3 = olympics_US[olympics_US["Sport"] == Sport]
    trace1 = go.Bar(
        x=filtered_s1["Sport"].unique(),
        y=filtered_s1.groupby("Sport")["Gold"].agg(sum),
        text=filtered_s1.groupby("Sport")["Gold"].agg(sum),
        textposition="outside",
        marker_color=px.colors.qualitative.Dark2[5],
        name="Gold", showlegend=False
    )
    trace2 = go.Bar(
        x=filtered_s2["Sport"].unique(),
        y=filtered_s2.groupby("Sport")["Silver"].agg(sum),
        text=filtered_s2.groupby("Sport")["Silver"].agg(sum),
        textposition="outside",
        marker_color=px.colors.qualitative.Dark2[7],
        name="Silver", showlegend=False
    )
    trace3 = go.Bar(
        x=filtered_s3["Sport"].unique(),
        y=filtered_s3.groupby("Sport")["Bronze"].agg(sum),
        text=filtered_s3.groupby("Sport")["Bronze"].agg(sum),
        textposition="outside",
        marker_color=px.colors.qualitative.Dark2[6],
        name="Bronze", showlegend=False
    )
    data = [trace1, trace2, trace3]
    layout = go.Layout(barmode="group", title="US Medals Awarded by Sport")
    US_sports_plot = go.Figure(data=data, layout=layout)
    US_sports_plot.update_layout(
        title=dict(x=0.5),
        xaxis_title="Sport",
        yaxis_title="Total Medals",
        paper_bgcolor="aliceblue",
        margin=dict(l=20, r=20, t=60, b=20),
    )
    US_sports_plot.update_traces(texttemplate="%{text:.2s}")
    return US_sports_plot


#Populates US events plot
@app.callback(Output("US_events_plot", "figure"),
              [Input("events-dropdown", "value")],)
def update_US_events(Event):
    filtered_s1 = olympics_US[olympics_US["Event"] == Event]
    filtered_s2 = olympics_US[olympics_US["Event"] == Event]
    filtered_s3 = olympics_US[olympics_US["Event"] == Event]
    trace1 = go.Bar(
        x=filtered_s1["Event"].unique(),
        y=filtered_s1.groupby("Event")["Gold"].agg(sum),
        text=filtered_s1.groupby("Event")["Gold"].agg(sum),
        textposition="outside",
        marker_color=px.colors.qualitative.Dark2[5],
        name="Gold",
    )
    trace2 = go.Bar(
        x=filtered_s2["Event"].unique(),
        y=filtered_s2.groupby("Event")["Silver"].agg(sum),
        text=filtered_s2.groupby("Event")["Silver"].agg(sum),
        textposition="outside",
        marker_color=px.colors.qualitative.Dark2[7],
        name="Silver",
    )
    trace3 = go.Bar(
        x=filtered_s3["Event"].unique(),
        y=filtered_s3.groupby("Event")["Bronze"].agg(sum),
        text=filtered_s3.groupby("Event")["Bronze"].agg(sum),
        textposition="outside",
        marker_color=px.colors.qualitative.Dark2[6],
        name="Bronze",
    )
    data = [trace1, trace2, trace3]
    layout = go.Layout(barmode="group", title="US Medals Awarded by Event")
    US_events_plot = go.Figure(data=data, layout=layout)
    US_events_plot.update_layout(
        title=dict(x=0.5),
        xaxis_title="Event",
        yaxis_title="Total Medals",
        paper_bgcolor="aliceblue",
        margin=dict(l=20, r=20, t=60, b=20),
    )
    US_events_plot.update_traces(texttemplate="%{text:.2s}")
    return US_events_plot



#keep at the bottom
if __name__ == '__main__':
    app.run_server(debug=True)
    
    
