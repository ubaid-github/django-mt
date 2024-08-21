import os
import yaml
import django
from django.conf import settings

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '../../project.settings')
django.setup()

from app.models import Client, Domain  # Import your models

def create_or_update_tenants():
    # Load clients data from YAML file
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'config', 'clients.yaml')

    with open(file_path, 'r') as file:
        clients_data = yaml.safe_load(file)

    for client_data in clients_data:
        tenant, created = Client.objects.get_or_create(
            schema_name=client_data['schema_name'],
            defaults={'name': client_data['name']}
        )

        if not created:
            tenant.name = client_data['name']
            tenant.save()

        domain, created = Domain.objects.get_or_create(
            domain=client_data['domain'],
            tenant=tenant,
            defaults={'is_primary': client_data['is_primary']}
        )

        if not created:
            domain.is_primary = client_data['is_primary']
            domain.save()

if __name__ == "__main__":
    create_or_update_tenants()
    print("Tenant creation/updating complete.")
