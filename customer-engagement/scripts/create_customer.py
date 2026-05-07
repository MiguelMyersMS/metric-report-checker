"""Create a new customer folder from templates."""

import shutil
from datetime import date
from pathlib import Path

from rich.console import Console
from rich.prompt import Prompt

from config import (
    CUSTOMERS_DIR,
    TEMPLATES_DIR,
    find_customer,
    load_customers,
    save_customers,
)

console = Console()


def create_customer():
    """Interactive customer creation."""
    name = Prompt.ask("Customer name")

    if find_customer(name):
        console.print(f"[yellow]Customer '{name}' already exists.[/yellow]")
        return

    tpid = Prompt.ask("TPID (Top Parent ID)")
    industry = Prompt.ask("Industry")
    geography = Prompt.ask("Geography", default="United States")
    keywords = Prompt.ask("Search keywords (comma-separated)", default=name)

    # Create folder from template
    customer_dir = CUSTOMERS_DIR / name
    if customer_dir.exists():
        console.print(f"[yellow]Folder already exists: {customer_dir}[/yellow]")
        return

    shutil.copytree(TEMPLATES_DIR, customer_dir)

    # Replace placeholders in template files
    today = date.today().isoformat()
    for md_file in customer_dir.rglob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        content = content.replace("{Customer Name}", name)
        content = content.replace("{TPID}", tpid)
        content = content.replace("{Industry}", industry)
        content = content.replace("{Geography}", geography)
        content = content.replace("{date}", today)
        md_file.write_text(content, encoding="utf-8")

    # Register in customers.yaml
    data = load_customers()
    data["customers"].append(
        {
            "name": name,
            "folder": name,
            "account": name.upper(),
            "tpid": tpid,
            "industry": industry,
            "geography": geography,
            "keywords": [k.strip() for k in keywords.split(",")],
        }
    )
    save_customers(data)

    console.print(f"[green]Created customer folder: {customer_dir}[/green]")
    console.print(f"[green]Registered in customers.yaml[/green]")


if __name__ == "__main__":
    create_customer()
