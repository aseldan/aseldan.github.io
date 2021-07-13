from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def start():
    title = "The Haunted House"
    
    text = """It is a dark and cold night and the moon is full. You walk up to the haunted house.  
    As you approach the door, it creaks open and a chill runs down your spine!"""

    choices = [
        ('enter_house',"Go inside"),
        ('run_away',"Run away as fast as you can!!!")
    ]
    house=url_for('static', filename='house.jpeg')
    
    return render_template('adventure.html', title=title, text=text, choices=choices, picture_url=house)



@app.route("/inside")
def enter_house():
    title = "You go inside..."
    
    text = """... and the door slams shut behind you!  And then -- absolute silence.  It is so quiet you can hear the 
    sound of your own heart beating.  A dusty wooden staircase leads up to the second floor.  Through a tangle of cobwebs
    you can see the faint, flickering light of a small candle."""

    choices = [
        ('up_stairs',"Go up the stairs"),
        ('living_room',"Check out the livivng room"),
        ('run_away',"Try to escape out the front door")
    ]
    room=url_for('static', filename='room.jpeg')
    return render_template('adventure.html', title=title, text=text, choices=choices, picture_url=room)

@app.route("/escape")
def run_away():
    title = "You run away!"
    
    text = """You bolt away from the house to safety.  You hear the sound of a sinister voice cackling madly behind you."""

    choices = []
    house=url_for('static', filename='house.jpeg')
    return render_template('adventure.html', title=title, text=text, choices=choices, picture_url=house)



@app.route("/stairs")
def up_stairs():
    title = "Look out!"
    
    text = """As you climb the stairs, a sea of spiders rains down on you from the cobwebs.  You feel the excruciating bites of 
    ten thousand tiny fangs as they eat you alive."""

    choices = [
        ('downstairs',"Run away downstairs!"),
        ('fire',"Fight back the spiders with fire")
    ]
    upstairs=url_for('static', filename='upstairs.png')
    return render_template('adventure.html', title=title, text=text, choices=choices, picture_url=upstairs)

@app.route("/livingroom")
def living_room():
    title = "Look out!"
    
    text = """As you walk into the living room the candles light up. There is a sofa in the living room, 
    which appears to be a right place for a nap after a long day..."""

    choices = [
        ('nap',"Get a nap on the sofa"),
        ('awake',"No! Stay awake till morning")
        ]
    candles=url_for('static', filename='livingroom.jpeg')
    return render_template('adventure.html', title=title, text=text, choices=choices, picture_url=candles)

@app.route("/downstairs")
def downstairs():
    title = "You go downstairs..."
    
    text = """...  It is so quiet you can hear the sound of your own heart beating. You can go back up the stairs or check the living room."""

    choices = [
        ('up_stairs',"Go up the stairs"),
        ('living_room',"Check out the livivng room"),
        ('run_away',"Try to escape out the front door")
    ]
    room=url_for('static', filename='room.jpeg')
    return render_template('adventure.html', title=title, text=text, choices=choices, picture_url=room)

@app.route("/fight")
def fire():
    title = "Oh no!"
    
    text = """Looks like the spiders are not afaird of the fire. """

    choices = []
    spider=url_for('static', filename='spider.jpeg')
    return render_template('adventure.html', title=title, text=text, choices=choices, picture_url=spider)

@app.route("/sleep")
def nap():
    title = "Oh no! You are a ghost now!"
    
    text = """Never fall asleep in the haunted house."""

    choices = []
    sleep=url_for('static', filename='sleep.jpeg')
    return render_template('adventure.html', title=title, text=text, choices=choices, picture_url=sleep)

@app.route("/awake")
def awake():
    title = "You should have left when you had a chance!"
    
    text = """You tried hard, but you still fell asleep and became a ghost at this house."""

    choices = []
    sleep=url_for('static', filename='sleep.jpeg')
    return render_template('adventure.html', title=title, text=text, choices=choices, picture_url=sleep)