from django.test import SimpleTestCase
from django.urls import resolve, reverse

from plans import views


class PlanUrlsTest(SimpleTestCase):
    def test_plan_list_url_resolves(self):
        url = reverse("plans:plan-list")
        self.assertEqual(resolve(url).func.view_class, views.PlanListView)

    def test_plan_detail_url_resolves(self):
        url = reverse("plans:plan-detail", args=[1])
        self.assertEqual(resolve(url).func.view_class, views.PlanDetailView)

    def test_plan_create_url_resolves(self):
        url = reverse("plans:plan-create")
        self.assertEqual(resolve(url).func.view_class, views.PlanCreateView)

    def test_plan_update_url_resolves(self):
        url = reverse("plans:plan-update", args=[1])
        self.assertEqual(resolve(url).func.view_class, views.PlanUpdateView)

    def test_plan_delete_url_resolves(self):
        url = reverse("plans:plan-delete", args=[1])
        self.assertEqual(resolve(url).func.view_class, views.PlanDeleteView)
