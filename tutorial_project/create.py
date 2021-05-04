from app import db, Customers, Products, Army, Orders

db.drop_all()
db.create_all()

customer_1 = Customers(name='Alicia')
product_1 = Products(name='Borderlands',price=29.99)
order_1 = Orders(customer_id=1,product_id=1)

db.session.add(customer_1)
db.session.add(product_1)
db.session.add(order_1)
db.session.commit()

necron = Army(army_name='Necrons', faction ='Xeno', alignment='Evil')


db.session.add(necron)
db.session.commit()