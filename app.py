from flask import Flask
from flask import request, jsonify, make_response
import flask
import psycopg2

app = flask.Flask(__name__)


conn = psycopg2.connect("dbname=pet_pie_hotel")

cur = conn.cursor()

@app.route('/owners', methods=['GET'])
def dbtest():
    cur.execute('SELECT * FROM owners')
    return jsonify(cur.fetchall())

@app.route('/pets', methods=['GET'])
def fetchPets() :
    cur.execute('SELECT * FROM pets')
    allPets = cur.fetchall()
    return jsonify(allPets)

@app.route('/pets', methods=['POST'])
def addPet() :
    pet = request.form['pet']
    breed = request.form['breed']
    color = request.form['color']
    owner_id = request.form['owner_id']

    try:
        query = 'INSERT INTO "pets" ("pet", "breed", "color", "owner_id") VALUES (%s, %s, %s, %s)'
        cur.execute(query, (pet, breed, color, owner_id))
        conn.commit()
        result = {'status': 'CREATED'}
        return make_response(jsonify(result), 201)
    except (Exception, psycopg2.Error) as error:
        if(conn):
            print('Failled to add pet', error)
            result = {'status': 'ERROR'}
            return make_response(jsonify(result), 500)
    finally:
        if(conn):
            cur.close()
            conn.close()
            print("PostgreSQL connection is closed")

@app.route('/pets', methods=['PUT'])
def editCheckIn():
    pet_id = request.form['id']
    checked_in = request.form['checked_in']
    checked_in_date = request.form['checked_in_date']
    try:
        query = 'UPDATE "pets" SET "checked_in" = %s, "checked_in_date" = %s WHERE "id" = %s'
        cur.execute(query, (checked_in, checked_in_date, pet_id))
        conn.commit()
        result = {'status': 'OK'}
        return make_response(jsonify(result), 200)
    except (Exception, psycopg2.Error) as error:
        if(conn):
            print('Failled to edit pet', error)
            result = {'status': 'ERROR'}
            return make_response(jsonify(result), 500)
    finally:
        if(conn):
            cur.close()
            conn.close()
            print("PostgreSQL connection is closed")

@app.route('/pets', methods=['DELETE'])
def deletePet():
    pet_id = request.form['id']

    try:
        query: 'DELETE FROM pets WHERE "id" = %s'
        cur.execute(query, (pet_id))
        conn.commit()
        result = {'status': 'OK'}
        return make_response(jsonify(result), 200)
    except (Exception, psycopg2.Error) as error:
        if(conn):
            print('Failled to edit pet', error)
            result = {'status': 'ERROR'}
            return make_response(jsonify(result), 500)
    finally:
        if(conn):
            cur.close()
            conn.close()
            print("PostgreSQL connection is closed")


if __name__ == "__main__" :
    app.run(debug=True)