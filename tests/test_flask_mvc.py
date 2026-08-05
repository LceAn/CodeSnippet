import sys
import unittest
import logging
from pathlib import Path
from unittest.mock import patch


DEMO_ROOT = Path(__file__).resolve().parents[1] / 'python' / 'Flask_MVC' / 'Demo1'
sys.path.insert(0, str(DEMO_ROOT))

from app import create_app
from app.config import ProductionConfig
from app.models.model import ExampleModel
from manager import valid_port


class FlaskTemplateTests(unittest.TestCase):
    def test_testing_app_routes(self):
        app = create_app('app.config.TestingConfig')
        client = app.test_client()

        self.assertEqual(client.get('/').status_code, 200)
        response = client.get('/api/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['status'], 'healthy')
        self.assertEqual(client.get('/missing').status_code, 404)
        self.assertEqual(app.logger.level, logging.INFO)

    def test_production_requires_secret_and_database(self):
        with patch.object(ProductionConfig, 'SECRET_KEY', None), patch.object(
            ProductionConfig, 'SQLALCHEMY_DATABASE_URI', None
        ):
            with self.assertRaisesRegex(RuntimeError, 'SECRET_KEY'):
                create_app(ProductionConfig)

    def test_model_round_trip(self):
        model = ExampleModel.from_dict({'id': 7, 'name': 'sample'})
        self.assertEqual(model.to_dict(), {'id': 7, 'name': 'sample'})

    def test_port_validation(self):
        self.assertEqual(valid_port('8080'), 8080)
        with self.assertRaises(Exception):
            valid_port('70000')


if __name__ == '__main__':
    unittest.main()
