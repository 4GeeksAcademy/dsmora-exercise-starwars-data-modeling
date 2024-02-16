import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "blog_user"
    user_id = Column(Integer, primary_key=True)
    user_name = Column (String)
    user_password = Column (String)
    user_fav_character_id = Column(Integer)
    user_fav_planet_id = Column(Integer)

class Character(Base):
    __tablename__ = "character"
    character_id = Column(Integer, ForeignKey('characters.user_fav_character_id'), primary_key=True)
    characters = relationship(User)
    birth_year = Column(String)
    eye_color = Column(String)
    gender = Column(String)
    hair_color = Column(String)
    height = Column(Integer)
    mass = Column(Integer)
    name = Column(String)
    skin_color = Column(String)
    created = Column(String)
    edited = Column(String)
    url = Column(String)
    film_id = Column(Integer)
    homeworld_id = Column(Integer)
    vehicle_id = Column(Integer)

class Film(Base):
    __tablename__ = "film"
    film_id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.character_id'))
    characters = relationship(Character)
    planet_id = Column(Integer)
    created = Column(String)
    director = Column(String)
    edited = Column(String)
    opening_crawl = Column(String)
    producer = Column(String)
    release_date = Column(String)
    title = Column(String)
    url = Column(String)

class Planet(Base):
    __tablename__ = "planet"
    planet_id = Column(Integer, ForeignKey('planets.user_fav_planet_id'), primary_key=True)
    planets = relationship(User)
    climate = Column(String)
    created = Column(String)
    diameter = Column(String)
    edited = Column(String)
    gravity = Column(String)
    name = Column(String)
    orbital_period = Column(String)
    population = Column(Integer)
    rotation_period = Column(String)
    surface_water = Column(String)
    terrain = Column(String)
    url = Column(String)
    resident_id = Column(Integer, ForeignKey('characters.chr_id'))
    characters = relationship(Character)
    film_id = Column(Integer, ForeignKey('films.film_id'))
    films = relationship(Film)

class Vehicle(Base):
    __tablename__ = "vehicle"
    vehicle_id = Column(Integer, ForeignKey('characters.character_id'), primary_key=True)
    characters = relationship(Character)
    cargo_capacity = Column(Integer)
    consumables = Column(String)
    cost_in_credits = Column(Integer)
    created = Column(String)
    crew = Column(Integer)
    edited = Column(String)
    length = Column(Integer)
    manufacturer = Column(String)
    max_atmosphering_speed = Column(Integer)
    model = Column(String)
    name = Column(String)
    passengers = Column(Integer)
    film_id = Column(Integer, ForeignKey('films.film_id'))
    films = relationship(Film)
    url = Column(String)
    vehicle_class = Column(String)
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e