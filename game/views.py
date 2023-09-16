from django.shortcuts import redirect, render
from django.db import models, IntegrityError
from django.utils import timezone

from game.utils import generate_combination

from .models import Game


def home(request):
    request.session.clear()
    return render(request, "game/home.html")


def play_game(request):
    if "new_game" in request.POST:
        request.session.clear()
        return redirect("play_game")

    combination = request.session.get("combination")
    feedback_history = request.session.get("feedback_history", [])
    attempts = request.session.get("attempts", 10)
    win = request.session.get("win", False)

    if not combination:
        combination = generate_combination()
        request.session["combination"] = combination
        request.session["start_time"] = timezone.now().timestamp()

    if request.method == "POST":
        guess = [int(num) for num in request.POST["guess"]]
        correct_nums = 0
        correct_positions = 0

        # matched_combination_indices = set()

        # for i, num in enumerate(guess):
        #     if num == combination[i]:
        #         correct_positions += 1
        #         correct_nums += 1
        #         matched_combination_indices.add(i)

        # for i, num in enumerate(guess):
        #     if num in combination and i not in matched_combination_indices:
        #         position = combination.index(num)
        #         if position not in matched_combination_indices:
        #             correct_nums += 1
        #             matched_combination_indices.add(position)

        matched_combination_indices = set()
        matched_guess_indices = set()

        for i, num in enumerate(guess):
            if num == combination[i]:
                correct_positions += 1
                correct_nums += 1
                matched_combination_indices.add(i)
                matched_guess_indices.add(i)

        for i, num in enumerate(guess):
            if i not in matched_guess_indices:
                for j, c_num in enumerate(combination):
                    if c_num == num and j not in matched_combination_indices:
                        correct_nums += 1
                        matched_combination_indices.add(j)
                        break

        feedback = f"{correct_nums} correct number(s) and {correct_positions} correct position(s)"

        feedback_history.append((guess, feedback))
        request.session["feedback_history"] = feedback_history

        if correct_positions == 4:
            win = True
            request.session["win"] = True
        else:
            attempts -= 1
            request.session["attempts"] = attempts

        if win or attempts == 0:
            end_time = timezone.now().timestamp()
            total_seconds = end_time - request.session.get(
                "start_time", end_time
            )

            context = {
                "win": win,
                "combination": combination,
                "feedback_history": feedback_history,
                "total_seconds": round(total_seconds),
            }
            return render(request, "game/game_over.html", context)

    context = {
        "attempts": attempts,
        "feedback_history": feedback_history,
    }

    return render(request, "game/game.html", context)


def game_history(request):
    games = Game.objects.all()
    context = {
        "games": games,
    }
    return render(request, "game/history.html", context)
