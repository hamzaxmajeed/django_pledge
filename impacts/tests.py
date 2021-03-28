from django.test import TestCase
from .models import Bills, Veg
from decimal import Decimal

class PledgeTest(TestCase):
    
    def setUp(self):
        
        # setup for Bills pledge
        impact = int(49 * 0.5 * 5 * 2)
        Bills.objects.create(name="Name1", energy_supplier="bog standard",
            num_of_people=2, heating_source="gas or oil", message="Save Energy", impact=impact)

        # setup for Veg Out pledge
        co_impact = 0.884 * 2.5 * 8.7
        water_impact = 0.75 * 6
        waste_impact = 0.2 * 6 * 2.5
        Veg.objects.create(name="Name2", current_meals=6,
            veggie_meals=5, co_impact=co_impact, water_impact=water_impact,
                waste_impact=waste_impact, message="Going Vegan")

    def test_bills_impact(self):
        b = Bills.objects.get(name="Name1")
        self.assertEqual(b.impact, 245)

    def test_veg_impact(self):
        v = Veg.objects.get(name="Name2")
        self.assertEqual(v.co_impact, Decimal('19.227'))
        self.assertEqual(v.water_impact, Decimal('4.5'))
        self.assertEqual(v.waste_impact, Decimal('3'))