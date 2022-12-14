#!/usr/bin/env python3
from .flask_setup import api
from ..health_resources.health_check import HealthCheck
from ..read_resources.read import Read
from ..stat_resources.stat import Stat
from typing import Optional


def add_resources() -> Optional[bool]:
    try:
        api.add_resource(
            HealthCheck,
            '/health')

        api.add_resource(
            Stat,
            '/file/<string:uuid>/stat/')

        api.add_resource(
            Read,
            '/file/<string:uuid>/read/')
        return True

    except Exception:
        print('Adding API resources failed...')
        exit(1)
