from flask import request
from flask_restful import Resource

from api import db
from api.models import Champion as _Champion


class Champion(Resource):

    def post(self):
        name = request.json.get('name', None)
        q = request.json.get('q', None)
        w = request.json.get('w', None)
        e = request.json.get('e', None)
        r = request.json.get('r', None)
        store_price = request.json.get('store_price', None)
        champ = _Champion(name=name, q=q, w=w, e=e, r=r, store_price=store_price)
        db.session.add(champ)
        db.session.commit()
        return {
            'message': 'champion resource created'
        }, 201

    def get(self):
        champions = _Champion.query.all()
        return {
            'champions': [
                {
                    'id': champ.id,
                    'name': champ.name,
                    'q': champ.q,
                    'w': champ.w,
                    'e': champ.e,
                    'r': champ.r,
                    'store_price': champ.store_price
                } for champ in champions
            ] if len(champions) > 0 else []
        }

    def patch(self):
        id = request.json.get('id', None)
        name = request.json.get('name', None)
        q = request.json.get('q', None)
        w = request.json.get('w', None)
        e = request.json.get('e', None)
        r = request.json.get('r', None)
        store_price = request.json.get('store_price', None)

        champ = _Champion.query.filter_by(id=id).first()
        if champ:
            if name:
                champ.name = name
            if q:
                champ.q = q
            if w:
                champ.w = w
            if e:
                champ.e = e
            if r:
                champ.r = r
            if store_price:
                champ.store_price = store_price

            db.session.commit()
            return { 'message': 'champion resource updated' }, 200

        return { 'message': 'there is no champion resource with given id' }, 404

    def delete(self):
        id = request.json.get('id', None)
        if id:
            champ = _Champion.query.filter_by(id=id).first()
            if champ:
                db.session.delete(champ)
                db.session.commit()
                return { 'message': 'champion resource deleted' },200
            return { 'message': 'there is no champion resource with given id' }, 404
        return { 'message': 'you did not provide an id' }, 400

