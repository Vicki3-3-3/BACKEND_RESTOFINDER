from app.database import get_db

class Reserva:
    def __init__(self, id_reserva=None, restaurant=None, date=None):
        self.id_reserva = id_reserva
        self.restaurant = restaurant
        self.date = date

    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_reserva:
            cursor.execute("""
                UPDATE reservas SET restaurant = %s, date = %s
                WHERE id_reserva = %s
            """, (self.restaurant, self.date, self.id_reserva))
        else:
            cursor.execute("""
                INSERT INTO reservas (restaurant, date) VALUES (%s, %s)
            """, (self.restaurant, self.date))
            self.id_reserva = cursor.lastrowid
        db.commit()
        cursor.close()

    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM reservas")
        rows = cursor.fetchall()
        movies = [Reserva(id_reserva=row[0], title=row[1], date=row[2]) for row in rows]
        cursor.close()
        #RESORVER ASOCIANDO A BASE DE DATOS
        #return reservas

    @staticmethod
    def get_by_id(reserva_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM movies WHERE id_movie = %s", (reserva_id))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Reserva(id_reserva=row[0], restaurant=row[1], date=row[2])
        return None

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM reservas WHERE id_reservas = %s", (self.id_reserva,))
        db.commit()
        cursor.close()

    def serialize(self):
        return {
            'id_reserva': self.id_reserva,
            'restaurant': self.restaurant,
            'date': self.date.strftime('%Y-%m-%d'),
        }