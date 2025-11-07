from service.database import app, db
from service import routes  

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  
    print(f"Database tables created")
    app.run(debug=True)
