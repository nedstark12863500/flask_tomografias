from app import create_app, db, iniciar_datos, iniciar_vistas

app = create_app()
with app.app_context():
    db.create_all()
    iniciar_datos()
    #iniciar_vistas()

if __name__ == "__main__":
    app.run(debug=True)
