from database import Base, motor
import models.usuario, models.pedido, models.possui

Base.metadata.create_all(bind=motor)