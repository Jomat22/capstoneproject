from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from littlelemon.restaurant.models import menu # Assumiamo che il modello Menu sia in 'restaurant.models'
from littlelemon.restaurant.serializers import MenuItemSerializer # Assumiamo che il serializzatore sia in 'restaurant.serializers'

class MenuViewTest(TestCase):
    """
    Test class for the Menu API views.
    This class subclasses Django's TestCase to provide a test database
    for isolated testing.
    """

    def setUp(self):
        """
        Set up the test environment by adding a few test instances of the Menu model.
        This method runs before each test method.
        """
        # Create a test client
        self.client = APIClient()

        # Add a few test Menu instances
        self.menu_item1 = menu.objects.create(title="Pizza Margherita", price=12.50)
        self.menu_item2 = menu.objects.create(title="Pasta Carbonara", price=15.00)
        self.menu_item3 = menu.objects.create(title="Tiramisu", price=7.00)

        print(f"Created Menu items: {self.menu_item1.title}, {self.menu_item2.title}, {self.menu_item3.title}")


    def test_getall(self):
        """
        Test to retrieve all Menu objects and verify serialization.
        This method sends a GET request to the menu list endpoint,
        retrieves all Menu objects from the database, serializes them,
        and asserts that the response data matches the serialized data.
        """
        print("\nRunning test_getall...")

        # 1. Make a GET request to the menu list endpoint
        # Assumiamo che l'endpoint per la lista del menu sia '/api/menu/'
        # Assicurati che il tuo urls.py sia configurato per gestire questo percorso.
        response = self.client.get('/api/menu/')

        # 2. Retrieve all Menu objects added for the test purpose directly from the DB
        menu_items = menu.objects.all().order_by('id') # Order by ID to ensure consistent order for comparison

        # 3. Serialize the retrieved objects
        # Many=True è necessario perché stiamo serializzando una queryset di più oggetti
        serializer = MenuItemSerializer(menu_items, many=True)
        expected_data = serializer.data

        print(f"Expected data (serialized from DB): {expected_data}")
        print(f"Actual response data: {response.data}")

        # 4. Assert that the status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 5. Assert that the serialized data equals the response data
        # Confrontiamo i dati della risposta con i dati serializzati dal modello
        self.assertEqual(response.data, expected_data)

        print("test_getall completed successfully.")

