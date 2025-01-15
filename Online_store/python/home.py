from flask import Flask, render_template, request, session
import random
    

def home_route(app,cursor,mydb):
    @app.route('/', methods=['GET', 'POST'])
    def home():
        # if 'email' not in session:
        # return redirect('/login')
        if request.method == 'POST':
            items = dict(request.form)

            modified_items = {}
            for sku,quantity in items.items():
                if int(quantity) > 0:
                    modified_items[int(sku)] = int(quantity)

            order_num = random.randint(100000, 999999)

            cursor.execute("""INSERT INTO online_store.transactions (order_num, date, hour, email) VALUES (%s, CURDATE(), CURTIME(), %s)""",(order_num, session['email'])
)               
            mydb.commit()


            for sku, quantity in modified_items.items():
                cursor.execute("""INSERT INTO clothes_in_transaction (order_num, sku, amount) VALUES (%s, %s, %s)""",  (order_num, sku, quantity),)
                  
            mydb.commit()

            return render_template("transaction.html", order_num=order_num, items=modified_items)
        else:
            session['email'] = "jane.doe@example.com"
         
            cursor.execute("SELECT u.is_admin FROM online_store.users u WHERE email = %s",(session['email'],))    
            is_admin = cursor.fetchone()[0]

            cursor.execute("SELECT * FROM online_store.clothes ORDER BY is_promoted")
            clothes = cursor.fetchall()
            return render_template("home_page.html",clothes=clothes, is_admin = is_admin)
        


        
