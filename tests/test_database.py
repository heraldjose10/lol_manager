from tests import ApiBaseTestCase
from api import db
from api.models import Champion


class DatabaseTestCase(ApiBaseTestCase):
    """test case to test database"""

    def test_add_champion(self):
        """test addition of new champion to database"""
        champion1 = Champion(
            id=99,
            name='Garen',
            q='sword',
            w='shield',
            e='spin',
            r='**kill**',
            store_price=400
        )
        db.session.add(champion1)
        db.session.commit()

        champs = Champion.query.all()
        self.assertEqual(1, len(champs))

    def test_remove_champion(self):
        """test removal of new champion from database"""
        champion1 = Champion(
            id=99,
            name='Garen',
            q='sword',
            w='shield',
            e='spin',
            r='**kill**',
            store_price=400
        )
        champion2 = Champion(
            id=45,
            name='Master Yi',
            q='Alpha Strike',
            w='Meditate',
            e='Wuju Style',
            r='Highlander',
            store_price=400
        )
        champion3 = Champion(
            id=44,
            name='Jinx',
            q='Switcheroo!',
            w='Zap!',
            e='Flame Chompers!',
            r='Super Mega Death Rocket!',
            store_price=4800
        )
        db.session.add(champion1)
        db.session.add(champion2)
        db.session.add(champion3)
        db.session.commit()

        champs = Champion.query.all()
        self.assertEqual(3, len(champs))

        db.session.delete(champion1)
        champs = Champion.query.all()
        self.assertEqual(2, len(champs))

        self.assertEqual('Jinx', champs[0].name)
        self.assertEqual('Master Yi', champs[1].name)
        self.assertEqual(4800, champs[0].store_price)
        self.assertEqual(400, champs[1].store_price)

    def test_update_champion(self):
        """test updation of champion objects"""
        champion2 = Champion(
            id=45,
            name='Master Yi',
            q='Alpha Strike',
            w='Meditate',
            e='Wuju Style',
            r='Highlander',
            store_price=400
        )
        db.session.add(champion2)
        db.session.commit()

        master_yi = Champion.query.filter_by(id=45).first()
        self.assertEqual('Master Yi', master_yi.name)

        master_yi.store_price = 800
        db.session.commit()

        champs = Champion.query.all()
        self.assertNotEqual(0, len(champs))
        self.assertEqual(800, champs[0].store_price)
