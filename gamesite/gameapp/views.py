from django.shortcuts import render

# import pandas for data analysis
import pandas as pd

# Import from other files in the program
from .models import Game
from .forms import CreateNewGame

# Allows rendering of the home page
def home(request):
    game_list = Game.objects.all()
    return render(request, "gameapp/home.html",
        {'game_list': game_list, "title":"Home"})

# Shows all the games that have at least 1000 user reviews
def rated_index(request):
    # Creates a dataframe from the games in the Game database
    item=Game.objects.all().values()
    df=pd.DataFrame(item)
    # Filters out any columns that are not required and sorts them by average rating
    filtered_added_df = df[["BGGId", "Name", "AvgRating", "Ratings", "Thematic", "Strategy", "War", "Family", "CGS", "Abstract", "Party", "Child"]].sort_values(by="AvgRating").iloc[::-1]
    # Removes any games that have less than 1000 user reviews
    rated_df = filtered_added_df[filtered_added_df["Ratings"] > 1000]
    # Creates a dictionary of the remaining information which is returned to the view
    mydict={
        'df':rated_df.to_html()
    }
    return render(request, "gameapp/index.html", context=mydict)

# Shows all the games that are in the thematic category
def thematic_index(request):
    # Creates a dataframe from the games in the Game database
    item=Game.objects.all().values()
    df=pd.DataFrame(item)
    # Filters out any columns that are not required and sorts them by average rating
    filtered_added_df = df[["BGGId", "Name", "AvgRating", "Ratings", "Thematic"]].sort_values(by="AvgRating").iloc[::-1]
    # Removes any games that are of the wrong category
    rated_df = filtered_added_df[filtered_added_df["Thematic"] == True]
    # Creates a dictionary of the remaining information which is returned to the view
    mydict={
        'df':rated_df.to_html()
    }
    return render(request, "gameapp/index.html", context=mydict)

# Shows all the games that are in the strategy category
def strategic_index(request):
    # Creates a dataframe from the games in the Game database
    item=Game.objects.all().values()
    df=pd.DataFrame(item)
    # Filters out any columns that are not required and sorts them by average rating
    filtered_added_df = df[["BGGId", "Name", "AvgRating", "Ratings", "Strategy"]].sort_values(by="AvgRating").iloc[::-1]
    # Removes any games that are of the wrong category
    rated_df = filtered_added_df[filtered_added_df["Strategy"] == True]
    # Creates a dictionary of the remaining information which is returned to the view
    mydict={
        'df':rated_df.to_html()
    }
    return render(request, "gameapp/index.html", context=mydict)

# Shows all the games that are in the war category
def war_index(request):
    # Creates a dataframe from the games in the Game database
    item=Game.objects.all().values()
    df=pd.DataFrame(item)
    # Filters out any columns that are not required and sorts them by average rating
    filtered_added_df = df[["BGGId", "Name", "AvgRating", "Ratings", "War"]].sort_values(by="AvgRating").iloc[::-1]
    # Removes any games that are of the wrong category
    rated_df = filtered_added_df[filtered_added_df["War"] == True]
    # Creates a dictionary of the remaining information which is returned to the view
    mydict={
        'df':rated_df.to_html()
    }
    return render(request, "gameapp/index.html", context=mydict)

# Shows all the games that are in the family category
def family_index(request):
    # Creates a dataframe from the games in the Game database
    item=Game.objects.all().values()
    df=pd.DataFrame(item)
    # Filters out any columns that are not required and sorts them by average rating
    filtered_added_df = df[["BGGId", "Name", "AvgRating", "Ratings", "Family"]].sort_values(by="AvgRating").iloc[::-1]
    # Removes any games that are of the wrong category
    rated_df = filtered_added_df[filtered_added_df["Family"] == True]
    # Creates a dictionary of the remaining information which is returned to the view
    mydict={
        'df':rated_df.to_html()
    }
    return render(request, "gameapp/index.html", context=mydict)

# Shows all the games that are in the CGS category
def cgs_index(request):
    # Creates a dataframe from the games in the Game database
    item=Game.objects.all().values()
    df=pd.DataFrame(item)
    # Filters out any columns that are not required and sorts them by average rating
    filtered_added_df = df[["BGGId", "Name", "AvgRating", "Ratings", "CGS"]].sort_values(by="AvgRating").iloc[::-1]
    # Removes any games that are of the wrong category
    rated_df = filtered_added_df[filtered_added_df["CGS"] == True]
    # Creates a dictionary of the remaining information which is returned to the view
    mydict={
        'df':rated_df.to_html()
    }
    return render(request, "gameapp/index.html", context=mydict)

# Shows all the games that are in the abstract category
def abstract_index(request):
    # Creates a dataframe from the games in the Game database
    item = Game.objects.all().values()
    df = pd.DataFrame(item)
    # Filters out any columns that are not required and sorts them by average rating
    filtered_added_df = df[["BGGId", "Name", "AvgRating", "Ratings", "Abstract"]].sort_values(
        by="AvgRating").iloc[::-1]
    # Removes any games that are of the wrong category
    rated_df = filtered_added_df[filtered_added_df["Abstract"] == True]
    # Creates a dictionary of the remaining information which is returned to the view
    mydict = {
        'df': rated_df.to_html()
    }
    return render(request, "gameapp/index.html", context=mydict)

# Shows all the games that are in the party category
def party_index(request):
    # Creates a dataframe from the games in the Game database
    item = Game.objects.all().values()
    df = pd.DataFrame(item)
    # Filters out any columns that are not required and sorts them by average rating
    filtered_added_df = df[["BGGId", "Name", "AvgRating", "Ratings", "Party"]].sort_values(
        by="AvgRating").iloc[::-1]
    # Removes any games that are of the wrong category
    rated_df = filtered_added_df[filtered_added_df["Party"] == True]
    # Creates a dictionary of the remaining information which is returned to the view
    mydict = {
        'df': rated_df.to_html()
    }
    return render(request, "gameapp/index.html", context=mydict)

# Shows all the games that are in the children's category
def children_index(request):
    # Creates a dataframe from the games in the Game database
    item = Game.objects.all().values()
    df = pd.DataFrame(item)
    # Filters out any columns that are not required and sorts them by average rating
    filtered_added_df = df[["BGGId", "Name", "AvgRating", "Ratings", "Child"]].sort_values(
        by="AvgRating").iloc[::-1]
    # Removes any games that are of the wrong category
    rated_df = filtered_added_df[filtered_added_df["Child"] == True]
    # Creates a dictionary of the remaining information which is returned to the view
    mydict = {
        'df': rated_df.to_html()
    }
    return render(request, "gameapp/index.html", context=mydict)

# Allows rendering of the links webpage
def links(request):
    return render(request, "gameapp/links.html")

# Allows rendering of the add_game webpage
def add_game(request):
    # If the user uses a post request through the form
    if request.method == "POST":
        # Passes all the information form the form to Game
        form = CreateNewGame(request.POST)

        # Saves the entered data to the Game database if it is valid
        if form.is_valid():
            form.save()
            return render(request, "gameapp/home.html")
    # If the user uses a get request, calls CreateNewGame
    else:
        form = CreateNewGame()
    return render(request, "gameapp/add_game.html", {"form":form})

# Allows rendering of each game's webpage
def game_index(request, BGGId):
    # Identifies a game based on BGGId, and gets the relevant data
    game = Game.objects.get(BGGId=BGGId)
    return render(request, 'gameapp/game_details.html', {'game':game})
