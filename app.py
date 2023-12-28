import warnings
warnings.filterwarnings('ignore', category=FutureWarning)
from flask import abort, render_template, Flask
import logging
import db

APP = Flask(__name__)

# Start page
@APP.route('/')
def index():
    stats = {}
    stats = db.execute('''
    SELECT * FROM
      (SELECT COUNT(*) linhaID FROM Linhas)
    JOIN
      (SELECT COUNT(*) viagemID FROM Viagens)
    JOIN
      (SELECT COUNT(*) zonaIdOrigem FROM Zonas)
    JOIN 
      (SELECT COUNT(*) idParagem FROM Paragens)
    ''').fetchone()
    logging.info(stats)
    return render_template('index.html',stats=stats)

# Routes
@APP.route('/routes/')
def list_routes():
    routes = db.execute(
      '''
      SELECT nome as Name, cor as Color
      FROM Linhas
      ORDER BY Name
      ''').fetchall()
    if not routes:
        abort(404)  # or handle it in another way, e.g., render an error template

    return render_template('routes-list.html', routes=routes)

@APP.route('/routes/A')
def route_A():
    routes = db.execute(
      '''
      SELECT nome as Name, cor as Color
      FROM Linhas
      WHERE nome = 'A'
      ''').fetchall()
    if not routes:
        abort(404)  # or handle it in another way, e.g., render an error template

    return render_template('routes-list.html', routes=routes)

@APP.route('/routes/B')
def route_B():
    routes = db.execute(
      '''
      SELECT nome as Name, cor as Color
      FROM Linhas
      WHERE nome = 'B'

      ''').fetchall()
    if not routes:
        abort(404)  # or handle it in another way, e.g., render an error template

    return render_template('routes-list.html', routes=routes)   

@APP.route('/routes/Bx')
def route_Bx():
    routes = db.execute(
      '''
      SELECT nome as Name, cor as Color
      FROM Linhas
      WHERE nome = 'Bx' 

      ''').fetchall()
    if not routes:
        abort(404)  # or handle it in another way, e.g., render an error template

    return render_template('routes-list.html', routes=routes)




@APP.route('/routes/C')
def route_C():
    routes = db.execute(
      '''
      SELECT nome as Name, cor as Color
      FROM Linhas
      WHERE nome = 'C'

      ''').fetchall()
    if not routes:
        abort(404)  # or handle it in another way, e.g., render an error template

    return render_template('routes-list.html', routes=routes)

@APP.route('/routes/D')
def route_D():
    routes = db.execute(
      '''
      SELECT nome as Name, cor as Color
      FROM Linhas
      WHERE nome = 'D'
      ''').fetchall()
    if not routes:
        abort(404)  # or handle it in another way, e.g., render an error template

    return render_template('routes-list.html', routes=routes)

@APP.route('/routes/E')
def route_E():
    routes = db.execute(
      '''
      SELECT nome as Name, cor as Color
      FROM Linhas
      WHERE nome = 'E'
      ''').fetchall()
    if not routes:
        abort(404)  # or handle it in another way, e.g., render an error template

    return render_template('routes-list.html', routes=routes)

@APP.route('/routes/F')
def route_F():
    routes = db.execute(
      '''
      SELECT nome as Name, cor as Color
      FROM Linhas
      WHERE nome = 'F'
      ''').fetchall()
    if not routes:
        abort(404)  # or handle it in another way, e.g., render an error template

    return render_template('routes-list.html', routes=routes)




@APP.route('/routes-search/<color>/')
def color_search(color):
    # Use a parameterized query to avoid SQL injection
    query = '''
        SELECT nome as Name, cor as Color
        FROM Linhas
        WHERE cor = ?
    '''
    routes = db.execute(query, (color,)).fetchall()

    if not routes:
        abort(404)  # or handle it in another way, e.g., render an error template

    return render_template('routes-search.html', color=color, routes=routes)


#  Pagina das paragens
@APP.route('/stops/')
def list_stops():
    stops = db.execute(
    '''
    SELECT idParagem as ID, zonaIdOrigem as Zone, nomeDaParagem as Name
    FROM Paragens
    ORDER BY ID
    ''').fetchall()
    return render_template('stops-list.html',stops=stops)

@APP.route('/stops/<ID>/')
def stop(ID):
    query = '''
    SELECT
    nomeDaParagem AS Name,
    zonaIdOrigem AS Zone,
    idParagem AS ID,
    linhaID AS Route
FROM
    Paragens
  JOIN
    Horarios ON idParagem = paragemID
WHERE
    idParagem = ?
    '''
    paragens = db.execute(query, (ID,)).fetchall()
    if not paragens:
        abort(404)  # or handle it in another way, e.g., render an error template

    return render_template('stops.html', ID=ID, paragens=paragens)


@APP.route('/stops_by_name/<Name>/')
def stop_search_By_Name(Name):
    query = '''
    SELECT
    nomeDaParagem AS Name,
    zonaIdOrigem AS Zone,
    idParagem AS ID,
    linhaID AS Route
FROM
    Paragens
  JOIN
    Horarios ON idParagem = paragemID
WHERE
    Name = ?
    '''
    stations = db.execute(query, (Name,)).fetchall()
    if not stations:
        abort(404)  # or handle it in another way, e.g., render an error template

    return render_template('stops_by_name.html', Name=Name, stations=stations)


# Pagina dos tickets
@APP.route('/tickets/')
def list_ticket_prices():
    tickets = db.execute(
    '''
    SELECT tituloID as Ticket, preco as Price
    FROM Titulos
    GROUP BY Ticket, Price
    HAVING COUNT(*) > 1
    ''').fetchall()
    if not tickets:
        abort(404)
    return render_template('tickets-price-list.html', tickets=tickets)

@APP.route('/tickets/<zone>/')
def search_by_Zone(zone):
    query =  '''
            Select  tituloID as Ticket, preco as Price, zonaIdOrigem , zonaIdDestino
            FROM Titulos
            Where Ticket = ?
        '''
    zonas = db.execute(query, (zone,)).fetchall()
    if not zonas:
        abort(404)
    return render_template('tickets-search.html', zonas=zonas)



