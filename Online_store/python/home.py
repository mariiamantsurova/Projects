from flask import render_template, request, session, redirect
import random
    

def home_route(app,cursor,mydb):
    @app.route('/', methods=['GET', 'POST'])
    def home():
        if 'email' not in session:
            return redirect('/login')
        if request.method == 'POST':
            items = dict(request.form)
            try:
                modified_items = {}
                for sku,quantity in items.items():
                    if int(quantity) > 0:
                        modified_items[int(sku)] = int(quantity)
                if modified_items:
                    order_num = random.randint(100000, 999999)
                    cursor.execute("""INSERT INTO online_store.transactions (order_num, date, hour, email) VALUES (%s, CURDATE(), CURTIME(), %s)""",(order_num, session['email'])
                        )               
                    mydb.commit()
                    for sku, quantity in modified_items.items():
                        cursor.execute("""INSERT INTO clothes_in_transaction (order_num, sku, amount) VALUES (%s, %s, %s)""",  (order_num, sku, quantity),)
                        cursor.execute("UPDATE clothes SET available_amount = available_amount - %s WHERE sku = %s", (quantity, sku))
                    mydb.commit()
                    return render_template("transaction.html", order_num=order_num, items=modified_items)
                else:
                    return render_template("error.html", error="No item was added to the cart")
            except Exception as e:
                error = f"error: {e}"
                return render_template('error.html', error=error)
            
        else:
            try:
                cursor.execute("SELECT u.is_admin FROM online_store.users u WHERE email = %s",(session['email'],))    
                is_admin = cursor.fetchone()[0]

                cursor.execute("SELECT * FROM online_store.clothes ORDER BY is_promoted DESC")
                clothes = cursor.fetchall()
                
                modified_clothes = []
                for cloth in clothes:
                    if cloth[3] > 0:
                        modified_clothes.append(cloth)
                return render_template("home_page.html",clothes=modified_clothes, is_admin = is_admin)
            except Exception as e:
                error = f"error: {e}"
                return render_template('error.html', error=error)
        
    @app.route('/logout')
    def logout():
        session.clear() 
        return redirect("/login")  


