"""Shared configuration for Customer Engagements scripts."""

import os
from pathlib import Path

import yaml


WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
CUSTOMERS_YAML = WORKSPACE_ROOT / "customers.yaml"
CUSTOMERS_DIR = WORKSPACE_ROOT / "customers"
TEMPLATES_DIR = CUSTOMERS_DIR / "_templates"


def load_customers():
    """Load the customer registry from customers.yaml."""
    if not CUSTOMERS_YAML.exists():
        return {"customers": []}
    with open(CUSTOMERS_YAML, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {"customers": []}


def save_customers(data):
    """Save the customer registry to customers.yaml."""
    with open(CUSTOMERS_YAML, "w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True)


def find_customer(name):
    """Find a customer by name (case-insensitive)."""
    data = load_customers()
    for customer in data.get("customers", []):
        if customer["name"].lower() == name.lower():
            return customer
    return None
