from django.test import SimpleTestCase

from plandiet_app.forms import MacroCalculatorForm


class MacroCalculatorFormTest(SimpleTestCase):
    def test_form_fields(self):
        form = MacroCalculatorForm()
        self.assertTrue("age" in form.fields)
        self.assertTrue("height" in form.fields)
        self.assertTrue("weight" in form.fields)
        self.assertTrue("sex" in form.fields)
        self.assertTrue("activity" in form.fields)
        self.assertTrue("goal" in form.fields)

    def test_valid_data(self):
        form_data = {"age": 25, "height": 170, "weight": 70, "sex": "male", "activity": "1.2", "goal": "bulk"}
        form = MacroCalculatorForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_age(self):
        form_data = {"age": -25, "height": 170, "weight": 70, "sex": "male", "activity": "1.2", "goal": "reduce"}
        form = MacroCalculatorForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("age", form.errors)

    def test_invalid_height(self):
        form_data = {"age": 25, "height": -170, "weight": 70, "sex": "male", "activity": "1.2", "goal": "reduce"}
        form = MacroCalculatorForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("height", form.errors)

    def test_invalid_weight(self):
        form_data = {"age": 25, "height": 170, "weight": -70, "sex": "male", "activity": "1.2", "goal": "maintain"}
        form = MacroCalculatorForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("weight", form.errors)
