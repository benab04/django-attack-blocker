from .core import MLIPBlocker, block_if_malicious, with_ip_blocking

__version__ = "0.1.0"
__all__ = ["MLIPBlocker", "block_if_malicious", "with_ip_blocking"]


import os
import pkg_resources

def get_default_model_path():
    """Returns the path to the default model included with the package"""
    return pkg_resources.resource_filename('django_attack_blocker', 'models/model.joblib')

def get_default_encoder():
    """Returns the path to the default vectorizer included with the package"""
    return pkg_resources.resource_filename('django_attack_blocker', 'models/column_transformer.pkl')