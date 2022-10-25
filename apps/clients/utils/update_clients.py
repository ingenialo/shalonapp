from apps.clients.models import Clients

def update_consumidor_final():
    """
        with this function you can update all the clients records if is a consumidor final
        to execute:
        from apps.clients.utils.update_clients import update_consumidor_final
        update_consumidor_final()
    """
    clients = Clients.objects.all()
    for instance in clients:
        print(f'actualizando cliente: {instance.id}')
        if not instance.identification_number or not instance.email or not instance.address:
            instance.consumidor_final = True
        else:
            instance.consumidor_final = False
        instance.save()