from django.http import HttpResponseServerError
from django.shortcuts import render
from django.views import View

from .calculators.bmr_calculator import bmr_calc
from .calculators.cpm_calculator import cpm_calc
from .forms import MacroCalculatorForm


class Index(View):
    def get(self, request):
        return render(request, "index.html")


class MacroCalculatorView(View):
    def get(self, request):
        try:
            current_user = request.user
            form = MacroCalculatorForm(
                initial={
                    "age": current_user.age,
                    "height": current_user.height,
                    "weight": current_user.weight,
                    "sex": current_user.sex,
                }
            )
            return render(request, "plandiet_app/macrocalculator.html", {"form": form})

        except AttributeError:
            form = MacroCalculatorForm()
            return render(request, "plandiet_app/macrocalculator.html", {"form": form})

        except Exception as e:
            return HttpResponseServerError("An error occurred while processing your request.", e)

    def post(self, request):
        form = MacroCalculatorForm(request.POST)
        bmr = None
        cpm = None
        if form.is_valid():
            age = form.cleaned_data["age"]
            height = form.cleaned_data["height"]
            weight = form.cleaned_data["weight"]
            sex = form.cleaned_data["sex"]
            activity = form.cleaned_data["activity"]
            goal = form.cleaned_data["goal"]

            bmr = bmr_calc(sex, weight, height, age)
            cpm = cpm_calc(goal, bmr, activity)

        return render(request, "plandiet_app/macrocalculator.html", {"form": form, "bmr": bmr, "cpm": cpm})
