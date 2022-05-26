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
