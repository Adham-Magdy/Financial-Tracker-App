from faker import Faker
from django.core.management.base import BaseCommand
import random
from tracker.models import User, Category, Transaction


class Command(BaseCommand):

    help = "Create Transactions For Testing"

    def handle(self, *args, **options):
        fake = Faker()
        
        """
        create categories choices for user
        """
        categories = [
            "Bills",
            "Food",
            "Clothes",
            "Medical",
            "Housing",
            "Salary",
            "Social",
            "Transport",
            "Vacation",
        ]
        
        for category in categories:
            #  insert categories options
            Category.objects.get_or_create(name=category)
            
        
        """
        check if user is found or not and returned it
        """
        user = User.objects.filter(username="adhamdev").first()
        if not user:
            user = User.objects.create_superuser(username="adhamdev",password="adhamdev139")
        
        
        """
        Create number of dummy transactions for testing purpose
        """
        categories = Category.objects.all()
        types = [x[0] for x in Transaction.TRANSACTION_TYPE_CHOICES]
        for i in range(20):
            Transaction.objects.create(
                category = random.choice(categories),
                user = user,
                amount = random.uniform(1,250),
                date = fake.date_between(start_date='-1y',end_date='today'),
                type = random.choice(types)
            )
