from flask import Flask, render_template, request, redirect
from datetime import datetime

# class Item_Card:
#     def __init__(self, price, img_path, is_promoted, sku, name, available_amount):
#         self.price = price
#         self.img_path = img_path
#         self.is_promoted = is_promoted
#         self.sku = sku
#         self.name = name
#         self.available_amount = available_amount
      



def home_route(app,cursor,mydb):
    @app.route('/', methods=['GET', 'POST'])
    def home():
        if request.method == 'POST':
            return "HELLO WORLD"
        else:
            cursor.execute("SELECT * FROM online_store.clothes ORDER BY is_promoted")
            clothes = cursor.fetchall()
            return render_template("home_page.html",clothes=clothes)


        
