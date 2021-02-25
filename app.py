from flask import Flask
from flask import request, jsonify, make_response
from psycopg2.extras import RealDictCursor
import flask
import psycopg2

app = flask.Flask(__name__)


conn = psycopg2.connect("dbname=pet_pie_hotel")

cur = conn.cursor(cursor_factory=RealDictCursor)

@app.route('/owners', methods=['GET'])
def fetchOwners():
    cur.execute('SELECT "owners".id, "name", COUNT(pets.id) AS "total_pets" FROM "owners" LEFT JOIN pets ON pets.owner_id = "owners".id GROUP BY "owners".id, "name"')
    return jsonify(cur.fetchall())

@app.route('/owners', methods=['POST'])
def addOwner():
    name = request.form['name']
    
    try:
        query = 'INSERT INTO "owners" ("name") VALUES ( %s )'
        cur.execute(query, (name,))
        conn.commit()
        result = {'status': 'CREATED'}
        return make_response(jsonify(result), 201)
    except (Exception, psycopg2.Error) as error:
        if(conn):
            print('Failed to add owner', error)
            result = {'status': 'ERROR'}
            return make_response(jsonify(result), 500)

@app.route('/owners/<owner_id>', methods=['DELETE'])
def deleteOwner(owner_id):

    try:
        query = 'DELETE FROM "owners" WHERE id = %s'
        cur.execute(query, (owner_id,))
        conn.commit()
        result = {'status': 'OK'}
        return make_response(jsonify(result), 201)
    except (Exception, psycopg2.Error) as error:
        if(conn):
            print('Failed to delete owner', error)
            result = {'status': 'ERROR'}
            return make_response(jsonify(result), 500)

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


@app.route('/pets/<pet_id>', methods=['DELETE'])
def deletePet(pet_id):
    

    try:
        query = 'DELETE FROM pets WHERE "id" = %s'
        cur.execute(query, (pet_id))
        conn.commit()
        result = {'status': 'OK'}
        return make_response(jsonify(result), 200)
    except (Exception, psycopg2.Error) as error:
        if(conn):
            print('Failled to delete pet', error)
            result = {'status': 'ERROR'}
            return make_response(jsonify(result), 500)


if __name__ == "__main__" :
    app.run(debug=True)